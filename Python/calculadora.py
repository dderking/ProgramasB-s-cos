def adicao(num1,num2):
    return  num1+num2
def subtracao(num1,num2):
    return  num1-num2
def multiplicacao(num1,num2):
    return  num1*num2
def divisao(num1,num2):
    if num2 ==0:
        return 'Erro: Divisão por 0'
    return  num1//num2

while True:
    entrada = input().split()
    op = int(entrada[0])
    if op == 5: break
    num1 = int(entrada[1])
    num2 = int(entrada[2])
    if op == 1:
        l = adicao(num1,num2)
    if op == 2:
        l = subtracao(num1,num2)
    if op == 3:
        l = multiplicacao(num1,num2)
    if op == 4:
        l = divisao(num1,num2)
    print(l)
    if l == 'Erro: Divisão por 0':break
