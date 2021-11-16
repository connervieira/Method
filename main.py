from bitcoinpython import Key
from os import system, name
from bitcoinpython.network import satoshi_to_currency
import pyqrcode


# ----- Configuration Start -----

private_key = "" # The BitcoinCash wallet key in hex form.
fee = 0.1 # This is the percentage of the purchase that will be taken as a fee. For example, with a value of 0.1 (or 10%), insterting $1 will result in receiving $0.90 in BitcoinCash.
max_purchase = 5 # This value defines the maximum purchase size in USD of any individual transaction.
min_purchase = 0.1 # This value defines the minimum purchase size in USd of any individual transaction.

# ----- Configuration End -----


# Method is built on BitcoinPython which has documentation at: https://bitcoinpython.mercier.link


# Define the function to clear the screen.
def clear():
    if name == 'posix': # If OS is Linux or Mac, use the correct command for the platform.
        system('clear')
    else: # If OS is Windows, use the correct command for the platform.
        system('cls')


# Define some styling information
class style:
    # Define colors
    purple = '\033[95m'
    cyan = '\033[96m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'

    # Define text decoration
    bold = '\033[1m'
    underline = '\033[4m'

    # Define styling end marker
    end = '\033[0m'



clear() # Clear the screen on first launch


# Load the private key from the configuration
if (private_key == ""):
    # If no private key has been set, generate one automatically.
    k = Key()
    print(style.bold + style.yellow + "Warning: No private key has been set. A temporary one has been generated, but this will change on next launch. Before funding the ATM, configure a static private key. Otherwise, you will lose the contents of this wallet if the ATM restarts." + style.end)
    input("Press enter to continue...")
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
        print(style.bold + style.red + "Error: Unknown selection" + style.end)
    
    
elif (selection == "2"): # Boot into normal ATM mode.
    while True:

        # Render the main ATM interface.
        clear()
        print("              ███╗   ███╗███████╗████████╗██╗  ██╗ ██████╗ ██████╗ ")
        print("              ████╗ ████║██╔════╝╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗")
        print("              ██╔████╔██║█████╗     ██║   ███████║██║   ██║██║  ██║")
        print("              ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║   ██║██║  ██║")
        print("              ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝")
        print("              ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ")
        print("===================================================================================")
        print("===================================================================================")
        print("██████╗ ██╗████████╗ ██████╗ ██████╗ ██╗███╗   ██╗  ██████╗ █████╗ ███████╗██╗  ██╗")
        print("██╔══██╗██║╚══██╔══╝██╔════╝██╔═══██╗██║████╗  ██║ ██╔════╝██╔══██╗██╔════╝██║  ██║")
        print("██████╔╝██║   ██║   ██║     ██║   ██║██║██╔██╗ ██║ ██║     ███████║███████╗███████║")
        print("██╔══██╗██║   ██║   ██║     ██║   ██║██║██║╚██╗██║ ██║     ██╔══██║╚════██║██╔══██║")
        print("██████╔╝██║   ██║   ╚██████╗╚██████╔╝██║██║ ╚████║ ╚██████╗██║  ██║███████║██║  ██║")
        print("╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
        print("")
        print("                           █████╗ ████████╗███╗   ███╗")
        print("                          ██╔══██╗╚══██╔══╝████╗ ████║")
        print("                          ███████║   ██║   ██╔████╔██║")
        print("                          ██╔══██║   ██║   ██║╚██╔╝██║")
        print("                          ██║  ██║   ██║   ██║ ╚═╝ ██║")
        print("                          ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝")
        print("")
        print("Please make a selection.")
        print("1. Start transaction")
        print("2. Learn more")
        selection = input("Selection: ")

        if (selection == "1"): # The user has selected to start a transaction.
            clear()
            pass
        elif (selection == "2"): # The user has selected to learn more about the BitcoinCash ATM.
            clear()
            print("    _   _              _     ___ _ _          _      ___         _    ")
            print("   /_\ | |__  ___ _  _| |_  | _ |_) |_ __ ___(_)_ _ / __|__ _ __| |_  ")
            print("  / _ \| '_ \/ _ \ || |  _| | _ \ |  _/ _/ _ \ | ' \ (__/ _` (_-< ' \ ")
            print(" /_/ \_\_.__/\___/\_,_|\__| |___/_|\__\__\___/_|_||_\___\__,_/__/_||_|")
            print("")
            print("BitcoinCash is a derivative of Bitcoin that focuses on being usable like everyday cash. BitcoinCash boasts extremely low transaction fees while still maintaining the same security and decentralization that Bitcoin is known for.")
            print("")
            print("Due to BitcoinCash's extremely low transaction fees, it's quick and convenient to spend on every day items. Instead of spending $10 in fees on a $20 meal, BitcoinCash fees rarely exceed more than a cent.")

            print("    _   _              _     __  __     _   _            _ ")
            print("   /_\ | |__  ___ _  _| |_  |  \/  |___| |_| |_  ___  __| |")
            print("  / _ \| '_ \/ _ \ || |  _| | |\/| / -_)  _| ' \/ _ \/ _` |")
            print(" /_/ \_\_.__/\___/\_,_|\__| |_|  |_\___|\__|_||_\___/\__,_|")
            print("")
            print("Method is a quick and easy ATM designed to turn lose change into BitcoinCash. Just insert change you don't want to carry around, enter your BitcoinCash wallet, and receive cryptocurrency in seconds!")
            print("")
            print("Unlike other cryptocurreny ATMs, Method is completely open source and anonymous. No accounts, ID, or other personal information is required. Method is also designed around small transactions, as opposed to larger ones. Unlike typical cryptocurrency ATMs with minimum purchase amounts of $20 or more, Method's minimum purchase amount is significantly less than a dollar!")

            print("")
            print("  ___ _        _   _    _   _       ")
            print(" / __| |_ __ _| |_(_)__| |_(_)__ ___")
            print(" \__ \  _/ _` |  _| (_-<  _| / _(_-<")
            print(" |___/\__\__,_|\__|_/__/\__|_\__/__/")
            print("")
            print("Here's some quick reference information about this Method instance:")
            print("Minimum purchase amount (USD): $" + "{:.2f}".format(min_purchase))
            print("Maximum purchase amount (USD): $" + "{:.2f}".format(max_purchase))
            print("")
            print("")

            input("Press enter to continue...")
        else:
            clear()
            print(style.bold + style.red + "Error: Unknown selection" + style.end)
            input("Press enter to continue...")

else: # An unknown mode was selected.
    print(style.bold + style.red + "Error: Unknown selection" + style.end)
    print("Exiting")
