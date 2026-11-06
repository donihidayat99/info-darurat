<template>
  <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-6">
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
      <div>
        <h2 class="font-bold text-gray-900 text-base">Atur Kategori & Tampilan Ikon (Emoji / SVG / PNG)</h2>
        <p class="text-xs text-gray-500">Kelola klasifikasi bantuan dan sesuaikan ikon visual yang tampil pada kartu listing warga.</p>
      </div>
      <button @click="$emit('openModal')" class="bg-red-600 hover:bg-red-700 text-white text-xs font-bold px-4 py-2.5 rounded-xl shadow-sm transition flex items-center gap-1 cursor-pointer">
        + Tambah Kategori Baru
      </button>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div v-for="cat in categories" :key="cat.id" class="p-4 rounded-2xl border border-gray-100 bg-gray-50/50 space-y-3 flex flex-col justify-between">
        <div class="flex items-start justify-between gap-3">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-xl bg-red-50 text-red-600 flex items-center justify-center text-2xl border border-red-100 shrink-0 overflow-hidden">
              <span>{{ cat.iconValue }}</span>
            </div>
            <div>
              <h3 class="font-bold text-gray-900 text-sm">{{ cat.name }}</h3>
              <span class="text-[10px] text-gray-400 font-mono">slug: /{{ cat.slug }}</span>
            </div>
          </div>
          <span :class="cat.active ? 'bg-emerald-50 text-emerald-700' : 'bg-gray-100 text-gray-500'" class="text-[10px] font-bold px-2 py-0.5 rounded">
            {{ cat.active ? 'Aktif' : 'Non-Aktif' }}
          </span>
        </div>
        <p class="text-xs text-gray-500 line-clamp-2">{{ cat.description }}</p>
        <div class="pt-2 border-t border-gray-100 flex items-center justify-between text-xs">
          <span class="text-gray-400 font-medium">{{ cat.count }} Listing Terkait</span>
          <div class="space-x-2">
            <button @click="$emit('edit', cat)" class="text-blue-600 hover:underline font-bold cursor-pointer">Edit</button>
            <button @click="$emit('delete', cat.id)" class="text-red-600 hover:underline font-bold cursor-pointer">Hapus</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ categories: Array })
defineEmits(['openModal', 'edit', 'delete'])
</script>