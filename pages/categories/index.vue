<template>
  <div class="bg-gray-50 min-h-screen py-8">
    <div class="container mx-auto px-4 max-w-5xl space-y-6">
      
      <!-- Navigasi Kembali -->
      <div>
        <NuxtLink to="/" class="text-xs font-bold text-gray-600 hover:text-red-600 flex items-center gap-1">
          ← Kembali ke Beranda
        </NuxtLink>
      </div>

      <!-- Header Halaman Kategori -->
      <div class="bg-white p-6 sm:p-8 rounded-2xl border border-gray-100 shadow-sm space-y-2">
        <span class="bg-red-50 text-red-600 text-xs font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">
          Direktori Kategori Bantuan
        </span>
        <h1 class="text-2xl sm:text-3xl font-black text-gray-900">Seluruh Kategori Aset & Layanan Darurat</h1>
        <p class="text-xs sm:text-sm text-gray-500">
          Pilih kategori di bawah untuk menemukan ketersediaan tabung oksigen, armada evakuasi, ambulans, hingga logistik terdekat.
        </p>
      </div>

      <!-- Grid Katalog Kategori Lengkap -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        <div 
          v-for="cat in categoryCatalog" 
          :key="cat.name"
          @click="goToCategorySearch(cat.name)"
          class="bg-white p-5 rounded-2xl border border-gray-100 shadow-sm hover:border-red-300 hover:shadow-md transition cursor-pointer flex items-center justify-between group space-x-4"
        >
          <div class="flex items-center space-x-4">
            <div class="w-12 h-12 rounded-2xl bg-red-50 text-red-600 flex items-center justify-center text-2xl group-hover:scale-110 transition shrink-0">
              {{ cat.icon }}
            </div>
            <div>
              <h3 class="font-bold text-sm text-gray-900 group-hover:text-red-600 transition">{{ cat.name }}</h3>
              <p class="text-xs text-gray-400 mt-0.5">{{ cat.description }}</p>
            </div>
          </div>
          <div class="text-right shrink-0">
            <span class="text-xs font-bold text-gray-700 bg-gray-50 px-2.5 py-1 rounded-lg border border-gray-100 block">
              {{ cat.count }} Aset
            </span>
            <span class="text-[10px] text-red-600 font-bold group-hover:underline mt-1 block">Lihat ➔</span>
          </div>
        </div>
      </div>

      <!-- Banner Navigasi Cepat ke Pencarian Universal -->
      <div class="bg-gradient-to-r from-red-600 to-red-700 text-white p-6 rounded-2xl shadow-md flex flex-col sm:flex-row justify-between items-center gap-4">
        <div class="space-y-1 text-center sm:text-left">
          <h3 class="font-bold text-base">Tidak Menemukan Kategori yang Sesuai?</h3>
          <p class="text-xs text-red-100">Gunakan fitur Pencarian Cerdas Universal untuk menemukan alat atau mitra berdasarkan kata kunci bebas.</p>
        </div>
        <NuxtLink to="/listings" class="bg-white text-red-600 font-bold text-xs px-5 py-3 rounded-xl shadow hover:bg-red-50 transition shrink-0">
          🔍 Buka Pencarian Universal
        </NuxtLink>
      </div>

    </div>
  </div>
</template>

<script setup>
const router = useRouter()

const categoryCatalog = [
  { name: 'Darurat Medis', icon: '🏥', count: 124, description: 'Tabung oksigen, regulator, alat medis darurat' },
  { name: 'Pemadam Kebakaran', icon: '🚒', count: 45, description: 'Posko & armada penanganan pemadam kebakaran' },
  { name: 'SAR & Evakuasi', icon: '🛶', count: 88, description: 'Perahu karet, pelampung, perlengkapan SAR' },
  { name: 'Posko Bencana', icon: '🏕️', count: 32, description: 'Tenda pengungsian & tempat penampungan darurat' },
  { name: 'Bantuan Logistik', icon: '📦', count: 95, description: 'Bahan makanan, selimut, air bersih, & pakaian' },
  { name: 'Ambulans Gratis', icon: '🚑', count: 76, description: 'Layanan armada ambulans bantuan kemanusiaan' }
]

const goToCategorySearch = (categoryName) => {
  router.push({ path: '/listings', query: { category: categoryName } })
}
</script>