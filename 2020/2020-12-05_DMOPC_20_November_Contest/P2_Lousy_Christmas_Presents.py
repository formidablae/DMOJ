N_length_of_scarf, M_relatives = map(int, input().split())
colors = list(map(int, input().split()))
max_size = 0
for el in range(M_relatives):
    a_first_color, b_last_color = map(int, input().split())
    start = 0
    end = N_length_of_scarf - 1
    while start < N_length_of_scarf and start + max_size - 1 < N_length_of_scarf and colors[start] != a_first_color:
        start += 1
    while end - start + 1 > max_size and colors[end] != b_last_color:
        end -= 1
    if start != N_length_of_scarf and end >= start:
        max_size = max(max_size, end - start + 1)
print(max_size)
