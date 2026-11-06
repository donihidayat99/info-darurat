<template>
  <div class="bg-white rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition overflow-hidden flex flex-col justify-between group">
    
    <!-- Area Gambar Sampul / Fallback Ikon Kategori -->
    <div class="h-44 bg-gray-100 relative flex items-center justify-center overflow-hidden">
      <!-- Jika ada gambar cover -->
      <img 
        v-if="article?.image" 
        :src="article.image" 
        :alt="article?.title || 'Artikel Bantuan'" 
        class="w-full h-full object-cover group-hover:scale-105 transition duration-300"
      />
      
      <!-- Smart Fallback Ikon Kategori jika gambar kosong -->
      <div v-else class="text-center p-4 space-y-1">
        <div class="w-12 h-12 mx-auto rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center text-2xl font-bold">
          {{ getCategoryIcon(article?.category) }}
        </div>
        <span class="text-[10px] text-gray-400 font-medium block">Info Darurat Edukasi</span>
      </div>

      <!-- Badge Kategori Atas -->
      <span class="absolute top-3 left-3 bg-white/90 backdrop-blur-md text-purple-700 font-bold text-[10px] px-2.5 py-1 rounded-lg border border-purple-100 shadow-sm">
        {{ article?.category || 'Edukasi' }}
      </span>
    </div>

    <!-- Isi Ringkasan Artikel -->
    <div class="p-5 space-y-2 flex-1 flex flex-col justify-between">
      <div class="space-y-1.5">
        <div class="flex items-center justify-between text-[11px] text-gray-400">
          <span>⏱️ {{ article?.readTime || '3 min' }} baca</span>
          <span>{{ article?.date || 'Terbaru' }}</span>
        </div>
        <h3 class="font-bold text-sm text-gray-900 group-hover:text-purple-600 transition line-clamp-2">
          {{ article?.title || 'Judul Artikel Edukasi' }}
        </h3>
        <p class="text-xs text-gray-500 line-clamp-3 leading-relaxed">
          {{ article?.snippet || 'Tidak ada ringkasan artikel.' }}
        </p>
      </div>

      <!-- Link Baca Selengkapnya -->
      <div class="pt-3 border-t border-gray-100 flex items-center justify-between">
        <NuxtLink 
          :to="`/blog/${article?.slug || article?.id || 'detail'}`" 
          class="text-xs font-bold text-purple-600 hover:underline flex items-center gap-1"
        >
          Baca Selengkapnya ➔
        </NuxtLink>
      </div>
    </div>

  </div>
</template>

<script setup>
const props = defineProps({
  article: {
    type: Object,
    default: () => ({})
  }
})

// Function Smart Fallback Ikon berdasarkan Kategori
const getCategoryIcon = (category) => {
  switch (category) {
    case 'Edukasi Medis': return '🏥'
    case 'Siaga Bencana': return '🏕️'
    case 'Komunitas': return '🤝'
    default: return '📖'
  }
}
</script>