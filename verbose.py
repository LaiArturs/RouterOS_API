# Author: Arturs Laizans
# Package for displaying and saving verbose log

import logging


class Log:

    def __init__(self, path, logic, file_mode):
        if path is not True and type(path) == str:
            logging.basicConfig(filename=path, filemode=file_mode,
                                format='%(asctime)s - %(message)s', level=logging.DEBUG)

        def nothing(message):
            pass

        def to_file(message):
            logging.debug(message)

        def to_stdout(message):
            print(message)

        def both(message):
            print(message)
            logging.debug(message)

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
