
#==============# Problem:
"""

Ronaldo was getting bored at university so he decided to create and play a game. 
The game is going to take a 4 digit number as input and he will have 3 lives to win this game. 
First, he is going to get the last digit and check if the number is prime or not. 
If he finds 3 prime numbers before he loses his 3 lives then he wins. Otherwise, 
game over and he lost.

"""
#==============# Solution:

def Get4DigitNumber():

    while True:
        try:
            number=int(input("Pleae Enter 4 Digit number:"))
            if  (number>=1000 and number<=9999):
                return number #print ("ok")#
            else:
                    print("Invalid number")

        except Exception as e:
            print(f"Unexpected Error Occured: Only 4 digits numeber are allowed") #{e}
     


def PrimeCheck(inputNumber):
    
    if inputNumber > 1:
        for i in range(2,inputNumber):
            if (inputNumber % i) == 0:
                return False
                break
    else:
        return False
    
    return True
#Initialize variables
found:int =0
lives:int =3

InputNumber=Get4DigitNumber()


ReversedNumber=str(InputNumber)[::-1]

for i in range(0,4):
    CurNumber=int(str(ReversedNumber)[i:i+1])
  
    if PrimeCheck(CurNumber):
       found+=1
       
       if found<4:
         print(f"{CurNumber} is prime! ({found}/3 found)")
       
    else:
       lives-=1 
            
       if i<3:
        print(f"{CurNumber} is not prime. lives left {lives}" )
       

if found>=3:
    print(f"Congratulations! You won the game!" )
else:
    print(f"Game over! You Lost" )








