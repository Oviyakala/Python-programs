import os
def create_file (filename):
    try:
        with open (filename,'w') as f:
           f.write ('hello, world!\n')
        print("File "+ filename +" created successfully. ")
    except IOError:
        print("error: could not create file" + filename)
def read_file (filename):
    try:
        with open (filename, 'r')as f:
            contents = f. read()
            print(contents)
    except IOError :
        print("error:could not read file"+ filename)
def append_file (filename,text):
    try:
        with open(filename,'a') as f:
            f.write(text)
        print("text appended to file" + filename+"successfully") 
    except IOError:
        print("error: could not appendedto file" + filename)
def rename_file(filename,new_filename) :
    try:
        os.rename(filename,new_filename)
        print("file" + filename + "renamed to" + new_filename + "successfully.")
    except IOError:
        print("error:could not rename file" + filename)
def delete_file(filename):
    try:
        os.remove(filename)
        print("file" + filename + " deleted successfully.")
    except IOError:
        print("error: could not delete file" + filename)
if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example . txt" 
    create_file(filename)   
    read_file(filename)
    append_file(filename , "this is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)

    
    
            
       