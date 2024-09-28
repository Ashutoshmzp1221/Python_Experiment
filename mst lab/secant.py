def count_unique_labels(A: str, B: str) -> int:
    # Convert both strings into sets to get unique characters from each
    set_A = set(A)
    set_B = set(B)
    
    # Find the union of both sets, which will give us unique characters in both A and B
    unique_labels = set_A.union(set_B)
    
    # Return the size of the union
    return len(unique_labels)

# Example usage
input1 = "hea"
input2 = "oed"
output = count_unique_labels(input1, input2)
print(output)  # Output: 5
 