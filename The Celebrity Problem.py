def knows(i, j, MATRIX):
    # Returns True if person i knows person j, False otherwise
    return MATRIX[i][j] == 1

def find_celebrity(n, MATRIX):
    # Find the celebrity among n people
    for i in range(n):
        is_celebrity = True
        for j in range(n):
            if i == j:
                continue
            if knows(i, j, MATRIX) or not knows(j, i, MATRIX):
                is_celebrity = False
                break
        if is_celebrity:
            return i
    return -1  # No celebrity found

# Example usage
MATRIX = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]

n = len(MATRIX)  # Number of people
celebrity = find_celebrity(n, MATRIX)

if celebrity == -1:
    print("No celebrity found")
else:
    print("Celebrity is:", celebrity)
