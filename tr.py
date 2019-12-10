from yandex_translate import YandexTranslate
translate = YandexTranslate('trnsl.1.1.20191210T100948Z.67a2ac42cb051b0f.11b5efa3a42db2009745d447f7d78010e3acaf23')
print('Translate:', translate.translate('Привет, мир!', 'en')['text'][0])  # or just 'e