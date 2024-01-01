def generate_txt_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content+ '\n')


def add_line_to_txt_file(filename, line):
    with open(filename, 'a') as f:
        f.write(line + '\n')

