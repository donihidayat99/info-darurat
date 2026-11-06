<template>
  <div class="bg-gray-50 min-h-screen py-8">
    <div class="container mx-auto px-4 max-w-6xl space-y-8">
      
      <!-- Navigasi Kembali -->
      <div>
        <NuxtLink to="/" class="text-xs font-bold text-gray-600 hover:text-red-600 flex items-center gap-1">
          ← Kembali ke Beranda
        </NuxtLink>
      </div>

      <!-- Header Halaman Blog -->
      <div class="bg-white p-6 sm:p-8 rounded-2xl border border-gray-100 shadow-sm flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <div class="space-y-1">
          <span class="bg-red-50 text-red-600 text-xs font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">
            Pusat Edukasi Warga
          </span>
          <h1 class="text-2xl sm:text-3xl font-black text-gray-900">
            Artikel Tanggap Bencana & Tips Medis
          </h1>
          <p class="text-xs sm:text-sm text-gray-500">
            Kumpulan panduan pertolongan pertama, pencegahan, dan informasi siaga darurat untuk keluarga.
          </p>
        </div>

        <!-- Filter / Pencarian Artikel Sederhana -->
        <input 
          v-model="searchKeyword"
          type="text" 
          placeholder="Cari judul artikel..." 
          class="px-4 py-2.5 rounded-xl border border-gray-200 text-xs w-full sm:w-64 focus:outline-none focus:ring-2 focus:ring-red-500 bg-white font-medium"
        />
      </div>

      <!-- Grid Daftar Artikel Menggunakan Komponen Standar -->
      <div v-if="filteredPosts.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <BlogCard 
          v-for="post in filteredPosts" 
          :key="post.id" 
          :post="post" 
        />
      </div>

      <!-- State Kosong Jika Tidak Ditemukan -->
      <div v-else class="bg-white p-12 rounded-2xl border border-gray-100 text-center space-y-3">
        <div class="text-4xl">📭</div>
        <h3 class="font-bold text-gray-900 text-base">Artikel Tidak Ditemukan</h3>
        <p class="text-xs text-gray-500">Tidak ada artikel yang cocok dengan kata kunci "{{ searchKeyword }}".</p>
      </div>

    </div>
  </div>
</template>

<script setup>
const searchKeyword = ref('')

const allPosts = ref([
  {
    id: 1,
    title: 'Panduan Pertama Pemasangan & Pertolongan Tabung Oksigen di Rumah',
    slug: 'panduan-pertolongan-tabung-oksigen',
    category: 'Edukasi Medis',
    readTime: '3 min',
    date: '24 Okt 2026',
    snippet: 'Langkah aman menggunakan regulator oksigen dan tindakan pencegahan kebocoran gas saat kondisi darurat keluarga.',
    image: null // Contoh smart fallback aktif
  },
  {
    id: 2,
    title: 'Langkah Siaga Evakuasi Mandiri Saat Banjir & Pohon Tumbang',
    slug: 'langkah-siaga-evakuasi-banjir',
    category: 'Siaga Bencana',
    readTime: '4 min',
    date: '18 Okt 2026',
    snippet: 'Daftar tas siaga bencana yang wajib disiapkan serta panduan menghubungi tim SAR terdekat di wilayah Banyumas.',
    image: null
  },
  {
    id: 3,
    title: 'Cara Mendaftar Menjadi Mitra Penolong & Berbagi Aset Bantuan',
    slug: 'cara-daftar-mitra-penolong',
    category: 'Komunitas',
    readTime: '2 min',
    date: '10 Okt 2026',
    snippet: 'Ingin meminjamkan alat medis atau menjadi armada relawan? Simak alur verifikasi resmi di platform Info Darurat.',
    image: null
  }
])

const filteredPosts = computed(() => {
  if (!searchKeyword.value) return allPosts.value
  return allPosts.value.filter(p => 
    p.title.toLowerCase().includes(searchKeyword.value.toLowerCase()) ||
    p.category.toLowerCase().includes(searchKeyword.value.toLowerCase())
  )
})
</script>