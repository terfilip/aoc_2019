import pyperclip
from op_code_thing import OpCodeThing

with open('2.txt', 'r') as f:
    octh = OpCodeThing(f.read())

octh.codes[1] = 12
octh.codes[2] = 2

octh.run()

print(f'2.1 {octh.codes[0]}')
pyperclip.copy(octh.codes[0])

octh.reset()

tgt = 19690720

for noun in range(100):

    for verb in range(100):
        octh.codes[1] = noun
        octh.codes[2] = verb
        octh.run()
        res = octh.codes[0]
        octh.reset()

        if res == tgt:
            ans = 100 * noun + verb
            print(noun)
            print(verb)
            print(f'ans: {ans}')
            pyperclip.copy(ans)
            break
