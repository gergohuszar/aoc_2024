




def list_check(report):
    """
    Check if the report is safe according to the rules:
    - All levels are either increasing or decreasing.
    - Any two adjacent levels differ by at least 1 and at most 3.
    """
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    increasing = all(1 <= diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff <= -1 for diff in differences)
    return increasing or decreasing


def list_remove_every_index(a):
    for i in range(len(a)):
        nums_copy = a.copy()
        nums_copy.pop(i)
        if list_check(nums_copy):
            return True
    return False




count = 0
with open("input.txt") as f:
    lines = f.readlines()
    lines = [x.strip().split(" ") for x in lines]
    for line in lines:
        nums = [int(i) for i in line]
        
        if list_check(nums):
            
            count += 1
        else:
            if list_remove_every_index(nums):
                
                count += 1


print(count)