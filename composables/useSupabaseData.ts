export const useSupabaseData = () => {
  const client = useSupabaseClient()

  // Fetch Listings
  const getListings = async () => {
    const { data, error } = await client.from('listings').select('*').order('created_at', { ascending: false })
    return { data, error }
  }

  // Fetch Articles
  const getArticles = async () => {
    const { data, error } = await client.from('articles').select('*').order('created_at', { ascending: false })
    return { data, error }
  }

  // Insert Article
  const addArticle = async (articleData: any) => {
    const { data, error } = await client.from('articles').insert([articleData])
    return { data, error }
  }

  return {
    getListings,
    getArticles,
    addArticle
  }
}
