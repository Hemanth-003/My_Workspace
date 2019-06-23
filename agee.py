print("enter the date format as dd/mm/yy ")
a=input("enter current date :-")
l1=a.split("/")
l3=[]
for i in l1:
      l3.append(int(i))
if(l3[2]%4!=0 and l3[1]==2 and l3[0]==29):
      print("invalid current date")
      exit()
elif(l3[2]==0 or l3[1]==0 or l3[0]==0):
      print("invalid current date")
      exit()
elif(l3[1]==4 and  l3[0]>30):
      print("invalid current date")
      exit()
elif(l3[1]==6 and  l3[0]>30):
      print("invalid current date")
      exit()
elif(l3[1]==9 and  l3[0]>30):
      print("invalid current date")
      exit()
elif(l3[1]==11 and  l3[0]>30):
      print("invalid current date")
      exit()
elif((l3[1]==1 or l3[1]==3 or l3[1]==5 or l3[1]==7 or l3[1]==8 or l3[1]==10 or l3[1]==12) and  l3[0]>31):
      print("invalid current date")
      exit()
b=input("enter date of birth :-")
l2=b.split("/")
l4=[]
for i in l2:
      l4.append(int(i))
if(l4[2]>l3[2]  or l4[1]>12 or l3[1]>12 or l4[0]>31 or  l3[0]>31):
                print("invalid current or birth date")
                exit()
else:
       if(l4[2]%4!=0 and l4[1]==2 and l4[0]==29):
             print("invalid birth date")
             exit()
       elif (l4[2] == 0 or l4[1] == 0 or l4[0] == 0):
           print("invalid birth date")
           exit()
       elif( l4[1]==2 and l4[0]>29):
             print("invalid birth date")
             exit()
       elif (l4[2]==l3[2]  and l4[1]>=l3[1] and l4[0]>=l3[0] ):
             print("invalid birth date")
             exit()
       elif(l4[1]==4 and  l4[0]>30):
             print("invalid birth date")
             exit()
       elif(l4[1]==6 and  l4[0]>30):
             print("invalid birth date")
             exit()
       elif(l4[1]==9 and  l4[0]>30):
             print("invalid birth date")
             exit()
       elif(l4[1]==11 and  l4[0]>30):
             print("invalid birth date")
             exit()
       elif((l4[1]==1 or l4[1]==3 or l4[1]==5 or l4[1]==7 or l4[1]==8 or l4[1]==10 or l4[1]==12) and  l4[0]>31):
             print("invalid  birth date")
             exit()
       elif(l4[2]<l3[2]  and l4[1]<=l3[1] and l4[0]<l3[0]):
             print("age=",l3[2]-l4[2],"years")
       elif ((l4[2]<l3[2]  and l4[1]>=l3[1]) and l4[0]>l3[0]):
             print("age=",l3[2]-l4[2]-1,"years")
       else:
             print("age=",l3[2]-l4[2],"years")