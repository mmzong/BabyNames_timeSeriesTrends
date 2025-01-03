import os
import re


def retrieve_file(ext):
    """
    Traverses every folder in project directory.
    Creates and returns a list containing the file
    path and name for every file with the extension
    given.

    Args:
        ext (str): file extension

    Return
        file_list (list): list of path/file_name.txt for
        every file that contains file extension specified
    """
    file_list = []
    for dir_paths, dir_names, file_names, in os.walk('/Users/michellezong/Documents/'
                                                     'GitHub/BabyNames_timeSeriesTrends/'):
        # print("\nCurrent location:", dir_paths)
        # print("\nDirectories:", dir_names)
        # print("Files:", file_names, end="\n\n")

        for f in file_names:
            if f.endswith(ext):
                # print(file_names)
                # print(dir_paths)
                file_list.append(os.path.join(str(dir_paths), str(f)))
    # print(file_list)
    return file_list


def record_loader_gen(path_list):
    """
    A generator that opens a file and yields each line from every file.
    Each record line it yields is composed of the name, gender, births,
    and year. Uses a regular expression to extract year from file name.
    Casts births and year into ints to do math on them later.

    Args:
        path_list (list): list of file-path names

    Return:
        name (str): name of row
        sex (str): gender of row
        births (int): number of births of row
        year (int): corresponding year of row
    """

    for path in path_list:
        year_found = re.search(r'yob(\d{4})\.txt$', path)

        if not year_found:
            break

        year = int(year_found.group(1))

        with open(path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                name = parts[0]
                sex = parts[1]
                births = int(parts[2])
                # print(type(births))
                # print(type(year))
                yield name, sex, births, year


if __name__ == "__main__":
    retrieve_file('.txt')

    # Call record_loader_gen() method when testing it
    # for row in record_loader_gen(retrieve_file('.txt')):
    #     print(row)

