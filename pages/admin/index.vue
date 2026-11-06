<template>
  <div class="bg-gray-100 min-h-screen flex flex-col md:flex-row">
    
    <!-- SIDEBAR KIRI (NAVIGASI VERTIKAL) -->
    <aside class="w-full md:w-64 bg-slate-900 text-slate-300 flex flex-col justify-between p-4 shrink-0 shadow-lg">
      <div class="space-y-6">
        <!-- Logo / Brand Admin -->
        <div class="flex items-center gap-3 px-2 pt-2">
          <div class="w-10 h-10 rounded-xl bg-red-600 text-white flex items-center justify-center font-black text-lg shadow">
            🚨
          </div>
          <div>
            <h2 class="text-white font-bold text-sm">Info Darurat</h2>
            <span class="text-[10px] text-red-400 font-semibold uppercase tracking-wider">Panel Admin</span>
          </div>
        </div>

        <!-- Menu Navigasi Samping -->
        <nav class="space-y-1.5 text-xs font-medium">
          <button 
            @click="currentTab = 'overview'" 
            :class="currentTab === 'overview' ? 'bg-red-600 text-white shadow' : 'hover:bg-slate-800 text-slate-400 hover:text-white'"
            class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition cursor-pointer"
          >
            📊 <span>Ringkasan & Statistik</span>
          </button>
          <button 
            @click="currentTab = 'verification'" 
            :class="currentTab === 'verification' ? 'bg-red-600 text-white shadow' : 'hover:bg-slate-800 text-slate-400 hover:text-white'"
            class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition cursor-pointer justify-between"
          >
            <span class="flex items-center gap-3">🔍 Verifikasi Aset</span>
            <span class="bg-blue-500 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">{{ pendingVerificationAssets.length }}</span>
          </button>
          <button 
            @click="currentTab = 'approval'" 
            :class="currentTab === 'approval' ? 'bg-red-600 text-white shadow' : 'hover:bg-slate-800 text-slate-400 hover:text-white'"
            class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition cursor-pointer justify-between"
          >
            <span class="flex items-center gap-3">🛡️ Approval Mitra</span>
            <span class="bg-amber-500 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">{{ pendingMitra.length }}</span>
          </button>
          <button 
            @click="currentTab = 'articles'" 
            :class="currentTab === 'articles' ? 'bg-red-600 text-white shadow' : 'hover:bg-slate-800 text-slate-400 hover:text-white'"
            class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition cursor-pointer"
          >
            📖 <span>Kelola Artikel</span>
          </button>
          <button 
            @click="currentTab = 'categories'" 
            :class="currentTab === 'categories' ? 'bg-red-600 text-white shadow' : 'hover:bg-slate-800 text-slate-400 hover:text-white'"
            class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition cursor-pointer"
          >
            🗂️ <span>Kategori & Ikon</span>
          </button>
          <button 
            @click="currentTab = 'mitra'" 
            :class="currentTab === 'mitra' ? 'bg-red-600 text-white shadow' : 'hover:bg-slate-800 text-slate-400 hover:text-white'"
            class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition cursor-pointer"
          >
            👥 <span>Manajemen Mitra</span>
          </button>
          <button 
            @click="currentTab = 'reports'" 
            :class="currentTab === 'reports' ? 'bg-red-600 text-white shadow' : 'hover:bg-slate-800 text-slate-400 hover:text-white'"
            class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl transition cursor-pointer justify-between"
          >
            <span class="flex items-center gap-3">🚨 Pantauan Darurat</span>
            <span class="bg-red-500 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">{{ activeReports.length }}</span>
          </button>
        </nav>
      </div>

      <!-- Tombol Keluar / Kembali ke Beranda -->
<div class="pt-4 border-t border-slate-800">
  <NuxtLink to="/" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-medium text-slate-400 hover:bg-slate-800 hover:text-white transition">
    🏠 <span>Keluar ke Beranda</span>
  </NuxtLink>
</div>

    </aside>

    <!-- KONTEN UTAMA SEBELAH KANAN -->
    <main class="flex-1 p-6 sm:p-8 space-y-6 overflow-y-auto">
      
      <!-- Top Welcome Banner -->
      <div class="bg-gradient-to-r from-red-600 to-red-700 text-white p-6 rounded-3xl shadow-md flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
        <div class="space-y-1">
          <span class="bg-white/20 text-white text-[10px] font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">
            Selamat Datang, Administrator!
          </span>
          <h1 class="text-xl sm:text-2xl font-black tracking-tight">
            Pusat Kontrol & Verifikasi Platform
          </h1>
          <p class="text-xs text-red-100 max-w-xl">
            Pantau laporan darurat real-time, verifikasi aset bantuan, dan kelola mitra penolong langsung dari satu panel terpadu.
          </p>
        </div>
        <div class="bg-white/10 backdrop-blur-md px-3.5 py-2 rounded-2xl border border-white/20 text-xs font-bold flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>Sistem Aktif 24/7</span>
        </div>
      </div>

      <!-- TAB 1: OVERVIEW / RINGKASAN DATA (GAYA DASHBOARD BARU) -->
      <div v-if="currentTab === 'overview'" class="space-y-6">
        <h2 class="font-bold text-gray-900 text-base">Ringkasan Statistik Sistem</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div class="bg-white p-5 rounded-3xl border border-gray-100 shadow-sm space-y-2">
            <span class="text-xs text-gray-400 font-medium">Verifikasi Aset Baru</span>
            <h4 class="text-3xl font-black text-blue-600">{{ pendingVerificationAssets.length }} Unit</h4>
            <span class="text-[11px] text-blue-600 font-semibold block">Perlu review segera</span>
          </div>
          <div class="bg-white p-5 rounded-3xl border border-gray-100 shadow-sm space-y-2">
            <span class="text-xs text-gray-400 font-medium">Mitra Penolong</span>
            <h4 class="text-3xl font-black text-gray-900">{{ allMitra.length }} Akun</h4>
            <span class="text-[11px] text-emerald-600 font-semibold block">✓ {{ pendingMitra.length }} Pending approval</span>
          </div>
          <div class="bg-white p-5 rounded-3xl border border-gray-100 shadow-sm space-y-2">
            <span class="text-xs text-gray-400 font-medium">Artikel Edukasi</span>
            <h4 class="text-3xl font-black text-purple-600">{{ articleList.length }} Post</h4>
            <span class="text-[11px] text-purple-600 font-semibold block">Internal Tim</span>
          </div>
          <div class="bg-white p-5 rounded-3xl border border-gray-100 shadow-sm space-y-2">
            <span class="text-xs text-gray-400 font-medium">Laporan Darurat Warga</span>
            <h4 class="text-3xl font-black text-red-600">{{ activeReports.length }} Kasus</h4>
            <span class="text-[11px] text-red-600 font-semibold block">Aktif ditangani</span>
          </div>
        </div>

        <!-- Quick Access Shortcuts -->
        <div class="bg-white p-6 rounded-3xl border border-gray-100 shadow-sm space-y-4">
          <h3 class="font-bold text-gray-900 text-sm">Akses Cepat Panel Utama</h3>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <button @click="currentTab = 'verification'" class="p-4 bg-gray-50 hover:bg-red-50 hover:border-red-200 border border-gray-100 rounded-2xl text-left transition cursor-pointer space-y-1">
              <span class="text-xl">🔍</span>
              <h4 class="font-bold text-xs text-gray-900">Verifikasi Aset</h4>
              <span class="text-[10px] text-blue-600 font-bold">{{ pendingVerificationAssets.length }} pending</span>
            </button>
            <button @click="currentTab = 'approval'" class="p-4 bg-gray-50 hover:bg-red-50 hover:border-red-200 border border-gray-100 rounded-2xl text-left transition cursor-pointer space-y-1">
              <span class="text-xl">🛡️</span>
              <h4 class="font-bold text-xs text-gray-900">Approval Mitra</h4>
              <span class="text-[10px] text-amber-600 font-bold">{{ pendingMitra.length }} antrean</span>
            </button>
            <button @click="currentTab = 'articles'" class="p-4 bg-gray-50 hover:bg-red-50 hover:border-red-200 border border-gray-100 rounded-2xl text-left transition cursor-pointer space-y-1">
              <span class="text-xl">📖</span>
              <h4 class="font-bold text-xs text-gray-900">Kelola Artikel</h4>
              <span class="text-[10px] text-purple-600 font-bold">Buat post</span>
            </button>
            <button @click="currentTab = 'reports'" class="p-4 bg-gray-50 hover:bg-red-50 hover:border-red-200 border border-gray-100 rounded-2xl text-left transition cursor-pointer space-y-1">
              <span class="text-xl">🚨</span>
              <h4 class="font-bold text-xs text-gray-900">Pantau Darurat</h4>
              <span class="text-[10px] text-red-600 font-bold">{{ activeReports.length }} kasus</span>
            </button>
          </div>
        </div>
      </div>

      <!-- PEMANGGILAN KOMPONEN MODULAR SESUAI TAB AKTIF -->
      <AdminVerificationTab v-if="currentTab === 'verification'" :assets="pendingVerificationAssets" @approve="approveAsset" @reject="rejectAsset" />
      <AdminApprovalTab v-if="currentTab === 'approval'" :pendingMitra="pendingMitra" @approve="approveMitra" @reject="rejectMitra" />
      <AdminArticlesTab v-if="currentTab === 'articles'" :articles="articleList" @toggleSuspend="toggleSuspendArticle" @delete="deleteArticle" />
      <AdminCategoriesTab v-if="currentTab === 'categories'" :categories="categoryList" @delete="deleteCategory" />
      <AdminMitraTab v-if="currentTab === 'mitra'" :mitraList="allMitra" @toggleSuspend="toggleSuspend" @delete="deleteMitra" />
      <AdminReportsTab v-if="currentTab === 'reports'" :reports="activeReports" @resolve="resolveReport" />

    </main>

  </div>
</template>

<script setup>
const currentTab = ref('overview')

// Data Mock
const pendingVerificationAssets = ref([
  { id: 1, title: 'Tabung Oksigen 2m3 + Regulator', category: 'Darurat Medis', costType: 'Gratis', provider: 'Relawan Mandiri', location: 'Purwokerto Timur', phone: '081234567890' },
  { id: 2, title: 'Perahu Karet Evakuasi Banjir', category: 'Alat Evakuasi', costType: 'Sukarela', provider: 'Komunitas SAR', location: 'Banyumas', phone: '081987654321' }
])

const pendingMitra = ref([
  { id: 1, name: 'Yayasan Ambulans Berkah', type: 'Lembaga Sosial', email: 'berkah@gmail.com', pic: 'Ust. Juman', phone: '081298765432', location: 'Wangon' }
])

const allMitra = ref([
  { id: 101, name: 'Relawan Kemanusiaan', type: 'Lembaga', phone: '081234567890', location: 'Purwokerto Utara', status: 'Aktif' },
  { id: 103, name: 'Posko Siaga Banyumas', type: 'Lembaga', phone: '085678901234', location: 'Banyumas', status: 'Suspended' }
])

const activeReports = ref([
  { id: 1, type: 'Kecelakaan', reporter: 'Budi', phone: '6281234567890', location: 'Jl. Raya Baturraden', description: 'Butuh evakuasi.' }
])

const articleList = ref([
  { id: 1, title: 'Panduan Pemasangan Tabung Oksigen', category: 'Edukasi Medis', date: '24 Okt 2026', snippet: 'Langkah aman menggunakan regulator oksigen.', status: 'Published' }
])

const categoryList = ref([
  { id: 1, name: 'Darurat Medis', slug: 'medis', iconValue: '🏥', description: 'Tabung oksigen', count: 124, active: true },
  { id: 2, name: 'Pemadam Kebakaran', slug: 'pemadam', iconValue: '🚒', description: 'Pemadam kebakaran', count: 45, active: true }
])

// Actions
const approveAsset = (id) => { pendingVerificationAssets.value = pendingVerificationAssets.value.filter(a => a.id !== id); alert('✓ Disetujui!') }
const rejectAsset = (id) => { pendingVerificationAssets.value = pendingVerificationAssets.value.filter(a => a.id !== id); alert('✕ Ditolak!') }
const approveMitra = (id) => { pendingMitra.value = pendingMitra.value.filter(m => m.id !== id); alert('✓ Mitra disetujui!') }
const rejectMitra = (id) => { pendingMitra.value = pendingMitra.value.filter(m => m.id !== id); alert('✕ Mitra ditolak!') }
const toggleSuspend = (m) => { m.status = m.status === 'Aktif' ? 'Suspended' : 'Aktif' }
const deleteMitra = (id) => { allMitra.value = allMitra.value.filter(m => m.id !== id) }
const resolveReport = (id) => { activeReports.value = activeReports.value.filter(r => r.id !== id) }
const deleteCategory = (id) => { categoryList.value = categoryList.value.filter(c => c.id !== id) }
const toggleSuspendArticle = (art) => { art.status = art.status === 'Published' ? 'Suspended' : 'Published' }
const deleteArticle = (id) => { articleList.value = articleList.value.filter(a => a.id !== id) }
</script>