import os

# Welcome Message
print("Welcome to Ocean's PC Cleaner")

# User defined directories
directory = input("Please enter the full directory to clean")

# Clear temporary files
for root, dirs, files in os.walk('C:\\Windows\\Temp'):
    for file in files:
        os.remove(os.path.join(root, file))

# Clean old files from defined directories
for dir_path in directory:
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.stat(file_path).st_mtime < (os.time() - 30 * 24 * 60 * 60):
                os.remove(file_path)

# Empty Recycle Bin
os.system('cmd /c "echo Y|PowerShell.exe -NoProfile -Command Clear-RecycleBin"')


