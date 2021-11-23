"""
"log_a.jsonl" и "log_b.jsonl".
timestamp
<your_script>.py <path/to/log1> <path/to/log2> -o <path/to/merged/log>
"""


import json
from datetime import datetime


def main():
    # table = []
    a = 0
    with open('log_a.jsonl', 'r') as file:
        for i in range(3):
            line = next(file)
            print(json.loads(line)['timestamp'])

            print(json.loads(line)['timestamp'].split())

            print('__________')


        # for line in file:
        #         # print(line)
        #         print(json.loads(line))
        #         a += 1

            # table.append(json.loads(line[7:]))

    # for row in table:
    #     print(row)

if __name__ == '__main__':
    main()



