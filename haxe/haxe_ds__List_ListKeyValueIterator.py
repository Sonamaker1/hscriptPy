class haxe_ds__List_ListKeyValueIterator:
    _hx_class_name = "haxe.ds._List.ListKeyValueIterator"
    __slots__ = ("idx", "head")
    _hx_fields = ["idx", "head"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,head):
        self.head = head
        self.idx = 0

    def hasNext(self):
        return (self.head is not None)

    def next(self):
        val = self.head.item
        self.head = self.head.next
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.idx
                _hx_local_0.idx = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_AnonObject({'value': val, 'key': _hx_local_2()})
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.idx = None
        _hx_o.head = None
haxe_ds__List_ListKeyValueIterator._hx_class = haxe_ds__List_ListKeyValueIterator
_hx_classes["haxe.ds._List.ListKeyValueIterator"] = haxe_ds__List_ListKeyValueIterator


