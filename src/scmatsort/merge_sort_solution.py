from collections import deque
from collections.abc import Iterator
from itertools import chain

def merge_sorted_sequences(seq_1, seq_2,
                           descending=False, key_func=lambda x: x):
    try:
        seq_1 = iter(seq_1)
    except Exception:
        raise AttributeError("Sequence 1 cannot be iterated over")

    try:
        seq_2 = iter(seq_2)
    except Exception:
        raise AttributeError("Sequence 2 cannot be iterated over")

    head_1, head_2 = (None, None)
    while True:
        if head_1 is None:
            try:
                head_1 = next(seq_1)
            except StopIteration:
                if head_2 is not None:
                    seq_2 = chain([head_2,], seq_2)
                for head in seq_2:
                    yield head
                break

        if head_2 is None:
            try:
                head_2 = next(seq_2)
            except StopIteration:
                if head_1 is not None:
                    seq_1 = chain([head_1,], seq_1)
                for head in seq_1:
                    yield head
                break

        if descending:
            comp_func = lambda x, y: x>=y
        else:
            comp_func = lambda x, y: x<=y

        if comp_func(key_func(head_1), key_func(head_2)):
            yield_val = head_1
            head_1 = None
        else:
            yield_val = head_2
            head_2 = None

        yield yield_val
        continue

def sequential_merge_sort(x, descending=False, key_func=lambda x: x):
    x = (y if isinstance(y, Iterator) else [y]
         for y in iter(x))

    splits_queue = deque(x)

    while True:
        try:
            pop_1 = splits_queue.pop()
        except IndexError:
            raise AttributeError("x is empty")

        try:
            pop_2 = splits_queue.pop()
        except IndexError:
            break

        merged_item = merge_sorted_sequences(pop_1, pop_2, descending,
                                             key_func)

        splits_queue.appendleft(merged_item)

    return pop_1

