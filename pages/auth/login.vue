<template>
  <div class="bg-gray-50 min-h-[80vh] flex items-center justify-center py-12 px-4">
    <div class="max-w-md w-full bg-white p-8 rounded-2xl border border-gray-100 shadow-sm space-y-6">
      
      <!-- Header -->
      <div class="text-center space-y-2">
        <div class="inline-block bg-red-600 text-white font-black px-3 py-1.5 rounded-lg text-lg mb-2">
          INFO DARURAT
        </div>
        <h1 class="text-2xl font-black text-gray-900">Masuk ke Akun Mitra</h1>
        <p class="text-xs text-gray-500">Kelola Aset Bantuan dan respon laporan darurat dengan cepat.</p>
      </div>

      <!-- Form Login -->
      <form @submit.prevent="handleLogin" class="space-y-4">
        <div>
          <label class="block text-xs font-semibold text-gray-700 mb-1">Email Terdaftar</label>
          <input 
            type="email" 
            placeholder="nama@email.com" 
            class="w-full px-3 py-2.5 rounded-xl border border-gray-200 text-xs focus:ring-2 focus:ring-red-500 focus:outline-none"
            required
          />
        </div>

        <div>
          <label class="block text-xs font-semibold text-gray-700 mb-1">Kata Sandi</label>
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
          Masuk Sekarang
        </button>
      </form>

      <!-- Footer Link Register -->
      <div class="text-center text-xs text-gray-500 pt-2 border-t border-gray-100">
        Belum punya akun Mitra Darurat? 
        <NuxtLink to="/auth/register" class="text-red-600 font-bold hover:underline">Daftar di sini</NuxtLink>
      </div>

    </div>
  </div>
</template>

<script setup>
const router = useRouter()

const handleLogin = () => {
  // Simulasi login sukses langsung ke dashboard
  router.push('/dashboard')
}
</script>