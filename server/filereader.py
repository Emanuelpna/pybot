def read_file(file_name: str):
    file = open(file_name)

    content = file.read()

    file.close()

    return content