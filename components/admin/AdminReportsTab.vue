<template>
  <div class="bg-white p-6 rounded-2xl border border-red-100 shadow-sm space-y-6">
    <h2 class="font-bold text-gray-900 text-base flex items-center gap-2">
      🚨 Pantauan & Laporan Darurat Warga Aktif
    </h2>
    <div class="space-y-4">
      <div v-for="report in reports" :key="report.id" class="p-4 rounded-xl border border-red-200 bg-red-50/30 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span class="bg-red-600 text-white text-[10px] font-bold px-2 py-0.5 rounded uppercase">{{ report.type }}</span>
            <span class="text-xs text-gray-500">Pelapor: <strong>{{ report.reporter }}</strong> ({{ report.phone }})</span>
          </div>
          <h3 class="font-bold text-gray-900 text-sm">{{ report.location }}</h3>
          <p class="text-xs text-gray-600">{{ report.description }}</p>
        </div>
        <div class="flex items-center gap-2">
          <a :href="`https://wa.me/${report.phone}`" target="_blank" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold px-4 py-2 rounded-xl cursor-pointer">
            💬 Hubungi Pelapor
          </a>
          <button @click="$emit('resolve', report.id)" class="bg-gray-800 hover:bg-gray-900 text-white text-xs font-bold px-4 py-2 rounded-xl cursor-pointer">
            Selesaikan Kasus
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ reports: Array })
defineEmits(['resolve'])
</script>