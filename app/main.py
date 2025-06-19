from fastapi import FastAPI
from app.routers import arithmetic_parenthesis, graph, string,intervals,monotonic_stack, dp, container_with_most_water, string_compression, max_vowels, pivot_index, close_strings, leaf_similar_trees, peak_element, good_nodes, reorder_routes
from mangum import Mangum
from fastapi.responses import HTMLResponse

app = FastAPI()

app.include_router(graph.router)
app.include_router(string.router)
app.include_router(intervals.router)
app.include_router(monotonic_stack.router)
app.include_router(dp.router)
app.include_router(arithmetic_parenthesis.router)
app.include_router(container_with_most_water.router)
app.include_router(string_compression.router)
app.include_router(max_vowels.router)
app.include_router(pivot_index.router)
app.include_router(close_strings.router)
app.include_router(leaf_similar_trees.router)
app.include_router(peak_element.router)
app.include_router(good_nodes.router)
app.include_router(reorder_routes.router)


@app.get("/",include_in_schema=False)
def landing_page():
    return HTMLResponse(content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Algorithms API</title>
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="bg-gradient-to-br from-indigo-50 to-blue-100 min-h-screen">
  <header class="w-full py-6 bg-white shadow-sm">
    <div class="container mx-auto flex justify-between items-center px-4">
      <span class="text-2xl font-bold text-indigo-700 tracking-tight">Algorithms API</span>
      <a href="#get-started" class="bg-indigo-600 text-white rounded-xl px-5 py-2 hover:bg-indigo-700 transition">Get Started</a>
    </div>
  </header>

  <main class="container mx-auto px-4 py-16 flex flex-col items-center">
    <h1 class="text-5xl md:text-6xl font-extrabold text-center text-indigo-800 mb-6 drop-shadow-sm">
      Fast, Reliable Algorithms<br>
      <span class="text-blue-600">— as an API</span>
    </h1>
    <p class="text-xl text-slate-700 max-w-2xl text-center mb-10">
      Solve algorithmic problems with optimized implementations—dynamic programming, graph traversal, string processing, and more—directly from your code. No setup required, just API calls.
    </p>
    <a href="#get-started" class="mb-16 bg-blue-600 text-white font-semibold px-8 py-3 rounded-xl shadow-lg hover:bg-blue-700 transition text-lg">Start Using</a>

    <!-- Features -->
    <div class="grid md:grid-cols-3 gap-8 w-full max-w-5xl mb-20">
      <div class="bg-white p-8 rounded-2xl shadow hover:shadow-lg transition">
        <h3 class="text-xl font-bold text-indigo-700 mb-2">Dynamic Programming</h3>
        <p class="text-slate-600">Longest common subsequence and other DP solutions optimized for performance.</p>
      </div>
      <div class="bg-white p-8 rounded-2xl shadow hover:shadow-lg transition">
        <h3 class="text-xl font-bold text-indigo-700 mb-2">Graph & Array Problems</h3>
        <p class="text-slate-600">BFS traversal, pivot index, peak element finding, and interval processing.</p>
      </div>
      <div class="bg-white p-8 rounded-2xl shadow hover:shadow-lg transition">
        <h3 class="text-xl font-bold text-indigo-700 mb-2">String & Stack Operations</h3>
        <p class="text-slate-600">Palindrome checks, max vowels, daily temperatures, and monotonic stack algorithms.</p>
      </div>
    </div>

    <!-- Example API usage -->
    <div class="w-full max-w-3xl bg-white rounded-2xl shadow p-8 mb-16">
      <h2 class="text-2xl font-bold text-indigo-800 mb-4">Example: Longest Common Subsequence</h2>
      <pre class="bg-slate-900 rounded-xl text-slate-100 p-4 text-sm overflow-x-auto"><code>
POST /LCS
{
  "text1": "abcde",
  "text2": "ace"
}

// Response:
{
  "result": 3
}
      </code></pre>
    </div>

    <!-- CTA -->
    <section id="get-started" class="w-full flex flex-col items-center gap-4">
      <h2 class="text-2xl md:text-3xl font-bold text-indigo-800 mb-2">Ready to simplify your code?</h2>
      <a href="/docs" class="bg-indigo-600 text-white rounded-xl px-6 py-3 text-lg font-semibold shadow hover:bg-indigo-700 transition">Read the Docs</a>
    </section>
  </main>

  <footer class="w-full py-6 mt-10 bg-white border-t">
    <div class="container mx-auto px-4 text-center text-slate-500 text-sm">
      &copy; 2025 Algorithms API. Built for developers.
    </div>
  </footer>
</body>
</html>
""")

handler = Mangum(app)