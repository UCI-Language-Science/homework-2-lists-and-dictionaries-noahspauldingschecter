# Write code that takes the provided list and removes all
# duplicates of numbers that have occurred earlier in the
# list, preserving the order otherwise
# 
# For the example below, the output should be
# "[1, 4, 3, 2, 5, 7, 9]"
# 
def duplicate_remover():
    duplicates_list = [1, 4, 3, 4, 2, 5, 1, 2, 7, 9, 4]
    removed_duplicates_list = []

    for num in duplicates_list:
        if num not in removed_duplicates_list:
            removed_duplicates_list.append(num)
    print(removed_duplicates_list)
        

if __name__ == "__main__":
    duplicate_remover()