import os

os.chdir('/home/vick/Downloads/Video/pythonvids')
for files in os.listdir():
    file_name, file_ext = os.path.splitext(files)
    new_file = (file_name.strip('()0123456789--').capitalize())
    print(new_file.capitalize())

    os.rename(files, new_file)
