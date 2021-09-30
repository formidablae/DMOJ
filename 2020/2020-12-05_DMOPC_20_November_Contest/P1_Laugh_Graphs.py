N = int(input())
pitches = input()
answer = [["." for col in range(N)] for row in range(2 * N + 1)]
ans_str = []
row_now = N
for i in range(N):
    if pitches[i] == 'v':
        row_now += 1
        answer[row_now][i] = "\\"
    elif pitches[i] == '>':
        answer[row_now][i] = "_"
    else:  # pitches[i] == '^'
        answer[row_now][i] = "/"
        row_now -= 1
for row in answer:
    ans_str.append(''.join(map(str, row)))
for st in ans_str:
    if st != "." * N:
        print(st)
