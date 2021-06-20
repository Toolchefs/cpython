import os
from os import listdir
from os.path import isfile, join
from shutil import copyfile

def main():
    print("Copy to deploy..")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    libs_path = dir_path + "/../libs"
    if not os.path.exists(libs_path):
        os.mkdir(libs_path)
    build_path = dir_path + "/amd64"
    onlyfiles = [f for f in listdir(build_path) if isfile(join(build_path, f))]
    for file_name in onlyfiles:
        current_file = build_path + "/" + file_name
        if file_name.endswith(".exe") or file_name.endswith(".dll"):
            copyfile(current_file, dir_path + "/../" + file_name)
        if file_name.endswith(".lib"):
            copyfile(current_file, dir_path + "/../libs/" + file_name)

if __name__ == "__main__":
    main()