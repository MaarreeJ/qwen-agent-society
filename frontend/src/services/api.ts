export async function analyzeQuery(query: string) {
  const response = await fetch(
    `http://127.0.0.1:8000/agent?query=${encodeURIComponent(query)}`
  )

  return response.json()
}

