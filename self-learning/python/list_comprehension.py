def demonstrate_comprehensions():
    """Shows various practical uses of comprehensions in Python."""
    # 1. Standard List Comprehension
    numbers = range(1, 21)
    evens = [x for x in numbers if x % 2 == 0]
    print(f"Even numbers 1-20: {evens}")
    
    # 2. String Manipulation
    words = ["data", "visualization", "training", "python", "sql"]
    capitalized = [word.capitalize() for word in words]
    print(f"Capitalized words: {capitalized}")
    
    # 3. Dictionary Comprehension
    word_lengths = {word: len(word) for word in words}
    print(f"Word lengths mapping: {word_lengths}")
    
    # 4. Complex List Comprehension (Matrix flattening)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"Flattened matrix: {flattened}")

if __name__ == "__main__":
    demonstrate_comprehensions()
