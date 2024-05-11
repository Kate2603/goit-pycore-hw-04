import sys
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)

def list_directory_structure(directory_path):
    """
    Function to list the directory structure recursively
    """
    directory_path = Path(directory_path)
    
    # Validate if the directory exists
    if not directory_path.exists():
        print(Fore.RED + "Error: Specified path does not exist.")
        return

    # Validate if the specified path is a directory
    if not directory_path.is_dir():
        print(Fore.RED + "Error: Specified path is not a directory.")
        return

    print(Fore.YELLOW + "Directory structure of", directory_path)
    _list_directory_structure(directory_path)


def _list_directory_structure(directory_path, indent=""):
    """
    Helper function to list directory structure recursively
    """
    for item in directory_path.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + "|-- " + Style.BRIGHT + item.name)
            _list_directory_structure(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + "|-- " + item.name)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        list_directory_structure(directory_path)


list_directory_structure("task_1")
list_directory_structure("task_2")
list_directory_structure("task_4")