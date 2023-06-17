def largest_rectangle_area(histogram):
    max_area = 0

    for i in range(len(histogram)):
        min_height = float('inf')
        for j in range(i, len(histogram)):
            min_height = min(min_height, histogram[j])
            width = j - i + 1
            area = min_height * width
            max_area = max(max_area, area)

    return max_area

# Example usage
histogram = [2, 1, 5, 6, 2, 3]
max_area = largest_rectangle_area(histogram)
print("Histogram:", histogram)
print("Largest rectangle area:", max_area)
