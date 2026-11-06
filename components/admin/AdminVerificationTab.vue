<template>
  <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-6">
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
      <div>
        <h2 class="font-bold text-gray-900 text-base">Verifikasi & Preview Aset Bantuan Masuk</h2>
        <p class="text-xs text-gray-500">Tinjau kelayakan isi dan detail aset sebelum dipublikasikan ke warga.</p>
      </div>
      <input 
        v-model="search"
        type="text" 
        placeholder="Filter judul / kategori..." 
        class="px-3 py-2 border border-gray-200 rounded-xl text-xs w-full sm:w-64 focus:outline-none focus:ring-2 focus:ring-red-500" 
      />
    </div>

    <div class="space-y-4">
      <div v-for="item in filteredList" :key="item.id" class="p-5 rounded-2xl border border-gray-100 bg-gray-50/60 space-y-4">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 border-b border-gray-200/60 pb-3">
          <div class="space-y-1">
            <div class="flex items-center gap-2">
              <span class="bg-blue-50 text-blue-600 text-[10px] font-bold px-2 py-0.5 rounded">{{ item.category }}</span>
              <span class="bg-emerald-50 text-emerald-700 text-[10px] font-bold px-2 py-0.5 rounded">{{ item.costType }}</span>
            </div>
            <h3 class="font-black text-gray-900 text-base">{{ item.title }}</h3>
          </div>
          <div class="flex items-center gap-2 w-full sm:w-auto justify-end">
            <button @click="$emit('preview', item)" class="bg-white border border-gray-300 text-gray-700 text-xs font-bold px-4 py-2 rounded-xl hover:bg-gray-100 transition shadow-sm cursor-pointer">
              👁️ Preview Full
            </button>
            <button @click="$emit('approve', item.id)" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold px-4 py-2 rounded-xl transition shadow-sm cursor-pointer">
              ✓ Layak Tayang
            </button>
            <button @click="$emit('reject', item.id)" class="bg-white border border-red-200 text-red-600 text-xs font-bold px-4 py-2 rounded-xl hover:bg-red-50 transition cursor-pointer">
              ✕ Tolak
            </button>
          </div>
        </div>
        <div class="text-xs text-gray-600 grid grid-cols-1 sm:grid-cols-3 gap-2">
          <div>👤 Pendaftar: <strong>{{ item.provider }}</strong></div>
          <div>📍 Lokasi: <strong>{{ item.location }}</strong></div>
          <div>📞 Telp: <strong>{{ item.phone }}</strong></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({ assets: Array })
defineEmits(['preview', 'approve', 'reject'])
const search = ref('')

const filteredList = computed(() => {
  if (!search.value) return props.assets
  return props.assets.filter(i => i.title.toLowerCase().includes(search.value.toLowerCase()))
})
</script>