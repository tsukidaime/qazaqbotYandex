alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'j', 'з': 'z', 'и': "i'",
            'й': "i'", 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': "y'", 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'ы': 'y', 'ә': "a'", 'і': 'i', 'ң': "n'",
            'ғ': "g'", 'ү': "u'",'ұ': "u", 'қ': 'q', 'ө': "o'", 'һ': "h"}

def changetolatin(text):
    i = 0
    str = list(text)
    while i < len(text):
        if str[i].lower() in alphabet:
            str[i] = alphabet[str[i].lower()]
        i += 1
    return ''.join(str)

