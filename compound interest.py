#compound interest calculator
import math
def compound_interest(principle, rate, time):   
    CI = principle * (math.pow((1 + rate / 100), time)) 
    print("Compound interest is Rs.", CI)

    
prin=int(input("Enter Principal Value : "))
rate=float(input("Enter Rate of Interest : "))
tim=int(input("Enter time period :"))
compound_interest(prin,rate,tim)
