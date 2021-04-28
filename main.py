import re


def main():
    counter_of_problems = 0
    file = open("/home/myr/Python/lab5/access_log_Jul95", encoding = "ISO-8859-1")

    for line in file:
        if re.search(r"01/Jul/1995:0[1-5]:[0-5][0-9]:\d\d", line) or re.search(r"01/Jul/1995:00:2[1-9]:\d\d",line) or re.search(r"01/Jul/1995:00:[3-5][0-9]:\d\d",line) or re.search(r"01/Jul/1995:06:[0-4][0-9]:\d\d",line) or re.search(r"01/Jul/1995:06:5[0-2]:\d\d",line) is not None:
        
            if re.search(r"POST", line) and re.search(r" 40[0-4] ", line) is not None:
                counter_of_problems = counter_of_problems + 1

            if re.search(r"PUT", line) and re.search(r" 40[0-4] ", line)  is not None:
                counter_of_problems = counter_of_problems + 1

            if re.search(r"DELETE", line) and re.search(r" 40[0-4] ", line) is not None:
                counter_of_problems = counter_of_problems +1
            
    print(f"Number of appeared problems :",counter_of_problems)


if __name__ == '__main__':
    main()