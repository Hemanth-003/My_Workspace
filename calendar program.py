sd=int(input("enter start day in that month(0 - 7) ;"))
days=int(input("enter number of days :"))
print("sun mon tue wed thu fri sat")
print("- - - - - - - - - - - - - - - - - ")
for i in range (sd-1):
   print(end="    ")
i=sd-1
for j in range(1,days+1):
   if(i>6):
      print()
      i=1
   else:
      i=i+1
   print(str(j),end=" \t ")
