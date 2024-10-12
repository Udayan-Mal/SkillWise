
def print_even_numbers(start, end):
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    return even_numbers

try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    if start > end:
        print("Start of the range should be less than or equal to the end.")
    else:
        even_numbers = print_even_numbers(start, end)
        print("Even numbers in the range:", even_numbers)

except ValueError:
    print("Please enter valid integers.")
