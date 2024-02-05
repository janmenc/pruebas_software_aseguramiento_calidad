"""Program than read a file input, execute all
descriptive statistics and write the results
"""
import sys
import time

def calculate_mean(data):
    """Calculate the mean with basic
    algorithm    
    """
    return sum(data) / len(data) if len(data) > 0 else None

def calculate_median(data):
    """Calculate the median with basic
    algorithm    
    """
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 0:
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]
        return (middle1 + middle2) / 2
    return sorted_data[n // 2]

def calculate_mode(data):
    """Calculate mode with basic
    algorithm    
    """
    if not data:
        return None

    count_dict = {}
    for num in data:
        count_dict[num] = count_dict.get(num, 0) + 1

    mode = max(count_dict, key=count_dict.get)
    return mode

def calculate_variance(data, mean):
    """Calculate the variance with basic
    algorithm    
    """
    n = len(data) - 1
    return sum((x - mean) ** 2 for x in data) / n if n > 1 else None

def calculate_standard_deviation(data, mean):
    """Calculate the standard deviation with basic
    algorithm    
    """
    n = len(data)
    return (sum((x - mean) ** 2 for x in data) / n) ** (1/2) if n > 1 else None

def compute_statistics(file_path):
    """Read input file, calculate statistics
    and write file with results
    """
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:
            data = [float(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except ValueError:
        print(f"Error: Invalid data in '{file_path}'. Please ensure all items are numbers.")
        return None

    mean_value = calculate_mean(data)
    median_value = calculate_median(data)
    mode_value = calculate_mode(data)
    variance_value = calculate_variance(data, mean_value)
    stdev_value = calculate_standard_deviation(data, mean_value)

    return mean_value, median_value, mode_value, stdev_value, variance_value

def main():
    """
    Contain the logic of the program 
    """
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()
    result = compute_statistics(file_path)
    end_time = time.time()

    if result is not None:
        mean, median, mode, stdev, variance = result
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Mode: {mode}")
        print(f"Standard Deviation: {stdev}")
        print(f"Variance: {variance}")

        elapsed_time = end_time - start_time
        print(f"\nExecution time: {elapsed_time:.4f} seconds")

        # Save results to a file
        with open("StatisticsResults.txt", 'w', encoding = 'utf-8') as result_file:
            result_file.write(f"Mean: {mean}\n")
            result_file.write(f"Median: {median}\n")
            result_file.write(f"Mode: {mode}\n")
            result_file.write(f"Standard Deviation: {stdev}\n")
            result_file.write(f"Variance: {variance}\n")
            result_file.write(f"\nExecution time: {elapsed_time:.4f} seconds\n")

if __name__ == "__main__":
    main()
