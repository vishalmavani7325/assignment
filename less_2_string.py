# # chars from a given a string. If the string length is less than 2, return 
# # instead of the empty string


# def string(str):
#     if(len(str))<2:
#         return ''
    
#     return str[:2]+str[-2:]

# print(string('VishalMavani'))
        
        
new_string='Analysts believe that HAL is on a trajectory to experience a re-rating similar to that witnessed by Bharat Electronics in the past decade. The optimistic sentiment is underscored by the expectation that HAL will successfully execute its plans, including faster order completions, production ramp-ups, & enhanced manufacturing value.'
l1=new_string.split(' ')
print(l1)
l2=[]

for i in l1:
    # print(i.capitalize())
    l2.append(i.capitalize())
    print(l2)
    
ans=' '.join(l2)
print(ans)