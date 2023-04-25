# Напишите программу, которая на вход принимает два числа A и B, и возводит 
# число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

A = int(input('A:'))
B = int(input('B:'))
def Power(A, B):
    if B > 0:
        return A * Power(A, B-1)
    else:
        return 1
res = Power(A, B)
print("res = ", res)