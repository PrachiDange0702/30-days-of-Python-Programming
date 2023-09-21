def is_string_in_file(file_path, search_string):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if search_string in line:
                    return True
        return False
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


file_path = 'example.txt'  
search_string = 'computer'  

if is_string_in_file(file_path, search_string):
    print(f"The string '{search_string}' was found in the file.")
else:
    print(f"The string '{search_string}' was not found in the file.")
