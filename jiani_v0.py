print ("hello world")
print ("2nd line", end = '')
print(' continue 2nd line')
a = 153
b = 546
c = a+b
print(c)
print(f'a={a}')
print(f'b={b}')
print(f'c={c}')
type_c = type(c)
print(f'type:{type(c)} c={c}')

d = 14896179785614614164721136614114876323678999053288653268765443
e = 1
f = d + e
print(f'f={f}')
print(f'type_f:{type(f)}')

s_d = str(d)
num_digits_d = len(s_d)
print(f'num_digits_d:{num_digits_d}')

arr_a = [3,5,7,9]
print(f'arr_a={arr_a}')
print(f'3rd elem: {arr_a[2]}')

s_1 = 'abcdefg'
s_2 = 'hijkl'
s_3 = s_1 + s_2
print(f's_3={s_3}')
print(f's_1[0]={s_1[0]}')