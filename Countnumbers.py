# CountNumbers.py

def count_numbers(numbers):
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    return positive_count, negative_count, zero_count

# Get input from programmer
input_str = input("Enter numbers separated by space: ")
number_list = list(map(int, input_str.split()))

# Count numbers
pos, neg, zero = count_numbers(number_list)

# Output the result
print("Positive numbers:", pos)
print("Negative numbers:", neg)
print("Zeros:", zero)
