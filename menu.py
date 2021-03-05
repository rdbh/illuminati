# Illuminati tool for dark web searching
import config
import darkcheck
import file_handler
from os import getcwd

# global variables
work_dir = getcwd()

def check_darkweb():
    # get address or address list
    print(darkcheck.BANNER)
    print("Enter a .onion address to check")
    print("Or a file name to load from file")
    address_raw = input("-> ")
    address_list = []

    # assume a string ending in .onion is a single entry
    if address_raw[-6:].lower() == ".onion":
        address_list = [address_raw]
    # if nothing was 
    elif address_raw == "":
        print("No address entered")
        return
    else:
        address_list = file_handler.get_addresses(address_raw)
        print(f"\n{len(address_list)} addresses retrieved from {address_raw}")
    
    # pass the list to darkcheck, catch list of results
    results = darkcheck.check(address_list)
    print(f"\n{len(results)} retrieved.")
    
    # display or save results
    while True:
        print("[D]isplay or [S]ave results")
        choice = input("[X] to eXit: ")
        if choice.upper() == "X":
            break
        elif choice.upper() == "D":   
            # display
            print("Address List:")
            for key in results:
                print(f"\tAddress: {key} returned status {results[key]}")
        elif choice.upper() == "S":
            # save
            # get save file name
            choice = input("Enter save file name: ")
            if choice == "":
                print("No file selected")
                break
            save_file = choice
            # create a save string
            save_string = ""
            for address in results:
                save_string += address + str(results[address] + '\n')
            # open the save file
            with file_handler.writeable(save_file) as save_fo:
                # write save string to save file
                try:
                    save_fo.write(save_string)
                except:
                    print("Write to file failed")
        else:
            print(f"Invalid Selection {choice}\n")

def change_settings():
    print("Change Default Settings")

def change_directory():
    work_dir = file_handler.change_dir()

def main():
    while True:
    # build a simple menu
        # menu options
        print(config.BANNER)
        print("Enter [D] to check Darkweb addresses")
        print("Enter [S] to change default Settings")
        print("Enter [W] to change Working directory")
        print()
        print(f"Current working directory is:\n\t{work_dir}")

        # get user input
        choice = input("\nEnter X to quit: ")
        print("\n\n")

        # exit code
        if choice.upper() == 'X':
            print("Exiting")
            quit()
        # Check Darkweb
        elif choice.upper() == 'D':
            check_darkweb()
        # Change Settings
        elif choice.upper() == 'S':
            change_settings()
        # Change Settings
        elif choice.upper() == 'W':
            change_directory()
        # handle non-options
        else:
            print("Please select a valid option")

if __name__ == "__main__":
    main()