# Create an iterator that accepts a sequence and can iterate over values
# ​​over a given range. CustomIterator(sequence, start_index, end_index)

class CustomIterator:
    def __init__(self, sequence, start_index, end_index):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index >= 0 and (len(self.__sequence) - 1 >= self.__end_index >= self.__start_index):
            if self.__start_index < len(self.__sequence):
                item = self.__sequence[self.__start_index]
                self.__start_index += 1
                return item
            else:
                raise StopIteration
        else:
            raise StopIteration


if __name__ == '__main__':
    my_iterator = CustomIterator([1, 2, 3, 4, 5], 2, 3)
    for iter_obj in my_iterator:
        print(iter_obj)
