<template>
  <div class="bg-gray-50 min-h-[85vh] flex items-center justify-center py-12 px-4">
    <div class="max-w-md w-full bg-white p-8 rounded-2xl border border-gray-100 shadow-sm text-center space-y-6">
      
      <!-- Ilustrasi / Icon Jam Pasir -->
      <div class="w-20 h-20 bg-amber-50 text-amber-500 rounded-full flex items-center justify-center mx-auto text-4xl shadow-inner border border-amber-100">
        ⏳
      </div>

      <!-- Teks Informasi -->
      <div class="space-y-2">
        <span class="bg-amber-100 text-amber-800 text-[11px] font-bold px-3 py-1 rounded-full uppercase">
          Verifikasi Tertunda
        </span>
        <h1 class="text-2xl font-black text-gray-900 mt-2">Pendaftaran Sedang Ditinjau</h1>
        <p class="text-xs text-gray-500 leading-relaxed">
          Terima kasih telah mendaftar sebagai <strong>Mitra Darurat</strong>. Tim admin kami sedang melakukan verifikasi data dan legalitas penunjang Anda demi keamanan platform.
        </p>
      </div>

      <!-- Detail Status Box -->
      <div class="p-4 bg-gray-50 rounded-xl border border-gray-100 text-left space-y-2 text-xs text-gray-600">
        <div class="flex justify-between">
          <span class="text-gray-400">Estimasi Waktu:</span>
          <span class="font-semibold text-gray-800">1 x 24 Jam Kerja</span>
        </div>
        <div class="flex justify-between">
          <span class="text-gray-400">Status Akun:</span>
          <span class="font-semibold text-amber-600">Menunggu Review Admin</span>
        </div>
      </div>

      <!-- Tombol Aksi -->
      <div class="space-y-2 pt-2">
        <NuxtLink 
          to="/dashboard" 
          class="block w-full bg-red-600 hover:bg-red-700 text-white font-bold text-xs py-3 rounded-xl shadow-md transition"
        >
          Simulasi Masuk ke Dashboard (Demo)
        </NuxtLink>
        <NuxtLink 
          to="/" 
          class="block w-full bg-gray-100 hover:bg-gray-200 text-gray-700 font-bold text-xs py-3 rounded-xl transition"
        >
          Kembali ke Beranda
        </NuxtLink>
      </div>

    </div>
  </div>
</template>