from os_and_files.abstract_reader import Reader
from os_and_files.txt_reader import TxtReader

from os_and_files.abstract_writer import Writer
from os_and_files.txt_writer import TxtWriter

actual_status = False


class TxtProxyReader(Reader):

    def __init__(self, txt_reader: TxtReader):
        self.result = ''
        self.is_actual = actual_status
        self.reader = txt_reader

    def read_file(self):
        """
        Read file and return status
        :return: True of False
        """
        if self.is_actual:
            return self.result
        else:
            self.result = self.reader.read_file()
            self.is_actual = True
            return self.result


class TxtProxyWriter(Writer):
    def __init__(self, txt_writer: TxtWriter):
        self.result = ''
        self.is_actual = actual_status
        self.writer = txt_writer

    def write_file(self):
        """
        write file and set status from True to False
        :return: False
        """
        if self.is_actual:
            return self.result
        else:
            self.result = self.writer.write_file()
            self.is_actual = False
            return self.result


if __name__ == '__main__':
    txt_reader = TxtReader('text.txt')
    proxy_reader = TxtProxyReader(txt_reader)
    print(proxy_reader.read_file())

# if __name__ == '__main__':
#     txt_writer = TxtWriter('text.txt', '11test111111').write_file()
#     proxy_writer = TxtProxyWriter(txt_writer)
