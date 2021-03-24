str=input("enter the string")
s={}
for i in str:
  if i in s:
     s[i]+=1
  else:
     s[i]=1
print("count of all characters are: ",s)