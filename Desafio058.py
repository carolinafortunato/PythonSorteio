from random import randint
s = randint(0, 10)
num = int(input('Tente adivinhar qual número de 0 e 10 o computador pensou: '))
c = 1
# while not acertou:
while s != num:
    if s < num:
        print('O número é menor!')
    if s > num:
        print('O número é maior!')
    num = int(input('Tente novamente: '))
    c += 1
print('O número sorteado pelo computador foi {}.' .format(s))
print('Parabéns, você acertou na {}ª tentativa!' .format(c))
