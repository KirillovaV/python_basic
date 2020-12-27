"""
zip
reduce
filter
enumerate
range
map
sum
min
max
len
"""


def my_min(*args, key=None):
    result = args[0]
    if key:
        for itm in args:
            if key(itm) < key(result):
                result = itm
    else:
        for itm in args:
            if itm < result:
                result = itm
    return result


def my_max(*args, key=None):
    result = args[0]
    if key:
        for itm in args:
            if key(itm) > key(result):
                result = itm
    else:
        for itm in args:
            if itm > result:
                result = itm
    return result


# стащено с урока и добавлен старт
def my_sum(*args, start=0):
    result = start
    for n in args:
        result += n
    return result


# стащено с урока
def my_map(funk, iter_obj):
    for item in iter_obj:
        yield funk(item)


# так и не поняла, к чему же ближе 'range' object
# раз по нему можно запускать цикл for решила,
# что эффективнее через итератор, чем просто список...
def my_range(stop: int, start=0, step=1):
    result = start
    while result < stop:
        yield result
        result += step


def my_enumerate(iter_obj, start=0):
    for itm in iter_obj:
        yield start, itm
        start += 1


def my_filter(iter_obj, func=None):
    if func:
        for itm in iter_obj:
            if func(itm):
                yield itm
    else:
        for itm in iter_obj:
            if itm:
                yield itm


# def reduce(function, sequence, initial=_initial_missing)
#     it = iter(sequence) - и ТАК тоже можно???

def my_reduce(func, iter_obj, start=None):
    if start:
        result = func(start, iter_obj[0])
    else:
        result = iter_obj[0]
    for itm in iter_obj[1:]:
        result = func(result, itm)
    return result


def my_zip(*args):
    for i in range(len(min(args, key=len))):
        zip_list = []
        for itm in args:
            zip_list.append(itm[i])
        yield tuple(zip_list)


def my_len(itm):
    result = 0
    for _ in itm:
        result += 1
    return result
