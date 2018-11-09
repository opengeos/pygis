# https://www.geeksforgeeks.org/working-zip-files-python/

# importing required modules 
import os
from zipfile import ZipFile 
import datetime
import shutil

# Getting all information about a zip file
def read_zipfile(file_name):
    # opening the zip file in READ mode 
    with ZipFile(file_name, 'r') as zip: 
        for info in zip.infolist(): 
            print(info.filename) 
            print('\tModified:\t' + str(datetime.datetime(*info.date_time))) 
            print('\tSystem:\t\t' + str(info.create_system) + '(0 = Windows, 3 = Unix)') 
            print('\tZIP version:\t' + str(info.create_version)) 
            print('\tCompressed:\t' + str(info.compress_size) + ' bytes') 
            print('\tUncompressed:\t' + str(info.file_size) + ' bytes') 


# Extracting a zip file
def extract_zipfile(file_name, out_dir='./'):
    # opening the zip file in READ mode 
    with ZipFile(file_name, 'r') as zip: 
        # printing all the contents of the zip file 
        zip.printdir() 
    
        # extracting all the files 
        print('Extracting all the files now...') 
        zip.extractall(out_dir) 
        print('Unzipping done! Files saved at {}'.format(os.path.realpath(out_dir))) 


# get all file paths in a directory
def get_all_file_paths(directory): 
  
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths      


# Writing to a zip file
def write_zipfile(directory, zip_name):
  
    # calling function to get all file paths in the directory 
    file_paths = get_all_file_paths(directory) 
  
    # printing the list of all files to be zipped 
    print('Following files will be zipped:') 
    for file_name in file_paths: 
        print(file_name) 
  
    # writing files to a zipfile 
    with ZipFile(zip_name,'w') as zip: 
        # writing each file one by one 
        for file in file_paths: 
            zip.write(file) 
  
    print('All files zipped successfully!')      



if __name__ == "__main__":
    
    pkg_dir = os.path.dirname(__file__)
    print(pkg_dir)
    data_dir = './pygis/testdata'
    zip_name = './pygis/testdata.zip'
    out_dir = './data'
    write_zipfile(data_dir, zip_name)
    read_zipfile(zip_name)
    extract_zipfile(zip_name, out_dir)
    shutil.rmtree(out_dir)
    os.remove(zip_name)
    