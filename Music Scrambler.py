import os, fnmatch, random

file_path = 'D:\\Testing Folder\\'

files_to_rename = fnmatch.filter(os.listdir(file_path), '*.mp4')

total_files = len(files_to_rename)

num_used = [False] * total_files

for i, file_name in enumerate(files_to_rename):

    rnd_num = random.randint(1,total_files)

    while (num_used[rnd_num - 1]):
        rnd_num = random.randint(1, total_files)

    num_used[rnd_num - 1] = True

    new_file_name = str(rnd_num) + '-' + file_name

    os.rename(file_path + file_name,file_path + new_file_name)