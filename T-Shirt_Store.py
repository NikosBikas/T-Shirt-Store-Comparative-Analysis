# Import the modules needed to run the script.
import sys, time
from Lib.context import Call, User_Input, print_banner, clear

# Main definition - constants
menu_actions  = {}
tshirt_list = []
dummy_tshirt_list = []

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    clear()
    print_banner()
    print ("Main Menu:")
    print ("")
    print ("1 Add a T-shirt to the Cart  ")
    print ("2 View Items in the Cart  ")
    print ("3 Check Out ")
    print ("4 Comparative analysis")   
    print ("0 Quit")
    print ("")
    choice = input("Enter your choice: ")
    exec_menu(choice)
    return

# Execute menu
def exec_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print_banner()
            print ("Invalid selection, please try again.\n")
            time.sleep(2)
            menu_actions['main_menu']()
    return

# Menu Item Add New Product!
def shirtToCart():
    clear()
    print_banner("- Here you can add one or more T-shirts to the shopping Cart -")
    User_Input.tshirt_buy(tshirt_list)
    input("")
    return main_menu()

def viewCart():
    clear()
    print_banner("- Here you can view all the items that were added to the shopping Cart -")
    Call.ViewCart(tshirt_list)
    return main_menu()

def transaction():
    clear()
    print_banner("- Transaction using the Strategy models! -")
    Call.Transaction(tshirt_list)
    return main_menu()

def assignment():
    clear()
    print_banner("- Comparative analysis -")
    Call.createDummyData()
    return main_menu()


#Comparative analysis 4 SubMenu
def comparative_analysis_menu():
    clear()
    print_banner()
    print ("Comparative analysis Sub-Menu:")
    print ("")
    print ("1 Create Dummy Data ")
    print ("2 View list of 40 items before sorting ")
    print ("3 Use Bubble-Sort Method")
    print ("4 Use Bucket-Sort Method") 
    print ("5 Use Quick-Sort Method") 
    print ("9 Return at main menu")  
    print ("0 Quit")
    print ("")
    choice = input("Enter your choice: ")
    exec_sub_menu(choice)
    return
#
#
# Execute Sub-Menu
def exec_sub_menu(choice):
    clear()
    ch = choice.lower()
    if ch == '':
        comparative_analysis_menu_actions['comparative_analysis_menu']()
    else:
        try:
            comparative_analysis_menu_actions[ch]()
        except KeyError:
            print_banner()
            print ("Invalid selection, please try again.\n")
            time.sleep(2)
            comparative_analysis_menu_actions['comparative_analysis_menu']()
    return

def createDummy():
    clear()
    print_banner()
    Call.createDummyData(dummy_tshirt_list)
    input("Press Enter to return at the Assignment Menu!...")
    return comparative_analysis_menu()

def viewDummyBeforeShort():
    clear()
    print_banner()
    Call.listBeforeSort(dummy_tshirt_list)
    input("\nPress Enter to return at the Assignment Menu!...")
    return comparative_analysis_menu()

def method_bubble_sort():
    clear()
    print_banner()
    Call.bubble_sort(dummy_tshirt_list)
    input("Press Enter to return at the Assignment Menu!...")
    return comparative_analysis_menu()

def method_bucket_sort():
    clear()
    print_banner()
    Call.bucket_sort(dummy_tshirt_list)
    input("Press Enter to return at the Assignment Menu!...")
    return comparative_analysis_menu()

def method_quick_sort():
    clear()
    print_banner()
    Call.quick_sort(dummy_tshirt_list)
    input("Press Enter to return at the Assignment Menu!...")
    return comparative_analysis_menu()
#
#
# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    print('buy')
    time.sleep(1)
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definitions
menu_actions = {
    'main_menu': main_menu,
    '1': shirtToCart,
    '2': viewCart,
    '3': transaction,
    '4': comparative_analysis_menu,  
    '9': back,
    '0': exit,
}

comparative_analysis_menu_actions = {
    'comparative_analysis_menu' : comparative_analysis_menu,
    '1': createDummy,
    '2': viewDummyBeforeShort,
    '3': method_bubble_sort,
    '4': method_bucket_sort,
    '5': method_quick_sort,
    '9': back,
    '0': exit,
}






# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
