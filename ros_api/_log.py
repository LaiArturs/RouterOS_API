# Author: Arturs Laizans
# Package for displaying and saving verbose log

import logging


class Log:

    # For initialization, class Log takes 3 arguments: path, logic, file_mode.
    # path:
    #  - False - don't do logging. It won't save anything to file and won't print anything to stdout.
    #  - True - will print verbose output to stdout.
    #  - string - will save the verbose output to file named as this string.
    # logic:
    #  - 'OR' - if the path is a string, only saves verbose to file;
    #  - 'AND' - if the path is string, prints verbose output to stdout and saves to file.
    # file_mode:
    #  - 'a' - appends log to existing file
    #  - 'w' - creates a new file for logging, if a file with such name already exists, it will be overwritten.

    def __init__(self, path, logic, file_mode):

        # If logging to file is needed, configure it
        if path is not True and type(path) == str:
            logging.basicConfig(filename=path, filemode=file_mode,
                                format='%(asctime)s - %(message)s', level=logging.DEBUG)

        # Define different log actions that can be used
        def nothing(message):
            pass

        def to_file(message):
            logging.debug(message)

        def to_stdout(message):
            print(message)

        def both(message):
            print(message)
            logging.debug(message)

        # Set appropriate action depending on path and logic values
        if not path:
            self.func = nothing

        elif path is True:
            self.func = to_stdout

        elif path is not True and type(path) == str and logic == 'OR':
            self.func = to_file

        elif path is not True and type(path) == str and logic == 'AND':
            self.func = both
        else:
            self.func = to_stdout

    def __call__(self, message):
        self.func(message)
