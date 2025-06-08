from os import walk

def get_files_from_folder(folder: str):
    files = []

    for (dirpath, dirnames, filenames) in walk(folder):
        files.extend(filenames)
        break

    return files