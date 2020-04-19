import os
import datetime


def store_extensions():
    extensions = []
    yes_strings = ['Y', 'y', 'Yes', 'YES', 'yes']
    no_strings = ['N', 'n', 'No', 'NO', 'no']
    # Ask user to add extension
    print('Type in extension to add to filter:')
    current_extension = raw_input()
    # Check empty entry
    while not current_extension:
        print('Put in an extension or use Ctrl+C to abort the program')
        current_extension = raw_input()
    # Correct the extension if it doen't start with a dot ('.'')
    if current_extension[0] == '.':
        extensions.append(current_extension)
    else:
        extensions.append('.{}'.format(current_extension))
    # Ask for another extensions and return resuls
    print('Sucessfully added. Do you want to add another extension? (Y/N)')
    if raw_input() in yes_strings:
        extensions.extend(store_extensions())
    return extensions


def rename_files(directory='./', extensions=None):
    if not extensions:
        extensions = store_extensions()
    # Create list for file names
    file_list = os.listdir(directory)
    # New file dictionary
    new_files_dict = {}
    # Count the number of files that are renamed for statistics
    count = 0

    for file in file_list:
        # Split the file into filename and extension and check extensions
        file_name, extension = os.path.splitext(file)
        if (extension in extensions):
            # Get the create time of the file and convert into human-readable
            create_time = os.path.getctime(file)
            format_time = datetime.datetime.fromtimestamp(create_time)
            format_time_string = format_time.strftime("%Y-%m-%d %H.%M.%S")
            # Create the new name for the file
            new_name = format_time_string + extension
            # If other file is created at the same timestamp, add an symbol
            if (new_name in new_files_dict.keys()):
                index = new_files_dict[new_name] + 1
                new_files_dict[new_name] = index
                new_name = format_time_string + '-' + str(index) + extension
            else:
                new_files_dict[new_name] = 0

            # Rename the file
            os.rename(file, new_name)
            # printing log
            count = count + 1
            print(file.rjust(35) + '    =>    ' + new_name.ljust(35))

    print('All done. {} files are renamed.'.format(str(count))


if __name__ == '__main__':
    rename_files()
