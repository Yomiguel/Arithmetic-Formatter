from ast import operator
import re

def arithmetic_arranger(operations, solve):
    format = ''
    firstLine = []
    secondLine = []
    lines = ''
    top = '      '
    bottom = '      '
    if(5 < len(operations)):
        return 'Error: Too many problems.'
    for operation in operations:
        terms = re.split(r'\D+', operation)
        firstNumber = terms[0]
        secondNumber = terms[1]
        if '+' in operation or '-' in operation:
            if(re.search(r'\D',firstNumber) or re.search(r'\D',secondNumber)):
                return 'Error: Numbers must only contain digits.'
            else:
                if(len(firstNumber) <= 4 and len(secondNumber) <= 4):
                    firstLine.append(firstNumber)
                    firstLine.append(top)
                    if('+' in operation):
                        secondLine.append('+ ')
                        secondLine.append(secondNumber)
                        secondLine.append(bottom)
                    else:
                        secondLine.append('- ')
                        secondLine.append(secondNumber)
                        secondLine.append(bottom)
                else:
                    return 'Numbers cannot be more than four digits.'
        else:
            return 'Error: Operator must be "+" or "-".'
    format = ''.join(firstLine) + '\n' + ''.join(secondLine)
    return (format)

print(arithmetic_arranger(["32 + 698", "3801 - 2", "4511 - 43", "123 + 49", "489 - 15"], True))

