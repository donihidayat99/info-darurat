<template>
  <div class="bg-gray-50 min-h-screen space-y-12 pb-12">
    
    <!-- Hero Section dengan Universal Search Bar -->
    <section class="bg-gradient-to-b from-red-600 to-red-700 text-white py-12 sm:py-16 px-4 rounded-b-3xl shadow-lg relative overflow-hidden">
      <div class="container mx-auto max-w-4xl text-center space-y-6 relative z-10">
        
        <!-- Badge Status Platform -->
        <div class="inline-flex items-center gap-2 bg-white/10 backdrop-blur-md border border-white/20 px-3 py-1 rounded-full text-xs font-medium text-red-100">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>Platform Tanggap Bantuan Kemanusiaan & Darurat</span>
        </div>

        <!-- Judul Utama -->
        <h1 class="text-3xl sm:text-5xl font-black tracking-tight leading-tight">
          Cari Aset & Layanan Darurat <br class="hidden sm:inline" />Cepat & Tepat di Sekitar Anda
        </h1>
        <p class="text-xs sm:text-base text-red-100 max-w-2xl mx-auto font-normal">
          Akses kilat ke posko bantuan, tabung oksigen, perahu evakuasi, hingga ambulans dari jaringan Mitra Penolong terpercaya.
        </p>

        <!-- Universal Search Box Ala E-Commerce -->
        <div class="bg-white p-3 sm:p-4 rounded-2xl shadow-xl max-w-2xl mx-auto text-gray-800 space-y-3">
          <form @submit.prevent="handleSearch" class="flex flex-col sm:flex-row gap-2">
            <div class="relative flex-1">
              <input 
                v-model="searchQuery"
                type="text" 
                placeholder="Ketik kata kunci (misal: 'oksigen', 'banyumas', 'ambulan')..." 
                class="w-full pl-10 pr-4 py-3 rounded-xl border border-gray-200 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-red-500 font-medium"
              />
              <span class="absolute left-3.5 top-3.5 text-base">🔍</span>
            </div>
            <button 
              type="submit" 
              class="bg-red-600 hover:bg-red-700 text-white font-bold text-xs sm:text-sm px-6 py-3 rounded-xl transition shadow-md flex items-center justify-center gap-2 shrink-0 cursor-pointer"
            >
              <span>Cari Bantuan</span>
              <span>➔</span>
            </button>
          </form>

          <!-- Kata Kunci Populer / Tag Cepat -->
          <div class="flex items-center gap-2 overflow-x-auto text-[11px] text-gray-500 pt-1 px-1 scrollbar-none">
            <span class="font-bold text-gray-400 shrink-0">Populer:</span>
            <button 
              v-for="tag in popularTags" 
              :key="tag"
              @click="quickSearch(tag)"
              class="bg-gray-100 hover:bg-red-50 hover:text-red-600 px-2.5 py-1 rounded-lg transition shrink-0 font-medium cursor-pointer"
            >
              {{ tag }}
            </button>
          </div>
        </div>

        <!-- Opsi Akses Cepat Tombol Laporan Darurat Warga -->
        <div class="pt-2">
          <NuxtLink 
            to="/report" 
            class="inline-flex items-center gap-2 bg-amber-400 hover:bg-amber-500 text-gray-950 font-black text-xs px-5 py-2.5 rounded-xl shadow-md transition"
          >
            <span>🚨</span>
            <span>Butuh Pertolongan Cepat? Kirim Laporan Darurat ➔</span>
          </NuxtLink>
        </div>

      </div>
    </section>

    <!-- Kategori Quick Access Grid -->
    <section class="container mx-auto px-4 max-w-5xl space-y-4">
      <div class="flex justify-between items-end">
        <div>
          <h2 class="text-xl font-bold text-gray-900">Kategori Bantuan Utama</h2>
          <p class="text-xs text-gray-500">Pilih jenis aset bantuan atau layanan yang dibutuhkan</p>
        </div>
        <NuxtLink to="/categories" class="text-xs font-bold text-red-600 hover:underline">
          Lihat Semua Kategori ➔
        </NuxtLink>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 sm:gap-4">
        <NuxtLink 
          v-for="(cat, i) in quickCategories" 
          :key="i"
          :to="`/listings?category=${encodeURIComponent(cat.name)}`"
          class="bg-white p-4 rounded-2xl border border-gray-100 shadow-sm hover:border-red-200 hover:shadow-md transition text-center space-y-2 group"
        >
          <div class="text-3xl group-hover:scale-110 transition">{{ cat.icon }}</div>
          <div class="font-bold text-xs text-gray-800 group-hover:text-red-600 transition">{{ cat.name }}</div>
        </NuxtLink>
      </div>
    </section>

    <!-- Section Aset Bantuan Terbaru / Siaga -->
    <section class="container mx-auto px-4 max-w-5xl space-y-4">
      <div class="flex justify-between items-end">
        <div>
          <h2 class="text-xl font-bold text-gray-900">Aset Bantuan Siaga Terbaru</h2>
          <p class="text-xs text-gray-500">Aset dan layanan bantuan terkini dari Mitra Penolong</p>
        </div>
        <NuxtLink to="/listings" class="text-xs font-bold text-red-600 hover:underline">
          Jelajahi Semua Aset ➔
        </NuxtLink>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <ListingCard 
          v-for="listing in sampleListings" 
          :key="listing.id" 
          :listing="listing" 
        />
      </div>
    </section>

    <!-- SECTION BLOG & EDUKASI (MENGGUNAKAN KOMPONEN blog/BlogCard) -->
    <section class="container mx-auto px-4 max-w-5xl space-y-6 pt-4">
      <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-200/80 pb-3">
        <div>
          <span class="bg-red-50 text-red-600 text-[10px] font-bold px-2.5 py-0.5 rounded uppercase tracking-wider">
            Edukasi & Panduan Warga
          </span>
          <h2 class="text-xl sm:text-2xl font-black text-gray-900 mt-1">Artikel Tanggap Bencana & Tips Medis</h2>
          <p class="text-xs text-gray-500">Informasi penting seputar pertolongan pertama, navigasi bencana, dan panduan darurat.</p>
        </div>
        <NuxtLink to="/blog" class="text-xs font-bold text-red-600 hover:underline shrink-0">
          Lihat Semua Artikel ➔
        </NuxtLink>
      </div>

      <!-- Render Menggunakan Komponen Standar blog/BlogCard -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <BlogCard 
          v-for="post in blogPosts" 
          :key="post.id" 
          :post="post" 
        />
      </div>
    </section>

  </div>
</template>

<script setup>
const router = useRouter()
const searchQuery = ref('')

const popularTags = ['Oksigen', 'Ambulans', 'Kursi Roda', 'Banyumas', 'SAR', 'Kebakaran']

const quickCategories = [
  { name: 'Darurat Medis', icon: '🏥' },
  { name: 'Pemadam Kebakaran', icon: '🚒' },
  { name: 'SAR & Evakuasi', icon: '🛶' },
  { name: 'Posko Bencana', icon: '🏕️' },
  { name: 'Bantuan Logistik', icon: '📦' },
  { name: 'Ambulans Gratis', icon: '🚑' }
]

const sampleListings = ref([
  { id: 1, title: 'Tabung Oksigen 1m3 + Regulator', category: 'Darurat Medis', costType: 'Gratis', provider: 'Relawan Kemanusiaan Purwokerto', location: 'Purwokerto Utara, Kab. Banyumas', phone: '081234567890', image: null },
  { id: 2, title: 'Kursi Roda Lipat Standar Medis', category: 'Darurat Medis', costType: 'Sukarela', provider: 'Budi Santoso (Personal)', location: 'Purwokerto Selatan, Kab. Banyumas', phone: '081987654321', image: null },
  { id: 3, title: 'Ambulans Siaga 24 Jam Komunitas', category: 'Ambulans Gratis', costType: 'Gratis', provider: 'Yayasan Ambulans Berkah', location: 'Wangon, Kab. Banyumas', phone: '081298765432', image: null }
])

// Data Artikel Blog (Menggunakan format objek yang kompatibel dengan blog/BlogCard)
const blogPosts = ref([
  {
    id: 1,
    title: 'Panduan Pertama Pemasangan & Pertolongan Tabung Oksigen di Rumah',
    slug: 'panduan-pertolongan-tabung-oksigen',
    category: 'Edukasi Medis',
    readTime: '3 min',
    date: '24 Okt 2026',
    snippet: 'Langkah aman menggunakan regulator oksigen dan tindakan pencegahan kebocoran gas saat kondisi darurat keluarga.',
    image: null
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

const handleSearch = () => {
  if (searchQuery.value.trim()) {
    router.push({ path: '/listings', query: { q: searchQuery.value.trim() } })
  } else {
    router.push('/listings')
  }
}

const quickSearch = (tag) => {
  router.push({ path: '/listings', query: { q: tag } })
}
</script>