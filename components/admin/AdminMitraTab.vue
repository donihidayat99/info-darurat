<template>
  <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-6">
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
      <div>
        <h2 class="font-bold text-gray-900 text-base">Manajemen Seluruh Mitra Penolong</h2>
        <p class="text-xs text-gray-500">Hubungi mitra via WhatsApp terlebih dahulu untuk konfirmasi sebelum suspend/hapus akun.</p>
      </div>
      <div class="flex items-center gap-3 w-full sm:w-auto">
        <input 
          v-model="keyword"
          type="text" 
          placeholder="Cari nama / wilayah..." 
          class="px-3 py-2 border border-gray-200 rounded-xl text-xs w-full sm:w-64 focus:outline-none focus:ring-2 focus:ring-red-500" 
        />
        <select 
          v-model="status"
          class="px-3 py-2 border border-gray-200 rounded-xl text-xs bg-white focus:outline-none"
        >
          <option value="">Semua Status</option>
          <option value="Aktif">Aktif</option>
          <option value="Suspended">Suspended</option>
        </select>
      </div>
    </div>

    <div class="overflow-x-auto">
      <table class="w-full text-left text-xs">
        <thead class="bg-gray-50 text-gray-500 border-b border-gray-100">
          <tr>
            <th class="p-3">Nama Mitra Penolong</th>
            <th class="p-3">Tipe</th>
            <th class="p-3">Kontak / Telp</th>
            <th class="p-3">Wilayah</th>
            <th class="p-3">Status</th>
            <th class="p-3 text-right">Aksi Admin</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-100">
          <tr v-for="m in filteredList" :key="m.id" class="hover:bg-gray-50/50">
            <td class="p-3 font-bold text-gray-900">{{ m.name }}</td>
            <td class="p-3 text-gray-600">{{ m.type }}</td>
            <td class="p-3 text-gray-600">{{ m.phone }}</td>
            <td class="p-3 text-gray-600">{{ m.location }}</td>
            <td class="p-3">
              <span :class="m.status === 'Aktif' ? 'bg-emerald-50 text-emerald-700' : 'bg-red-50 text-red-700'" class="px-2 py-0.5 rounded font-bold text-[10px]">
                {{ m.status }}
              </span>
            </td>
            <td class="p-3 text-right space-x-2">
              <a :href="`https://wa.me/${m.phone}`" target="_blank" class="text-blue-600 hover:underline font-semibold">💬 Hubungi</a>
              <button @click="$emit('toggleSuspend', m)" class="text-amber-600 hover:underline font-semibold cursor-pointer">
                {{ m.status === 'Aktif' ? 'Suspend' : 'Aktifkan' }}
              </button>
              <button @click="$emit('delete', m.id)" class="text-red-600 hover:underline font-semibold cursor-pointer">Hapus</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({ mitraList: Array })
defineEmits(['toggleSuspend', 'delete'])
const keyword = ref('')
const status = ref('')

const filteredList = computed(() => {
  return props.mitraList.filter(m => {
    const matchKeyword = m.name.toLowerCase().includes(keyword.value.toLowerCase()) || m.location.toLowerCase().includes(keyword.value.toLowerCase())
    const matchStatus = status.value ? m.status === status.value : true
    return matchKeyword && matchStatus
  })
})
</script>