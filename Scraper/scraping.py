import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import time

# URL
base_url = "https://www.larazon.es/espana/"
domain = "https://www.larazon.es"

# Obtener HTML de la portada
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar las secciones
sections = soup.find_all('section', class_='row distributiva')

# Extraer enlaces 
article_links = []
for sec in sections:
    articles = sec.find_all('article')
    for art in articles:
        a_tag = art.find('a', href=True)
        if a_tag:
            url = urljoin(domain, a_tag['href'])
            if url not in article_links:
                article_links.append(url)

# Limitar a 10
article_links = article_links[:10]
print(f"📰 Procesando {len(article_links)} artículos.\n")

# Función para scrapear cada artículo
def extract_article_content(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Título y subtítulo
        title_tag = soup.find("h1")
        subtitle_tag = soup.find("h2")
        title = title_tag.get_text(strip=True) if title_tag else ""
        subtitle = subtitle_tag.get_text(strip=True) if subtitle_tag else ""

        full_title = f"{title}. {subtitle}" if subtitle else title

        # Buscar el segundo div con class='article-main'
        all_main_divs = soup.find_all("div", class_="article-main")
        if len(all_main_divs) >= 2:
            main_div = all_main_divs[1]
            content_div = main_div.find("div", id="intext")

            if content_div:
                paragraphs = content_div.find_all("p")
                summary = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
            else:
                summary = "Contenido no encontrado."
        else:
            summary = "El div 'article-main' no encontrado."

        return {
            "text": full_title,
            "summary": summary
        }

    except Exception as e:
        print(f"Se ha producido un error en {url}: {e}")
        return None

# Recolectar datos
data = []
for link in article_links:
    print(f"\n--- Procesando artículo --\n{link}")
    content = extract_article_content(link)
    if content:
        data.append(content)
    time.sleep(1)  

# Guardar en CSV
df = pd.DataFrame(data)
df.to_csv("noticias_10.csv", index=False, encoding='utf-8')

