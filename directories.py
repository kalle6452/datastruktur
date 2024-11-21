import os


def dir(path):
    # This will print out all directories in path.
    direc = os.listdir(path)
    # Going through all files in path.
    for i in direc:
        # if filename starts with . it is hidden file.
        if not i.startswith('.'):
            # Adding the previous directories in front of path
            # so that it can be called upon globally.
            path_dir = os.path.join(path, i)
            # If we stumble upon a file we call upon the function again
            # so that we can repeat the procedure for all nested dir.
            if os.path.isdir(path_dir):
                dir(path_dir)
            # We just print if it's a file.
            elif os.path.isfile(path_dir):
                print(i) 


dir('/home/kalle/Dokument')
