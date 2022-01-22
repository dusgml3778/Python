# color = input('Enter color:')
# if color =='blue':
#   pass
# elif color == 'red':
#   print('No')  
# else :
#   print('End')  
  
a = range(10)
print(a) # 리스트화 안하면 함수자체가 출력
print(list(a))

for i in [1,2,3,4,5]:
  print(i)

sum = 0
for i in range(1,11):
  sum+=i
print(sum)    

for x in range(2,5):
  print(f'==={x}===')
  for y in range(1,10):
    print(f'{x}*{y}={x*y:2d}')
  print()

a = 10

print('%d' %a)
print('{}'.format(a))
print(f'{a}')

a = [(1,2),(3,4),(5,6)]

for (first,last) in a :
  print(f'{first}+{last}={first+last}')