def a(key,size=11):
    hash1= key%size
    return hash1
    
def b(key):
    hash2=7-(key%7)
    return hash2


print(a(16)+b(16)*2)
print(a(58)+b(58)*2)
print(a(10))
print(b(58))