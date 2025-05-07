chmod = "calculadora.sh"
chmod 744  calculadora.sh

def soma(a , b):
  return(a + b)
def subtracao(a , b):
  return(a - b)
def multiplicacao(a , b):
  return(a * b)
def divisao(a , b):
  return(a / b)
print("Olá vamos cálcular?")
nome = input("Como posso te chamar? ")
print(f"Olá, {nome}! Prazer em te conhecer.")
while True:
  print("1. Soma (+)")
  print("2. Subtração (-)")
  print("3. Multiplicação (*)")
  print("4. Divisão (/)")
  print("5. Sair")

  escolha = input("Escolha uma opção: ")

  if escolha == "5":
    print("Saindo do programa...")
    break

  if escolha not in ("1", "2", "3", "4"):
    print("Opção inválida. Tente novamente")
    continue

  try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
  except ValueError:
    print("Entrada inválida. Certifique-se de digitar números válidos.")
    continue

  if escolha == "1":
    resultado = soma(num1, num2)
    operacao = "+"

  if escolha =="2":
    resultado = subtracao(num1, num2)
    operacao = "-"

  if escolha =="3":
    resultado = multiplicacao(num1, num2)
    operacao = "*"

  if escolha == "4":
    resultado = divisao(num1, num2)
    operacao = "/"

  print(f"{nome} seu resultado é: {num1} {operacao} {num2} = {resultado}")