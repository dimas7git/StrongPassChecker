import string
import random

def strong_pass(length=18):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

passw = input("Digite a senha: ")
letraMaius = string.ascii_uppercase + "Ç"
letraMinus = string.ascii_lowercase + "ç"

countLower = any(c in letraMinus for c in passw)
countUpper = any(c in letraMaius for c in passw)
countNum = any(c in string.digits for c in passw)
countSpecial = any(c in string.punctuation for c in passw)

score = countLower + countUpper + countNum + countSpecial
score += len(passw) > 8
score += len(passw) > 10
score += len(passw) > 13
score += len(passw) > 15

with open('senha_comum.txt', 'r') as f:
    senha = f.read().splitlines()

vazada = False
if passw in senha:
    print("Senha comum/vazada\n")
    vazada = True

if(vazada==False):
    if score <= 2:
        print("Senha Muito Fraca")
    elif score <= 4:
        print("Senha Fraca")
    elif score <= 6:
        print("Senha Mediana")
    elif score < 8:
        print("Senha Forte")
    else:
        print("Senha Muito Forte")

if(vazada==True) or (score <= 6):
        answer = input("Sua senha é vazada ou não é forte. Deseja gerar uma senha forte? (S/N): ")
        if answer.lower() == 's':
            new_passw = strong_pass()
            print("Senha forte gerada:", new_passw)