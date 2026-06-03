import os
import stat

def analyze_directory(dir_path):
    if not os.path.exists(dir_path):
        print(f"Error: The path '{dir_path}' does not exist.")
        return
    if not os.path.isdir(dir_path):
        print(f"Error: '{dir_path}' is not a directory.")
        return

    print("=" * 60)
    print(f"  ANALYZING DIRECTORY: {os.path.abspath(dir_path)}")
    print("=" * 60)
    print(f"{'File Name':<30} | {'Size (Bytes)':<12} | {'Permissions':<12}")
    print("-" * 60)

    try:
        items = os.listdir(dir_path)
        
        if not items:
            print("The directory is empty.")
            return

        for item in items:
            full_path = os.path.join(dir_path, item)
            
            if os.path.isfile(full_path):
                file_stats = os.stat(full_path)
                file_size = file_stats.st_size
                file_perms = stat.filemode(file_stats.st_mode)
                print(f"{item:<30} | {file_size:<12} | {file_perms:<12}")
                
    except PermissionError:
        print("Error: Permission denied to read this directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("=" * 60)

if __name__ == "__main__":
    target_directory = "."  # fonctionne partout : Colab, Windows, Linux
    analyze_directory(target_directory)