<template>
  <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-6">
    <h2 class="font-bold text-gray-900 text-base">Antrean Pendaftaran Akun Mitra Penolong Baru</h2>
    <div class="space-y-4">
      <div v-for="mitra in pendingMitra" :key="mitra.id" class="p-4 rounded-xl border border-gray-100 bg-gray-50/50 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span class="bg-red-50 text-red-600 text-[10px] font-bold px-2 py-0.5 rounded">{{ mitra.type }}</span>
            <span class="text-xs text-gray-400">{{ mitra.email }}</span>
          </div>
          <h3 class="font-bold text-gray-900 text-sm">{{ mitra.name }}</h3>
          <p class="text-xs text-gray-500">PIC: <strong>{{ mitra.pic }}</strong> | Telp: {{ mitra.phone }} | Lokasi: {{ mitra.location }}</p>
        </div>
        <div class="flex items-center gap-2">
          <button @click="$emit('approve', mitra.id)" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold px-4 py-2 rounded-xl cursor-pointer">✓ Setujui</button>
          <button @click="$emit('reject', mitra.id)" class="bg-white border border-red-200 text-red-600 text-xs font-bold px-4 py-2 rounded-xl hover:bg-red-50 cursor-pointer">✕ Tolak</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ pendingMitra: Array })
defineEmits(['approve', 'reject'])
</script>