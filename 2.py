import random
from collections import Counter


def generate():
    deck = []
    for v in C_VALUES:
        for s in C_SUITS:
            deck.append(v + s)
    hand = random.sample(deck, 5)
    return hand


C_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
C_SUITS = ['♠', '♥', '♦', '♣']
street = "234567891AJKQ"


def th(s):
    c = 0
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            c += 1
    if c != 0:
        return False
    else:
        return True


def fl(s):
    s = list(set(s))
    if len(s) == 1:
        return True
    else:
        return False


def check_combination(hand):
    v, s = [], []
    vs = ''
    hand.sort()
    for i in range(len(hand)):
        v.append(hand[i][0])
        s.append(hand[i][-1])
    # print(v, s)
    pairs = []
    counter = Counter(v)
    for count in counter.items():
        pairs.append(count[1])
    # print(pairs)

    for i in range(5):
        vs += v[i]
    # print(vs)
    if len(pairs) == 4:
        return "Одна пара"
    if (3 in pairs) and (2 not in pairs):
        return "Тройка"
    if (len(pairs) == 3) and (3 not in pairs):
        return "Две пары"
    if (len(pairs) == 5) and (th(s) == True) and (vs in street):
        return "Стрит"
    if fl(s) == True:
        return "Флэш"
    if (len(pairs) == 2) and (4 in pairs):
        return "Каре"
    if v == ['1', 'A', 'J', 'K', 'Q'] and fl(s) == True:
        return "Флэш-рояль"
    if (vs in street) and ("A" not in vs) and (fl(s) == True):
        return "Стрит-флэш"
    if (2 in pairs) and (3 in pairs):
        return "Фулл-хаус"
    return "Старшая карта"


hand = generate()
print("Карты на руке:", hand)
combination = check_combination(hand)
print("Покерная комбинация:", combination)
