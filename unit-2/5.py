# 5. Write a program to demonstrate the use of break continue and pass statements. 


print("Break Statement")

for i in range(1, 6):

    if i == 4:
        break     

    print(i)



print("\nContinue Statement")

for i in range(1, 6):

    if i == 3: # skip number 3.
        continue  
    print(i)



print("\nPass Statement")

for i in range(1, 6):

    if i == 3: # does not skip
        pass       

    print(i)
