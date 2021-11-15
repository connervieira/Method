from bitcoinpython import Key
from os import system, name


# ----- Configuration Start -----

private_key = "" # The BitcoinCash wallet key in hex form.
generate_key = False # Generate a Bitcoin Cash private key, then exit.

# ----- Configuration End -----


# Define the function to clear the screen.
def clear():
    if name == 'posix': # If OS is Linux or Mac, use the correct command for the platform.
        system('clear')
    else: # If OS is Windows, use the correct command for the platform.
        system('cls')


clear() # Clear the screen on first launch


if (generate_key == True):
    k = Key()
    print("Generated private key: " + k.to_hex())
else:
    # Load the private key from the configuration
    k = Key.from_hex(private_key)


    # After intial start-up, ask what mode to boot into.
    print("Please choose an option:")
    print("1. Admin mode")
    print("2. ATM mode")
    selection = input("Selection: ")

    if (selection == "1"): # Boot into admin mode.
        clear()

        # Ask for an option selection.
        print("Please choose an option:")
        print("1. View public address")
        print("2. View ATM balance")
        selection = input("Selection: ")

        if (selection == "1"):
            print(k.address)
        elif (selection == "2"):
            print(k.balance)
        else:
            print("Error: Unknown option")
        
        
    elif (selection == "2"): # Boot into normal ATM mode.
        pass
    else: # An unknown mode was selected.
        print("Error: Unknown mode.")
        print("Exiting")
