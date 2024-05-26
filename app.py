from scrapegraphai.graphs import SmartScraperGraph
import nest_asyncio
import json

nest_asyncio.apply()

graph_config = {
    "llm": {
        "model": "ollama/llama3",
        "temperature": 0,
        "format": "json",
        "base_url": "http://localhost:11435",
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11435",
    },
    "verbose": True,
}

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Page</title>
</head>
<body>
    <div class="product">
        <h1>Haylou LS02 Touch Screen Smart Watch</h1>
        <p>Description: A smart watch with heart monitoring, call alerts, and IP68 waterproofing.</p>
    </div>
</body>
</html>
"""

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the products with their descriptions",
    source=html_content,
    config=graph_config)

result = smart_scraper_graph.run()

output = json.dumps(result, indent=2)

for line in output.split("\n"):
    print(line)
