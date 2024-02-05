"""Program that convert numbers to binary and hexadecimal base from an
input file
"""
import sys
import time

def convert_numbers(file_path):
    """Function that read an input file and the numbers there and
    convert them in binary and hexadecimal base
    """
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:
            data = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except ValueError:
        print(f"Error: Invalid data in '{file_path}'. Please ensure all items are numbers.")
        return None

    binary_results = []
    hex_results = []

    for item in data:
        try:
            num = int(item)
            binary_results.append(bin(num)[2:])
            hex_results.append(hex(num)[2:])
        except ValueError:
            print(f"Error: Invalid number '{item}' in '{file_path}'. Skipping.")

    return binary_results, hex_results

def main():
    """Contain the logic of the program"""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()
    results = convert_numbers(file_path)
    end_time = time.time()

    if results is not None:
        binary_results, hex_results = results

        print("Binary Results:")
        for binary_num in binary_results:
            print(binary_num)

        print("\nHexadecimal Results:")
        for hex_num in hex_results:
            print(hex_num)

        elapsed_time = end_time - start_time
        print(f"\nExecution time: {elapsed_time:.4f} seconds")

        # Save results to a file
        with open("ConvertionResults.txt", 'w', encoding = 'utf-8') as result_file:
            result_file.write("Binary Results:\n")
            result_file.write('\n'.join(binary_results) + '\n\n')
            result_file.write("Hexadecimal Results:\n")
            result_file.write('\n'.join(hex_results) + '\n\n')
            result_file.write(f"Execution time: {elapsed_time:.4f} seconds\n")

if __name__ == "__main__":
    main()
