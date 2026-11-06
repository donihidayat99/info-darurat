<template>
  <header class="bg-white border-b border-gray-100 sticky top-0 z-40 shadow-sm">
    <div class="container mx-auto px-4 max-w-7xl h-16 flex items-center justify-between gap-4">
      
      <!-- Brand Logo -->
      <NuxtLink to="/" class="flex items-center gap-2 shrink-0">
        <div class="w-9 h-9 rounded-xl bg-red-600 text-white font-black text-lg flex items-center justify-center shadow-sm">
          🚨
        </div>
        <div>
          <span class="font-black text-base text-gray-900 tracking-tight block leading-none">
            Info<span class="text-red-600">Darurat</span>
          </span>
          <span class="text-[9px] font-semibold text-gray-400 block tracking-wider uppercase">
            Tanggap Bantuan Warga
          </span>
        </div>
      </NuxtLink>

      <!-- Desktop Nav Menu -->
      <nav class="hidden md:flex items-center gap-6 text-xs font-bold text-gray-600">
        <NuxtLink 
          to="/" 
          active-class="text-red-600 font-black"
          class="hover:text-red-600 transition"
        >
          Beranda
        </NuxtLink>
        <NuxtLink 
          to="/listings" 
          active-class="text-red-600 font-black"
          class="hover:text-red-600 transition"
        >
          Cari Bantuan
        </NuxtLink>
        <NuxtLink 
          to="/categories" 
          active-class="text-red-600 font-black"
          class="hover:text-red-600 transition"
        >
          Kategori
        </NuxtLink>
        <NuxtLink 
          to="/blog" 
          active-class="text-red-600 font-black"
          class="hover:text-red-600 transition"
        >
          Edukasi & Blog
        </NuxtLink>
      </nav>

      <!-- Desktop Action Buttons -->
      <div class="hidden md:flex items-center gap-3">
        <NuxtLink 
          to="/report" 
          class="bg-amber-400 hover:bg-amber-500 text-gray-950 text-xs font-black px-4 py-2 rounded-xl transition shadow-sm flex items-center gap-1.5"
        >
          <span>🚨</span>
          <span>Lapor Darurat</span>
        </NuxtLink>

        <!-- Tombol Smart Portal Mitra (Mengarah ke /auth/login jika belum login) -->
        <button 
          @click="handleMitraPortalAccess"
          class="bg-gray-900 hover:bg-gray-800 text-white text-xs font-bold px-4 py-2 rounded-xl transition shadow-sm cursor-pointer flex items-center gap-1.5"
        >
          <span>{{ isLoggedIn ? '👤 Profil Mitra' : '🤝 Portal Mitra' }}</span>
        </button>
      </div>

      <!-- Mobile Hamburger Button -->
      <button 
        @click="isMobileMenuOpen = !isMobileMenuOpen"
        class="md:hidden p-2 rounded-xl bg-gray-100 text-gray-700 hover:bg-gray-200 transition text-lg cursor-pointer"
      >
        {{ isMobileMenuOpen ? '✕' : '☰' }}
      </button>

    </div>

    <!-- Mobile Menu Drawer -->
    <div 
      v-if="isMobileMenuOpen" 
      class="md:hidden bg-white border-b border-gray-100 p-4 space-y-3 animate-fadeIn"
    >
      <nav class="flex flex-col space-y-2 text-sm font-bold text-gray-700">
        <NuxtLink 
          to="/" 
          @click="isMobileMenuOpen = false" 
          class="p-2.5 rounded-xl hover:bg-gray-50 flex items-center gap-2"
        >
          🏠 Beranda
        </NuxtLink>
        <NuxtLink 
          to="/listings" 
          @click="isMobileMenuOpen = false" 
          class="p-2.5 rounded-xl hover:bg-gray-50 flex items-center gap-2"
        >
          🔍 Cari Bantuan & Direktori
        </NuxtLink>
        <NuxtLink 
          to="/categories" 
          @click="isMobileMenuOpen = false" 
          class="p-2.5 rounded-xl hover:bg-gray-50 flex items-center gap-2"
        >
          🗂️ Semua Kategori
        </NuxtLink>
        <NuxtLink 
          to="/blog" 
          @click="isMobileMenuOpen = false" 
          class="p-2.5 rounded-xl hover:bg-gray-50 flex items-center gap-2"
        >
          📖 Edukasi & Blog
        </NuxtLink>
      </nav>

      <div class="pt-2 border-t border-gray-100 flex flex-col gap-2">
        <NuxtLink 
          to="/report" 
          @click="isMobileMenuOpen = false" 
          class="w-full text-center bg-amber-400 hover:bg-amber-500 text-gray-950 font-black text-xs py-3 rounded-xl transition"
        >
          🚨 Kirim Laporan Darurat
        </NuxtLink>
        <button 
          @click="handleMitraPortalAccess(); isMobileMenuOpen = false;" 
          class="w-full text-center bg-gray-900 text-white font-bold text-xs py-3 rounded-xl transition cursor-pointer"
        >
          {{ isLoggedIn ? '👤 Profil Mitra Penolong' : '🤝 Portal Mitra Penolong' }}
        </button>
      </div>
    </div>
  </header>
</template>

<script setup>
const router = useRouter()
const isMobileMenuOpen = ref(false)

// Status simulasi login (false = belum login, true = sudah login)
const isLoggedIn = ref(false) 

const handleMitraPortalAccess = () => {
  if (isLoggedIn.value) {
    // Jika sudah login -> Masuk ke dashboard mitra
    router.push('/dashboard')
  } else {
    // Jika belum login -> Diarahkan ke folder auth/login.vue
    router.push('/auth/login')
  }
}
</script>