
# Metodo para agregar un elemento a la lista, usando .append()
def add_element(list):
    new_element = input("Enter the new element: ")
    list.append(new_element)
    return "Element added!"


def modify_element(list):
    index = int(input(f"Enter the index of the element to modify: {list}"))
    if index < 0 or index >= len(list):
        print("Invalid index. Please enter a valid index.")
        return
    new_value = input("Enter the new value for the element: ")
    list[index] = new_value
    return "Element modified!"


def delete_element(list):
    index = int(input("Enter the index of the element to delete: "))
    deleted_element = list.pop(index)
    return f"Element deleted: {deleted_element}"


def show_menu():
    print("1. Add a value to the list")
    print("2. Modify a value in the list")
    print("3. Delete a value from the list")
    menu_option = int(input("Select a menu option: "))
    return menu_option
