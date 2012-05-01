from src.Items import ItemStashFull

class Item(object):
    def __init__(self, name, uses):
        self.name = name
        self._uses = uses

    def use(self, amount=1):
        self._uses -= amount

    @property
    def uses_left(self):
        return self._uses


class ItemStash(object):
    def __init__(self, size):
        self.size = size
        self._items = []

    def add_item(self, item):

        if self.size == len(self._items):
            raise ItemStashFull('The stash can only hold {} items!'.format(self.size))

        self._items.append(item)

    def drop_item(self, item):
        if item in self._items:
            self._items.remove(item)

    def next(self):
        pass

    def __iter__(self):
        for item in self._items[:]:
            yield item
        raise StopIteration
