# # Write a Python program to add 'ing' at the end of a given string (length 
# # should be at least 3). If the given string already ends with 'ing' then add 
# # 'ly' instead if the string length of the given string is less than 3, leave it 
# # unchanged





# # str1 = "Training"
# # str2 = " MuMbai, India"
# # print("The given original string : " + str(str1))
# # print("The string given to append to the previous string: " + str(str2))
# # res = str1 + str2
# # print("The Modified string is obtained as follows:")
# # print(res)


# def add_string(str1):
#     if(len(str1)>=3):
#       if (str1[-3::] == 'ing'):
#         str1+='ly'
#       else:
#         str1+='ing'
#     return str1

# str1="com"
# print(add_string(str1))

# # ///////

# def a(s):
#   if len(s) >= 3:
#     if s.endswith("ing"):
#       s += "ly"
#     else:
#       s += "ing"
#   return s

# s='com'
# print(a(s))


# # //////////////

# #  Write a Python program to find the first appearance of the substring 
# # 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
# # whole 'not'...'poor' substring with 'good'. Return the resulting string.


# def not_poor(str):
#     snot=str.find('not')
#     spoor = str.find('poor')
#     if spoor > snot and snot > 0 and spoor > 0:
#         str = str.replace(str[snot:(spoor+4)], 'good')
#         return str
#     else:
#         return str
    

# print(not_poor('The lyrics is not that poor!'))  
# print(not_poor('The lyrics is poor!'))    



# # Write a Python function that takes a list of words and returns the length 
# # of the longest one


# def word(words_list):
#     word_len=[]
    
#     for n in words_list:
#         word_len.append((len(n),n))
#         word_len.sort()     
#     return word_len[-1][0],word_len[-1][1]
    
# result = word(["PHP", "Exercises", "Backend"])
# print('\n',result[1])
# print(result[0])



# # Write a Python function to reverses a string if its length is a multiple of

# def string(srt):
#     if len(str)%4==0:
#         return ''.join(reversed(str))
#     else:
#         return str
        
# str='vishalmavani'
# print(string(str))


# # Write a Python function to insert a string in the middle of a string


# def string_middle(str,word):
#     return str[:2]+word+str[-2:]

# print(string_middle('1001','paython'))


# a='what {} you '.format('are')
# print(a)
