# Write a Python program that will return true if the two given integer 
# values are equal or their sum or difference is 5


# 5,5=true
# 2+3=true
# 10-5=true


def test(a,b):
    if a==b or(a-b)==5 or (a+b)==5:
        return True
    else:
        return False
print(test(7,5))
print(test(2,4))
print(test(10,5))