def main():
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
    
    
main()




    
