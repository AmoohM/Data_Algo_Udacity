import os

def find_files(suffix, path):
  """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
  """
  filepaths=[] #list of path files with given suffix 

  if os.path.exists(path):
    try:
      for file in os.listdir(path): # list of files and directories under working folder
        current_path = os.path.join(path,file)
        #print(os.path.splitext(file)[-1].lower(),suffix)
        if(os.path.splitext(file)[-1].lower() == suffix): #Check if current file has suffix
          filepaths.append(current_path)
        else:
          find_files(suffix,current_path)   # if current file has sub-directories
    except (FileNotFoundError,NotADirectoryError) : #currect file has no subdirectories
      pass
    
    
  return filepaths

#tests
print(find_files('.c', 'testdir'))
#print(find_files('.h', 'testdir'))
#print(find_files('.c', ''))
#print(find_files('.c', 'testdir\subdir5'))
