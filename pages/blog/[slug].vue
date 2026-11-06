<template>
  <div class="bg-gray-50 min-h-screen py-8">
    <div class="container mx-auto px-4 max-w-4xl space-y-8">
      
      <!-- Navigasi Kembali -->
      <div>
        <NuxtLink to="/blog" class="text-xs font-bold text-gray-600 hover:text-red-600 flex items-center gap-1">
          ← Kembali ke Daftar Artikel
        </NuxtLink>
      </div>

      <!-- Konten Utama Artikel -->
      <article class="bg-white p-6 sm:p-10 rounded-2xl border border-gray-100 shadow-sm space-y-6">
        
        <!-- Header Artikel -->
        <div class="space-y-3 border-b border-gray-100 pb-6">
          <div class="flex items-center gap-3 text-xs text-gray-500">
            <span class="bg-red-50 text-red-600 font-bold px-3 py-1 rounded-lg">Edukasi Medis</span>
            <span>📅 24 Oktober 2026</span>
            <span>⏱️ 3 menit baca</span>
          </div>
          <h1 class="text-2xl sm:text-4xl font-black text-gray-900 leading-tight">
            Panduan Pertama Pemasangan & Pertolongan Tabung Oksigen di Rumah
          </h1>
          <p class="text-sm sm:text-base text-gray-600 leading-relaxed font-normal">
            Langkah aman menggunakan regulator oksigen dan tindakan pencegahan kebocoran gas saat kondisi darurat keluarga.
          </p>
        </div>

        <!-- Badan Artikel (Simulasi Paragraf) -->
        <div class="space-y-4 text-xs sm:text-sm text-gray-800 leading-relaxed">
          <p>
            Dalam situasi darurat medis yang melibatkan sesak napas berat, ketersediaan tabung oksigen portabel di rumah sangat krusial. Namun, penggunaan alat ini tidak boleh sembarangan dan harus memperhatikan standar keselamatan dasar.
          </p>
          <h3 class="font-bold text-base text-gray-900 pt-2">1. Pengecekan Tekanan Tabung & Regulator</h3>
          <p>
            Pastikan jarum indikator pada regulator menunjukkan angka hijau (tekanan penuh). Jauhkan tabung oksigen dari sumber api terbuka, kompor, atau percikan listrik karena oksigen mempercepat proses pembakaran.
          </p>
          <h3 class="font-bold text-base text-gray-900 pt-2">2. Pemasangan Selang Nasal Cannula</h3>
          <p>
            Atur aliran meteran sesuai anjuran medis (umumnya 2-4 liter per menit untuk pertolongan pertama). Bersihkan selang secara berkala dan pastikan posisi duduk pasien rileks.
          </p>
        </div>

        <!-- Kotak Kontak Darurat Bantuan di Dalam Artikel -->
        <div class="p-4 bg-red-50 rounded-2xl border border-red-100 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div class="space-y-0.5 text-center sm:text-left">
            <h4 class="font-bold text-red-900 text-sm">Butuh Peminjaman Tabung Oksigen Terdekat?</h4>
            <p class="text-xs text-red-700">Cari penyedia tabung oksigen gratis atau sukarela di wilayah Banyumas.</p>
          </div>
          <NuxtLink to="/listings?q=oksigen" class="bg-red-600 hover:bg-red-700 text-white font-bold text-xs px-5 py-2.5 rounded-xl shadow transition shrink-0">
            Cari Tabung Oksigen ➔
          </NuxtLink>
        </div>

      </article>

      <!-- SECTION RELATED POSTS (Menggunakan Komponen blog/BlogCard yang Sama!) -->
      <section class="space-y-4 pt-6 border-t border-gray-200">
        <h2 class="text-lg font-bold text-gray-900">Artikel Terkait Lainnya</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <BlogCard 
            v-for="related in relatedPosts" 
            :key="related.id" 
            :post="related" 
          />
        </div>
      </section>

    </div>
  </div>
</template>

<script setup>
// Mock Related Posts
const relatedPosts = ref([
  {
    id: 2,
    title: 'Langkah Siaga Evakuasi Mandiri Saat Banjir & Pohon Tumbang',
    slug: 'langkah-siaga-evakuasi-banjir',
    category: 'Siaga Bencana',
    readTime: '4 min',
    date: '18 Okt 2026',
    snippet: 'Daftar tas siaga bencana yang wajib disiapkan serta panduan menghubungi tim SAR terdekat.',
    image: null
  },
  {
    id: 3,
    title: 'Cara Mendaftar Menjadi Mitra Penolong & Berbagi Aset Bantuan',
    slug: 'cara-daftar-mitra-penolong',
    category: 'Komunitas',
    readTime: '2 min',
    date: '10 Okt 2026',
    snippet: 'Ingin meminjamkan alat medis atau menjadi armada relawan? Simak alur verifikasi resmi.',
    image: null
  }
])
</script>