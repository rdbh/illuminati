# File handler for illuminati
import os

def change_dir():
    work_dir = input("Enter new working directory: ")
    if work_dir == "":
        work_dir = "./"

    if os.path.isdir(work_dir):
        os.chdir(work_dir)
    else:
        try:
            os.mkdir(work_dir)
        except: 
            print("Cannot create working directory")
        os.chdir(work_dir)
    return os.getcwd()

def get_addresses(file_name):
    working_file = readable(file_name)
    contents = working_file.read()
    addresses = contents.splitlines()
    working_file.close()
    return addresses

def readable(file_name):
    # assumes file_name is passed correctly
    try:
        fo = open(file_name, 'r')
        return fo
    except:
        print(f"\nCould not open {file_name}\n")
        return

def writeable(file_name):
    # assumes file_name and mode are passed correctly
    # check to see if file exists
    if os.path.exists(file_name):
        # overwrite or append?
        choice = input(f"{file_name} exists.\n" + \
                "[O]verwrite or [A]ppend: ")
        if choice.upper() == 'A':
            mode = 'a'
        elif choice.upper() == 'O':
            mode = 'w'
        else:
            print("Invalid choice")
            return
    else:
        mode = 'w'
    try:
        fo = open(file_name, mode)
    except:
        print(f"\nCould not open {file_name}\n")
    return fo

def main():
    pass

if __name__ == "__main__":
    main()