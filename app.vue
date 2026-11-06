<template>
  <div class="min-h-screen flex flex-col bg-gray-50 text-gray-900 font-sans">
    <!-- Navbar Utama -->
    <CommonNavbar />

    <!-- Konten Halaman -->
    <main class="flex-grow">
      <NuxtPage />
    </main>

    <!-- Footer Utama -->
    <CommonFooter />
  </div>
</template>