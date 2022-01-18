dan =input('Enter Number')

for i in range(1,10):
  print(dan,'x',i,'=',int(dan)*i)
  
#eval함수를 쓰면 스트링 형식의 명령어를 그대로 해석하지 않고 명령어가 실행되게 해준다
eval('print(10)')
