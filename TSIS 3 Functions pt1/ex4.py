def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

if __name__ == "__main__":
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    prime_numbers = filter_prime(numbers)
    print("Prime numbers in the list:", prime_numbers)
