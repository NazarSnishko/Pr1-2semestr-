import math
def Herona(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
def Height(a, b):
    return 0.5 * a * b
def kyt(a, b, c):
    radiys= math.radians(c)
    return 0.5 * a * b * math.sin(radiys)
metod={
    1: Herona,
    2: Height,
    3: kyt
}
NomerMetod= int(input("Виберіть спосіб : 1. Формула Герона, 2. За висотою, 3. За 2 сторонами і кутом : "))
if NomerMetod in metod:
    dani=map(float, input("Введіть дані: ").split())
    P=metod[NomerMetod](*dani)
    print("Площа трикутника: ",P)
else:
    print("помилка")
    
