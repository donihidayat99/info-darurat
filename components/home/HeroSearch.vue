<template>
  <section class="bg-gradient-to-b from-red-50 to-white py-12 lg:py-16 border-b border-gray-100">
    <div class="container mx-auto px-4 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
      
      <!-- Teks Utama -->
      <div class="lg:col-span-7 space-y-4">
        <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black text-gray-900 tracking-tight leading-tight">
          Temukan Bantuan & <span class="text-red-600">Layanan Darurat</span> Cepat
        </h1>
        <p class="text-gray-600 text-base sm:text-lg">
          Akses direktori posko siaga, alat evakuasi, fasilitas medis, dan kontak darurat di seluruh Indonesia secara real-time dan offline-first.
        </p>

        <!-- Kotak Pencarian Utama -->
        <div class="bg-white p-3 rounded-2xl shadow-xl border border-gray-100 mt-6">
          <form @submit.prevent="handleSearch" class="grid grid-cols-1 sm:grid-cols-12 gap-3">
            
            <!-- Input Kata Kunci / Keperluan -->
            <div class="sm:col-span-4 relative">
              <input 
                v-model="searchQuery" 
                type="text" 
                placeholder="Cari alat / posko..." 
                class="w-full pl-3 pr-3 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-red-500 text-sm"
              />
            </div>

            <!-- Select Kategori -->
            <div class="sm:col-span-3">
              <select 
                v-model="selectedCategory" 
                class="w-full px-3 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-red-500 text-sm text-gray-700 bg-white"
              >
                <option value="">Semua Kategori</option>
                <option value="medis">Darurat Medis</option>
                <option value="sar">SAR & Evakuasi</option>
                <option value="pemadam">Pemadam Kebakaran</option>
                <option value="bencana">Posko Bencana</option>
                <option value="logistik">Bantuan Logistik</option>
              </select>
            </div>

            <!-- Cascade Dropdown Wilayah (Provinsi/Kabupaten) -->
            <div class="sm:col-span-3">
              <select 
                v-model="selectedLocation" 
                class="w-full px-3 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-red-500 text-sm text-gray-700 bg-white"
              >
                <option value="">Semua Wilayah</option>
                <option value="jateng">Jawa Tengah</option>
                <option value="jabar">Jawa Barat</option>
                <option value="jatim">Jawa Timur</option>
                <option value="dki">DKI Jakarta</option>
              </select>
            </div>

            <!-- Tombol Cari -->
            <div class="sm:col-span-2">
              <button 
                type="submit" 
                class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-3 px-4 rounded-xl transition duration-200 text-sm shadow-md flex items-center justify-center gap-1"
              >
                🔍 Cari
              </button>
            </div>

          </form>
        </div>
      </div>

      <!-- Ilustrasi / Banner Samping -->
      <div class="lg:col-span-5 flex justify-center">
        <div class="bg-red-100 rounded-3xl p-8 text-center relative overflow-hidden border border-red-200 w-full max-w-md">
          <div class="text-6xl mb-4">🚨</div>
          <h3 class="text-xl font-bold text-red-800 mb-2">Pusat Layanan Siaga 24 Jam</h3>
          <p class="text-xs text-red-600 mb-4">Gunakan fitur offline PWA untuk menyimpan kontak penting di HP Anda agar tetap bisa diakses tanpa sinyal.</p>
          <NuxtLink to="/locations" class="inline-block bg-red-600 text-white text-xs font-bold px-4 py-2 rounded-lg shadow hover:bg-red-700">
            Cek Peta Wilayah ➔
          </NuxtLink>
        </div>
      </div>

    </div>
  </section>
</template>

<script setup>
const searchQuery = ref('')
const selectedCategory = ref('')
const selectedLocation = ref('')

const router = useRouter()

const handleSearch = () => {
  router.push({
    path: '/listings',
    query: {
      q: searchQuery.value,
      category: selectedCategory.value,
      location: selectedLocation.value
    }
  })
}
</script>