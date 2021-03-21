def is_bouncy(n):
    '''This function determines if arbitrary number N is a bouncy number.'''
    n_as_list = [*str(n)]
    sorted_n = sorted(n_as_list)
    return sorted_n != n_as_list and sorted_n[::-1] != n_as_list

number = 1
total_numbers = 0
bouncy_numbers = 0 
while True:
    total_numbers += 1
    if is_bouncy(number):
        bouncy_numbers += 1
    if bouncy_numbers/total_numbers == 0.99:
        print(f"{number} - {bouncy_numbers/total_numbers*100}%")
        break
    number += 1
