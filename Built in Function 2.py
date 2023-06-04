


#--------------------------------------
#----------- Built in Function 2---
#--------------------------------------
# sum()
# round()
# range()
# print()
#--------------------------------------

# sum(iterable , start)


a = [1, 40, 19, 10]
print(sum(a)) # 70
print(sum(a , 40)) #110

print("-" * 50) # --------------------------------------------------

# round(number, numofdigits)

print(round(150.499)) # 150
print(round(150.501)) # 151
print(round(150.501 , 2)) # 150.5


print("-" * 50) # --------------------------------------------------

# range(start , end , steps)

print(list(range(0))) # []
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0,20,2))) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print("-" * 50) # -------------------------------------------------

# print()

print("Hello Salar ") # Hello Salar
print("Hello" ,  "Salar") # Hello Salar


print("Hello Salar How Are You") # Hello Salar How Are You
print("Hello" , "Salar" , "How" , "Are" , "You") # Hello Salar How Are You


print("First Line" , end ="/n") # First line
print("Second Line", end ="/n" ) # Seconde Line


print("First Line" , end =" ") # First Line Second Line/n
print("Second Line") # Third line
print("Third Line") # 

