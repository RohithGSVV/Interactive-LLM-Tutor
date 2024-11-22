const response = await fetch('http://localhost:8000/v1/rag/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'llama3.1',
    messages: [{ role: 'user', content: 'What is Trial Balance?' }],
    stream: true,
  }),
});

const reader = response.body.getReader();
const decoder = new TextDecoder();

while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  
  const chunk = decoder.decode(value);
  const lines = chunk.split('\n');
  
  for (const line of lines) {
    if (line.startsWith('data: ')) {
      const data = line.slice(6);
      if (data === '[DONE]') {
        console.log('Stream finished');
      } else {
        const parsed = JSON.parse(data);
        console.log(parsed.choices[0].delta.content);
      }
    }
  }
}
