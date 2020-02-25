import re

run = True

while(run):
    equation = input('Please, enter equation: ')
    if(equation == 'quit'):
        print('Good bye:)')
        run = False
    else:
        equation = re.sub("[a-zA-Z#,.?!@~$\{\}<>:~'\"]",'',equation)
        answer = eval(equation)
        print(answer)
