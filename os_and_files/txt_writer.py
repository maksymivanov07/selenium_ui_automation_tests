from os_and_files.abstract_writer import Writer


class TxtWriter(Writer):

    def __init__(self, file_path, add_text):
        self.file_path = file_path
        self.add_text = add_text

    def write_file(self):
        """
        This method write to file
        :return: text
        """
        with open(self.file_path, 'w') as file:
            text = file.write(self.add_text)
        return text