def read_numbers_from_file(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(num) for num in file.read().split(',')]
    return numbers


def calculate_max(numbers):
    return max(numbers)


def calculate_min(numbers):
    return min(numbers)


def calculate_sum(numbers):
    return sum(numbers)


def write_results_to_file(file_name, max_value, min_value, sum_value, numbers):
    with open(file_name, 'w') as file:
        file.write("Integers: [" + ', '.join(str(num) for num in numbers) + "]\n")
        file.write(f"Maximum: {max_value}\n")
        file.write(f"Minimum: {min_value}\n")
        file.write(f"Sum: {sum_value}\n")


def print_results(max_value, min_value, sum_value, numbers):
    print("Integers:", numbers)
    print("Maximum:", max_value)
    print("Minimum:", min_value)
    print("Sum:", sum_value)


def main():
    input_file_name = "data.txt"
    output_file_name = "results.txt"

    numbers = read_numbers_from_file(input_file_name)
    max_value = calculate_max(numbers)
    min_value = calculate_min(numbers)
    sum_value = calculate_sum(numbers)

    write_results_to_file(output_file_name, max_value, min_value, sum_value, numbers)
    print_results(max_value, min_value, sum_value, numbers)


if __name__ == "__main__":
    main()
