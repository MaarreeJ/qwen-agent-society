import { useState } from "react"
import { analyzeQuery } from "./services/api"
import { getMemory } from "./services/memory"

function App() {
  const [query, setQuery] = useState("")
  const [result, setResult] = useState<any>(null)
  const [memory, setMemory] = useState<any>(null)
  const [loading, setLoading] = useState(false)

  const handleAnalyze = async () => {
    if (!query.trim()) return

    setLoading(true)

    try {
      const data = await analyzeQuery(query)
      setResult(data)
    } catch (error) {
      console.error(error)
      alert("Analysis failed")
    }

    setLoading(false)
  }

  const loadMemory = async () => {
    try {
      const data = await getMemory()
      setMemory(data)
    } catch (error) {
      console.error(error)
      alert("Failed to load memory")
    }
  }

  return (
    <div
      style={{
        maxWidth: "1200px",
        margin: "auto",
        padding: "20px"
      }}
    >
      <h1>🚀 Qwen Agent Society</h1>

      <div
        style={{
          display: "flex",
          gap: "10px",
          marginBottom: "20px"
        }}
      >
        <input
          type="text"
          placeholder="Enter Query"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{
            flex: 1,
            padding: "12px"
          }}
        />

        <button
          onClick={handleAnalyze}
          style={{
            padding: "12px 20px"
          }}
        >
          Analyze
        </button>

        <button
          onClick={loadMemory}
          style={{
            padding: "12px 20px"
          }}
        >
          View Memory
        </button>
      </div>

      {loading && <h3>Running Agents...</h3>}

      {result && (
        <>
          {/* Research */}

          <div
            style={{
              border: "1px solid gray",
              padding: "20px",
              marginBottom: "20px"
            }}
          >
            <h2>Research</h2>

            <div
              style={{
                maxHeight: "350px",
                overflowY: "auto",
                whiteSpace: "pre-wrap"
              }}
            >
              {result.research}
            </div>
          </div>

          {/* Finance */}

          <div
            style={{
              border: "1px solid gray",
              padding: "20px",
              marginBottom: "20px"
            }}
          >
            <h2>Finance</h2>

            <p>
              <b>Financial Risk:</b>{" "}
              {result.finance?.financial_risk}
            </p>

            <p>
              <b>Investment Outlook:</b>{" "}
              {result.finance?.investment_outlook}
            </p>

            <p>
              <b>Summary:</b>
            </p>

            <p>{result.finance?.summary}</p>
          </div>

          {/* Compliance */}

          <div
            style={{
              border: "1px solid gray",
              padding: "20px",
              marginBottom: "20px"
            }}
          >
            <h2>Compliance</h2>

            <p>
              <b>Compliance Score:</b>{" "}
              {result.compliance?.compliance_score}
            </p>

            <p>
              <b>Regulatory Risk:</b>{" "}
              {result.compliance?.regulatory_risk}
            </p>

            <p>
              <b>Summary:</b>
            </p>

            <p>{result.compliance?.summary}</p>
          </div>

          {/* Validation */}

          <div
            style={{
              border: "1px solid gray",
              padding: "20px",
              marginBottom: "20px"
            }}
          >
            <h2>Validation</h2>

            <p>
              <b>Status:</b>{" "}
              {result.validation?.status}
            </p>

            <p>
              <b>Overall Score:</b>{" "}
              {result.validation?.overall_score}
            </p>

            <p>
              <b>Final Summary:</b>
            </p>

            <p>{result.validation?.final_summary}</p>
          </div>
        </>
      )}

      {memory && (
        <div
          style={{
            border: "1px solid green",
            padding: "20px",
            marginTop: "20px"
          }}
        >
          <h2>Memory</h2>

          <pre
            style={{
              whiteSpace: "pre-wrap"
            }}
          >
            {JSON.stringify(memory, null, 2)}
          </pre>
        </div>
      )}
    </div>
  )
}

export default App

