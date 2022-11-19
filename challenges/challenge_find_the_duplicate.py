def check_for_valid_args(args):
    if not isinstance(args, list) or not len(args) > 1:
        return False
    return True


def check_for_valid_items_list(list):
    for item in list:
        if not isinstance(item, int) or not item > 0:
            return False
    
    return True

def find_duplicate(nums):    
    if not check_for_valid_args(nums) or not check_for_valid_items_list(nums):
        return False

    n = len(nums)
 
    nums.sort()

    for index in range(0, n):
        if nums[index - 1] == nums[index]:
            return nums[index]
    
    return False