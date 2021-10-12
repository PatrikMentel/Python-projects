
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
def get_y(m, b, x):
  y = m*x + b
  return y
def calculate_error(m, b, point):
    x_point, y_point = point
    line = get_y(m, b, x_point)
    distance = line - y_point
    return abs(distance)
def calculate_all_error(m, b, points):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error

possible_ms = [round(i*0.1, 2) for i in range(-100, 101)]
possible_bs = [round(i*0.1, 2) for i in range(-200, 201)]

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = (float("inf"))
best_m = 0
best_b = 0
for m in possible_ms:
    for b in possible_bs:
        this_error = calculate_all_error(m, b, datapoints)
        if this_error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = this_error
print(best_m)
print(best_b)
print(smallest_error)