# Возвращает False, если не уникально и True, если уникально
def unique_string_in_file(string, file_name):
    file = open(file_name, "r")
    for file_string in file:
        if string == file_string[:len(file_string)-1]:
            return False
    return True