n=int(input("enter a number:))
f=0
for x in range(2,n-1):
  if(n%x==0):
    f=1
if(f==1):
  print('not prime')
else:
  print('prime')
