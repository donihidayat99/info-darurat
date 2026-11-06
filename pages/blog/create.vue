<template>
  <div class="bg-gray-50 min-h-screen py-8">
    <div class="container mx-auto px-4 max-w-4xl space-y-6">
      
      <!-- Navigasi Kembali -->
      <div class="flex items-center justify-between">
        <NuxtLink to="/admin" class="text-xs font-bold text-gray-600 hover:text-red-600 flex items-center gap-1 cursor-pointer">
          ← Kembali ke Panel Admin
        </NuxtLink>
        <span class="bg-purple-50 text-purple-700 text-[10px] font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">
          Eksklusif Tim Internal
        </span>
      </div>

      <!-- Header Halaman -->
      <div class="bg-white p-6 sm:p-8 rounded-2xl border border-gray-100 shadow-sm space-y-1">
        <h1 class="text-2xl sm:text-3xl font-black text-gray-900">
          Tulis Artikel Edukasi & Panduan Baru
        </h1>
        <p class="text-xs sm:text-sm text-gray-500">
          Buat artikel edukasi pertolongan pertama, siaga bencana, atau informasi komunitas untuk warga.
        </p>
      </div>

      <!-- Form Utama Penulisan Artikel -->
      <form @submit.prevent="handlePublish" class="bg-white p-6 sm:p-8 rounded-2xl border border-gray-100 shadow-sm space-y-6">
        
        <!-- Judul Artikel -->
        <div class="space-y-1.5">
          <label class="block font-bold text-gray-800 text-xs sm:text-sm">Judul Artikel / Panduan *</label>
          <input 
            v-model="articleForm.title"
            type="text" 
            placeholder="Contoh: Panduan Pertama Pemasangan Tabung Oksigen di Rumah"
            class="w-full px-4 py-3 rounded-xl border border-gray-200 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-purple-500 font-medium"
            required
          />
        </div>

        <!-- Grid Kategori, Estimasi Waktu Baca, & Status -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div class="space-y-1.5">
            <label class="block font-bold text-gray-800 text-xs sm:text-sm">Kategori *</label>
            <select 
              v-model="articleForm.category"
              class="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-purple-500 font-medium"
            >
              <option value="Edukasi Medis">Edukasi Medis</option>
              <option value="Siaga Bencana">Siaga Bencana</option>
              <option value="Komunitas">Komunitas</option>
            </select>
          </div>

          <div class="space-y-1.5">
            <label class="block font-bold text-gray-800 text-xs sm:text-sm">Waktu Baca *</label>
            <input 
              v-model="articleForm.readTime"
              type="text" 
              placeholder="Misal: 3 min"
              class="w-full px-4 py-3 rounded-xl border border-gray-200 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-purple-500 font-medium"
              required
            />
          </div>

          <div class="space-y-1.5">
            <label class="block font-bold text-gray-800 text-xs sm:text-sm">Status Publikasi</label>
            <select 
              v-model="articleForm.status"
              class="w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-purple-500 font-medium"
            >
              <option value="Published">Langsung Terbit (Published)</option>
              <option value="Draft">Simpan Draf (Draft)</option>
            </select>
          </div>
        </div>

        <!-- Ringkasan / Snippet -->
        <div class="space-y-1.5">
          <label class="block font-bold text-gray-800 text-xs sm:text-sm">Ringkasan / Snippet Singkat *</label>
          <textarea 
            v-model="articleForm.snippet"
            rows="2"
            placeholder="Tulis ringkasan 1-2 kalimat yang akan muncul pada kartu artikel di beranda..."
            class="w-full px-4 py-3 rounded-xl border border-gray-200 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-purple-500 leading-relaxed font-medium"
            required
          ></textarea>
        </div>

        <!-- URL Gambar Cover (Opsional dengan Smart Fallback) -->
        <div class="space-y-1.5">
          <label class="block font-bold text-gray-800 text-xs sm:text-sm">
            URL Gambar Sampul / Cover <span class="text-gray-400 font-normal text-xs">(Opsional - Kosongkan untuk Smart Fallback Ikon)</span>
          </label>
          <input 
            v-model="articleForm.image"
            type="text" 
            placeholder="https://domain.com/gambar.jpg"
            class="w-full px-4 py-3 rounded-xl border border-gray-200 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-purple-500 font-medium"
          />
        </div>

        <!-- Isi Konten Artikel Lengkap -->
        <div class="space-y-1.5">
          <label class="block font-bold text-gray-800 text-xs sm:text-sm">Isi Konten Artikel Lengkap *</label>
          <textarea 
            v-model="articleForm.content"
            rows="12"
            placeholder="Tuliskan isi panduan, langkah-langkah pertolongan, atau edukasi secara mendalam di sini..."
            class="w-full px-4 py-3 rounded-xl border border-gray-200 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-purple-500 leading-relaxed font-medium"
            required
          ></textarea>
        </div>

        <!-- Tombol Aksi Simpan & Batal -->
        <div class="pt-4 border-t border-gray-100 flex items-center justify-end gap-3">
          <NuxtLink 
            to="/admin" 
            class="px-5 py-3 bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold text-xs sm:text-sm rounded-xl transition cursor-pointer"
          >
            Batal
          </NuxtLink>
          <button 
            type="submit" 
            class="px-6 py-3 bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs sm:text-sm rounded-xl transition shadow-md flex items-center gap-2 cursor-pointer"
          >
            <span>💾 Simpan & Publikasikan</span>
          </button>
        </div>

      </form>

    </div>
  </div>
</template>

<script setup>
const router = useRouter()

const articleForm = ref({
  title: '',
  category: 'Edukasi Medis',
  readTime: '3 min',
  status: 'Published',
  snippet: '',
  image: '',
  content: ''
})

const handlePublish = () => {
  alert(`✓ Artikel "${articleForm.value.title}" berhasil disimpan!`)
  router.push('/admin')
}
</script>