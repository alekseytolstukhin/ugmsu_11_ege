file = open('24-178.txt', 'r', encoding='utf8')
line = file.read().replace('\n', '')
size = len(line)
max_count = 0
temp_count = 1
round = 0
i = 0
while round < 2:
    i = i % size
    j = (i + 1) % size
    if line[i] <= line[j]:
        temp_count += 1
    else:
        if temp_count > max_count:
            max_count = temp_count
        temp_count = 1
    i += 1
    if i == size - 1:
        round += 1
print(max_count)
