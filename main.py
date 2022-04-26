nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]
# 1. Написать итератор, который принимает список списков, и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов.

class FlatIterator:
    def __init__(self, start_list):
        self.start_list = start_list

    def __iter__(self):
        my_list = []
        for i in self.start_list:
            for j in i:
                my_list.append(j)
        self.my_list = my_list
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.my_list):
            raise StopIteration
        return self.my_list[self.cursor]

for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

# 2. Написать генератор, который принимает список списков, и возвращает их плоское представление.

def flat_generator(flat_list):
    for i in flat_list:
        for j in i:
            yield j

for item in flat_generator(nested_list):
    print(item)

print(list(flat_generator(nested_list)))

# 3. Написать итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности

class FlatIteratorList:
    def __init__(self, start_list):
        self.start_list = start_list

    def __iter__(self):
        self.my_list = []
        self.current_iter = iter(self.start_list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iter)
            except StopIteration:
                if not self.my_list:
                    raise StopIteration
                else:
                    self.current_iter = self.my_list.pop()
                    continue
            if isinstance(self.current_element, list):
                self.my_list.append(self.current_iter)
                self.current_iter = iter(self.current_element)
            else:
                return self.current_element

for item in FlatIteratorList(nested_list):
    print(item)
flat_list = [item for item in FlatIteratorList(nested_list)]
print(flat_list)


 # 4. Написать генератор аналогичный генератор из задания 2, но обрабатывающий списки с любым уровнем вложенности

def flattenlist(start_list):
    for i in start_list:
        if isinstance(i, list):
            yield from flattenlist(i)
        else:
            yield i

for item in flattenlist(nested_list):
    print(item)