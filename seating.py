h1={1:11,2:9,3:7,4:5,5:3,6:1,7:-1,8:-3,9:-5,10:-7,11:-9,0:-11}
h={1:"WS",2:"MS",3:"AS",4:"AS",5:"MS",6:"WS",7:"WS",8:"MS",9:"AS",10:"AS",11:"MS",0:"WS"}
n=int(input())
for i in range(n):
    a=int(input())
    res=a
    a=a%12
    print(""+str(res+int(h1[a]))+" "+str(h[a]))
