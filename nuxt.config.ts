// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  compatibilityDate: '2026-11-06',

  modules: [
    '@nuxtjs/tailwindcss',
    '@vite-pwa/nuxt'
  ],

  experimental: {
    appManifest: false
  },

  // Pengaturan direktori komponen (agar folder listings bisa dipanggil langsung tanpa prefix)
  components: [
    {
      path: '~/components/listings',
      pathPrefix: false,
    },
    '~/components'
  ],

  app: {
    head: {
      title: 'Info Darurat - Layanan & Posko Darurat Indonesia',
      meta: [
        { name: 'description', content: 'Direktori cepat dan reliable untuk informasi posko, alat, dan layanan darurat.' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    }
  },

  pwa: {
    registerType: 'autoUpdate',
    manifest: {
      name: 'Info Darurat Indonesia',
      short_name: 'InfoDarurat',
      description: 'Platform direktori darurat cepat dan offline-first',
      theme_color: '#dc2626',
      icons: [
        {
          src: 'pwa-192x192.png',
          sizes: '192x192',
          type: 'image/png'
        },
        {
          src: 'pwa-512x512.png',
          sizes: '512x512',
          type: 'image/png'
        }
      ]
    },
    workbox: {
      navigateFallback: '/',
      globPatterns: ['**/*.{js,css,html,png,svg,ico}']
    }
  }
})