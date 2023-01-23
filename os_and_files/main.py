from os_and_files.proxy_txt_reader_writer import TxtProxyReader
from os_and_files.proxy_txt_reader_writer import TxtProxyWriter
from os_and_files.txt_reader import TxtReader
from os_and_files.txt_writer import TxtWriter


def read_from_file():
    txt_reader = TxtReader('text.txt')
    proxy_reader = TxtProxyReader(txt_reader)
    print(proxy_reader.read_file())


def put_to_file():
    txt_writer = TxtWriter('text.txt', '---------------')
    proxy_writer = TxtProxyWriter(txt_writer)
    proxy_writer.write_file()
    read_from_file()


def custom_print_and_count():
    txt_reader = TxtReader('text.txt')
    TxtProxyReader(txt_reader)
    massive = "abcdefghijklmnopqrstuvwxyz"

    for letter in massive:
        txt_reader.print_count_file(letter)
    return


#add_to_file()
custom_print_and_count()
