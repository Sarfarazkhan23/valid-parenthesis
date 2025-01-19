def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

def main():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter the target sum: "))
    print(twoSum(nums, target))

if name == "__main__":
    main()