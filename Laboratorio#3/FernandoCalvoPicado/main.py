from methods import *


def main():
    my_list = []
    while True:
        option = show_menu()
        if option == 1:
            add_element(my_list)
        elif option == 2:
            modify_element(my_list)
        elif option == 3:
            delete_element(my_list)
        else:
            print("Invalid option, try again!!")


if __name__ == '__main__':
    main()
