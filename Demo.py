#Translator using python

from translate import Translator

def translate(text,lang):
    translator = Translator(to_lang=lang)
    translation = translator.translate(text)
    print(translation)

myText = "This is pen"
lan = "zh"

translate(myText,lan)

