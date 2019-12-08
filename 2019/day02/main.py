import json

with open("input", 'r') as f:
    content = f.read()
content_json = "[" + content + "]"
code_raw = json.loads(content_json)

code = code_raw.copy()

code[1] = 12
code[2] = 2

def run_code(code):
    i = 0
    length = len(code)
    while i < length:
        opcode = code[i]
        if opcode == 1:
            operator = lambda x: x[0] + x[1]
        elif opcode == 2:
            operator = lambda x: x[0] * x[1]
        elif opcode == 99:
            break
        else:
            raise ValueError
        idx1 = code[i+1]
        idx2 = code[i+2]
        idx3 = code[i+3]

        code[idx3] = operator([code[idx1], code[idx2]])
        i = i + 4
        pass
    return code
code = run_code(code)
print("Part 1:", code[0])


expected_result = 19690720
for noun in range(0, 100):
    for verb in range(0, noun):
        code = code_raw.copy()
        code[1] = noun
        code[2] = verb
        code = run_code(code)
        if code[0] == expected_result:
            print("part 2:", 100 * code[1] + code[2])
            break
        pass
    pass

