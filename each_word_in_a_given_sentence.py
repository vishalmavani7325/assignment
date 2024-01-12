#  Write a Python program to count the occurrences of each word in a 
# given sentence


# a=input('enter a paragraph:- ')
# b=a.split()
# c={}
# for i in b:
#     if i in c:
#         c[i]+=1
#     else:
#         c[i]=1
# print(c)


def count(str):
    dict={}
    a=str.split()
    for i in a:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
        return dict
    
para=input('enter a para: ')
print(count(para))