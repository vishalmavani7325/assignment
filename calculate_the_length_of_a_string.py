# a='vishal mavani'
# print(len(a))


# # /////
# def string(str1):
#     count=0
#     for i in str1:
#         count+=1
#     return count
# print(string('vishal mavani '))


class st:
    def __init__(self,id):
        self.id=id
obj=st(100)
obj.__dict__['name']='vishal'
print(obj.id+len(obj.__dict__))