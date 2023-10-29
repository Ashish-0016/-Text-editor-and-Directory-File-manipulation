import os

def Options():
    while True:
        print("\nOptions:")
        print("1. List Files in Directory")
        print("2. Create a Directory")
        print("3. Delete a file")
        print("4. Rename a file")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_files_in_directory()
        elif choice == '2':
            create_directory()
        elif choice == '3':
            delete_file()
        elif choice == '4':
            rename_file()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def list_files_in_directory():
    directory_path = input("Enter the directory path: ")
    
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        files = os.listdir(directory_path)
        print("Files in the directory:")
        for file in files:
            print(file)
    else:
        print("Directory not found.")

def create_directory():
    directory_path = input("Enter the directory path: ")
    
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)
        print("Directory created successfully.")
    else:
        print("Directory already exists.")

def delete_file():
    file_path = input("Enter the file path: ")
    
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print("File deleted successfully.")
        except Exception as e:
            print(f"An error occurred while deleting the file: {e}")
    else:
        print("File not found.")

def rename_file():
    old_file_path = input("Enter the current file path: ")
    new_file_name = input("Enter the new file name: ")
    
    if os.path.exists(old_file_path):
        file_directory = os.path.dirname(old_file_path)
        new_file_path = os.path.join(file_directory, new_file_name)
        os.rename(old_file_path, new_file_path)
        print("File renamed successfully.")
    else:
        print("File not found.")

if __name__ == "__main__":
    Options()
