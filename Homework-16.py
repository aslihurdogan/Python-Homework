# Task 1: Merge two lists
def merge_lists(list1, list2):
    return list1 + list2

# Task 2: Check if a number is positive, negative, or zero
def check_number():
    try:
        num = float(input("Enter a number: "))
        if num > 0:
            print("The number is positive.")
        elif num < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid input. Please enter a number.")
# Task 3: Greet the user based on name
def greet_user():
    name = input("Enter your name: ")
    if name == "Alice" or name == "Bob":
        print(f"Hello, {name}!")
    else:
        print("Hello, guest!")
# Run tasks interactively
if __name__ == "__main__":
    print("--- Task 1: Merge Lists Example ---")
    print(merge_lists([1, 2, 3], [4, 5, 6]))
    print("\n--- Task 2: Check Number ---")
    check_number()
    print("\n--- Task 3: Greet User ---")
    greet_user()
