import re

def get_process_mem_mapping(file):
    process_mem = {}

    with open(file, 'r') as top_file:
        # skip first 7 rows
        top_output = top_file.read().split("\n")[7:]

        # print(top_output)
        #     processes = ""
        #     for line in top_output:
        #         p = line.split(" ")[-1]
        #         processes += p + " "
        #     print(processes)


        # print(top_output)
        # skip the last empty string (newline character)
        for line in top_output[:-1]:
            # print('1: ', line)
            # remove extra void spaces
            line = re.sub(r'\s+', ' ', line).strip()
            # print('2: ', line)
            fields = line.split(" ")
            # print("Fields: ", fields)
            process = fields[11]
            # 9th column is of memory consumption in %
            memory_usage = float(fields[9])
            # print(memory_usage)
            process_mem[process] = memory_usage
            # print(process_mem)

    return process_mem