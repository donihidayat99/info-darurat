import os
import sys
import sqlite3
from google import genai
from google.genai import types

# Validasi API Key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("❌ Error: GEMINI_API_KEY belum di-export di terminal!")
    print("Jalankan: export GEMINI_API_KEY='your_key'")
    sys.exit(1)

client = genai.Client(api_key=api_key)

# ==========================================
# DEFINISI TOOLS (Dibuat Lebih Selektif)
# ==========================================

def list_files(directory: str = ".") -> list:
    """Mendaftar file proyek penting saja (.vue, .js, .ts, .py, .json), otomatis mengabaikan node_modules, .git, .nuxt, dll."""
    ignore_dirs = {'.git', '.nuxt', 'node_modules', '.output', 'dist', '.vscode', 'vendor'}
    allowed_extensions = {'.vue', '.js', '.ts', '.py', '.json', '.css', '.md', '.html'}
    
    file_list = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            # Hanya ambil ekstensi file yang relevan dengan pengembangan web/aplikasi
            _, ext = os.path.splitext(file)
            if ext.lower() in allowed_extensions:
                filepath = os.path.join(root, file)
                file_list.append(filepath.replace("./", ""))
    return file_list

def read_file(filepath: str) -> str:
    """Membaca isi teks dari satu file spesifik tertentu di dalam proyek."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error membaca file: {str(e)}"

def write_file(filepath: str, content: str) -> str:
    """Menulis atau mengedit file secara spesifik di dalam proyek (membuat file baru jika belum ada)."""
    try:
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"✅ Sukses menulis/memperbarui file: {filepath}"
    except Exception as e:
        return f"❌ Error menulis file: {str(e)}"

def create_sqlite_database(db_path: str = "database.sqlite") -> str:
    """Membuat file database SQLite baru beserta tabel dasar jika diperlukan."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS listings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT,
                contact_method TEXT DEFAULT 'whatsapp',
                whatsapp_number TEXT,
                contact_email TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
        return f"✅ Database SQLite berhasil dibuat/dikonfirmasi di: {db_path}"
    except Exception as e:
        return f"❌ Error membuat database SQLite: {str(e)}"

my_tools = [list_files, read_file, write_file, create_sqlite_database]

# ==========================================
# LOOP UTAMA CHAT AGENT
# ==========================================
def main():
    print("🤖 Asisten Gemini (Acode Mobile Dev Agent) Siap!")
    print("Ketik perintah Anda dalam Bahasa Indonesia (contoh: 'Tulis kode untuk komponen Navbar.vue').")
    print("Ketik 'exit' untuk keluar.\n")

    # System instruction yang melarang AI membaca file sembarangan
    system_instruction = """
    Anda adalah agen AI senior developer yang membantu mengelola proyek Nuxt.js 'info-darurat' langsung dari terminal Acode.
    ATURAN UTAMA:
    1. Bekerjalah secara efektif dan presisi. Jangan pernah membaca seluruh file atau folder jika user hanya meminta edit file spesifik.
    2. Jika user meminta mengedit file tertentu (misal: 'ubah file pages/index.vue'), cukup baca file tersebut menggunakan `read_file`, lalu langsung perbarui menggunakan `write_file`.
    3. Gunakan Bahasa Indonesia yang natural dan ramah dalam merespons.
    4. Selalu laporkan hasil tindakan tool dengan ringkas.
    """

    chat = client.chats.create(
        model="gemini-3.8-flash", # Sesuaikan dengan model stabil yang digunakan
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            tools=my_tools,
            temperature=0.2,
        )
    )

    while True:
        try:
            user_input = input("Anda: ")
            if user_input.lower() in ['exit', 'quit']:
                break
            if not user_input.strip():
                continue

            print("⏳ Gemini sedang memproses perintah...")
            
            # Kirim pesan ke model
            response = chat.send_message(user_input)

            print(f"\nGemini:\n{response.text}\n" + "-"*50)

        except KeyboardInterrupt:
            print("\nKeluar...")
            break
        except Exception as e:
            print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()