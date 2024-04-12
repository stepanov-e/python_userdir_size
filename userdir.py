import os
import shutil
import datetime

def get_directory_size(directory):
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.exists(filepath):
              total_size += os.path.getsize(filepath)
    return total_size


lines = []
script_dir = os.path.dirname(os.path.abspath(__file__))

with open('/etc/passwd', 'r') as file:
  for line in file:
    lines.append(line.strip())


for passwdLine in lines:
    parts = passwdLine.split(':')

    uid_str = parts[2]
    dir_str = parts[5]
    username = parts[0]
    uid = int(uid_str)

    exists = os.path.exists(dir_str) and os.path.isdir(dir_str)


    if uid >= 1000 and username != "nobody" and exists == True:
      size_in_bytes = get_directory_size(dir_str)
      size_in_mb = int(size_in_bytes / (1024 * 1024))
      current_date = datetime.datetime.now()

      with open(script_dir+'/passwd_python.txt', 'a') as file:
        file.write(f"{current_date} size {size_in_mb} Mb (size in bytes: {size_in_bytes}) {dir_str} (username: {username})\n")
      with open(script_dir+'/passwd_python.html', 'a') as file:
        file.write(f"{current_date} size {size_in_mb} Mb (size in bytes: {size_in_bytes}) {dir_str} (username: {username})<br>\n")



source_file = script_dir+"/passwd_python.html"
destination_file = "/var/www/html/passwd_python.html"

shutil.copy(source_file, destination_file)
