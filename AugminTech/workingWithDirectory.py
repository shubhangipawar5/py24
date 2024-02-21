#its a folder consisting files
#get path of current working director


import os

print(os.getcwd())   #o/p--> C:\Users\shubh\HomeWork\2023\PyByRahulSir_2023\pyB\yRahul\AugminTech

print(os.listdir())   #all files.direct inside the current directory -> ['fileHandlingConcept', 'Modules', 'workingWithDirectory.py']

# os.mkdir('mypiks')   # to create directory
# os.rename('mypiks','myimages') #to rename directory
# os.rmdir('myimages')  #to remove the directory   - directory will be deletedd

print(os.getcwd())
check_dir=os.path.isdir('C:\\Users\\shubh\\HomeWork\\2023\PyByRahulSir_2023\\pyB\\yRahul\\AugminTech\\Modules')
print(check_dir)   # boolean output-> True


os.remove('filename')   #toremove/delete the file