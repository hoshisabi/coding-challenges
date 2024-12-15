def area(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0

# if a triangle contains the origin, then it should be the same
# area as the three triangles of each replaced by the origin
def contains_origin(x1, y1, x2, y2, x3, y3):
    total_area = area(x1, y1, x2, y2, x3, y3)
    area1 = area(0, 0, x2, y2, x3, y3)
    area2 = area(x1, y1, 0, 0, x3, y3)
    area3 = area(x1, y1, x2, y2, 0, 0)
    return total_area == (area1 + area2 + area3)

def count_triangles_with_origin(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            x1, y1, x2, y2, x3, y3 = map(int, line.strip().split(','))
            if contains_origin(x1, y1, x2, y2, x3, y3):
                count += 1
    return count

filename = "PE102_input.txt"
print(f"Number of triangles containing the origin: {count_triangles_with_origin(filename)}")
