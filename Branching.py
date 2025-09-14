#==============# Problem:
"""
After working for a year finally Karim got his salary and bonus for Eid 2025,
now he decides to do some kind of shopping for his family.
His salary is x Tk and he got 75% bonus of his salary. He decides to 
spend money on shopping precisely so that everyone gets what they want. 
He planned to distribute 45% of his total money for his wife and 45% for 
his son. The remaining 10% will be saved for emergency cases. His wife wants a 
new laptop that costs around 90,000 Tk and his son wants a PS5 that costs 
about 70,000 Tk with games and an extra controller to play with friends that 
costs about 7,000 Tk. Now, take x as input from the user and see if Karim can fully 
fulfill his families wish, if not possible then see whether he can use remaining budget 
from son and wife to fulfill each other's wish. The saving part should not 
be touched by any means.
"""
#==============# Solution:



Salary = float(input("Enter Karim's Salary: "))
Bonus = (75/100)*Salary
Total = Salary + Bonus
WifeBudget=(45/100)*Total
SonBudget = (45/100)*Total
Savings = (10/100)*Total
Costs = Total - Savings
WifeCosts = 90000
SonCosts= (70000 + 7000)

print("Amount with Bonus:",Total)
print("Wife Budget: ",WifeBudget)
print("Son Budget: ",SonBudget)
print("Savings: ",Savings)
if WifeCosts <= Costs-SonCosts:
    print("Shopping Done for Wife with remaining money from Sons budget!")
elif SonBudget >= Costs - SonCosts:
    print("Cannot do shopping for either of them!")
elif WifeCosts >= Costs - SonCosts:
    print("Cannot do shopping for wife even with remaining money from his son's budget!")



if SonBudget <= Costs - SonCosts:
    print("Shopping Done for Son!")

elif SonBudget >= Costs - SonCosts:
    print("")
    
    





    
