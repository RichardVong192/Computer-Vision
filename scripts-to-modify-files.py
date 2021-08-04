import os, shutil, random
from os import listdir
from os.path import isfile, join
train_dir = '/home/cosc/student/rvo16/Documents/2021/Cocs428/Assignment1/datasetMasks/train'
val_dir = '/home/cosc/student/rvo16/Documents/2021/Cocs428/Assignment1/datasetMasks/validation'
test_dir = '/home/cosc/student/rvo16/Documents/2021/Cocs428/Assignment1/datasetMasks/test'

def delete_all_from_file():
    for pokemon_folder in os.listdir(train_dir): #for folder in train directory
        folder = val_dir + '/' + pokemon_folder
        
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        

#copy a percent from train to a new directory
def copy_a_percent_to_new_directory():
    
    for folder_name in os.listdir(train_dir): #for folder in train directory
        source = train_dir + '/' + folder_name
        dest = test_dir + '/' + folder_name
        
        files = os.listdir(source)
        no_of_files = round(len(files) * 0.2) #copies a percentage to a new file
            
        for file_name in random.sample(files, no_of_files):
            shutil.move(os.path.join(source, file_name), dest)    
    
def rename_files():
    
    for pokemon_files in os.listdir(train_dir): #for folder in train directory
        specific_directory = train_dir + '/' + pokemon_files
        for count, filename in enumerate(os.listdir(specific_directory)):
            
            dst = '/' + pokemon_files + '.' + str(count) + ".jpg"
            src = specific_directory + '/' +filename
            dst = specific_directory + dst
            
            os.rename(src, dst) #(actualname, newname)

def is_image(filename, verbose=False):

    data = open(filename,'rb').read(10)

    # check if file is JPG or JPEG
    if data[:3] == b'\xff\xd8\xff':
        #if verbose == True:
             #print(filename+" is: JPG/JPEG.")
        return True

    # check if file is PNG
    if data[:8] == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
        if verbose == True:
             print(filename+" is: PNG.")
             os.remove(filename)
        return True

    # check if file is GIF
    if data[:6] in [b'\x47\x49\x46\x38\x37\x61', b'\x47\x49\x46\x38\x39\x61']:
        if verbose == True:
            print(filename+" is: GIF.")
        return True

    return False


def remove_broken_files():
    abc = '/home/cosc/student/rvo16/Documents/2021/Cocs428/Assignment1/dataset/validation/'
    
    for folder in sorted(os.listdir(abc)):
        # go through all files in desired folder
        for filename in sorted(os.listdir(abc+folder)):
            #print(abc+folder+filename)
            # check if file is actually an image file
            thing = abc+folder+ '/'+ filename
            #print(folder + '/'+ filename)
            if is_image(thing, verbose=True) == False:
                # if the file is not valid, remove it
                os.remove(os. path. join(folder, filename))
     

#delete_all_from_file()
#rename_files()
copy_a_percent_to_new_directory()

print("DONE!")