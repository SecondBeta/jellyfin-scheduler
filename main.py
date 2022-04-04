#!/usr/bin/python3

import json
import os
import re
import shutil

with open('config.json', 'r') as config:
    configData = json.load(config)
    dirloc = (configData['dirloc'])
    target_dirloc = (configData['target_dirloc'])
    
    # Get latest file from original dirloc
    files = os.scandir(dirloc)
    original_dir = max(files, key=os.path.getctime)

    # Set name for new folder
    for file in os.scandir(dirloc):
        dir = os.path.splitext(os.path.basename(file.path))[0]
        regEx = re.sub(r'\[.*?\]', r'', dir)
        new_folder = regEx[:-13].lstrip().rstrip()
        
        newpath = (target_dirloc + '\\' + new_folder)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            
            src = original_dir
            dst = newpath
            shutil.copy(src, dst, follow_symlinks=True)
            print('File successfully downloaded to:\n' + newpath)