import { useState, useRef } from 'react'
import './App.css'

import DotGrid from './DotGrid';
import VariableProximity from './VariableProximity';
import ShinyText from './ShinyText';

function App() {
  const containerRef = useRef(null);
  const [text, setText] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const analyzeSentiment = async () => {
    if (!text.trim()) return

    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch('http://localhost:5001/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      })

      if (!response.ok) {
        throw new Error('Failed to analyze sentiment')
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <div style={{ position: 'fixed', top: 0, left: 0, width: '100%', height: '100%', zIndex: 0 }}>
        <DotGrid
          dotSize={4}
          gap={20}
          baseColor="#222244"
          activeColor="#646cff"
          proximity={120}
          shockRadius={250}
          shockStrength={5}
          resistance={750}
          returnDuration={1.5}
        />
      </div>
      <div className="container">
        <div className="card">
          <div ref={containerRef} style={{ position: 'relative', marginBottom: '1rem', display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '1rem' }}>
            <VariableProximity
              label={'Sentiment Analyzer'}
              className={'variable-proximity-demo'}
              fromFontVariationSettings="'wght' 400, 'opsz' 9"
              toFontVariationSettings="'wght' 1000, 'opsz' 40"
              containerRef={containerRef}
              radius={100}
              falloff='linear'
              style={{ fontSize: '3rem', color: '#646cff' }}
            />
          </div>
          <ShinyText
            text="Enter text to detect if it's Positive or Negative..."
            disabled={false}
            speed={3}
            className='subtitle'
          />
          <div className="input-group">
            <br />
            <textarea
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Type something here... (e.g., 'I love this product!')"
              rows={4}
            />
          </div>

          <button
            onClick={analyzeSentiment}
            disabled={loading || !text.trim()}
            className="analyze-btn"
          >
            {loading ? 'Analyzing...' : 'Analyze Sentiment'}
          </button>

          {error && <div className="error-message">{error}</div>}

          {result && (
            <div className={`result-card ${result.sentiment.toLowerCase()}`}>
              <h2>
                {result.sentiment === 'Positive' ? 'Positive 😄' : 'Negative 😩'}
              </h2>
              <div className="confidence-bar">
                <div
                  className="confidence-fill"
                  style={{ width: `${result.confidence * 100}%` }}
                ></div>
              </div>
              <p className="confidence-text">
                Confidence: {(result.confidence * 100).toFixed(1)}%
              </p>
            </div>
          )}
        </div>
      </div>
    </>
  )
}

export default App
