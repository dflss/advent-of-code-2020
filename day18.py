def parse_input_file():
    with open("day18_data.txt", "r") as file:
        return file.readlines()


def tokenize(s):
    tokens = []
    buf = []
    for t in s.split():
        if t.startswith('('):
            while t.startswith('('):
                tokens.append('(')
                t = t[1:]
            tokens.append(t)
        elif t.endswith(')'):
            while t.endswith(')'):
                buf.append(')')
                t = t[:-1]
            tokens.append(t)
            tokens.extend(buf)
            buf.clear()
        else:
            tokens.append(t)
    return tokens


def peek(stack):
    return stack[-1] if stack else None


def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    values.append(eval(f"{left}{operator}{right}"))


def greater_equal_precedence(op1, op2, precedences):
    return precedences[op1] >= precedences[op2]

def evaluate_shunting_yard(tokens, precedences):
    output_queue = []
    operator_stack = []
    for token in tokens:
        if token.isdigit():
            output_queue.append(int(token))
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            top = peek(operator_stack)
            while top is not None and top != '(':
                apply_operator(operator_stack, output_queue)
                top = peek(operator_stack)
            operator_stack.pop()  # Discard the '('
        elif token in precedences:
            top = peek(operator_stack)
            while top is not None and top not in "()" and greater_equal_precedence(top, token, precedences):
                apply_operator(operator_stack, output_queue)
                top = peek(operator_stack)
            operator_stack.append(token)
        else:
            raise ValueError(f"Unknown token: {token}")

    if len(list(set(list(precedences.values())))) == 1:
        output_queue.reverse()
        operator_stack.reverse()
    while peek(operator_stack) is not None:
        apply_operator(operator_stack, output_queue)

    return output_queue[0]


def part_1():
    precedences = {'+': 0, '*': 0}
    input = parse_input_file()
    sum = 0
    for expression in input:
        sum += evaluate_shunting_yard(tokenize(expression), precedences)
    print(sum)


def part_2():
    precedences = {'+': 1, '*': 0}
    input = parse_input_file()
    sum = 0
    for expression in input:
        sum += (evaluate_shunting_yard(tokenize(expression), precedences))
    print(sum)


part_1()
part_2()
