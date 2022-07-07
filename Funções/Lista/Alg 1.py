import Func as f

lados = [f.getMeds('Cateto 1'), f.getMeds('Cateto 2'), f.getMeds('Hipotenusa')]

if f.checkTry(lados):
    print(f'Seu triângulo é {f.triangType(lados)}')
else:
    print('Seu triângulo não existe!')