<template>
  <div class="bg-gray-50 min-h-screen py-8">
    <div class="container mx-auto px-4 max-w-4xl space-y-6">
      
      <!-- Navigasi Kembali ke Dashboard -->
      <div class="flex justify-between items-center">
        <NuxtLink to="/dashboard" class="text-xs font-bold text-gray-600 hover:text-red-600 flex items-center gap-1">
          ← Kembali ke Dashboard Utama
        </NuxtLink>
        <span class="text-xs text-gray-400">ID Mitra: #MTR-8821</span>
      </div>

      <!-- Card Utama Profil -->
      <div class="bg-white p-6 sm:p-8 rounded-2xl border border-gray-100 shadow-sm space-y-8">
        
        <!-- Header Profil (Avatar & Badge Status Verifikasi) -->
        <div class="flex flex-col sm:flex-row items-center gap-6 pb-6 border-b border-gray-100">
          <div class="w-24 h-24 rounded-2xl bg-red-100 text-red-600 font-bold flex items-center justify-center text-3xl shadow-inner border border-red-200">
            RK
          </div>
          <div class="text-center sm:text-left space-y-1">
            <div class="flex flex-wrap items-center justify-center sm:justify-start gap-2">
              <h1 class="text-2xl font-black text-gray-900">Relawan Kemanusiaan Purwokerto</h1>
              <span class="bg-emerald-50 text-emerald-700 text-[10px] font-bold px-2.5 py-1 rounded-full border border-emerald-200">
                ✓ Mitra Terverifikasi
              </span>
            </div>
            <p class="text-xs text-gray-500">Tipe Akun: <strong>Lembaga / Yayasan Sosial</strong></p>
            <p class="text-[11px] text-gray-400">Bergabung sejak: Oktober 2026</p>
          </div>
        </div>

        <!-- Form Pengaturan Informasi Profil -->
        <form @submit.prevent="handleSaveProfile" class="space-y-6">
          <h2 class="font-bold text-gray-900 text-base border-b border-gray-100 pb-2">
            Informasi Identitas & Kontak Siaga
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Nama Mitra / Lembaga *</label>
              <input 
                v-model="profile.name"
                type="text" 
                class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
                required
              />
            </div>
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Nama Penanggung Jawab (PIC) *</label>
              <input 
                v-model="profile.picName"
                type="text" 
                class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
                required
              />
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Alamat Email *</label>
              <input 
                v-model="profile.email"
                type="email" 
                class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none bg-gray-50"
                disabled
              />
              <span class="text-[10px] text-gray-400">Email tidak dapat diubah secara langsung.</span>
            </div>
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Nomor WhatsApp / Telp Siaga *</label>
              <input 
                v-model="profile.phone"
                type="text" 
                class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
                required
              />
            </div>
          </div>

          <!-- Wilayah Domisili Posko / Mitra -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Kabupaten / Kota *</label>
              <input 
                v-model="profile.city"
                type="text" 
                class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
                required
              />
            </div>
            <div>
              <label class="block text-xs font-semibold text-gray-700 mb-1">Kecamatan / Kelurahan *</label>
              <input 
                v-model="profile.district"
                type="text" 
                class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
                required
              />
            </div>
          </div>

          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Alamat Posko Utama / Rumah *</label>
            <textarea 
              v-model="profile.address"
              rows="3"
              class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
              required
            ></textarea>
          </div>

          <!-- Tombol Simpan -->
          <div class="pt-4 flex items-center justify-end gap-3 border-t border-gray-100">
            <button 
              type="submit" 
              class="bg-red-600 hover:bg-red-700 text-white font-bold text-xs px-6 py-2.5 rounded-xl shadow-md transition"
            >
              💾 Simpan Perubahan Profil
            </button>
          </div>

        </form>

      </div>
    </div>
  </div>
</template>

<script setup>
const profile = ref({
  name: 'Relawan Kemanusiaan Purwokerto',
  picName: 'Budi Santoso',
  email: 'relawan.purwokerto@gmail.com',
  phone: '081234567890',
  city: 'Kab. Banyumas',
  district: 'Purwokerto Utara',
  address: 'Jl. Serayu No. 12, Sumampir, Purwokerto Utara, Banyumas'
})

const handleSaveProfile = () => {
  alert('Informasi profil Mitra Darurat berhasil diperbarui!')
}
</script>