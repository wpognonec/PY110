def minilang(actions: str):
    stack = []
    register = 0
    valid_tokens = ["PUSH", "ADD", "SUB", "MULT",
                    "DIV", "REMAINDER", "POP", "PRINT"]
    message = None

    for element in actions.split():
        if element in valid_tokens or element.lstrip("-").isnumeric():
            try:
                match element:
                    case "PUSH":
                        stack.append(register)
                    case "ADD":
                        register += stack.pop()
                    case "SUB":
                        register -= stack.pop()
                    case "MULT":
                        register *= stack.pop()
                    case "DIV":
                        register //= stack.pop()
                    case "REMAINDER":
                        register %= stack.pop()
                    case "POP":
                        register = stack.pop()
                    case "PRINT":
                        print(register)
                    case _:
                        register = int(element)
            except IndexError:
                message = "The stack was empty"
                break
        else:
            message = "Invalid token detected"
    return message

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed because the `program` argument has no `PRINT` commands)
