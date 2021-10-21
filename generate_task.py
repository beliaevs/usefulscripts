import random

def generate_task():
    operations = ['+', '-']
    MaxResult = 100
    a = random.randrange(1, 99)
    sign = random.choice(operations)
    if sign == '-':
        b = random.randrange(0, a)
    else:
        b = random.randrange(0, MaxResult - a)
    return (a, sign, b)

def task2equation(task):
    return str(task[0]) + str(task[1]) + str(task[2]) + '&='

def main():
    columns = 4
    rows = 17
    myseed = 'gsfahegdgsgf'
    random.seed(myseed)

    headers = [r'\documentclass[12pt, a4paper]{article}', r'\usepackage{amsmath}',  r'\pagestyle{empty}', r'\begin{document}', r'\begin{align*}']
    footers = [r'\end{align*}', r'\end{document}']

    equations = []
    for i in range(rows):
        equation_row = ' & '.join([task2equation(generate_task()) for j in range(columns)])
        equations.append(equation_row)

    equations_string = '\\\\\n'.join(equations)
    print('\n'.join(headers) + '\n' + equations_string + '\n' + '\n'.join(footers))

if __name__=='__main__':
    main()