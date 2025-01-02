import os 
import shutil


def backup_file(source_dir , backup_dir):
    if os.path.exists(source_dir):
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            
        files = os.listdir(source_dir)
        
        for file in files:
            source_file = os.path.join(source_dir , file)
            backup_file_path = os.path.join(backup_dir , file)
            
            if os.path.isfile(source_file):
                shutil.copy(source_file , backup_file_path)
                print(f'Backed up {file}')
                
    else:
        print(f'No files to backup in {source_dir}')
            
            
            
source = ''
backup = ''
backup_file(source , backup)
