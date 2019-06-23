ones={0:"zero",1:"0ne",2:"two",3:"three",4:"f0ur",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
tens={0:"ten",1:"eleven",2:"twelve",3:"thirteen",4:"fourteen",5:"fifteen",6:"sixteen",7:"seventten",8:"eighteen",9:"ninteen"}
thy={2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninty"}
a=input("enter number from keyboard=")
print(int(a),"IN ENGLISH TRANSFORMATION IS:")
k=tuple(a)
s=list(k)
if(len(a)==1):
   print(ones[int(a)])
elif(len(a)==2):
   if(s[0]=="0"):
      print(ones[int(s[1])])
   elif(s[0]=="1"):
      print(tens[int(s[1])])
   elif(s[0]!="1" and s[1]=="0"):
      print(thy[int(s[0])])
   else:
      print(thy[int(s[0])]+" "+ones[int(s[1])])
elif(len(a)==3):
   if(s[0]=="0" and s[1]=="0"):
      print(ones[int(s[2])])
   elif(s[0]=="0" and s[1]=="1"):
      print(tens[int(s[2])])
   elif(s[0]=="0" and s[1]!="1" and s[2]=="0"):
      print(thy[int(s[1])])
   elif (s[0] == "0" and s[1] != "1" and s[2]!= "0"):
      print(thy[int(s[1])]+" "+ones[int(s[2])])
   elif(s[0]!="0" and s[1]=="0" and s[2]=="0"):
      print(ones[int(s[0])]+" "+"hundred")
   elif(s[1]=="0"):
      print(ones[int(s[0])]+" "+"hundred and"+" "+ones[int(s[2])])
   elif(s[1]=="1"):
      print(ones[int(s[0])] + " " + "hundred and" + " " + tens[int(s[2])])
   elif(s[2]=="0"):
      print(ones[int(s[0])] + " " + "hundred and" + " " + thy[int(s[1])])
   else:
      print(ones[int(s[0])] + " " + "hundred and" + " " + thy[int(s[1])]+" "+ones[int(s[2])])
elif(len(a)==4):
   if(s[0] != "0" and s[1] == "0" and s[2] == "0" and s[3]=="0"):
      print(ones[int(s[0])]+" "+"thousand")
   elif(s[0] != "0" and s[1] == "0" and s[2] == "0" and s[3]!="0"):
      print(ones[int(s[0])]+" "+"thousand"+" "+"and"+" "+ones[int(s[3])])
   elif (s[1] == "0" and s[2] == "1"):
      print(ones[int(s[0])]+" "+"thousand"+" "+"and"+" "+tens[int(s[3])])
   elif (s[1] == "0" and s[2]!= "1" and s[3]=="0"):
      print(ones[int(s[0])]+" "+"thousand"+" "+"and"+" "+thy[int(s[2])])
   elif (s[1] == "0" and s[2]!= "1" and s[3]!="0"):
      print(ones[int(s[0])]+" "+"thousand"+" "+"and"+" "+thy[int(s[2])]+" "+ones[int(s[3])])
   elif (s[0]!= "0" and s[1]!= "0" and s[2] == "0" and s[3] == "0"):
      print(ones[int(s[0])]+" "+"thousand"+" "+ones[int(s[1])]+" "+"hundred")
   elif (s[0]!= "0" and s[1]!= "0" and s[2] == "0" and s[3]!= "0"):
      print(ones[int(s[0])]+" "+"thousand"+" "+ones[int(s[1])]+" "+"hundred"+" "+"and"+" "+ones[int(s[3])])
   elif (s[2] == "1"):
      print(ones[int(s[0])]+" "+"thousand"+" "+ones[int(s[1])]+" "+"hundred"+" "+"and"+" "+tens[int(s[3])])
   elif (s[2]!= "1" and s[3]=="0"):
      print(ones[int(s[0])]+" "+"thousand"+" "+ones[int(s[1])]+" "+"hundred"+" "+"and"+" "+thy[int(s[2])])
   elif (s[2]!= "1"):
      print(ones[int(s[0])]+" "+"thousand"+" "+ones[int(s[1])]+" "+"hundred"+" "+"and"+" "+thy[int(s[2])]+" "+ones[int(s[3])])