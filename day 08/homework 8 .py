# And ოპერატორს როცა ვიყენებთ ორივეს პირობას უნდა აკმაყოფილებდეს, რომ მივიღოთ True. სხვა შემთხვევაში მივიღებთ False-ს


num=3 
num1=28
print(num < num1)
print(num > num1)
print(num <= num1)
print(num >= num1)



num2 = 5

# print(True and True) # True რადგან ორივე პირობას აკმაყოფილებდა 
# print(True and False) # False რადგან ერთი პირობას არ აკმაყოფილებდა 
# print(False and True) # False რადგან ერთი პირობას არ აკმაყოფილებდა 
# print(False and False) # False რადგან არცერთ პირობას არ აკმაყოფილებდა 

# print(True or True) # True რადგან ორივე პირობას აკმაყოფილებდა 
# print(True or False) # True რადგან ერთერთ პირობას აკმაყოფილებდა 
# print(False or True) # True რადგან ერთერთ პირობას აკმაყოფილებდა 
# print(False or False) # False რადგან არცერთ პირობას არ აკმაყოფილებდა 

print("----------- AND -----------")

print(num >= 1 and num <= 10) # Trueრადგან ორივე პირობას აკმაყოფილებდა 
print(num >= 1 and num <= 4) # False რადგან ერთ პირობას არ აკმაყოფილებდა  
print(num > 5 and num <= 10) # False რადგან ერთ პირობას არ აკმაყოფილებდა 
print(num > 5 and num > 10) # False რადან არცერთ პირობას არ აკმაყოფილებდა 

print("----------- OR -----------")

print(num >= 1 or num <= 10) # True რადგან ორივე პირობას აკმაყოფილებდა 
print(num >= 1 or num <= 4) # True რადგან ერთერთს აკმაყოფილრბდა 
print(num > 5 or num <= 10) # True რადგან ერთერთ პირობას აკმაყოფილებდა 
print(num > 5 or num > 10) # False რადგან არცერთ პირობას არ აკმაყოფილებდა 



num3=8

print(num3 >= 2 or num3 <= 10)  
print(num3 >= 2 or num3 <= 8)  
print(num3 > 7 or num3 <= 9)  
print(num3 > 6 or num3 > 6) 