# function definition for reading the .properties file

def read_properties(file_path):
    properties = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#') or not line:
                # skip comments and/or blanks lines
                continue
            key, value = [part.strip() for part in line.split('=', 1)]
            properties[key] = value
    return properties
# end of read_properties


