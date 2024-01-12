num=int(input("Enter a number :- "))
factorial=1
if num<0:
    print("factorial dose not exise")
else:
    for i in range(1,num+1):
        factorial=factorial*i
        print("factorial of ",num,"is",factorial)