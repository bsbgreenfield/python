def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    if 7 in nums:
        print("theres a 7 in there")
        return True
    else:
        print("no seven")
        return False


print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

