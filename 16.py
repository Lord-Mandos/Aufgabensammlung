both_lists = [[1, 2, 3, 3, 3, 3, 4, 4, 9],[2, 3, 9]]

def remove_entries(clear_list, remove_list):
    
    for number in remove_list:
        while True:
            if number in clear_list:
                clear_list.remove(number)
            else:
                break
    return clear_list

finished_list = remove_entries(both_lists[0], both_lists[1])
print(finished_list)