import transformers
import googletrans
from googletrans import Translator
from transformers import pipeline
text=('our hero named rocky was on a mission to kill his enemy named gaffar,gaffar comes into a meeting where rocky is ready with his plan to kill him with a gun pointing towards gaffar,then')
for i in range(0,2):
    generator = pipeline("text-generation")
    response="we are in a hotel "
    text1=""" (a adventure scene)"""
    prompt = text1 + response+text
    outputs = generator(prompt, max_length=200)
    print(outputs[0]['generated_text'])
    xxx=outputs[0]['generated_text']
    translator = Translator()
    val = str(input('enter the language\n'))
    my_dict = googletrans.LANGUAGES
    for key, value in my_dict.items():
        if val == value:
            x = key
    translator = Translator()
    translated = translator.translate(xxx, scr='en', dest=x)
    print(translated.text)
    print(x)