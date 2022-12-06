class haxe_ds__List_ListIterator:
    _hx_class_name = "haxe.ds._List.ListIterator"
    __slots__ = ("head",)
    _hx_fields = ["head"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,head):
        self.head = head

    def hasNext(self):
        return (self.head is not None)

    def next(self):
        val = self.head.item
        self.head = self.head.next
        return val

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.head = None
haxe_ds__List_ListIterator._hx_class = haxe_ds__List_ListIterator
_hx_classes["haxe.ds._List.ListIterator"] = haxe_ds__List_ListIterator


