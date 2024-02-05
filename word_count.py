"""Program that count the number of distinct words from an
input file
"""
import sys
import time

def word_count(file_path):
    """Function that count the number of distinct words from an
    input file
    """
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file:
            words = file.read().split()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    #except Exception as e:
    #    print(f"Error: {e}")
    #    return None

    word_freq = {}

    for word in words:
        word = word.lower()  # Convert to lowercase to ensure case-insensitive counting
        word_freq[word] = word_freq.get(word, 0) + 1

    distinct_words = list(word_freq.keys())
    distinct_words.sort()

    return distinct_words, word_freq

def main():
    """Contain the logic to execute the program"""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()
    results = word_count(file_path)
    end_time = time.time()

    if results is not None:
        distinct_words, word_freq = results

        print("Distinct Words and Frequencies:")
        for word in distinct_words:
            print(f"{word}: {word_freq[word]}")

        elapsed_time = end_time - start_time
        print(f"\nExecution time: {elapsed_time:.4f} seconds")

        # Save results to a file
        with open("WordCountResults.txt", 'w', encoding = 'utf-8') as result_file:
            result_file.write("Distinct Words and Frequencies:\n")
            for word in distinct_words:
                result_file.write(f"{word}: {word_freq[word]}\n")
            result_file.write(f"\nExecution time: {elapsed_time:.4f} seconds\n")

if __name__ == "__main__":
    main()
