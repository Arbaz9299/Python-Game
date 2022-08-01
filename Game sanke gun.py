import random

def gam (comp,you):

    if comp == you:
        return None

    elif comp == 's' and you== 'p':
        return False

    elif comp == 'p' and you== 'r':
        return False

    elif comp == 'r' and you== 's':
        return False
    else:
        return True

        
print("Computer turn: Roke = r , Paper = p , Scissor = s")

randno=random.randrange(1,3)
if randno ==1:
    comp= 'r'
if randno== 2:
    comp='p'
if randno == 3:
    comp='s'

you=input("Your turn :Roke = r , Paper = p , Scissor = s \n")


print("you select is ", you)
print ("computer select is " , comp )

temp=gam(comp,you)

if temp == None:
    print("Match tei")
elif temp == False:
    print("u lose")
else:
    print("you win ")

