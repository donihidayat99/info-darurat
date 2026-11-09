<template>
  <div class="bg-white rounded-2xl p-5 border border-gray-100 shadow-sm hover:shadow-md transition duration-200 flex flex-col justify-between">
    <div>
      
      <!-- Bagian Visual: Foto Asli ATAU Smart Fallback Ikon Kategori -->
      <div class="h-36 rounded-xl bg-gray-100 mb-4 overflow-hidden relative flex items-center justify-center border border-gray-200">
        <template v-if="listing.image">
          <img :src="listing.image" :alt="listing.title" class="w-full h-full object-cover" />
        </template>
        <template v-else>
          <!-- Smart Fallback Ikon Berdasarkan Kategori -->
          <div class="text-center space-y-1">
            <span class="text-3xl">{{ getCategoryIcon(listing.category) }}</span>
            <span class="text-[10px] text-gray-400 block font-medium uppercase tracking-wider">Aset Bantuan Siaga</span>
          </div>
        </template>

        <!-- Badge Biaya di Pojok Atas Gambar/Box -->
        <div class="absolute top-2 right-2">
          <span 
            :class="{
              'bg-emerald-50 text-emerald-700 border-emerald-200': listing.costType === 'Gratis',
              'bg-blue-50 text-blue-700 border-blue-200': listing.costType === 'Sukarela',
              'bg-amber-50 text-amber-700 border-amber-200': listing.costType === 'Berbayar / Ganti Operasional'
            }"
            class="text-[10px] font-bold px-2 py-0.5 rounded border shadow-sm bg-white"
          >
            {{ listing.costType || 'Gratis' }}
          </span>
        </div>
      </div>

      <!-- Header: Kategori & Status Ketersediaan -->
      <div class="flex justify-between items-center mb-2">
        <span class="bg-red-50 text-red-600 text-[11px] font-semibold px-2.5 py-0.5 rounded-md">
          {{ listing.category }}
        </span>
        <span class="text-[11px] text-emerald-600 font-medium bg-emerald-50 px-2 py-0.5 rounded">
          🟢 {{ listing.status || 'Ready' }}
        </span>
      </div>

      <!-- Judul & Instansi -->
      <h3 class="font-bold text-gray-900 text-base mb-1 hover:text-red-600 transition line-clamp-1">
        <NuxtLink :to="`/listings/${listing.id}`">
          {{ listing.title }}
        </NuxtLink>
      </h3>
      <p class="text-xs text-gray-500 mb-3">{{ listing.provider }}</p>

      <!-- Informasi Detail (Alamat / Kontak) -->
      <div class="space-y-1.5 text-xs text-gray-600 border-t border-gray-100 pt-3">
        <div class="flex items-center gap-2">
          <span>📍</span>
          <span class="line-clamp-1">{{ listing.location }}</span>
        </div>
        <div class="flex items-center gap-2">
          <span>📞</span>
          <span class="font-semibold text-gray-800">{{ listing.phone }}</span>
        </div>
      </div>
    </div>

    <!-- Tombol Aksi Cepat -->
    <div class="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between">
      <NuxtLink :to="`/listings/${listing.id}`" class="text-xs font-bold text-red-600 hover:underline">
        Lihat Detail ➔
      </NuxtLink>
      <a :href="`tel:${listing.phone}`" class="bg-red-600 hover:bg-red-700 text-white text-xs font-bold px-3 py-1.5 rounded-lg transition shadow-sm">
        📞 Hubungi
      </a>
    </div>
  </div>
</template>

<script setup>
defineProps({
  listing: {
    type: Object,
    required: true
  }
})

// Fungsi helper untuk menentukan ikon otomatis berdasarkan kategori
const getCategoryIcon = (category) => {
  const cat = category?.toLowerCase() || ''
  if (cat.includes('medis') || cat.includes('kesehatan')) return '🏥'
  if (cat.includes('pemadam') || cat.includes('kebakaran')) return '🚒'
  if (cat.includes('sar') || cat.includes('evakuasi') || cat.includes('kapal')) return '🛶'
  if (cat.includes('bencana') || cat.includes('posko')) return '🏕️'
  if (cat.includes('logistik') || cat.includes('pangan')) return '📦'
  if (cat.includes('ambulans')) return '🚑'
  return '🛡️'
}
</script>