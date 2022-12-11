try:
    import tabulate
except ImportError as err:
    import os
    os.system('cmd /c "pip install tabulate"')
def showcalc():
    global contents
    contents=[["CE","C","Exit"],
              ["sqr(x)","sqrt(x)","%"],
              ["/","*","-"],
              ["1/x","+","="]]
    calc=tabulate.tabulate(contents,tablefmt="rounded_grid")
    print(calc)
    calcin()
def calcin():
    print("Enter your desired numerical inputs and operations one by one")
    print("For square, square root use 'sqr', 'sqrt' respectively")
    eq=[]
    while True:
        choice=input()
        if choice.lower()=="exit":
            break
        elif choice.lower()=="ce":
            print("Current Input Cleared")
            eq.pop()
        elif choice.lower()=="c":
            eq.clear()
            print("All inputs Cleared")
        elif choice.lower()=="=":
            calc(eq)
            break
        else:
            eq.append(choice.lower())
        
def calc(eq):
    length=len(eq)
    result=float(eq[0])
    for i in range(length):
        if eq[i] == "+":
            if eq[i+2] == "%":
                result=result+(result*(float(eq[i+1])/100))
            else:
                result+=float(eq[i+1])
        elif eq[i] == "-":
            if eq[i+2] == "%":
                result=result-(result*(float(eq[i+1])/100))
            else:
                result-=float(eq[i+1])
        elif eq[i] == "*":
            if eq[i+2] == "%":
                result=result*(result*(float(eq[i+1])/100))
            else:
                result*=float(eq[i+1])
        elif eq[i] == "/":
            if eq[i+2] == "%":
                result=result/(result*(float(eq[i+1])/100))
            else:
                result/=float(eq[i+1])
        elif eq[i] == "sqr":
            result**=2
        elif eq[i] == "sqrt":
            result**=(1/2)
        elif eq[i] == "1/x":
            result=1/result
    print(result)
showcalc()