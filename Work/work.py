import time
import sys

# Purpose: Determines how many lines of code will be written
#          before the coder crashes to sleep.
# Input: lines_before_coffee - how many lines of code to write before coffee
#        prod_loss - factor for loss of productivity after coffee
# Output: returns the number of lines of code that will be written
#         before the coder falls asleep
def sum_series(lines_before_coffee, prod_loss):
    "sum series"
    ##### ADD CODE HERE #####
    loss_num=prod_loss
    new_lines = lines_before_coffee//prod_loss
    written_lines = lines_before_coffee
    while new_lines > 0:
        written_lines += new_lines
        loss_num *= prod_loss
        new_lines = lines_before_coffee//loss_num
    return written_lines
# Purpose: Uses a linear search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee and
#         the number of calls to sum_series as a tuple
def linear_search(total_lines, prod_loss):
    ##### ADD CODE HERE #####
    list_line=[i for i in range (1,total_lines+1)]
    sum_series_call=0
    for i in range (len(list_line)):
        if sum_series(list_line[i],prod_loss) == total_lines:
            sum_series_call += 1
            return list_line[i], sum_series_call
        sum_series_call+=1
        if sum_series(list_line[i],prod_loss) > total_lines:
            smallest_above_target = i+1
            return smallest_above_target, sum_series_call
# Purpose: Uses a binary search to find the initial lines of code to
#          write before the first cup of coffee, so that the coder
#          will complete the total lines of code before sleeping AND
#          get to have coffee as soon as possible.
# Input: total_lines - lines of code that need to be written
#        prod_loss - factor for loss of productivity after each coffee
# Output: returns the initial lines of code to write before coffee and
#         the number of calls to sum_series as a tuple
def binary_search(total_lines, prod_loss):
    "binary search"
    ##### ADD CODE HERE #####
    # TODO: Replace this return statement with your own
    initial_lines_list = [i for i in range (1,total_lines+1)]
    sum_series_call=0
    left=0
    right = len(initial_lines_list) - 1
    if len(initial_lines_list) == 1 and initial_lines_list[0]<total_lines:
        return 0, sum_series_call
    while left<=right:
        mid = (left +right)//2
        if sum_series(initial_lines_list[mid],prod_loss)==total_lines:
            sum_series_call+=1
            return initial_lines_list[mid], sum_series_call
        if sum_series(initial_lines_list[mid],prod_loss) < total_lines:
            sum_series_call+=1
            left = mid + 1
        else:
            smallest_above_target= initial_lines_list[mid]
            sum_series_call+=1
            right = mid -1 
    return smallest_above_target, sum_series_call
def main():
    "main"
    # TODO: read number of cases, and store it in num_cases
    list_case = [line.strip() for line in sys.stdin]
    num_cases = int(list_case[0])
    # TODO: Iterate for the number of test cases
    for i in range(num_cases):
        # read one line for one case
        # TODO: Replace this line with reading next line from stdin (input redirection or terminal)
        line = list_case[i+1]
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print(f"Elapsed Time: {binary_time:0.8f} seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print(f"Elapsed Time: {linear_time:0.8f} seconds")
        print()

        # Comparison
        comparison = linear_time / binary_time if binary_time else 1
        print(f"Binary Search was {comparison:0.1f}",
              "times faster.")
        print()
        print()


if __name__ == "__main__":
    main()
