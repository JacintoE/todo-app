FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    todo items.
    """
    with open(filepath, 'r') as f:
        return f.readlines()


def set_todos(todos_arg, filepath=FILEPATH):
    """Write the todo items List in the text file."""
    with open(filepath, 'w') as f:
        f.writelines(todos_arg)

if __name__ == "__main__":
    print("hello")