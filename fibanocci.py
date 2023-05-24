a=1
b=2
evenvalue =2

while b <= 4000000 :
    a=b
    b=a+b
if (b % 2== 0):
  evenvalue= evenvalue+b 
  print(evenvalue)
