class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        # Split the input string into words
        words = self.input_string.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join the reversed list back into a string
        return ' '.join(reversed_words)

    def display_reversed(self):
        reversed_string = self.reverse_words()
        print(f"Original String: '{self.input_string}'")
        print(f"Reversed String: '{reversed_string}'")

# Example usage
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    reverser = StringReverser(input_string)
    reverser.display_reversed()