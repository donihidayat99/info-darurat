<template>
  <div class="bg-gray-50 min-h-screen py-8">
    <div class="container mx-auto px-4 max-w-3xl space-y-6">
      
      <!-- Navigasi Kembali -->
      <div>
        <NuxtLink to="/dashboard" class="text-xs font-bold text-gray-600 hover:text-red-600 flex items-center gap-1">
          ← Kembali ke Dashboard
        </NuxtLink>
      </div>

      <!-- Form Card -->
      <div class="bg-white p-6 sm:p-8 rounded-2xl border border-gray-100 shadow-sm space-y-6">
        <div>
          <span class="bg-red-50 text-red-600 text-xs font-bold px-2.5 py-1 rounded-md uppercase">
            Formulir Publikasi
          </span>
          <h1 class="text-2xl font-black text-gray-900 mt-2">Tambah Aset Bantuan Baru</h1>
          <p class="text-xs text-gray-500 mt-1">
            Daftarkan alat medis, kendaraan, atau fasilitas darurat yang Anda miliki agar dapat diakses warga yang membutuhkan.
          </p>
        </div>

        <form @submit.prevent="handleSubmit" class="space-y-4">
          
          <!-- Judul Aset -->
          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Nama Aset / Layanan Bantuan *</label>
            <input 
              type="text" 
              placeholder="Contoh: Tabung Oksigen 1m3 / Ambulans Siaga" 
              class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
              required
            />
          </div>

          <!-- Kategori & Tipe Pendaftar -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Kategori Bantuan *</label>
              <select class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs text-gray-700 bg-white focus:ring-2 focus:ring-red-500 focus:outline-none">
                <option>Darurat Medis</option>
                <option>SAR & Evakuasi</option>
                <option>Pemadam Kebakaran</option>
                <option>Bantuan Logistik</option>
                <option>Ambulans Gratis</option>
              </select>
            </div>
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Status Kepemilikan *</label>
              <select class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs text-gray-700 bg-white focus:ring-2 focus:ring-red-500 focus:outline-none">
                <option>Personal / Warga</option>
                <option>Lembaga / Yayasan Sosial</option>
                <option>Instansi Pemerintah</option>
              </select>
            </div>
          </div>

          <!-- Status Biaya -->
          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Status / Jenis Biaya Peminjaman *</label>
            <select class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs text-gray-700 bg-white focus:ring-2 focus:ring-red-500 focus:outline-none">
              <option value="Gratis">100% Gratis (Bantuan Kemanusiaan)</option>
              <option value="Sukarela">Ikhlas / Sukarela</option>
              <option value="Berbayar / Ganti Operasional">Berbayar (Penggantian BBM / Operasional)</option>
            </select>
          </div>

          <!-- Upload Foto Fisik Aset (Opsional dengan Auto-Kompresi) -->
          <div class="p-4 bg-gray-50 rounded-xl border border-gray-200 space-y-2">
            <label class="block text-xs font-semibold text-gray-800">Foto Fisik Objek / Alat (Opsional)</label>
            <input 
              type="file" 
              accept="image/*"
              @change="handleFileUpload"
              class="w-full text-xs text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-bold file:bg-red-50 file:text-red-600 hover:file:bg-red-100 cursor-pointer"
            />
            <p class="text-[11px] text-gray-400">
              💡 <strong>Info Sistem:</strong> Foto apa pun yang Anda unggah akan otomatis dikompresi oleh sistem menjadi ukuran ringan berformat WebP agar akses warga tetap kilat. Jika dikosongkan, sistem otomatis menampilkan ikon kategori tematik.
            </p>
          </div>

          <!-- Wilayah / Lokasi -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Kabupaten / Kota *</label>
              <input 
                type="text" 
                placeholder="Contoh: Kab. Banyumas" 
                class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
                required
              />
            </div>
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Nomor Telepon / WhatsApp *</label>
              <input 
                type="text" 
                placeholder="Contoh: 081234567890" 
                class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
                required
              />
            </div>
          </div>

          <!-- Alamat Lengkap -->
          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Alamat Lengkap / Patokan Lokasi *</label>
            <input 
              type="text" 
              placeholder="Contoh: Jl. Serayu No. 12, Sumampir, Purwokerto Utara" 
              class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
              required
            />
          </div>

          <!-- Deskripsi & Syarat Peminjaman -->
          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Deskripsi & Catatan / Syarat Peminjaman *</label>
            <textarea 
              rows="4"
              placeholder="Jelaskan kondisi alat, rincian biaya jika ada, serta syarat peminjamannya..." 
              class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
              required
            ></textarea>
          </div>

          <!-- Tombol Submit -->
          <div class="pt-4 flex items-center justify-end gap-3">
            <NuxtLink to="/dashboard" class="px-5 py-2.5 rounded-xl border border-gray-200 text-xs font-bold text-gray-600 hover:bg-gray-100">
              Batal
            </NuxtLink>
            <button 
              type="submit" 
              class="bg-red-600 hover:bg-red-700 text-white font-bold text-xs px-6 py-2.5 rounded-xl shadow-md transition"
            >
              Simpan & Publikasikan Aset
            </button>
          </div>

        </form>
      </div>

    </div>
  </div>
</template>

<script setup>
const router = useRouter()

const handleFileUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    // Simulasi proses auto-kompresi di latar belakang
    console.log(`Mengompresi file ${file.name} (${(file.size / 1024 / 1024).toFixed(2)} MB)...`)
    // Di backend nanti, file akan di-resize dan dikonversi ke WebP otomatis
  }
}

const handleSubmit = () => {
  alert('Aset Bantuan berhasil ditambahkan dengan sistem auto-kompresi gambar!')
  router.push('/dashboard')
}
</script>