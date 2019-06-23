a=int(input("enter number :-"))
for i in range(1,a+1):
   for j in range(1,a+1):
      if(i==j):
         print("$",end="  ")
      elif(i==1 or i==a or j==1 or j==a):
         print("*",end="  ")
      else:
         print(" ",end="  ")
   print(" ")      
for i in range(1,a+1):
   for j in range(1,a+1):
      if(i==1 or i==a or j==1 or j==a):
         print("*",end=" ")
      else:
         print(" ",end=" ")
   print(" ")
for i in range(1,2000 ,2):
   print(i,end=",")
   if(i==1000):
      exit()
