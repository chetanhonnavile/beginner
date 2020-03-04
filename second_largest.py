def second_largest(given_list):

    largest = None
    second_largest = None

    for current_number in given_list:
        if largest == None:
            largest = current_number
        elif current_number > largest:
            second_largest = largest
            largest = current_number

        elif second_largest == None:
            second_largest = current_number
        elif current_number > second_largest:
            second_largest = current_number
    return second_largest

print(second_largest([99,1,56,87,102]))
