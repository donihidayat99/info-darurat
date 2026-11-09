<template>
  <div class="bg-gray-50 min-h-screen py-8">
    <div class="container mx-auto px-4 max-w-6xl space-y-8">
      
      <!-- Navigasi Kembali -->
      <div>
        <NuxtLink to="/" class="text-xs font-bold text-gray-600 hover:text-red-600 flex items-center gap-1">
          ← Kembali ke Beranda
        </NuxtLink>
      </div>

      <!-- Header & Universal Search Bar -->
      <div class="bg-white p-6 sm:p-8 rounded-2xl border border-gray-100 shadow-sm space-y-5">
        <div>
          <span class="bg-red-50 text-red-600 text-xs font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">
            Pusat Direktori & Pencarian Cerdas
          </span>
          <h1 class="text-2xl sm:text-3xl font-black text-gray-900 mt-2">Cari Aset, Alat, & Layanan Bantuan</h1>
          <p class="text-xs sm:text-sm text-gray-500 mt-1">
            Ketik kata kunci apa saja atau pilih langsung dari tren pencarian warga yang paling sering dicari bulan ini.
          </p>
        </div>

        <!-- Universal Search Input Ala Shopee -->
        <div class="relative">
          <input 
            v-model="searchQuery"
            type="text" 
            placeholder="Cari 'oksigen', 'ambulan', 'kursi roda', 'purwokerto', 'pmi'..." 
            class="w-full pl-11 pr-24 py-3.5 rounded-2xl border-2 border-red-100 text-xs sm:text-sm text-gray-900 focus:border-red-500 focus:ring-0 focus:outline-none transition shadow-sm font-medium"
          />
          <span class="absolute left-4 top-3.5 text-lg">🔍</span>
          <button 
            v-if="searchQuery || selectedCategory"
            @click="resetSearch"
            class="absolute right-3 top-3 bg-gray-100 hover:bg-gray-200 text-gray-600 font-bold text-xs px-3 py-1.5 rounded-xl transition cursor-pointer"
          >
            Reset
          </button>
        </div>

        <!-- 🔥 FILTER CEPAT BERDASARKAN TREN PENCARIAN TERBANYAK (TRENDING KEYWORDS) -->
        <div class="flex items-center gap-2 overflow-x-auto pb-1 pt-1 scrollbar-none">
          <span class="text-xs font-bold text-gray-400 shrink-0 flex items-center gap-1">
            🔥 Tren Bulan Ini:
          </span>
          <button 
            @click="searchQuery = ''"
            :class="!searchQuery ? 'bg-red-600 text-white font-bold' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'"
            class="text-xs px-3.5 py-1.5 rounded-xl transition shrink-0 whitespace-nowrap cursor-pointer"
          >
            Semua
          </button>
          <button 
            v-for="trend in trendingKeywords" 
            :key="trend.keyword"
            @click="applyTrendingSearch(trend.keyword)"
            :class="searchQuery.toLowerCase() === trend.keyword.toLowerCase() ? 'bg-red-600 text-white font-bold' : 'bg-orange-50 text-orange-800 border border-orange-100 hover:bg-orange-100'"
            class="text-xs px-3.5 py-1.5 rounded-xl transition shrink-0 whitespace-nowrap cursor-pointer flex items-center gap-1 font-medium"
          >
            <span>{{ trend.icon }}</span>
            <span>{{ trend.keyword }}</span>
            <span class="text-[9px] opacity-70 bg-white/50 px-1.5 py-0.2 rounded-full font-bold">({{ trend.count }})</span>
          </button>
        </div>
      </div>

      <!-- Informasi Hasil Pencarian -->
      <div class="flex justify-between items-center px-1">
        <p class="text-xs sm:text-sm text-gray-600 font-medium">
          Menampilkan <strong class="text-red-600">{{ filteredListings.length }}</strong> hasil bantuan
          <span v-if="selectedCategory"> dalam kategori "<span class="font-bold text-gray-800">{{ selectedCategory }}</span>"</span>
          <span v-if="searchQuery"> untuk kata kunci "<span class="italic font-bold text-gray-800">{{ searchQuery }}</span>"</span>
        </p>
      </div>

      <!-- Grid Hasil Pencarian Listing -->
      <div v-if="filteredListings.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
<ListingCard v-for="listing in filteredListings" :key="listing.id" :listing="listing" />
      </div>

      <!-- State Jika Tidak Ada Hasil -->
      <div v-else class="bg-white p-12 rounded-2xl border border-gray-100 text-center space-y-4">
        <div class="text-5xl">🔎</div>
        <div class="space-y-1">
          <h3 class="font-bold text-gray-900 text-base">Aset Bantuan Tidak Ditemukan</h3>
          <p class="text-xs text-gray-500 max-w-md mx-auto">
            Tidak ada bantuan yang cocok dengan kriteria pencarian Anda. Coba gunakan kata kunci tren lainnya di atas.
          </p>
        </div>
        <button @click="resetSearch" class="bg-red-50 text-red-600 font-bold text-xs px-4 py-2 rounded-xl hover:bg-red-100 transition cursor-pointer">
          Tampilkan Semua Aset
        </button>
      </div>

      <!-- SECTION SELEKSI KATALOG KATEGORI LENGKAP (DI BAGIAN BAWAH) -->
      <section class="bg-white p-6 sm:p-8 rounded-2xl border border-gray-100 shadow-sm space-y-4 pt-6">
        <div>
          <h2 class="text-lg font-bold text-gray-900">Jelajahi Berdasarkan Kategori Lengkap</h2>
          <p class="text-xs text-gray-500">Klik salah satu kategori di bawah untuk menyaring daftar aset bantuan.</p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 sm:gap-4">
          <button 
            v-for="cat in categoryCatalog" 
            :key="cat.name"
            @click="selectCategoryAndScroll(cat.name)"
            :class="selectedCategory === cat.name ? 'border-red-600 bg-red-50/50 ring-2 ring-red-500/20' : 'border-gray-100 bg-gray-50/50 hover:border-red-200'"
            class="p-4 rounded-2xl border text-center space-y-2 transition cursor-pointer group"
          >
            <div class="text-3xl group-hover:scale-110 transition">{{ cat.icon }}</div>
            <div class="font-bold text-xs text-gray-800 group-hover:text-red-600 transition">{{ cat.name }}</div>
            <div class="text-[10px] text-gray-400 font-medium">{{ cat.count }} Listing</div>
          </button>
        </div>
      </section>

    </div>
  </div>
</template>

<script setup>
const route = useRoute()

// State Pencarian
const searchQuery = ref(route.query.q || '')
const selectedCategory = ref(route.query.category || '')

// 🔥 Data Tren Pencarian Teratas Bulan Ini (Bisa dinamis dari database nanti)
const trendingKeywords = ref([
  { keyword: 'Oksigen', icon: '💨', count: '1.4rb' },
  { keyword: 'Ambulans', icon: '🚑', count: '980' },
  { keyword: 'Kursi Roda', icon: '🦽', count: '650' },
  { keyword: 'Perahu Karet', icon: '🛶', count: '430' },
  { keyword: 'Tabung Gas', icon: '🔥', count: '310' }
])

// Katalog Kategori Lengkap (Di Bagian Bawah)
const categoryCatalog = [
  { name: 'Darurat Medis', icon: '🏥', count: 124 },
  { name: 'Pemadam Kebakaran', icon: '🚒', count: 45 },
  { name: 'SAR & Evakuasi', icon: '🛶', count: 88 },
  { name: 'Posko Bencana', icon: '🏕️', count: 32 },
  { name: 'Bantuan Logistik', icon: '📦', count: 95 },
  { name: 'Ambulans Gratis', icon: '🚑', count: 76 }
]

// Data Mock Aset Bantuan
const listings = ref([
  { id: 1, title: 'Tabung Oksigen 1m3 + Regulator', category: 'Darurat Medis', costType: 'Gratis', provider: 'Relawan Kemanusiaan Purwokerto', location: 'Purwokerto Utara, Kab. Banyumas', phone: '081234567890', image: null },
  { id: 2, title: 'Kursi Roda Lipat Standar Medis', category: 'Darurat Medis', costType: 'Sukarela', provider: 'Budi Santoso (Personal)', location: 'Purwokerto Selatan, Kab. Banyumas', phone: '081987654321', image: null },
  { id: 3, title: 'Ambulans Siaga 24 Jam Komunitas', category: 'Ambulans Gratis', costType: 'Gratis', provider: 'Yayasan Ambulans Berkah', location: 'Wangon, Kab. Banyumas', phone: '081298765432', image: null },
  { id: 4, title: 'Perahu Karet Evakuasi Banjir', category: 'SAR & Evakuasi', costType: 'Gratis', provider: 'Komunitas SAR Lokal', location: 'Sumampir, Purwokerto Utara', phone: '085678901234', image: null }
])

// Helper fungsi normalisasi kata untuk toleransi typo dasar
const normalizeText = (str) => {
  return str.toLowerCase()
    .replace(/ambulan[sg]?/g, 'ambulans')
    .replace(/oksegen|oksegin|oxigen/g, 'oksigen')
    .replace(/karsi|korsi/g, 'kursi')
    .trim()
}

// Logika Pencarian Cerdas Multi-Keyword & Lintas Bidang
const filteredListings = computed(() => {
  return listings.value.filter(item => {
    // Filter Kategori Chips
    const matchesCategory = selectedCategory.value ? item.category === selectedCategory.value : true

    if (!searchQuery.value) return matchesCategory

    // 1. Normalisasi input user & data
    const q = normalizeText(searchQuery.value)
    
    // 2. Pecah query berdasarkan spasi menjadi array kata-kata individual (contoh: "ambulance banyumas" -> ["ambulance", "banyumas"])
    const queryWords = q.split(/\s+/).filter(word => word.length > 0)

    // Gabungkan seluruh teks dalam item menjadi satu string besar untuk dicari
    const itemText = normalizeText(`${item.title} ${item.category} ${item.provider} ${item.location} ${item.costType || ''}`)

    // 3. Pastikan SEMUA kata yang diketik oleh pengguna ada di dalam data (AND search)
    const matchesAllWords = queryWords.every(word => itemText.includes(word))

    return matchesCategory && matchesAllWords
  })
})


// Fungsi ketika chip tren pencarian diklik
const applyTrendingSearch = (keyword) => {
  searchQuery.value = keyword
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const selectCategoryAndScroll = (catName) => {
  selectedCategory.value = catName
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const resetSearch = () => {
  searchQuery.value = ''
  selectedCategory.value = ''
}
</script>