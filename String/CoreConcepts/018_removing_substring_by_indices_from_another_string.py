str = "We can watch a movie, or we can go out for dinner"
print(f"Original String = {str}")

remove_index_from = 12
remove_index_to = 21

str_on_removal = str[:12] + str[21:]
print(f"On removing substring from index: {remove_index_from} to index: {remove_index_to}, string = {str_on_removal}")