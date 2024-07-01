from menu import show_menu

if __name__ == '__main__':
    try:
        show_menu()
    except Exception as e:
        print(f'An error has ocurred : {e}')