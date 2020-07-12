def arithmetic_arranger(problems, *solve):

    if len(problems) > 5:
        return('Error: Too many problems.')
    else:

        first_operand = []
        operator = []
        second_operand = []
        line = []
        result = []

        first_line = ''
        second_line = ''
        third_line = ''
        fourth_line = ''
        seperator = '    '

        for problem in problems:

            problem_parts = problem.split()

            try:
                int(problem_parts[0])
                int(problem_parts[2])

                if len(problem_parts[0]) > 4 or len(problem_parts[2]) > 4:
                    return('Error: Numbers cannot be more than four digits.')
                else:
                    first_operand.append(problem_parts[0])
                    second_operand.append(problem_parts[2])

            except:
                return("Error: Numbers must only contain digits.")

            if (problem_parts[1] == '+') or (problem_parts[1] == '-'):
                operator.append(problem_parts[1])
            else:
                return("Error: Operator must be '+' or '-'.")


        for i in range(len(first_operand)):

            if len(first_operand[i]) - len(second_operand[i]) < 0:
                space = len(second_operand[i]) - len(first_operand[i]) + 2
                mid_space = 1
                line.append('-' * (len(second_operand[i]) + 2))
            else:
                space = 2
                mid_space = len(first_operand[i]) - len(second_operand[i]) + 1
                line.append('-' * (len(first_operand[i]) + 2))

            if operator[i] == '+':
                result.append(str(int(first_operand[i]) + int(second_operand[i])))
            else:
                result.append(str(int(first_operand[i]) - int(second_operand[i])))

            first_operand[i] = (' ' * space) + first_operand[i]
            second_operand[i] = operator[i] + (' ' * mid_space) + second_operand[i]

            space = len(line[i]) - len(result[i])
            result[i] = (' ' * space) + result[i]


        first_line = seperator.join(first_operand)
        second_line = seperator.join(second_operand)
        third_line = seperator.join(line)
        fourth_line = seperator.join(result)


        if solve:
            return(first_line + '\n' + second_line + '\n' + \
                    third_line + '\n' + fourth_line)
        else:
            return(first_line + '\n' + second_line + '\n' + third_line)
