my_string=input('Enter a string:- ')
count={}
for i in my_string:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print('Count Frequency')
for key,value in count.items():
    print(f'{key} occurs {value} items')