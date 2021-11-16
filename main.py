from bitcoinpython import Key
from os import system, name
from bitcoinpython.network import satoshi_to_currency
import pyqrcode


# ----- Configuration Start -----

private_key = "" # The BitcoinCash wallet key in hex form.

# ----- Configuration End -----


# Method is built on BitcoinPython which has documentation at: https://bitcoinpython.mercier.link


# Define the function to clear the screen.
def clear():
    if name == 'posix': # If OS is Linux or Mac, use the correct command for the platform.
        system('clear')
    else: # If OS is Windows, use the correct command for the platform.
        system('cls')


clear() # Clear the screen on first launch


# Load the private key from the configuration
if (private_key == ""):
    # If no private key has been set, generate one automatically.
    k = Key()
    print("Warning: No private key has been set. A temporary one has been generated, but this will change on next launch. Before funding the ATM, configure a static private key.")
    input("Press enter to continue")
    clear()
else:
    # If a private key has been set, load it.
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
    print("3. View BCH exchange rate")
    print("4. Generate private key")
    selection = input("Selection: ")

    if (selection == "1"):
        print(k.address)
        addressqr = pyqrcode.create(k.address)
        addressqr.svg('publicaddress.svg', scale=2)
        print(addressqr.terminal(quiet_zone=1))
    elif (selection == "2"):
        print(k.balance)
    elif (selection == "3"):
        print(satoshi_to_currency(100000000, 'usd'))
    elif (selection == "4"):
        k = Key()
        print("Generated private key: " + k.to_hex())
    else:
        print("Error: Unknown option")
    
    
elif (selection == "2"): # Boot into normal ATM mode.
    pass
else: # An unknown mode was selected.
    print("Error: Unknown mode.")
    print("Exiting")
