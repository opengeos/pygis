import os
import shutil


def mkdir(dir_name, root_dir='.'):
    temp_dir = os.path.join(os.path.expanduser(root_dir), dir_name)
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    print("Folder created: {}".format(temp_dir))
    return temp_dir

def rmdir(dir_name, root_dir='.'):
    temp_dir = os.path.join(os.path.expanduser(root_dir), dir_name)
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)


if __name__ == "__main__":
    mkdir('temp2', '~')
    rmdir('temp2', '~')