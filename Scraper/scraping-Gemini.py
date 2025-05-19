import wikipedia
wikipedia.set_lang("es")
import csv
import time
import re
import google.generativeai as genai

API_KEY = "AIzaSyBHkNwBzzWnma505XSHS2ZxcQXjsgRbsHk"
TEMAS = [
    "Inteligencia artificial",
    "Red neuronal artificial",
    "Algoritmo genético",
    "Teoría cuántica de campos",
    "Entropía",
    "Teoría del caos",
    "Célula madre",
    "Fotosíntesis",
    "Relatividad general",
    "Nanotecnología"
]
LIMITE_TEXTO = 4000
ARCHIVO_SALIDA = "wikipedia_resumenes.tsv"

genai.configure(api_key=API_KEY)
modelo = genai.GenerativeModel("gemini-1.5-flash")

import re

def limpiar_texto(texto):
    # Elimina encabezados de wikipedia
    texto = re.sub(r"^==.*?==\s*$", "", texto, flags=re.MULTILINE)

    # Elimina referencias como [1]
    texto = re.sub(r"\[\d+\]", "", texto)

    # Reemplaza saltos de línea múltiples por uno solo
    texto = re.sub(r"\n{2,}", "\n", texto)

    # Reemplaza saltos de línea por espacios para texto en bloque
    texto = texto.replace("\n", " ")

    return texto.strip()



def resumir(texto):
    prompt = f"Resume el siguiente texto en exactamente 2 frases claras y concisas:\n\n{texto}"
    try:
        respuesta = modelo.generate_content(prompt)
        return respuesta.text.strip()
    except Exception as e:
        return f"[ERROR] {e}"

with open(ARCHIVO_SALIDA, "w", encoding="utf-8", newline="") as archivo:
    writer = csv.writer(archivo, delimiter="\t")
    writer.writerow(["text", "summary"])

    for tema in TEMAS:
        print(f"\nProcesando tema: {tema}")
        try:
            texto = wikipedia.page(tema).content[:LIMITE_TEXTO]
            texto_limpio = limpiar_texto(texto)
            resumen = resumir(texto_limpio)
            writer.writerow([texto_limpio, resumen])
            print("Resumen generado.")
            time.sleep(1)  
        except Exception as e:
            print(f"Error con {tema}: {e}")
