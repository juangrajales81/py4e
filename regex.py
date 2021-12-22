###     ^           Matches the begining of a line
###     $           Matches the end of a line
###     .           Matches any character
###     \s          Matches whitespace
###     \S          Matches any non-whitespace character
###     *           Repeats a character zero or more times
###     *?          Repeats a character zero or more times (non-greedy)
###     +           Repeats a character one or more times
###     +?          Repeats a character one or more times (non-greedy)
###     [aeiou]     Matches a single character in the listed set
###     [^XYZ]      Matches a single character NOT in the listed set
###     [a-z0-9]    The set of characters can include a range
###     (           Indicates where the string extraction is to start
###     )           Indicates where the string extraction is to end

import re


### Using re.search like find()

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From', line):
        print(line)
hand.close()


### re.findall()

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x) ### [0-9]+ one o more digits
print(y)

y = re.findall('[AEIOU]+', x)
print(y) ### returns an empty list


hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    y  = re.findall('\S+@\S+', line)
    print(y)
hand.close()

z = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
ext = re.findall('\S+?@\S+', z)
print(ext)


