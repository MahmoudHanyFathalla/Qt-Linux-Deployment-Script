import subprocess
import shutil
import os
import sys
import stat
if len(sys.argv) != 3:
    print("Usage: python script_name.py qt_version executable_path")
    sys.exit(1)

qt_version = sys.argv[1]
qt_dir = os.path.expanduser(f"~/Qt/{qt_version}/gcc_64")
if os.path.exists(qt_dir):
    print(f"Found Qt directory at {qt_dir}")
    lib_dir = os.path.join(qt_dir, 'lib')
    plugins_dir = os.path.join(qt_dir, 'plugins')
    for dir in [lib_dir, plugins_dir]:
        dir_name = os.path.basename(dir)
        dst_dir = os.path.join(os.getcwd(), dir_name)
        if not os.path.exists(dst_dir):
            shutil.copytree(dir, dst_dir)
            print(f"Copied {dir_name} to {os.getcwd()}")
        else:
            print(f"{dir_name} already exists in the current directory")
else:
    print("Qt directory not found in the expected path")

custom_paths = [os.path.expanduser(f"~/Qt/{qt_version}/gcc_64/lib"),os.path.expanduser("~/opencv-4.x/build/lib")]

executable_path = sys.argv[2]

result = subprocess.run(['ldd', executable_path], stdout=subprocess.PIPE, text=True)
lines = result.stdout.splitlines()

for line in lines:
    parts = line.split(' => ')
    if len(parts)>1 and parts[1].startswith('/'):
        file_path = parts[1].split(' ')[0]
        file_name = os.path.basename(file_path)
        dst_path = os.path.join(os.getcwd(), file_name)
        try:
            shutil.copy(file_path, dst_path)
            print(f"Copied {file_name} to {os.getcwd()}")
        except shutil.SameFileError:
            print("File Already Exist")

    else:
        print("Can't find path for \t",parts[0]," \n ** Searching given paths")
        for path in custom_paths:
            file_name = parts[0].strip().split(' ')[0]
            new_path = path+'/'+file_name
            print(new_path)
            if(os.path.exists(new_path)):
                print(" Found !")
                dst_path = os.path.join(os.getcwd(), file_name)
                try:
                    shutil.copy(new_path, dst_path)
                except shutil.SameFileError:
                    print("File Already Exist")
                break
        print('\n')

# Create run.sh script
with open('run.sh', 'w') as f:
    f.write('#!/bin/bash\n')
    f.write(f'export LD_LIBRARY_PATH=$(pwd)/lib:$LD_LIBRARY_PATH\n')
    f.write(f'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)\n')
    f.write(f'./{os.path.basename(executable_path)}\n')

# Make run.sh executable
st = os.stat('run.sh')
os.chmod('run.sh', st.st_mode | stat.S_IEXEC)

