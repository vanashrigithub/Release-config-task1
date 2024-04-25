import os
import sys

def run_files(folder):
    folder_path = os.path.join(os.getcwd(), folder)
    if not os.path.exists(folder_path):
        print(f"Folder '{folder}' does not exist.")
        return

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".py"):
            file_path = os.path.join(folder_path, file_name)
            #print(f"Running file: {file_path}")
            print('---------------------------------------------------------')
            # Execute the Python file
            os.system(f"python {file_path}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments provided, set default value
        folders_to_run = ["Config_1", "Config_2", "Config_3", "Config_4", "Config_5"]
    else:
        # Use provided arguments
        folders_to_run = sys.argv[1:]
    for folder in folders_to_run:
        run_files(folder)
