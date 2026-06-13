import { useState } from "react"
import { analyzeQuery } from "./services/api"

function App() {
  const [query, setQuery] = useState("")
  const [result, setResult] = useState<any>(null)

  const handleAnalyze = async () => {
    const data = await analyzeQuery(query)
    setResult(data)
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Qwen Agent Society</h1>

      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter Query"
        style={{ width: "500px" }}
      />

      <button
        onClick={handleAnalyze}
        style={{ marginLeft: "10px" }}
      >
        Analyze
      </button>

      {result && (
        <pre>
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  )
}

export default App