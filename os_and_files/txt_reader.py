import sys
from os_and_files.abstract_reader import Reader


class TxtReader(Reader):

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        """
        This function read from file
        :return: text
        """
        with open(self.file_path) as file:
            text = file.read()
        return text

    def print_count_file(self, counter):
        """
        This function read file
        :param counter: receive some value for count
        :return: string
        """
        file = self.read_file()
        return sys.stdout.write(counter + ": " + (str(file.lower().count(counter)) + " "))
