a=5
factorial=1
if(a<0):
  print("the factorial number is negative") 
elif(a==0):
  print("the factorial number 0 is 1")
else:
  for i in range(1,a+1):
     factorial=factorial*i
  print("the factorial of",a,"is",factorial) 
