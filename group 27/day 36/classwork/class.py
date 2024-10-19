def sum_two_smallest_numbers(numbers):
numbers.sort()

return numbers[0] + numbers[1]


def remove_smallest(numbers):
if len(numbers) == 0:
return []




3) def stray(arr):
for num in arr:
if arr.count(num) == 1:
return num

def sort_by_length(arr):
return sorted(arr, key=len)


def is_anagram(test, original):
test_sorted = "".join(sorted(test.lower()))
original_sorted = "".join(sorted(original.lower()))

return test_sorted == original_sorted


def capitals(word):
indexes = []

for index in range(len(word)):
if word[index].isupper():
indexes.append(index)

return indexes


```def solve(s):
    count_u = 0
    count_l = 0
    
    for char in s:
        if char.isupper():
            count_u += 1
        else:
            count_l += 1
    
    if count_u <= count_l:
        return s.lower()
    else:
        return s.upper()```