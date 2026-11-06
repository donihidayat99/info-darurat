<template>
  <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-6">
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
      <div>
        <span class="bg-purple-50 text-purple-700 text-[10px] font-bold px-2 py-0.5 rounded uppercase tracking-wider">Eksklusif Tim Internal</span>
        <h2 class="font-bold text-gray-900 text-base mt-1">Manajemen Artikel, Panduan, & Tips Tanggap Bencana</h2>
        <p class="text-xs text-gray-500">Kelola publikasi artikel edukasi warga (tanpa melibatkan mitra penolong).</p>
      </div>
      <NuxtLink to="/blog/create" class="bg-purple-600 hover:bg-purple-700 text-white text-xs font-bold px-4 py-2.5 rounded-xl shadow-sm transition flex items-center gap-1 cursor-pointer">
        + Tulis Artikel Baru
      </NuxtLink>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="art in articles" :key="art.id" class="bg-white rounded-2xl border border-gray-100 shadow-sm p-5 space-y-3 flex flex-col justify-between group">
        <div class="space-y-2">
          <div class="flex items-center justify-between text-[11px]">
            <span class="bg-gray-100 text-gray-700 font-bold px-2.5 py-0.5 rounded-md">{{ art.category }}</span>
            <span :class="art.status === 'Published' ? 'text-emerald-600 bg-emerald-50' : 'text-amber-600 bg-amber-50'" class="font-bold px-2 py-0.5 rounded">
              {{ art.status }}
            </span>
          </div>
          <h3 class="font-bold text-sm text-gray-900 group-hover:text-purple-600 transition line-clamp-2">
            {{ art.title }}
          </h3>
          <p class="text-xs text-gray-500 line-clamp-3 leading-relaxed">
            {{ art.snippet }}
          </p>
        </div>

        <div class="pt-3 border-t border-gray-100 flex items-center justify-between text-xs">
          <span class="text-gray-400">{{ art.date }}</span>
          <div class="space-x-2">
            <NuxtLink to="/blog/create" class="text-blue-600 hover:underline font-bold cursor-pointer">Edit</NuxtLink>
            <button @click="$emit('toggleSuspend', art)" class="text-amber-600 hover:underline font-bold cursor-pointer">
              {{ art.status === 'Published' ? 'Suspend' : 'Publish' }}
            </button>
            <button @click="$emit('delete', art.id)" class="text-red-600 hover:underline font-bold cursor-pointer">Hapus</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ articles: Array })
defineEmits(['toggleSuspend', 'delete'])
</script>