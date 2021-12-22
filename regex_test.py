import re

sum = 0

hand = open('regex_sum_1400143.txt')
for line in hand:
    line = line.rstrip()
    numbers  = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number) if len(numbers) > 0 else sum    
print(sum)
hand.close()