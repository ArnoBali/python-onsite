'''
Write a function that takes in a list and finds the max, min, average and sum.

'''

l = [1 , 3, 4, 5, 4, 3, 5]

def min_max_av_sum(numbers):
    sum = 0
    numbers_max = max(numbers)
    numbers_min = min(numbers)
    for num in numbers:
        sum += num

    average = sum / len(numbers)
    return f"Sum = {sum}, Average = {average}, Max = {numbers_max}, Min = {numbers_min}"

print(min_max_av_sum(l))
