#  Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.


def mix_string(a,b):
    
    new_a=a[:2]+b[:2]
    
    new_b=b[:2]+a[:2]
    
    return new_a+' '+new_b


print(mix_string('xyz','abc'))