<template>
  <div class="bg-gray-50 min-h-screen py-8">
    <div class="container mx-auto px-4 max-w-5xl">
      
      <!-- Tombol Kembali & Breadcrumb (Tersinkron ke /listings) -->
      <div class="mb-6 flex items-center justify-between">
        <NuxtLink to="/listings" class="text-xs font-bold text-gray-600 hover:text-red-600 flex items-center gap-1 cursor-pointer">
          ← Kembali ke Pencarian & Direktori
        </NuxtLink>
        <span class="text-xs text-gray-400">ID Aset: #{{ listing.id }}</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <!-- Kolom Kiri: Detail Aset & Keterangan (8 Kolom) -->
        <div class="lg:col-span-8 space-y-6">
          
          <!-- Card Utama Detail -->
          <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-4">
            
            <!-- Tag Kategori & Badge Ketersediaan -->
            <div class="flex flex-wrap justify-between items-center gap-2">
              <span class="bg-red-50 text-red-600 text-xs font-bold px-3 py-1 rounded-lg">
                {{ listing.category }}
              </span>
              <span 
                :class="listing.isAvailable ? 'bg-emerald-50 text-emerald-600 border-emerald-200' : 'bg-amber-50 text-amber-600 border-amber-200'"
                class="text-xs font-bold px-3 py-1 rounded-lg border"
              >
                {{ listing.isAvailable ? '🟢 Siap Dipinjam / Digunakan' : '🟡 Sedang Dipakai / Terbatas' }}
              </span>
            </div>

            <!-- Judul Aset Bantuan -->
            <h1 class="text-2xl sm:text-3xl font-black text-gray-900 leading-tight">
              {{ listing.title }}
            </h1>

            <!-- Lokasi Singkat -->
            <p class="text-xs text-gray-500 flex items-center gap-1">
              <span>📍</span> {{ listing.location }}
            </p>

            <!-- Galeri Foto / Ilustrasi Aset -->
            <div class="h-64 sm:h-80 bg-gray-100 rounded-xl overflow-hidden flex items-center justify-center border border-gray-200 text-gray-400 text-sm">
              🖼️ Foto Alat / Kendaraan Darurat
            </div>

            <!-- Deskripsi & Ketentuan Peminjaman -->
            <div class="border-t border-gray-100 pt-4 space-y-3">
              <h2 class="font-bold text-gray-900 text-base">Deskripsi & Catatan Penolong</h2>
              <p class="text-xs text-gray-600 leading-relaxed whitespace-pre-line">
                {{ listing.description }}
              </p>
            </div>

            <!-- Spesifikasi / Fasilitas Aset -->
            <div class="border-t border-gray-100 pt-4">
              <h2 class="font-bold text-gray-900 text-base mb-3">Spesifikasi & Kondisi</h2>
              <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 text-xs">
                <div class="p-3 bg-gray-50 rounded-xl border border-gray-100">
                  <span class="text-gray-400 block mb-1">Status Kepemilikan</span>
                  <strong class="text-gray-800">{{ listing.ownerType }}</strong>
                </div>
                <div class="p-3 bg-gray-50 rounded-xl border border-gray-100">
                  <span class="text-gray-400 block mb-1">Biaya Layanan</span>
                  <strong class="text-emerald-600">{{ listing.cost }}</strong>
                </div>
                <div class="p-3 bg-gray-50 rounded-xl border border-gray-100">
                  <span class="text-gray-400 block mb-1">Cakupan Wilayah</span>
                  <strong class="text-gray-800">{{ listing.coverage }}</strong>
                </div>
              </div>
            </div>

          </div>

        </div>

        <!-- Kolom Kanan: Informasi Penolong & Akses Cepat (4 Kolom) -->
        <div class="lg:col-span-4 space-y-6">
          
          <!-- Card Profil Penolong / Penyedia -->
          <div class="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm space-y-4 sticky top-20">
            <h3 class="text-xs font-bold text-gray-400 uppercase tracking-wider">Informasi Penolong</h3>
            
            <div class="flex items-center gap-3">
              <div class="w-12 h-12 rounded-full bg-red-100 text-red-600 font-bold flex items-center justify-center text-lg">
                {{ listing.provider.charAt(0) }}
              </div>
              <div>
                <h4 class="font-bold text-gray-900 text-sm">{{ listing.provider }}</h4>
                <span class="text-xs text-emerald-600 font-medium">✓ Penolong Terverifikasi</span>
              </div>
            </div>

            <div class="border-t border-gray-100 pt-3 space-y-2 text-xs text-gray-600">
              <div class="flex justify-between">
                <span class="text-gray-400">Tipe Pendaftar:</span>
                <span class="font-semibold text-gray-800">{{ listing.ownerType }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-400">Respon Kontak:</span>
                <span class="font-semibold text-gray-800">Cepat (&lt; 15 menit)</span>
              </div>
            </div>

            <!-- Tombol Aksi Kontak Cepat -->
            <div class="space-y-2 border-t border-gray-100 pt-4">
              <a 
                :href="`tel:${listing.phone}`" 
                class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-3 px-4 rounded-xl text-xs transition duration-200 shadow-md flex items-center justify-center gap-2 cursor-pointer"
              >
                📞 Telepon Langsung
              </a>
              <a 
                :href="`https://wa.me/${listing.whatsapp}?text=Halo%20${listing.provider},%20saya%20butuh%20info%20terkait%20${listing.title}`" 
                target="_blank"
                class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3 px-4 rounded-xl text-xs transition duration-200 shadow-md flex items-center justify-center gap-2 cursor-pointer"
              >
                💬 Hubungi via WhatsApp
              </a>
            </div>

            <!-- Warning Keamanan -->
            <div class="p-3 bg-amber-50 rounded-xl border border-amber-200/60 text-[11px] text-amber-800">
              💡 <strong>Tips Keamanan:</strong> Selalu konfirmasi ketersediaan alat sebelum mendatangi lokasi. Jangan pernah mentransfer uang tanpa verifikasi resmi.
            </div>
          </div>

        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
const route = useRoute()

// Mock data detail aset bantuan (Nantinya diambil dari Database berdasarkan route.params.id)
const listing = ref({
  id: route.params.id || '1',
  title: 'Tabung Oksigen 1m3 + Regulator Siap Pakai',
  provider: 'Relawan Kemanusiaan Purwokerto',
  ownerType: 'Personal / Komunitas',
  category: 'Darurat Medis',
  isAvailable: true,
  cost: 'Gratis (Peminjaman)',
  coverage: 'Purwokerto & Sekitarnya',
  location: 'Jl. Serayu, Sumampir, Purwokerto Utara, Banyumas',
  phone: '081234567890',
  whatsapp: '6281234567890',
  description: `Tersedia 2 unit tabung oksigen ukuran 1m3 lengkap dengan regulator dan selang baru. 

Bisa dipinjamkan gratis untuk warga yang membutuhkan kondisi darurat medis di wilayah Purwokerto dan sekitarnya. 

Syarat Peminjaman:
1. Menunjukkan KTP Peminjam.
2. Surat rujukan / keterangan butuh oksigen dari fasilitas kesehatan (jika ada).
3. Pengambilan mandiri ke lokasi penolong.`
})
</script>