# a=int(input('enter first value:- '))
# b=int(input('enter second value:- '))
# c=int(input('enter third value:- '))

# if a==b or b==c or c==a:
#     print('sum is:- ',0)
# else:
#     print('sum is:- ',a+b+c)
    
    
# # function

def sum(a,b,c):
    if a==b or b==c or c==a:
        sum=0
    else:
        sum=a+b+c
    return sum
print(sum(2,3,4))
print(sum(2,3,2))
print(sum(1,2,3))