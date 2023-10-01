#wap  a program using other files to check which type of no is it
import ArmstrongNo
import PerfectNo
import PerfectSquare
import PerfectCube
import PetersonNo
import prime
import Pallindrome


no=int(input("Enter the no to check the type : "))
l=[]
if (ArmstrongNo.isArmstrong(no)):
    l.append("Armstrong")
resultPerfect=PerfectNo.isPerfect(no)
if(no==resultPerfect):
    l.append("PerfectNo")
resultSqaure=PerfectSquare.squareRoot(no)
if(resultSqaure%1==0):
    l.append("PerfectSquare")
resultCube=PerfectCube.cubeRoot(no)
if(resultCube%1==0):
    l.append("PerfectCube")
resultPerterson=PetersonNo.isPeterson(no)
if(no==resultPerterson):
    l.append("PetersonNo")
if(prime.isprime(no)):
    l.append("Prime")
resultPallindrome=Pallindrome.isPallindrome(no)
if (resultPallindrome==no):
    l.append("Pallindrome")
if len(l)==0:
    print("The Type not identified : ")
else :
    print(f"{no} is a ",end="")
    for i in l:
        print(f"{i}",end="  ")
