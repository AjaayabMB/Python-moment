num=range(2,100)
su=0
ch=0
for i in num:
  v=range(2,i-1)
  for j in v:
    if(i%j==0):
     ch=ch+1
  if(ch==0):
   su=su+i
  ch=0
print(su)