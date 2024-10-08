import pandas as pd
from dotenv import load_dotenv
import os
from googletrans import Translator
from langdetect import detect

#load_dotenv('.env')
#OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

#Takes a datframe and returns a list of identified languages in a clumn
def detect_text_lang(df):
    lst = []
    for x in df:
        lst.append(detect(x))
    return lst


#Takes a datframe and returns a list of translated decription in Spanish
def translate_Eng_to_Span(df):
    lst = []
    translator = Translator()
    for x in df:
        if detect(x) == "es":
            lst.append(x)
        else:
            translation = translator.translate(x, dest = "es").text
            lst.append(translation)
    return lst


#Takes a datframe and returns a list of translated decription in English 

def translate_Span_to_Eng(df):
    lst = []
    translator = Translator()
    for x in df:
        if detect(x) == "en":
            lst.append(x)
        else:
            translation = translator.translate(x, dest = "en").text
            lst.append(translation)
    return lst