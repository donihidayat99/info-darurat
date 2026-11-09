<template>
  <div class="bg-gray-50 min-h-screen py-8">
    <div class="container mx-auto px-4 max-w-3xl space-y-6">
      
      <!-- Navigasi Kembali -->
      <div>
        <NuxtLink to="/dashboard" class="text-xs font-bold text-gray-600 hover:text-red-600 flex items-center gap-1">
          ← Kembali ke Dashboard
        </NuxtLink>
      </div>

      <!-- Header Kartu -->
      <div class="bg-white p-6 sm:p-8 rounded-2xl border border-gray-100 shadow-sm space-y-6">
        <div>
          <span class="bg-red-50 text-red-600 text-xs font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">
            Pengaturan Akun & Privasi
          </span>
          <h1 class="text-2xl font-black text-gray-900 mt-2">Profil Mitra Penolong</h1>
          <p class="text-xs sm:text-sm text-gray-500 mt-1">
            Kelola informasi profil dan atur bagaimana warga dapat menghubungi Anda saat membutuhkan bantuan.
          </p>
        </div>

        <!-- Form Profil -->
        <form @submit.prevent="updateProfile" class="space-y-5">
          
          <!-- Nama Organisasi / Mitra -->
          <div>
            <label class="block text-xs font-bold text-gray-700 uppercase tracking-wider mb-2">
              Nama Organisasi / Mitra Penolong
            </label>
            <input 
              v-model="profile.name" 
              type="text" 
              placeholder="Contoh: Relawan Kemanusiaan Purwokerto"
              class="w-full px-4 py-3 rounded-xl border border-gray-200 text-xs sm:text-sm text-gray-900 focus:border-red-500 focus:outline-none transition font-medium"
              required
            />
          </div>

          <!-- Nomor WhatsApp -->
          <div>
            <label class="block text-xs font-bold text-gray-700 uppercase tracking-wider mb-2">
              Nomor WhatsApp Utama
            </label>
            <input 
              v-model="profile.whatsapp" 
              type="text" 
              placeholder="Contoh: 6281234567890"
              class="w-full px-4 py-3 rounded-xl border border-gray-200 text-xs sm:text-sm text-gray-900 focus:border-red-500 focus:outline-none transition font-medium"
            />
            <p class="text-[11px] text-gray-400 mt-1">Gunakan awalan kode negara (62...), tanpa tanda plus (+).</p>
          </div>

          <!-- Email Kontak -->
          <div>
            <label class="block text-xs font-bold text-gray-700 uppercase tracking-wider mb-2">
              Alamat Email (Untuk Notifikasi Bantuan)
            </label>
            <input 
              v-model="profile.email" 
              type="email" 
              placeholder="contoh@domain.com"
              class="w-full px-4 py-3 rounded-xl border border-gray-200 text-xs sm:text-sm text-gray-900 focus:border-red-500 focus:outline-none transition font-medium"
              required
            />
          </div>

          <!-- 🔥 FITUR BARU: Preferensi Kontak & Privasi -->
          <div class="pt-4 border-t border-gray-100 space-y-3">
            <div>
              <label class="block text-xs font-bold text-gray-900 uppercase tracking-wider">
                Preferensi Saluran Kontak Warga
              </label>
              <p class="text-xs text-gray-500 mt-0.5">
                Pilih bagaimana warga dapat menghubungi Anda pada setiap listing bantuan yang Anda buat.
              </p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
              
              <!-- Opsi 1: WhatsApp Direct -->
              <label 
                :class="profile.contact_preference === 'wa_direct' ? 'border-red-600 bg-red-50/40 ring-2 ring-red-500/20' : 'border-gray-200 bg-white'"
                class="flex flex-col p-4 rounded-xl border cursor-pointer transition space-y-1"
              >
                <div class="flex items-center justify-between">
                  <span class="font-bold text-xs text-gray-900">🟢 WhatsApp Direct</span>
                  <input type="radio" v-model="profile.contact_preference" value="wa_direct" class="text-red-600 focus:ring-red-500" />
                </div>
                <p class="text-[11px] text-gray-500 leading-relaxed">
                  Tombol langsung mengarah ke aplikasi WhatsApp Anda. Nomor HP terlihat oleh publik.
                </p>
              </label>

              <!-- Opsi 2: Email Form (Jaga Privasi) -->
              <label 
                :class="profile.contact_preference === 'email_form' ? 'border-red-600 bg-red-50/40 ring-2 ring-red-500/20' : 'border-gray-200 bg-white'"
                class="flex flex-col p-4 rounded-xl border cursor-pointer transition space-y-1"
              >
                <div class="flex items-center justify-between">
                  <span class="font-bold text-xs text-gray-900">✉️ Form Email (Privasi)</span>
                  <input type="radio" v-model="profile.contact_preference" value="email_form" class="text-red-600 focus:ring-red-500" />
                </div>
                <p class="text-[11px] text-gray-500 leading-relaxed">
                  Warga mengirim pesan via form pop-up web. Nomor HP Anda aman dan disembunyikan.
                </p>
              </label>

            </div>
          </div>

          <!-- Tombol Simpan -->
          <div class="pt-4">
            <button 
              type="submit" 
              :disabled="loading"
              class="w-full py-3.5 bg-red-600 hover:bg-red-700 text-white font-bold text-xs sm:text-sm rounded-xl transition shadow-sm cursor-pointer disabled:opacity-50"
            >
              {{ loading ? 'Menyimpan Perubahan...' : 'Simpan Pengaturan Profil' }}
            </button>
          </div>

          <!-- Pesan Sukses / Error -->
          <p v-if="feedbackMessage" :class="isError ? 'text-red-600 bg-red-50' : 'text-green-600 bg-green-50'" class="p-3 rounded-xl text-xs font-bold text-center">
            {{ feedbackMessage }}
          </p>

        </form>
      </div>

    </div>
  </div>
</template>

<script setup>
const loading = ref(false)
const feedbackMessage = ref('')
const isError = ref(false)

// Mock Data Profil Mitra (Nanti dihubungkan ke Supabase tabel profiles)
const profile = ref({
  name: 'Relawan Kemanusiaan Purwokerto',
  whatsapp: '6281234567890',
  email: 'relawan@infodarurat.id',
  contact_preference: 'email_form' // Default pilihan privasi
})

const updateProfile = async () => {
  loading.value = true
  feedbackMessage.value = ''
  
  try {
    // Simulasi simpan data ke database Supabase
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    // TODO: Ganti dengan logika update database Supabase yang sebenarnya
    // const { error } = await client.from('profiles').update(profile.value).eq('id', userId)

    isError.value = false
    feedbackMessage.value = '✅ Pengaturan profil dan preferensi kontak berhasil diperbarui!'
  } catch (err) {
    isError.value = true
    feedbackMessage.value = '❌ Gagal menyimpan perubahan. Silakan coba lagi.'
  } finally {
    loading.value = false
  }
}
</script>