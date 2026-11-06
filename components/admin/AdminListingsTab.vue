<template>
  <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-6">
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
      <div>
        <h2 class="font-bold text-gray-900 text-base">Manajemen Global Seluruh Aset Bantuan</h2>
        <p class="text-xs text-gray-500">Filter dan kelola seluruh listing yang tayang di platform.</p>
      </div>
      <div class="flex items-center gap-3 w-full sm:w-auto">
        <input 
          v-model="keyword"
          type="text" 
          placeholder="Cari nama aset / mitra..." 
          class="px-3 py-2 border border-gray-200 rounded-xl text-xs w-full sm:w-64 focus:outline-none focus:ring-2 focus:ring-red-500" 
        />
        <select 
          v-model="category"
          class="px-3 py-2 border border-gray-200 rounded-xl text-xs bg-white focus:outline-none"
        >
          <option value="">Semua Kategori</option>
          <option value="Darurat Medis">Darurat Medis</option>
          <option value="Alat Evakuasi">Alat Evakuasi</option>
          <option value="Ambulans Gratis">Ambulans Gratis</option>
        </select>
      </div>
    </div>

    <div class="space-y-3">
      <div v-for="item in filteredList" :key="item.id" class="p-4 rounded-xl border border-gray-100 bg-gray-50/50 flex justify-between items-center">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span class="bg-red-50 text-red-600 text-[10px] font-bold px-2 py-0.5 rounded">{{ item.category }}</span>
            <span class="text-xs text-gray-400">Mitra: <strong>{{ item.provider }}</strong></span>
          </div>
          <h3 class="font-bold text-gray-900 text-sm">{{ item.title }}</h3>
          <p class="text-xs text-gray-500">Dilihat warga: <strong>{{ item.views }}x</strong> | Biaya: {{ item.costType }}</p>
        </div>
        <div class="flex items-center gap-2">
          <button class="bg-white border border-gray-200 text-gray-700 text-xs font-bold px-3 py-1.5 rounded-lg hover:bg-gray-100 cursor-pointer">Edit</button>
          <button @click="$emit('delete', item.id)" class="bg-white border border-red-200 text-red-600 text-xs font-bold px-3 py-1.5 rounded-lg hover:bg-red-50 cursor-pointer">Hapus</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({ listings: Array })
defineEmits(['delete'])
const keyword = ref('')
const category = ref('')

const filteredList = computed(() => {
  return props.listings.filter(l => {
    const matchKeyword = l.title.toLowerCase().includes(keyword.value.toLowerCase()) || l.provider.toLowerCase().includes(keyword.value.toLowerCase())
    const matchCat = category.value ? l.category === category.value : true
    return matchKeyword && matchCat
  })
})
</script>