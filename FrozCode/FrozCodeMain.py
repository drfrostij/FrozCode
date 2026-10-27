
variables = {}

def run_program(code):
    for line_number, line in enumerate(code.splitlines(), start=1):
        line = line.strip()

        if not line:
            continue

        parts = line.split(" ", 2)
        command = parts[0]

        if command == "say":
            text = line[4:].strip()

            if text.startswith('"') and text.endswith('"'):
                text = text[1:-1]

            if text in variables:
                print(variables[text])
            else:
                print(text)

        elif command == "set":
            name = parts[1]
            value = parts[2]

            if value.isdigit():
                value = int(value)
            elif value.startswith('"') and value.endswith('"'):
                value = value[1:-1]

            variables[name] = value

        elif command == "add":
            name = parts[1]
            amount = int(parts[2])
            variables[name] += amount

        else:
            raise SyntaxError(
                f"Unknown command on line {line_number}: {command}"
            )


program = '''
say "Hello from FrostLang!"
set score = 10
add score 5
say score
'''

run_program(program)



# plan: make it basically like python but the coding language will be LMC