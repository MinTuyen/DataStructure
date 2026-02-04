
# Input: tuples_list is an unsorted list of interval tuples
# Output: A sorted and merged list of interval tuples, where
#         no interval in the merged list has any overlap.
def merge_tuples(tuples_list):
    "merge tuples"
    list_merge=[]
    for i in range(len(tuples_list)-1):
        smallest_num=i
        for j in range(i+1,len(tuples_list)):
            if tuples_list[j][0]<tuples_list[smallest_num][0]:
                smallest_num=j
        swap=tuples_list[i]
        tuples_list[i]=tuples_list[smallest_num]
        tuples_list[smallest_num]=swap
    list_merge = [tuples_list[0]]
    for start, end in tuples_list[1:]:
        last_start, last_end = list_merge[-1]
        if start <= last_end:
            list_merge[-1] = (last_start, max(last_end, end))
        else:
            list_merge.append((start, end))
    return list_merge
# Input: tuples_list is a list of tuples of denoting intervals
# Output: A list of tuples sorted by ascending order of the size
#         of the interval. If two intervals have the size then it breaks
#         ties putting the interval with the lower starting number first
def sort_by_interval_size (tuples_list):
    "sort by interval size"
    for i in range(len(tuples_list)-1):
        smallest_range_index= i
        for j in range(i+1,len(tuples_list)):
            smallest_range=abs(tuples_list[smallest_range_index][1]\
                               -tuples_list[smallest_range_index][0])
            current_range=abs(tuples_list[j][1]-tuples_list[j][0])
            if  current_range<smallest_range:
                smallest_range_index=j
        swap=tuples_list[i]
        tuples_list[i]=tuples_list[smallest_range_index]
        tuples_list[smallest_range_index]=swap
    return tuples_list


def main():
    """
    Uses input redirection to read the data and create a list of tuples
    """
    num_cases = int(input())

    tuples_list = []
    for i in range(num_cases):
        line = input()
        start, end = line.split()
        tuples_list.insert(i, (int(start), int(end)))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
