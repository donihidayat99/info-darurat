<template>
  <footer class="bg-gray-900 text-gray-300 py-12 border-t border-gray-800">
    <div class="container mx-auto px-4 grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
      
      <!-- Kolom 1: Tentang -->
      <div class="space-y-4">
        <div class="flex items-center gap-2">
          <span class="bg-red-600 text-white font-black px-2.5 py-1 rounded text-lg">INFO</span>
          <span class="text-xl font-bold text-white tracking-tight">DARURAT</span>
        </div>
        <p class="text-xs text-gray-400 leading-relaxed">
          Platform direktori digital terbuka untuk mempermudah masyarakat mengakses posko, layanan medis, dan alat darurat secara cepat dan andal.
        </p>
        <div class="text-xs text-gray-500">
          <p>Unduh versi PWA untuk akses offline.</p>
        </div>
      </div>

      <!-- Kolom 2: Kategori Utama -->
      <div>
        <h4 class="text-white font-bold text-sm mb-4">Kategori Layanan</h4>
        <ul class="space-y-2 text-xs text-gray-400">
          <li><NuxtLink to="/listings" class="hover:text-red-500">Darurat Medis & Ambulans</NuxtLink></li>
          <li><NuxtLink to="/listings" class="hover:text-red-500">Pemadam Kebakaran</NuxtLink></li>
          <li><NuxtLink to="/listings" class="hover:text-red-500">SAR & Evakuasi Bencana</NuxtLink></li>
          <li><NuxtLink to="/listings" class="hover:text-red-500">Logistik & Dapur Umum</NuxtLink></li>
        </ul>
      </div>

      <!-- Kolom 3: Tautan Cepat -->
      <div>
        <h4 class="text-white font-bold text-sm mb-4">Tautan Cepat</h4>
        <ul class="space-y-2 text-xs text-gray-400">
          <li><NuxtLink to="/donation" class="hover:text-red-500">Donasi & Dukungan</NuxtLink></li>
          <li><NuxtLink to="/blog" class="hover:text-red-500">Artikel & Tips Siaga</NuxtLink></li>
          <li><NuxtLink to="/legal/terms" class="hover:text-red-500">Syarat & Ketentuan</NuxtLink></li>
          <li><NuxtLink to="/legal/privacy" class="hover:text-red-500">Kebijakan Privasi</NuxtLink></li>
        </ul>
      </div>

      <!-- Kolom 4: Newsletter / Update -->
      <div>
        <h4 class="text-white font-bold text-sm mb-4">Buletin Darurat</h4>
        <p class="text-xs text-gray-400 mb-3">Dapatkan informasi pembaharuan posko siaga langsung ke email Anda.</p>
        <form @submit.prevent class="space-y-2">
          <input 
            type="email" 
            placeholder="Alamat email Anda..." 
            class="w-full px-3 py-2 rounded-lg bg-gray-800 border border-gray-700 text-xs text-white focus:outline-none focus:ring-1 focus:ring-red-500"
          />
          <button type="submit" class="w-full bg-red-600 hover:bg-red-700 text-white text-xs font-bold py-2 rounded-lg transition">
            Berlangganan
          </button>
        </form>
      </div>

    </div>

    <!-- Copyright -->
    <div class="container mx-auto px-4 pt-6 border-t border-gray-800 text-center text-xs text-gray-500">
      <p>&copy; 2026 Info Darurat Indonesia. Dibangun untuk kemanusiaan dan kecepatan akses.</p>
    </div>
  </footer>
</template>