'''
Recap - Frequency Counter:
#Challenge:
Create a function named frequency_counter that takes a list data_list as an argument.
The function should count the frequency of each item in the list and return a dictionary where the keys are the unique items from the list and the values are
the counts of how many times each item appears.

For example, if the input list is [1, 2, 2, 3, 3, 3, 4, 4, 4, 4], the function should return a dictionary like this:
    {1: 1, 2: 2, 3: 3, 4: 4}

'''
def frequency_counter(data_list):
    frequency_dict = {}
    for item in data_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

print(frequency_counter([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))  # Output: {1: 1, 2: 2, 3: 3, 4: 4}

