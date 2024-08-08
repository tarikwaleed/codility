def DecimalToBinary(num):
    return DecimalToBinary(num // 2) + str(num % 2) if num > 1 else str(num % 2)

# # Example usage:
binary_representation = DecimalToBinary(2)
print(binary_representation)  # Output: 1010
