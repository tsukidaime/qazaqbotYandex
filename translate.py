from yandex_translate import YandexTranslate
import six
translate = YandexTranslate('trnsl.1.1.20191210T100948Z.67a2ac42cb051b0f.11b5efa3a42db2009745d447f7d78010e3acaf23')

def Translate(text):
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    return translate.translate(text, 'en')['text'][0]