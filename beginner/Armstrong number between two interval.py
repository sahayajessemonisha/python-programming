a=150
b=160
for x in range(a,b+1):
   m=len(str(x)) 
   sum=0
   temp=x
   While(temp>0):
     r=temp%10
     sum=sum+(r**m)
     temp=temp//10
   if(x==sum):
      print(x) 
