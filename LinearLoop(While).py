from datetime import datetime as dt
import math

InitialOxygenCylinderP = float(input("Enter the initial price of an oxygen cylinder in 1999: "))
InitialWaterReserveP = float(input("Enter the initial price of a unit of water reserve in 1999: "))
MonthlyInflataionRateOxygenCylinder = float(input("Enter the monthly inflation rate (percentage) for oxygen cylinders:"))
MonthlyInflataionRateOxygenCylinderPercentage= MonthlyInflataionRateOxygenCylinder/100
MonthlyInflationRateWaterReserve = float(input("Enter the monthly inflation rate (percentage) for water reserves:"))
MonthlyInflationRateWaterReservePercentage = MonthlyInflationRateWaterReserve/100
InitialYear=1999
CurrentYear = dt.now().year
DifferenceYear=CurrentYear - InitialYear
Months = DifferenceYear*12
i=0
while i <= Months: 
    CurrentOxygenCylinderP = InitialOxygenCylinderP + (InitialOxygenCylinderP*MonthlyInflataionRateOxygenCylinderPercentage)
    InitialOxygenCylinderP = CurrentOxygenCylinderP

    CurrentWaterReserveP = InitialWaterReserveP + (InitialWaterReserveP*MonthlyInflationRateWaterReservePercentage)
    InitialWaterReserveP = CurrentWaterReserveP
    i = i+1    
print("Current price of an oxygen cylinder: ",math.ceil(CurrentOxygenCylinderP*100)/100)
print("Current price of a unit of water reserve: ",math.ceil(CurrentWaterReserveP*100)/100)
if CurrentOxygenCylinderP > CurrentWaterReserveP:
    print("The price of oxygen cylinders has increased more.")
elif CurrentOxygenCylinderP == CurrentWaterReserveP:
    print("The price of both oxygen cylinders and water reserves are same.")
else:
    print("The price of water reserves has increased more.")



    








