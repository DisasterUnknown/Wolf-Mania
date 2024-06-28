import os

number_of_folders = input("Enter the number of folders: ")

for i in range(1, (int(number_of_folders) + 1)):
    os.makedirs(f"Chapter {i}")