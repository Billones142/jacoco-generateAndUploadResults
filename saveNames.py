import os

def save_file_names(folder_path, file_path):
  """Saves the names of all the files and folders in the given folder to the given file.

  Args:
    folder_path: The path to the folder.
    file_path: The path to the file to save the file names to.
  """

  with open(file_path, 'w') as f:
    for file_name in os.listdir(folder_path):
      f.write(file_name + '\n')


if __name__ == '__main__':
  folder_path = './my_folder'
  file_path = './file_names.txt'

  save_file_names(folder_path, file_path)
