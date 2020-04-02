n=input()
h={"z":0,"o":0}
for i in n:
    h[i]=h[i]+1
if(2*h["z"]==h["o"]):
    print("Yes")
else:
    print("No")
