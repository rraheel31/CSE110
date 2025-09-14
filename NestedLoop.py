#==============# Problem:
"""

Ronaldo was getting bored at university so he decided to create and play a game. 
The game is going to take a 4 digit number as input and he will have 3 lives to win this game. 
First, he is going to get the last digit and check if the number is prime or not. 
If he finds 3 prime numbers before he loses his 3 lives then he wins. Otherwise, 
game over and he lost.

"""
#==============# Solution:



Entered=input("Enter a 4-digit number:")
num1=Entered[0:1]
num2=Entered[1:2]
num3=Entered[2:3]
num4=Entered[3:4]
ans1=int(num1)
ans2=int(num2)
ans3=int(num3)
ans4=int(num4)
lives = 3
found = 0
primecheck1=True
primecheck2=True
primecheck3=True
primecheck4=True


if ans1 > 1:
    for i in range(2,ans1):
        if (ans1 % i) == 0:
            primecheck1 = False
            break
else:
    primecheck1 = False




if ans2 > 1:
    for j in range(2,ans2):
        if (ans2 % j) == 0:
            primecheck2 = False
            break
else:
    primecheck2 = False




if ans3 > 1:
    for k in range(2,ans3):
        if (ans3 % k) == 0:
            primecheck3 = False
            break
else:
    primecheck3 = False



if ans4 > 1:
    for k in range(2,ans4):
        if (ans4 % k) == 0:
            primecheck4 = False
            break
else:
    primecheck4 = False

   


if primecheck4 == True:
    found += 1
    print(ans4, f"is prime!({found}/3 found) ")
else:
    lives -= 1
    print(ans4,"is not prime.Lives left: ",lives)

if primecheck3 == True:
    found += 1
    print(ans3,f"is prime!({found}/3 found)")
else:
    lives -= 1
    print(ans3,"is not prime.Lives left: ",lives)

if primecheck2 == True:
    found += 1
    print(ans2,f"is prime!({found}/3) found")
else:
    lives -= 1
    print(ans2,"is not prime.Lives left: ",lives)

if primecheck1 == True:
    found += 1
    print(ans1,f"is prime!({found}/3) found")
else:
    lives -= 1
    print(ans1,"is not prime.Lives left: ",lives)

if lives > 0 or found == 3:
    print("Congratulations! You won the game!")
else:
    print("Game over! You lost.")


  














