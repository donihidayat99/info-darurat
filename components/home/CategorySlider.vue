<template>
  <section class="py-12 bg-white">
    <div class="container mx-auto px-4">
      <div class="text-center max-w-xl mx-auto mb-10">
        <h2 class="text-2xl sm:text-3xl font-bold text-gray-900">Kategori Layanan Utama</h2>
        <p class="text-gray-500 text-sm mt-1">Pilih jenis bantuan darurat sesuai kebutuhan mendesak Anda</p>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
        <NuxtLink 
          v-for="(cat, i) in categories" 
          :key="i"
          to="/listings"
          class="p-5 rounded-2xl border border-gray-100 bg-gray-50 hover:bg-red-50 hover:border-red-200 transition duration-200 group flex items-center gap-4 shadow-sm"
        >
          <div class="w-12 h-12 rounded-xl bg-white shadow-sm flex items-center justify-center text-2xl group-hover:scale-110 transition">
            {{ cat.icon }}
          </div>
          <div>
            <h3 class="font-bold text-gray-800 group-hover:text-red-600 text-sm">{{ cat.name }}</h3>
            <span class="text-xs text-gray-400">{{ cat.count }} Posko/Alat</span>
          </div>
        </NuxtLink>
      </div>
    </div>
  </section>
</template>

<script setup>
const categories = [
  { name: 'Darurat Medis', icon: '🏥', count: 124 },
  { name: 'Pemadam Kebakaran', icon: '🚒', count: 45 },
  { name: 'SAR & Evakuasi', icon: '🛶', count: 88 },
  { name: 'Posko Bencana', icon: '🏕️', count: 62 },
  { name: 'Bantuan Logistik', icon: '📦', count: 91 },
  { name: 'Keamanan / Polisi', icon: '🚔', count: 110 },
  { name: 'Dapur Umum', icon: '🍲', count: 34 },
  { name: 'Ambulans Gratis', icon: '🚑', count: 76 },
]
</script>