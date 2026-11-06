<template>
  <div class="bg-gray-50 min-h-screen py-8">
    <div class="container mx-auto px-4 max-w-3xl space-y-6">
      
      <!-- Navigasi Kembali -->
      <div>
        <NuxtLink to="/" class="text-xs font-bold text-gray-600 hover:text-red-600 flex items-center gap-1">
          ← Kembali ke Beranda
        </NuxtLink>
      </div>

      <!-- Card Utama Laporan Darurat -->
      <div class="bg-white p-6 sm:p-8 rounded-2xl border border-red-100 shadow-sm space-y-6">
        
        <!-- Header Banner Darurat -->
        <div class="bg-red-50 p-4 rounded-xl border border-red-200 flex items-start gap-3">
          <span class="text-3xl">🚨</span>
          <div>
            <span class="bg-red-600 text-white text-[10px] font-bold px-2 py-0.5 rounded uppercase tracking-wider">
              Laporan Respon Cepat
            </span>
            <h1 class="text-xl sm:text-2xl font-black text-gray-900 mt-1">Kirim Laporan Kejadian Darurat</h1>
            <p class="text-xs text-red-700 mt-0.5">
              Laporan ini akan langsung diteruskan ke jaringan Mitra Darurat (Damkar, SAR, PMI, Ambulans) terdekat.
            </p>
          </div>
        </div>

        <form @submit.prevent="handleSubmitReport" class="space-y-4">
          
          <!-- Jenis Kejadian Darurat -->
          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Jenis Kejadian / Kebutuhan *</label>
            <select 
              v-model="form.type"
              class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs text-gray-800 bg-white focus:ring-2 focus:ring-red-500 focus:outline-none font-medium"
              required
            >
              <option value="" disabled>-- Pilih Jenis Darurat --</option>
              <option value="Kebakaran">🔥 Kebakaran</option>
              <option value="Kecelakaan / Evakuasi">🚑 Kecelakaan / Butuh Ambulans Medis</option>
              <option value="Bencana Alam (Banjir/Longsor)">🌊 Bencana Alam (Banjir / Longsor / Pohon Tumbang)</option>
              <option value="Pencarian & Pertolongan (SAR)">🛶 Pertolongan Orang Hilang / Tenggelam (SAR)</option>
              <option value="Kebutuhan Alat Medis Mendesak">💊 Kebutuhan Alat Medis / Oksigen Mendesak</option>
              <option value="Lainnya">⚠️ Keadaan Darurat Lainnya</option>
            </select>
          </div>

          <!-- Informasi Pelapor & Kontak -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Nama Pelapor *</label>
              <input 
                v-model="form.reporterName"
                type="text" 
                placeholder="Nama Anda / Saksi Mata" 
                class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
                required
              />
            </div>
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Nomor WhatsApp / Telp Aktif *</label>
              <input 
                v-model="form.reporterPhone"
                type="text" 
                placeholder="Contoh: 081234567890" 
                class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
                required
              />
            </div>
          </div>

          <!-- Fitur Deteksi Lokasi Otomatis (GPS) -->
          <div class="p-4 bg-gray-50 rounded-xl border border-gray-200 space-y-3">
            <div class="flex justify-between items-center">
              <label class="text-xs font-bold text-gray-800 flex items-center gap-1">
                📍 Lokasi Kejadian Presisi *
              </label>
              <button 
                type="button"
                @click="detectLocation"
                class="bg-red-50 hover:bg-red-100 text-red-600 text-[11px] font-bold px-3 py-1.5 rounded-lg border border-red-200 transition flex items-center gap-1"
              >
                🎯 {{ isLocating ? 'Mendeteksi GPS...' : 'Gunakan Lokasi GPS Saya' }}
              </button>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <input 
                v-model="form.district"
                type="text" 
                placeholder="Kecamatan / Kelurahan (Contoh: Purwokerto Utara)" 
                class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none bg-white"
                required
              />
              <input 
                v-model="form.city"
                type="text" 
                placeholder="Kabupaten / Kota (Contoh: Kab. Banyumas)" 
                class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none bg-white"
                required
              />
            </div>

            <textarea 
              v-model="form.fullAddress"
              rows="2"
              placeholder="Detail patokan lokasi (Contoh: Depan Masjid Al-Ikhlas, Jl. Serayu No. 12)" 
              class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none bg-white"
              required
            ></textarea>
          </div>

          <!-- Detail Deskripsi Kejadian -->
          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Deskripsi & Jumlah Korban / Kondisi Lapangan *</label>
            <textarea 
              v-model="form.description"
              rows="3"
              placeholder="Jelaskan situasi singkat, kondisi korban, atau bantuan mendesak yang dibutuhkan..." 
              class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
              required
            ></textarea>
          </div>

          <!-- Upload Foto Kejadian (Auto-Kompresi & Fallback) -->
          <div class="p-4 bg-gray-50 rounded-xl border border-gray-200 space-y-2">
            <label class="block text-xs font-semibold text-gray-800">Upload Foto Kondisi Lapangan (Opsional)</label>
            <input 
              type="file" 
              accept="image/*"
              @change="handleImageUpload"
              class="w-full text-xs text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-xl file:border-0 file:text-xs file:font-bold file:bg-red-50 file:text-red-600 hover:file:bg-red-100 cursor-pointer"
            />
            <p class="text-[11px] text-gray-400">
              💡 Foto akan otomatis dikompresi oleh sistem agar terproses kilat di HP Mitra Darurat. Jika tidak ada foto, sistem akan menggunakan ikon kategori darurat secara otomatis.
            </p>
          </div>

          <!-- Tombol Kirim Laporan -->
          <div class="pt-4 flex items-center justify-end gap-3 border-t border-gray-100">
            <NuxtLink to="/" class="px-5 py-3 rounded-xl border border-gray-200 text-xs font-bold text-gray-600 hover:bg-gray-100">
              Batal
            </NuxtLink>
            <button 
              type="submit" 
              class="w-full sm:w-auto bg-red-600 hover:bg-red-700 text-white font-bold text-xs px-8 py-3 rounded-xl shadow-md transition flex items-center justify-center gap-2"
            >
              🚨 Kirim Laporan Darurat Sekarang
            </button>
          </div>

        </form>

      </div>
    </div>
  </div>
</template>

<script setup>
const router = useRouter()
const isLocating = ref(false)

const form = ref({
  type: '',
  reporterName: '',
  reporterPhone: '',
  district: '',
  city: '',
  fullAddress: '',
  description: '',
  image: null
})

// Simulasi Deteksi GPS Warga
const detectLocation = () => {
  isLocating.value = true
  setTimeout(() => {
    form.value.district = 'Purwokerto Utara'
    form.value.city = 'Kab. Banyumas'
    form.value.fullAddress = 'Jl. Serayu, Sumampir (Terdeteksi via GPS)'
    isLocating.value = false
    alert('📍 Lokasi GPS Anda berhasil dideteksi!')
  }, 1000)
}

const handleImageUpload = (e) => {
  const file = e.target.files[0]
  if (file) {
    console.log(`Mengompresi foto laporan ${file.name}...`)
  }
}

const handleSubmitReport = () => {
  alert('🚨 Laporan Darurat berhasil dikirim! Tim Mitra Darurat terdekat akan segera menghubungi kontak Anda.')
  router.push('/')
}
</script>