<template>
  <div class="bg-gray-50 min-h-screen py-10">
    <div class="container mx-auto px-4 max-w-5xl space-y-12">
      
      <!-- 1. Hero / Header Donasi -->
      <div class="text-center space-y-4 max-w-2xl mx-auto">
        <span class="bg-red-50 text-red-600 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider">
          Gotong Royong & Transparansi
        </span>
        <h1 class="text-3xl sm:text-4xl font-black text-gray-900 tracking-tight">
          Dukungan Operasional & <span class="text-red-600">Mitra Kolaborasi</span>
        </h1>
        <p class="text-gray-600 text-sm sm:text-base leading-relaxed">
          Platform Info Darurat dikelola secara publik untuk memastikan setiap warga mendapatkan akses **Aset Bantuan** secara gratis, cepat, dan tanpa hambatan.
        </p>
      </div>

      <!-- 2. Alokasi Transparansi Penggunaan Dana -->
      <div class="bg-white p-6 sm:p-8 rounded-2xl border border-gray-100 shadow-sm space-y-6">
        <h2 class="text-xl font-bold text-gray-900 border-b border-gray-100 pb-3">
          💡 Transparansi Alokasi Dukungan
        </h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="p-4 bg-gray-50 rounded-xl border border-gray-100 space-y-2">
            <div class="text-2xl">🖥️</div>
            <h3 class="font-bold text-gray-800 text-sm">Server & PWA Infrastructure</h3>
            <p class="text-xs text-gray-500">Menjaga server tetap aktif 24/7 dan mengoptimalkan mode akses offline PWA saat bencana.</p>
          </div>
          <div class="p-4 bg-gray-50 rounded-xl border border-gray-100 space-y-2">
            <div class="text-2xl">🛡️</div>
            <h3 class="font-bold text-gray-800 text-sm">Verifikasi Mitra Darurat</h3>
            <p class="text-xs text-gray-500">Biaya verifikasi validitas data lembaga maupun personal pendaftar Aset Bantuan.</p>
          </div>
          <div class="p-4 bg-gray-50 rounded-xl border border-gray-100 space-y-2">
            <div class="text-2xl">📢</div>
            <h3 class="font-bold text-gray-800 text-sm">Edukasi & Sosialisasi</h3>
            <p class="text-xs text-gray-500">Penyebaran materi mitigasi bencana dan panduan kesiapsiagaan darurat ke masyarakat.</p>
          </div>
        </div>
      </div>

      <!-- 3. Rekening & Rekening Donasi -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Rekening Bank -->
        <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-4">
          <h3 class="font-bold text-gray-900 text-base flex items-center gap-2">
            💳 Transfer Bank Resmi
          </h3>
          <div class="p-4 bg-red-50/50 rounded-xl border border-red-100 space-y-3 text-xs">
            <div class="flex justify-between items-center">
              <span class="text-gray-500">Bank:</span>
              <span class="font-bold text-gray-800">Bank Syariah Indonesia (BSI)</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-gray-500">No. Rekening:</span>
              <strong class="text-red-600 font-mono text-sm">7123-4567-89</strong>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-gray-500">Atas Nama:</span>
              <span class="font-semibold text-gray-800">Yayasan Info Darurat Indonesia</span>
            </div>
          </div>
          <p class="text-[11px] text-gray-400">
            *Harap tambahkan kode unik <strong>011</strong> di akhir nominal (contoh: Rp100.011) untuk konfirmasi otomatis.
          </p>
        </div>

        <!-- Dompet Digital / QRIS -->
        <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-4">
          <h3 class="font-bold text-gray-900 text-base flex items-center gap-2">
            📱 QRIS / Dompet Digital
          </h3>
          <div class="p-4 bg-gray-50 rounded-xl border border-gray-100 flex items-center gap-4">
            <div class="w-24 h-24 bg-white p-2 rounded-lg border border-gray-200 flex items-center justify-center font-bold text-xs text-gray-400">
              [ QRIS Code ]
            </div>
            <div class="text-xs space-y-1">
              <p class="font-bold text-gray-800">Scan via GoPay, OVO, Dana, LinkAja, atau Mobile Banking</p>
              <p class="text-gray-500">Mendukung seluruh aplikasi pembayaran resmi berstandar QRIS Indonesia.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 4. Perusahaan & Lembaga Mitra Kolaborasi -->
      <div class="bg-white p-6 sm:p-8 rounded-2xl border border-gray-100 shadow-sm space-y-6">
        <div class="text-center space-y-2">
          <h2 class="text-2xl font-bold text-gray-900">Mitra Kolaborasi Kemanusiaan</h2>
          <p class="text-xs text-gray-500">
            Perusahaan, organisasi sosial, dan instansi yang berkolaborasi mendukung keberlangsungan platform dan jaringan Mitra Darurat.
          </p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4 pt-4">
          <div v-for="(partner, i) in partners" :key="i" class="p-4 rounded-xl border border-gray-100 bg-gray-50/60 flex flex-col items-center justify-center text-center space-y-2 hover:border-red-200 transition">
            <div class="w-12 h-12 rounded-full bg-white shadow-sm flex items-center justify-center text-xl">
              {{ partner.icon }}
            </div>
            <span class="font-bold text-xs text-gray-800">{{ partner.name }}</span>
            <span class="text-[10px] text-gray-400">{{ partner.type }}</span>
          </div>
        </div>
      </div>

      <!-- 5. Call To Action (Survei Dukungan & Feedback) -->
      <div class="bg-gradient-to-r from-red-600 to-red-700 text-white p-8 rounded-2xl text-center space-y-4 shadow-lg">
        <h3 class="text-xl sm:text-2xl font-bold">Punya Masukan atau Ingin Berkolaborasi?</h3>
        <p class="text-xs sm:text-sm text-red-100 max-w-xl mx-auto">
          Kami terus berusaha meningkatkan kualitas layanan. Bantu kami dengan mengisi survei singkat pengguna & mitra di bawah ini!
        </p>
        <div class="pt-2">
          <a 
            href="#survei" 
            class="inline-block bg-white text-red-600 hover:bg-red-50 font-bold text-xs px-6 py-3 rounded-xl shadow-sm transition"
          >
            📋 Isi Survei Masukan Pengguna
          </a>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
// Mock data lembaga & perusahaan mitra kolaborasi
const partners = [
  { name: 'BASARNAS Jawa Tengah', type: 'Instansi Pemerintah', icon: '🛶' },
  { name: 'Dinas Kesehatan Banyumas', type: 'Instansi Kesehatan', icon: '🏥' },
  { name: 'PMI Kabupaten Banyumas', type: 'Organisasi Sosial', icon: '🩸' },
  { name: 'Damkar Purwokerto Utara', type: 'Layanan Keamanan', icon: '🚒' },
  { name: 'Kaffah Herbal Indonesia', type: 'Mitra Perusahaan', icon: '🌿' },
  { name: 'Komunitas Relawan Banyumas', type: 'Komunitas Warga', icon: '🤝' },
  { name: 'Yayasan Ambulans Gratis', type: 'Layanan Kemanusiaan', icon: '🚑' },
  { name: 'Posko Siaga Bencana', type: 'Komunitas Lokal', icon: '🏕️' }
]
</script>