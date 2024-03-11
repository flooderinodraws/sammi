# `Function` definition starts here


def read_file(file):
    
    # Get `directory` data and convert to a correct path
    
    directory = "directory.txt"
    directory = open_file(directory)
    directory = "".join(directory)
    
    # Get `import_file` data
    
    import_file = directory + "\\" + file
    import_file = open_file(import_file)
    
    return import_file


def open_file(file):

    # Assign `content` to store `file`

    with open(file, "r") as file:
        content = file.read()
    
    # Convert `content` from string -> list

    content = content.split("\n")

    return content


def get_data(user, user_list):
    
    # Search all items in `user_list` as `element` 

    for element in user_list:
        
        # If `user` is in element, display it
        
        if user in element:
            user = element
    
    return user




# Assign `user_list` to store list of users

user_list = read_file("user_list.txt")

# Assign `user` to store one user and remove empty newline

user = read_file("search_user.txt")
user = "".join(user)

# Assign `data` to store user data

data = get_data(user, user_list)
print(data)
