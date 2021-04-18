import re


def main():
    time_in_timeframes = False
    counter_of_problems = 0
    file = open("/home/myr/Python/lab5/access_log_Jul95")

    for line in file:
        if re.search(r"01/Jul/1995:00:21:\d\d", line) is not None:
            time_in_timeframes = False
            break
        if re.search(r"01/Jul/1995:06:52:\d\d", line) is not None:
            time_in_timeframes = True
        
        if time_in_timeframes and re.search(r"POST", line) and re.search(r" 40[0-4] ", line) is not None:
            counter_of_problems = counter_of_problems + 1
        
        if time_in_timeframes and re.search(r"PUT", line) and re.search(r" 40[0-4] ", line)  is not None:
            counter_of_problems = counter_of_problems + 1
        
        
        if time_in_timeframes and re.search(r"DELETE", line) and re.search(r" 40[0-4] ", line) is not None:
            counter_of_problems = counter_of_problems + 1

    print(f"Number of appeared problems :",counter_of_problems)


if __name__ == '__main__':
    main()