# The postcondition verifies that return_value is a string containing only the words from the original sentence whose lengths are prime numbers, maintaining their original order and separated by a single space.
assert return_value == " ".join(filter(lambda word: len(word) > 1 and all(len(word) % x != 0 for x in range(2, int(len(word) ** 0.5) + 1)), sentence.split(" ")))


