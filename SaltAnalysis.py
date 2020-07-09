# This Program is about Salt Analysis

import random

print("Guess that salt!")
print("Here, you can test on the salt the number of times there are allowed chemicals.")
print("(P.S. Only one guess for the salt allowed)")
print()

anion = ['Carbonate', 'Sulphide', 'Sulphite', 'Chloride', 'Nitrate']
cation = ['Ammonium', 'Lead', 'Iron', 'Aluminium', 'Barium']

a = random.randint(0,4)
b = random.randint(0,4)
print("Anions: Carbonate, Sulphur, Sulphite, Chloride, Nitrate")
print()

print("Allowed chemicals for testing anion: dilH2SO4, concH2SO4, KMnO4, MgSO4, BaCl2, FeSO4, AgNO3, C12H11N")
print()

reply = 'Y'
count = 0
while reply == 'Y' or reply == 'y':
    print()
    acid = input("Enter a chemical from the given list for testing anion: ")
    sml = acid.lower()
    if anion[a] == 'Carbonate':
        if sml == 'conch2so4' or sml == 'kmno4' or sml == 'feso4' or sml == 'agno3' or sml == 'c12h11n':
            print("No reaction")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'dilh2so4':
            print("Colourless gas evolved. Turns lime water milky.")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'bacl2' or sml == 'mgso4':
            print("White precipitate formed.")
            reply = input("Do you want to test again? (Y or N): ")
        else:
            print("KABAM!")

    elif anion[a] == 'Sulphide':
        if sml == 'conch2so4' or sml == 'kmno4' or sml == 'mgso4' or sml == 'bacl2' or sml == 'feso4' or sml == 'agno3':
            print("No reaction")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'c12h11n':
            print("No reaction")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'dilh2so4':
            print("Suffocating rotten egg smell produced")
            reply = input("Do you want to test again? (Y or N): ")
        else:
            print("KABAM!")

    elif anion[a] == 'Sulphite':
        if sml == 'dilh2so4':
            print("Strong rotten egg smell produced")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'bacl2':
            print("White precipitate formed")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'kmno4':
            print("Purple colour observed")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'conch2so4' or sml == 'mgso4' or sml == 'feso4' or sml == 'agno3' or sml == 'c12h11n':
            print("No reaction")
            reply = input("Do you want to test again? (Y or N): ")
        else:
            print("KABAM!")

    elif anion[a] == 'Chloride':
        if sml == 'agno3':
            print("White precipitate formed which is soluble in NH4OH")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'conch2so4':
            print("Pungent smelling white fumes evolved")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'kmno4':
            print("Purple colour observed")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'mgso4' or sml == 'bacl2' or sml == 'feso4' or sml == 'dilh2so4' or sml == 'c12h11n':
            print("No reaction")
            reply = input("Do you want to test again? (Y or N): ")
        else:
            print("KABAM!")

    elif anion[a] == 'Nitrate':
        if sml == 'conch2so4':
            print("Brown gas evolved")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'c12h11n':
            print("Blue colour observed")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'kmno4' or sml == 'mgso4' or sml == 'bacl2' or sml == 'feso4' or sml == 'dilsh2so4' or sml == 'agno3':
            print("No reaction")
            reply = input("Do you want to test again? (Y or N): ")
        elif sml == 'dilh2so4':
            print("No reaction")
            reply = input("Do you want to test again? (Y or N): ")
        else:
            print("KABAM!")
    if count == 7:
        break
    
    count += 1

print()
print("Cations: Ammonium, Lead, Iron, Aluminium, Barium")
print("Allowed chemicals for testing cation: dilHCl, K2HgI4, K2CrO4, NaOH, KI, NH4OH+NH4Cl, NH4Cl+NH4OH+(NH4)2CO3")
print()

ans = 'Y'
chance = 0
while ans == 'Y' or ans == 'y':
    print()
    basic = input("Enter a chemical from the given list for testing cation: ")
    ncap = basic.lower()
    if cation[b] == 'Ammonium':
        if ncap == 'k2hgi4':
            print("Brown precipitate formed")
            ans = input("Do you want to test again? (Y or N): ")
        elif ncap == 'naoh':
            print("Pungent smell produced when gas is passed over a rod dipped in HCl")
            ans = input("Do you want to test again? (Y or N): ")
        elif ncap == 'dilhcl' or ncap == 'k2cro4' or ncap == 'ki' or ncap == 'nh4oh+nh4cl':
            print("No reaction")
            ans = input("Do you want to test again? (Y or N): ")
        elif ncap == 'nh4cl+nh4oh+(nh4)2co3':
            print("No reaction")
            ans = input("Do you want to test again? (Y or N): ")
        else:
            print("KABAM!")

    elif cation[b] == 'Lead':
        if ncap == 'dilhcl':
            print("White precipitate formed")
            ans = input("Do you want to test again? (Y or N): ")
        elif ncap == 'k2cro4':
            print("Yellow precipitate formed")
            ans = input("Do you want to test again? (Y or N): ")
        elif ncap == 'ki' or ncap == 'nh4oh+nh4cl' or ncap == 'k2hgi4' or ncap == 'nh4cl+nh4oh+(nh4)2co3' or ncap == 'naoh':
            print("No reaction")
            ans = input("Do you want to test again? (Y or N): ")
        else:
            print("KABAM!")

    elif cation[b] == 'Iron':
        if ncap == 'nh4oh+nh4cl':
            print("Greenish brown precipitate formed")
            ans = input("Do you want to test again? (Y or N): ")
        elif ncap == 'naoh':
            print("Greenish brown precipitate formed")
            ans = input("Do you want to test again? (Y or N): ")
        elif ncap == 'dilhcl' or ncap == 'k2cro4' or ncap == 'ki' or ncap == 'k2hgi4' or ncap == 'nh4cl+nh4oh+(nh4)2co3':
            print("No reaction")
            ans = input("Do you want to test again? (Y or N): ")
        else:
            print("KABAM!")

    elif cation[b] == 'Aluminium':
        if ncap == 'nh4oh+nh4cl':
            print("White precipitate formed")
            ans = input("Do you want to test again? (Y or N): ")
        elif ncap == 'naoh':
            print("White gelatinous precipitate formed")
            ans = input("Do you want to test again? (Y or N): ")
        elif ncap == 'dilhcl' or ncap == 'k2cro4' or ncap == 'ki' or ncap == 'k2hgi4' or ncap == 'nh4cl+nh4oh+(nh4)2co3':
            print("No reaction")
            ans = input("Do you want to test again? (Y or N): ")
        else:
            print("KABAM!")

    elif cation[b] == 'Barium':
        if ncap == 'nh4cl+nh4oh+(nh4)2co3':
            print('White precipitate formed')
            ans = input("Do you want to test again? (Y or N): ")
        elif ncap == 'k2cro4':
            print("Yellow precipitate formed")
            ans = input("Do you want to test again? (Y or N): ")
        elif ncap == 'dilhcl' or ncap == 'ki' or ncap == 'nh4oh+nh4cl' or ncap == 'k2hgi4' or ncap == 'naoh':
            print("No reaction")
            ans = input("Do you want to test again? (Y or N): ")
        else:
            print("KABAM!")
    if chance == 6:
        break
    
    chance += 1

guess = input("What is the salt? (Enter in format- Cation Anion): ")
if guess == cation[b] + ' ' + anion[a]:
    print("Correct")
else:
    print("Incorrect.")
    print("The salt was", cation[b], anion[a])
print()
print("Warning: Some salts may not exist, or may be insoluble.")
print("Taking care of all that is too much work. Please, have some mercy.")
print("Also, I should've typed this before you entered the salt, because you must've been confused and entered an existing salt.")
