def find_matching_pair(numbers, target_sum):
    left_pointer = 0
    right_pointer = len(numbers) - 1
    last_pair = None
    
    while left_pointer < right_pointer:
        current_sum = numbers[left_pointer] + numbers[right_pointer]
        if current_sum == target_sum:
            # Update last_pair with the current pair
            last_pair = (numbers[left_pointer], numbers[right_pointer])
            # Move the pointers to find the last pair
            left_pointer += 1
            right_pointer -= 1
        elif current_sum < target_sum:
            left_pointer += 1  # Move the left pointer to the right
        else:
            right_pointer -= 1  # Move the right pointer to the left
            
    return last_pair  # Return the last matching pair found

if __name__ == "__main__":
    numbers = [2, 3, 6, 7]
    target_sum = 9
    result = find_matching_pair(numbers, target_sum)
    if result:
        print("Matching pair:", result)
    else:
        print("No matching pair found.")
