import os
import sys
import json
import sqlite3
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5-coder:1.5b-instruct-q4_K_M"

# ==========================================
# DEFINISI TOOLS (Fungsi File & Database)
# ==========================================

def list_files(directory: str = ".") -> str:
    """Mendaftar file proyek penting saja (.vue, .js, .ts, .py, .json), mengabaikan node_modules, dll."""
    ignore_dirs = {'.git', '.nuxt', 'node_modules', '.output', 'dist', '.vscode', 'vendor'}
    allowed_extensions = {'.vue', '.js', '.ts', '.py', '.json', '.css', '.md', '.html'}
    
    file_list = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in allowed_extensions:
                filepath = os.path.join(root, file)
                file_list.append(filepath.replace("./", ""))
    return json.dumps(file_list, ensure_ascii=False)

def read_file(filepath: str) -> str:
    """Membaca isi teks dari satu file spesifik di proyek."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error membaca file: {str(e)}"

def write_file(filepath: str, content: str) -> str:
    """Menulis atau memperbarui file di proyek (membuat file baru jika belum ada)."""
    try:
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"✅ Sukses menulis/memperbarui file: {filepath}"
    except Exception as e:
        return f"❌ Error menulis file: {str(e)}"

def create_sqlite_database(db_path: str = "database.sqlite") -> str:
    """Membuat file database SQLite baru beserta tabel dasar."""
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
        return f"✅ Database SQLite berhasil dibuat di: {db_path}"
    except Exception as e:
        return f"❌ Error membuat database SQLite: {str(e)}"

# Mapping nama fungsi agar bisa dipanggil secara dinamis
available_tools = {
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file,
    "create_sqlite_database": create_sqlite_database
}

# ==========================================
# INTERAKSI DENGAN OLLAMA & TOOL PARSING
# ==========================================

def ask_ai(prompt: str) -> str:
    system_prompt = """
    Anda adalah agen AI senior developer untuk proyek Nuxt.js 'info-darurat'.
    Anda memiliki kemampuan memanggil tools untuk berinteraksi dengan file sistem lokal.
    Jika Anda ingin menjalankan tool, berikan respons DALAM FORMAT JSON BERIKUT TANPA TEKS LAIN:
    {"tool": "nama_fungsi", "arguments": {"parameter": "nilai"}}
    
    Tools yang tersedia:
    1. {"tool": "list_files", "arguments": {}} -> Untuk melihat daftar file penting.
    2. {"tool": "read_file", "arguments": {"filepath": "jalur/file"}} -> Untuk membaca isi file.
    3. {"tool": "write_file", "arguments": {"filepath": "jalur/file", "content": "isi kode lengkap"}} -> Untuk menulis/mengedit file.
    4. {"tool": "create_sqlite_database", "arguments": {}} -> Untuk membuat database sqlite.

    Jika perintah user tidak memerlukan tool (misal hanya tanya jawab biasa atau sapaan), jawab langsung dengan teks biasa dalam Bahasa Indonesia.
    """
    
    payload = {
        "model": MODEL_NAME,
        "prompt": f"{system_prompt}\n\nUser: {prompt}\nResponse:",
        "stream": False,
        "temperature": 0.1
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        OLLAMA_URL, 
        data=data, 
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            return res.get("response", "").strip()
    except Exception as e:
        return f"❌ Gagal terhubung ke Ollama: {str(e)}"

# ==========================================
# MAIN LOOP AGENT
# ==========================================

def main():
    print(f"🤖 Asisten AI Lokal Acode ({MODEL_NAME}) Siap!")
    print("Ketik perintah Anda (contoh: 'Tampilkan daftar file' atau 'Buatkan komponen Navbar.vue').")
    print("Ketik 'exit' untuk keluar.\n")

    while True:
        try:
            user_input = input("Anda: ")
            if user_input.lower() in ['exit', 'quit']:
                break
            if not user_input.strip():
                continue

            print("⏳ Qwen sedang menganalisis perintah...")
            ai_reply = ask_ai(user_input)

            # Cek apakah AI ingin memanggil tool (format JSON)
            try:
                # Bersihkan respons jika ada backtick markdown
                clean_reply = ai_reply.replace("```json", "").replace("```", "").strip()
                tool_call = json.loads(clean_reply)
                
                if "tool" in tool_call and tool_call["tool"] in available_tools:
                    tool_name = tool_call["tool"]
                    tool_args = tool_call.get("arguments", {})
                    
                    print(f"🔧 Menjalankan Tool secara otonom: [{tool_name}]...")
                    
                    # Eksekusi fungsi Python secara lokal
                    tool_function = available_tools[tool_name]
                    tool_result = tool_function(**tool_args)
                    
                    print(f"\nHasil Eksekusi Tool:\n{tool_result}\n" + "-"*50)
                else:
                    print(f"\nQwen:\n{ai_reply}\n" + "-"*50)
            except json.JSONDecodeError:
                # Jika bukan format JSON, berarti respons teks biasa
                print(f"\nQwen:\n{ai_reply}\n" + "-"*50)

        except KeyboardInterrupt:
            print("\nKeluar...")
            break

if __name__ == "__main__":
    main()