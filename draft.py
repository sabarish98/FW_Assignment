import json
import glob
import os
def json_merge(fold_path,input_base,output_base,Max_mem):
    count=0
    path_in=os.path.join(fold_path, input_base+'*.json')
    path_out = os.path.join(fold_path, output_base+str(count)+'.json')

    list_files=[]
    if glob.glob(path_in,recursive= True):
        list_files=glob.glob(path_in,recursive= True)
        merge=[]
        for file in list_files:
            with open(file, 'rb') as infile:
                merge.append(json.load(infile))
        with open(path_out,'w') as outfile:
            json.dump(merge,outfile,indent=2)
            info=os.stat(path_out)
            if info.st_size > Max_mem:
                print("Memory Limit Exceeded")
            else:
                print("Output file within memory limits")
        count=count+1
    else:
        print("File not found,Enter valid path and base name")


