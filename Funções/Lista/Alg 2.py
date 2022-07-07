import Func as f
a = input('Digite um Texto:\n').lower()
b = input('\nQual letra você deseja contar?\n').lower().strip()

print(f.letCount(b[:1], a))