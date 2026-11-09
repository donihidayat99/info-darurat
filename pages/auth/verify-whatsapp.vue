<template>
  <div class="bg-gray-50 min-h-screen py-12 flex items-center justify-center">
    <div class="container mx-auto px-4 max-w-md">
      
      <div class="bg-white p-8 rounded-2xl border border-gray-100 shadow-sm text-center space-y-6">
        
        <div class="w-16 h-16 bg-emerald-50 text-emerald-600 text-2xl font-bold rounded-2xl mx-auto flex items-center justify-center shadow-inner">
          🟢
        </div>

        <div class="space-y-2">
          <span class="bg-red-50 text-red-600 text-[10px] font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">
            Langkah Terakhir
          </span>
          <h1 class="text-xl font-black text-gray-900">Verifikasi WhatsApp Anda</h1>
          <p class="text-xs text-gray-500 leading-relaxed">
            Untuk mengaktifkan akun Mitra Penolong dan menerima notifikasi darurat warga, silakan verifikasi nomor WhatsApp Anda dengan mengeklik tombol di bawah ini.
          </p>
        </div>

        <!-- Tombol Buka WhatsApp -->
        <a 
          :href="whatsappVerificationUrl"
          target="_blank"
          class="w-full inline-flex items-center justify-center gap-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3.5 px-4 rounded-xl text-xs transition shadow-md cursor-pointer"
        >
          <span>💬 Kirim Pesan Verifikasi via WA</span>
        </a>

        <div class="p-4 bg-gray-50 rounded-xl border border-gray-100 text-left space-y-2">
          <h4 class="font-bold text-gray-800 text-xs">Petunjuk:</h4>
          <ol class="text-[11px] text-gray-500 space-y-1 list-decimal list-inside leading-relaxed">
            <li>Klik tombol hijau di atas untuk membuka aplikasi WhatsApp.</li>
            <li>Kirim pesan otomatis yang sudah disiapkan ke admin.</li>
            <li>Akun Anda akan otomatis terverifikasi oleh sistem setelah pesan terkirim.</li>
          </ol>
        </div>

        <div>
          <NuxtLink to="/dashboard" class="text-xs font-bold text-gray-600 hover:text-red-600 transition">
            ← Lewati sementara & ke Dashboard
          </NuxtLink>
        </div>

      </div>

    </div>
  </div>
</template>

<script setup>
// Ganti dengan nomor WhatsApp operasional admin Anda (format 62...)
const adminWhatsApp = '6281234567890'
const mitraId = '9876' // Nanti diambil dinamis dari user session

const whatsappVerificationUrl = computed(() => {
  const text = encodeURIComponent(`Halo Admin, saya ingin verifikasi akun Mitra Penolong Info Darurat dengan ID: #${mitraId}`)
  return `https://wa.me/${adminWhatsApp}?text=${text}`
})
</script>
