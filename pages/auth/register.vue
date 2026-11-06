<template>
  <div class="bg-gray-50 min-h-[85vh] flex items-center justify-center py-12 px-4">
    <div class="max-w-lg w-full bg-white p-8 rounded-2xl border border-gray-100 shadow-sm space-y-6">
      
      <!-- Header -->
      <div class="text-center space-y-2">
        <span class="bg-red-50 text-red-600 text-xs font-bold px-2.5 py-1 rounded-md uppercase">
          Pendaftaran Resmi
        </span>
        <h1 class="text-2xl font-black text-gray-900">Daftar Sebagai Mitra Darurat</h1>
        <p class="text-xs text-gray-500">Bergabunglah dalam jaringan gotong royong penyediaan Aset Bantuan kemanusiaan.</p>
      </div>

      <!-- Form Register -->
      <form @submit.prevent="handleRegister" class="space-y-4">
        
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Nama Lengkap / PIC *</label>
            <input 
              type="text" 
              placeholder="Contoh: Budi Santoso" 
              class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
              required
            />
          </div>
          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Tipe Pendaftar *</label>
            <select class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs text-gray-700 bg-white focus:ring-2 focus:ring-red-500 focus:outline-none">
              <option>Personal / Warga</option>
              <option>Lembaga / Yayasan Sosial</option>
              <option>Instansi Pemerintah</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block text-xs font-semibold text-gray-700 mb-1">Nama Lembaga / Komunitas (Opsional)</label>
          <input 
            type="text" 
            placeholder="Contoh: Relawan Kemanusiaan Purwokerto" 
            class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
          />
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Email Aktif *</label>
            <input 
              type="email" 
              placeholder="nama@email.com" 
              class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
              required
            />
          </div>
          <div>
            <label class="block text-xs font-semibold text-gray-700 mb-1">Nomor WhatsApp / Telp *</label>
            <input 
              type="text" 
              placeholder="081234567890" 
              class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
              required
            />
          </div>
        </div>

        <div>
          <label class="block text-xs font-semibold text-gray-700 mb-1">Kata Sandi *</label>
          <input 
            type="password" 
            placeholder="••••••••" 
            class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
            required
          />
        </div>

        <button 
          type="submit" 
          class="w-full bg-red-600 hover:bg-red-700 text-white font-bold text-xs py-3 rounded-xl shadow-md transition"
        >
          Daftar & Kirim Verifikasi
        </button>
      </form>

      <!-- Footer Link Login -->
      <div class="text-center text-xs text-gray-500 pt-2 border-t border-gray-100">
        Sudah punya akun? 
        <NuxtLink to="/auth/login" class="text-red-600 font-bold hover:underline">Masuk di sini</NuxtLink>
      </div>

    </div>
  </div>
</template>

<script setup>
const router = useRouter()

const handleRegister = () => {
  // Setelah register, arahkan ke halaman menunggu approval
  router.push('/auth/waiting-approval')
}
</script>