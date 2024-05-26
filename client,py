from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
import nest_asyncio
import uvicorn

nest_asyncio.apply()

app = FastAPI()


class HTMLContent(BaseModel):
    html: str


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    product = soup.find("div", class_="product")
    if not product:
        return None
    product_name = product.find("h1").text.strip()
    product_description = product.find("p").text.strip()
    return {"name": product_name, "description": product_description}


@app.post("/extract")
async def extract_product_info(html_content: HTMLContent):
    parsed_data = parse_html(html_content.html)
    if not parsed_data:
        raise HTTPException(status_code=400,
                            detail="No product information found")

    prompt = f"Extract the product information from the HTML: {html_content.html}"

    # Call the Ollama API for LLaMA model processing
    response = requests.post("http://localhost:11435/v1/completions",
                             json={
                                 "model": "llama3",
                                 "prompt": prompt,
                                 "temperature": 0,
                                 "format": "json"
                             })

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail="Error processing with LLaMA model")

    llm_output = response.json()

    result = {
        "product_name": parsed_data["name"],
        "product_description": parsed_data["description"],
        "llm_output": llm_output
    }

    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
