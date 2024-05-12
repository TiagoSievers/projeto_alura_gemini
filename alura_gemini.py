"""Bibliotecas necessárias

pip install streamlit
pip install google-generativeai
pip install python-dotenv
pip install pillow

Para rodar o programa: streamlit run alura_gemini.py"""

from dotenv import load_dotenv
load_dotenv() ## Carregar todas as variáveis do ambiente
import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="GOOGLE_API_KEY")

## função para carregar o Gemino Pro model and obter as resposta
generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input, image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

## inicializar o streamlit app

st.set_page_config(page_title="Gerador de descritivos de produto com IA")

st.header("Ganhe tempo e gere descrições incríveis dos seus produtos com IA utilizando apenas uma imagem")
##input=st.text_input("Input Prompt: ", key="input")

## Criar um file uploader

uploaded_file = st.file_uploader("Selecione a imagem...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Gerear descritivo")

## Se o botão for clicado
if submit:
    response=get_gemini_response('Crie uma descrição de anúncio em pt-BR irresistível para o produto na imagem, focando em: Que problema ele resolve? Quais são seus 3 principais benefícios? Quais características o tornam único? Inclua detalhes específicos sobre materiais, dimensões, cores, etc. Termine com uma chamada para ação persuasiva.',image)
    st.subheader("A descrição é")
    st.write(response)
