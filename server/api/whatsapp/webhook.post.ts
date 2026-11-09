export default defineEventHandler(async (event) => {
  try {
    // Membaca payload/data yang dikirim dari layanan WA Gateway (misal Fonnte/Wablas)
    const body = await readBody(event)
    
    // Struktur data umumnya tergantung provider gateway yang dipakai, contoh umum:
    const senderPhone = body.sender || body.from || ''
    const messageText = body.message || body.text || ''

    if (!senderPhone || !messageText) {
      return { status: false, message: 'Invalid webhook payload' }
    }

    // Contoh logika: Cek apakah pesan mengandung kata "Verifikasi... ID: #..."
    if (messageText.toLowerCase().includes('verifikasi')) {
      // Ambil nomor ID mitra dari teks pesan menggunakan regex sederhana
      const matchId = messageText.match(/#(\d+)/)
      
      if (matchId && matchId[1]) {
        const mitraId = matchId[1]

        console.log(`✅ [WHATSAPP WEBHOOK] Menerima verifikasi untuk Mitra ID: ${mitraId} dari nomor ${senderPhone}`)

        // =========================================================================
        // TODO: HUBUNGKAN KE SUPABASE
        // Contoh eksekusi update database:
        // await db.from('profiles').update({ is_verified: true, whatsapp: senderPhone }).eq('id', mitraId)
        // =========================================================================
      }
    }

    return {
      success: true,
      message: 'Webhook processed successfully'
    }

  } catch (error) {
    console.error('Error handling whatsapp webhook:', error)
    throw createError({
      statusCode: 500,
      statusMessage: 'Internal Server Error on Webhook'
    })
  }
})
