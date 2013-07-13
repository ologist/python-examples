import os

build_path = '/Users/ologist/dev'
log_history_size = 9

files = os.listdir(build_path)

files.sort(reverse=True)

display_size = log_history_size if len(files) > log_history_size else len(files)

for file in files[:display_size]:
    print(file)
