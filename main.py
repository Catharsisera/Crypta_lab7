RusAlphabet = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
EngAlphabet = list('abcdefghijklmnoprstuvwxyz')
OpenText = input('Введите текст: ')
OpenText = list(OpenText.lower())
KeyWord = list(input('Введите ключевое слово: '))

ChoiceLanguage = int(input ('Выберете: кирилица - 0, латиница - 1: '))

if ChoiceLanguage == 0:
    Alphabet = RusAlphabet
    AdditionalSymbol= 'ъ'
    AmtColumn=8

if ChoiceLanguage == 1:
    Alphabet = EngAlphabet
    AdditionalSymbol= 'x'
    AmtColumn=5

NewAlphabet = []
a = []

for i in OpenText:
    if i in Alphabet:
        a.append(i)
print('a1=',a)

for i in KeyWord:
    if i not in NewAlphabet:
        NewAlphabet.append(i)

for i in Alphabet:
    if i not in NewAlphabet:
        NewAlphabet.append(i)

print(NewAlphabet)

h=len(a)

ChoiceAction = int(input ('Выберете: зашифровать - 0, расшифровать - 1: '))

if ChoiceAction == 0:
    i = 0
    while h > 1:
        h -= 2
        if a[i] == a[i+1]:
            a.insert(i + 1, AdditionalSymbol)
            h += 1
        i += 2
    print('a2=',a)

    if len(a) % 2 == 1:
        a.append(AdditionalSymbol)

    for i in range(0, len(a), 2):
        z = NewAlphabet.index(a[i])
        x = NewAlphabet.index(a[i + 1])
        if z % AmtColumn == x % AmtColumn:
            a[i] = NewAlphabet[(z + AmtColumn) % 32]
            a[i+1] = NewAlphabet[(x + AmtColumn) % 32]
        else:
            if int(z / AmtColumn) == int(x / AmtColumn):
                if int(z / AmtColumn) == int((z + 1) / AmtColumn):
                    a[i] = NewAlphabet[z + 1]
                else:
                    a[i] = NewAlphabet[z - AmtColumn + 1]
                if int(x / AmtColumn) == int((x + 1) / AmtColumn):
                    a[i+1] = NewAlphabet[x + 1]
                else:
                    a[i+1] = NewAlphabet[x - AmtColumn + 1]
            else:
                a[i] = NewAlphabet[z + ((x % AmtColumn) - (z % AmtColumn))]
                a[i+1] = NewAlphabet[x - ((x % AmtColumn) - (z % AmtColumn))]

if ChoiceAction == 1:
    for i in range(0,len(a),2):
        z = NewAlphabet.index(a[i])
        x = NewAlphabet.index(a[i + 1])
        if z % AmtColumn == x % AmtColumn:
            a[i] = NewAlphabet[z - AmtColumn]
            a[i+1] = NewAlphabet[x - AmtColumn]
        else:
            if int(z / AmtColumn) == int(x / AmtColumn):
                if int(z / AmtColumn) == int((z - 1) / AmtColumn):
                    a[i] = NewAlphabet[z - 1]
                else:
                    a[i] = NewAlphabet[z + AmtColumn - 1]
                if int(x / AmtColumn) == int((x - 1) / AmtColumn):
                    a[i+1] = NewAlphabet[x - 1]
                else:
                    a[i+1] = NewAlphabet[x + AmtColumn - 1]
            else:
                a[i] = NewAlphabet[z + ((x % AmtColumn) - (z % AmtColumn))]
                a[i+1] = NewAlphabet[x - ((x % AmtColumn) - (z % AmtColumn))]
    i = 1
    while h > 2:
        h -= 1
        if a[i] == AdditionalSymbol and a[i - 1] == a[i + 1]:
            a.pop(i)
            h = h-1
        i = i+1
    if a[-1] == 'ъ':
        a.pop(-1)

print (*a, sep= '')