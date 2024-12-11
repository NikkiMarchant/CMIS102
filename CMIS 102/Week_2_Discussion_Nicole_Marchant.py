# adds 26 to two user inputs 

def main():
    constant = 26
    number = eval(input('Pick a number 1-100: '))
    number2 = eval(input('Pick a second number 1-100: '))
    result = constant+number+number2
    return result

numReturn = main()
print(numReturn)