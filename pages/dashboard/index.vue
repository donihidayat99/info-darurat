<template>
  <div class="bg-gray-50 min-h-screen py-8">
    <div class="container mx-auto px-4 max-w-6xl space-y-8">
      
      <!-- Top Bar: Selamat Datang & Tombol Tambah Aset -->
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-white p-6 rounded-2xl border border-gray-100 shadow-sm">
        <div>
          <span class="bg-red-50 text-red-600 text-xs font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">
            Panel Mitra Darurat
          </span>
          <h1 class="text-2xl sm:text-3xl font-black text-gray-900 mt-2">
            Selamat Datang, Relawan Kemanusiaan
          </h1>
          <p class="text-xs sm:text-sm text-gray-500 mt-1">
            Kelola Aset Bantuan dan pantau status ketersediaan layanan Anda secara real-time.
          </p>
        </div>
        <NuxtLink 
          to="/dashboard/listings/create" 
          class="bg-red-600 hover:bg-red-700 text-white font-bold text-xs sm:text-sm px-5 py-3 rounded-xl shadow-md transition flex items-center gap-2"
        >
          ➕ Tambah Aset Bantuan
        </NuxtLink>
      </div>

      <!-- Statistik Singkat Dashboard -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
        <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-1">
          <span class="text-xs text-gray-400 font-medium">Total Aset Terdaftar</span>
          <h4 class="text-3xl font-black text-gray-900">3 Unit</h4>
          <span class="text-[11px] text-emerald-600 font-medium">✓ Semua aktif terverifikasi</span>
        </div>
        <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-1">
          <span class="text-xs text-gray-400 font-medium">Total Permintaan Bantuan</span>
          <h4 class="text-3xl font-black text-red-600">28 Kali</h4>
          <span class="text-[11px] text-gray-500">Bulan ini</span>
        </div>
        <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-1">
          <span class="text-xs text-gray-400 font-medium">Status Akun Mitra</span>
          <h4 class="text-xl font-black text-emerald-600 mt-1">Terverifikasi</h4>
          <span class="text-[11px] text-gray-500">Akses penuh diberikan</span>
        </div>
      </div>

      <!-- Daftar Aset Bantuan Milik Mitra (Tabel / Card List) -->
      <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-6">
        <div class="flex justify-between items-center border-b border-gray-100 pb-4">
          <h2 class="font-bold text-gray-900 text-base">Dikelola oleh Anda</h2>
          <span class="text-xs text-gray-400">Menampilkan 3 dari 3 Aset</span>
        </div>

        <div class="space-y-4">
          <div v-for="item in myAssets" :key="item.id" class="p-4 rounded-xl border border-gray-100 bg-gray-50/50 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 hover:border-red-200 transition">
            <div class="space-y-1">
              <div class="flex items-center gap-2">
                <span class="bg-red-50 text-red-600 text-[10px] font-bold px-2 py-0.5 rounded">{{ item.category }}</span>
                <span :class="item.isAvailable ? 'bg-emerald-50 text-emerald-600' : 'bg-amber-50 text-amber-600'" class="text-[10px] font-bold px-2 py-0.5 rounded">
                  {{ item.isAvailable ? '🟢 Siap Dipinjam' : '🟡 Sedang Dipakai' }}
                </span>
              </div>
              <h3 class="font-bold text-gray-900 text-sm">{{ item.title }}</h3>
              <p class="text-xs text-gray-500">Lokasi: {{ item.location }}</p>
            </div>

            <!-- Tombol Aksi Kelola -->
            <div class="flex items-center gap-2 w-full sm:w-auto justify-end">
              <button class="bg-white border border-gray-200 hover:bg-gray-100 text-gray-700 text-xs font-bold px-3 py-2 rounded-lg transition">
                ✏️ Edit
              </button>
              <button class="bg-white border border-red-200 hover:bg-red-50 text-red-600 text-xs font-bold px-3 py-2 rounded-lg transition">
                🗑️ Hapus
              </button>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
// Mock data aset milik user yang login
const myAssets = ref([
  {
    id: 1,
    title: 'Tabung Oksigen 1m3 + Regulator',
    category: 'Darurat Medis',
    isAvailable: true,
    location: 'Purwokerto Utara, Banyumas'
  },
  {
    id: 2,
    title: 'Kursi Roda Lipat Standar',
    category: 'Alat Evakuasi',
    isAvailable: false,
    location: 'Purwokerto Selatan, Banyumas'
  },
  {
    id: 3,
    title: 'Ambulans Siaga Komunitas',
    category: 'Ambulans Gratis',
    isAvailable: true,
    location: 'Banyumas Raya'
  }
])
</script>