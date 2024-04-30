import os
import sys

def run_files(folder):
    folder_path = os.path.join(os.getcwd(), folder)
    try:
        files = os.listdir(folder_path)
    except FileNotFoundError:
        print(f"Folder '{folder}' does not exist in {os.path.dirname(folder_path)}.")
        return

    for file_name in files:
        if file_name.endswith(".py"):
            file_path = os.path.join(folder_path, file_name)
            print('---------------------------------------------------------')
            # Execute the Python file
            exit_code = os.system(f"python {file_path}")
            if exit_code != 0:
                print(f"Error running file: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments provided, set default value
        folders_to_run = ["Config_1", "Config_2", "Config_3", "Config_4", "Config_5"]
    else:
        # Use provided arguments
        folders_to_run = sys.argv[1:]
    for folder in folders_to_run:
        run_files(folder)
