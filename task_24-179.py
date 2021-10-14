file = open('24-179.txt', 'r', encoding='utf8')
line = file.read().replace('\n', '')
arr = ['CBCBC', 'CBDBC', 'CBEBC']

# line = 'CBCBCBCBCBCBC'

result = []
for i in range(len(arr)):
    word = arr[i]
    count = 0
    for j in range(len(line)):
        if line[j] == 'C' and line[j:j + 5] == word:
            count += 1
    result.append(count)

print(arr[result.index(max(result))][2], sum(result))
