<template>
  <div class="bg-gray-50 min-h-screen py-8">
    <div class="container mx-auto px-4 max-w-xl space-y-6">
      
      <!-- Tombol Kembali ke Detail Bantuan -->
      <div>
        <NuxtLink :to="`/listings/${listingId}`" class="text-xs font-bold text-gray-600 hover:text-red-600 flex items-center gap-1 cursor-pointer">
          ← Kembali ke Detail Bantuan
        </NuxtLink>
      </div>

      <!-- Kartu Form -->
      <div class="bg-white p-6 sm:p-8 rounded-2xl border border-gray-100 shadow-sm space-y-6">
        
        <div>
          <span class="bg-blue-50 text-blue-600 text-[10px] font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">
            🔒 Privasi Mitra Terjaga
          </span>
          <h1 class="text-xl sm:text-2xl font-black text-gray-900 mt-2">Kirim Pesan Bantuan</h1>
          <p class="text-xs text-gray-500 mt-1">
            Pesan Anda untuk listing ID <strong class="text-gray-800">#{{ listingId }}</strong> akan diteruskan secara rahasia kepada mitra penolong.
          </p>
        </div>

        <!-- State Sukses -->
        <div v-if="isSubmitted" class="bg-green-50 p-6 rounded-2xl text-center space-y-3">
          <div class="text-4xl">✅</div>
          <h4 class="font-bold text-green-900 text-sm">Pesan Berhasil Terkirim!</h4>
          <p class="text-xs text-green-700 leading-relaxed">
            Mitra penolong telah menerima notifikasi pesan Anda. Mereka akan segera menghubungi nomor WhatsApp Anda.
          </p>
          
          <!-- Tombol Aksi Setelah Sukses -->
          <div class="flex flex-col sm:flex-row items-center justify-center gap-2 pt-2">
            <NuxtLink 
              :to="`/listings/${listingId}`"
              class="w-full sm:w-auto bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold text-xs px-4 py-2.5 rounded-xl transition cursor-pointer"
            >
              Lihat Detail Bantuan
            </NuxtLink>
            <NuxtLink 
              to="/listings"
              class="w-full sm:w-auto bg-green-600 hover:bg-green-700 text-white font-bold text-xs px-5 py-2.5 rounded-xl transition cursor-pointer"
            >
              Kembali ke Direktori
            </NuxtLink>
          </div>
        </div>

        <!-- Form Input -->
        <form v-else @submit.prevent="submitForm" class="space-y-4">
          
          <div>
            <label class="block text-xs font-bold text-gray-700 uppercase tracking-wider mb-1.5">
              Nama Lengkap Anda
            </label>
            <input 
              v-model="form.senderName" 
              type="text" 
              placeholder="Contoh: Budi Santoso"
              class="w-full px-4 py-3 rounded-xl border border-gray-200 text-xs sm:text-sm text-gray-900 focus:border-red-500 focus:outline-none transition font-medium"
              required
            />
          </div>

          <div>
            <label class="block text-xs font-bold text-gray-700 uppercase tracking-wider mb-1.5">
              Nomor WhatsApp / HP Aktif
            </label>
            <input 
              v-model="form.senderPhone" 
              type="text" 
              placeholder="Contoh: 081234567890"
              class="w-full px-4 py-3 rounded-xl border border-gray-200 text-xs sm:text-sm text-gray-900 focus:border-red-500 focus:outline-none transition font-medium"
              required
            />
            <p class="text-[10px] text-gray-400 mt-1">Nomor ini aman dan hanya akan dilihat oleh mitra penolong terkait.</p>
          </div>

          <div>
            <label class="block text-xs font-bold text-gray-700 uppercase tracking-wider mb-1.5">
              Detail Kebutuhan Bantuan
            </label>
            <textarea 
              v-model="form.message" 
              rows="4" 
              placeholder="Jelaskan kebutuhan Anda secara rinci, misal lokasi dan waktu mendesak..."
              class="w-full px-4 py-3 rounded-xl border border-gray-200 text-xs sm:text-sm text-gray-900 focus:border-red-500 focus:outline-none transition font-medium"
              required
            ></textarea>
          </div>

          <p v-if="errorMessage" class="text-xs font-bold text-red-600 bg-red-50 p-3 rounded-xl text-center">
            {{ errorMessage }}
          </p>

          <button 
            type="submit" 
            :disabled="loading"
            class="w-full py-3.5 bg-red-600 hover:bg-red-700 text-white font-bold text-xs sm:text-sm rounded-xl transition shadow-sm cursor-pointer disabled:opacity-50 flex items-center justify-center gap-2"
          >
            <span v-if="loading" class="animate-spin text-sm">🌀</span>
            <span>{{ loading ? 'Mengirim Pesan...' : 'Kirim Pesan Sekarang' }}</span>
          </button>

        </form>

      </div>

    </div>
  </div>
</template>

<script setup>
const route = useRoute()
const listingId = route.params.id

const loading = ref(false)
const isSubmitted = ref(false)
const errorMessage = ref('')

const form = ref({
  senderName: '',
  senderPhone: '',
  message: ''
})

const submitForm = async () => {
  loading.value = true
  errorMessage.value = ''

  try {
    // Simulasi pengiriman data ke server
    await new Promise(resolve => setTimeout(resolve, 1000))
    isSubmitted.value = true
  } catch (err) {
    errorMessage.value = '❌ Gagal mengirim pesan. Silakan coba lagi.'
  } finally {
    loading.value = false
  }
}
</script>
