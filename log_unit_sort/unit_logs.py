"""
"log_a.jsonl" и "log_b.jsonl".
log_generator.py <path/to/dir>
timestamp
<your_script>.py <path/to/log1> <path/to/log2> -o <path/to/merged/log>
"""
import json
from datetime import datetime


log_file_a = "log_a.jsonl"
log_file_b = "log_b.jsonl"




def main():
    table_1 = []
    table_2 = []
    a = 0
    with open(log_file_a, 'r') as file:
        for i in range(3):
            line = next(file)
            # print(json.loads(line))
            # print(json.loads(line)['timestamp'])
            table_1.append(datetime.strptime(json.loads(line)['timestamp'], '%Y-%m-%d %H:%M:%S'))

            print(json.loads(line)['timestamp'].split())
    print('__________')

    with open(log_file_b, 'r') as file:
        for i in range(3):
            line = next(file)
            # print(json.loads(line))
            # print(json.loads(line)['timestamp'])
            table_2.append(datetime.strptime(json.loads(line)['timestamp'], '%Y-%m-%d %H:%M:%S'))

            print(json.loads(line)['timestamp'].split())
    print('__________')

    time_test = []
    with open(log_file_a, 'r') as file_1:
        with open(log_file_b, 'r') as file_2:
            line_1 = next(file_1)
            time_1 = datetime.strptime(json.loads(line_1)['timestamp'], '%Y-%m-%d %H:%M:%S')
            line_2 = next(file_2)
            time_2 = datetime.strptime(json.loads(line_2)['timestamp'], '%Y-%m-%d %H:%M:%S')
            i, j = 0, 0
            res = []
            while i < 3 or j < 3:
                if time_1 <= time_2 or time_1 == None:
                    time_test.append(('time_1', time_1))
                    i += 1
                    line_1 = next(file_1)
                    time_1 = datetime.strptime(json.loads(line_1)['timestamp'], '%Y-%m-%d %H:%M:%S')
                else:
                    time_test.append(('time_2', time_2))
                    j += 1
                    line_2 = next(file_2)
                    time_2 = datetime.strptime(json.loads(line_2)['timestamp'], '%Y-%m-%d %H:%M:%S')

            print(*time_test, sep='\n')



        # for line in file:
        #         # print(line)
        #         print(json.loads(line))
        #         a += 1

            # table.append(json.loads(line[7:]))

    # for row in table:
    #     print(row)

if __name__ == '__main__':
    main()



