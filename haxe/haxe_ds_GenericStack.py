class haxe_ds_GenericStack:
    _hx_class_name = "haxe.ds.GenericStack"
    __slots__ = ("head",)
    _hx_fields = ["head"]
    _hx_methods = ["add", "first", "pop", "isEmpty", "remove", "iterator", "toString"]

    def __init__(self):
        self.head = None

    def add(self,item):
        self.head = haxe_ds_GenericCell(item,self.head)

    def first(self):
        if (self.head is None):
            return None
        else:
            return self.head.elt

    def pop(self):
        k = self.head
        if (k is None):
            return None
        else:
            self.head = k.next
            return k.elt

    def isEmpty(self):
        return (self.head is None)

    def remove(self,v):
        prev = None
        l = self.head
        while (l is not None):
            if HxOverrides.eq(l.elt,v):
                if (prev is None):
                    self.head = l.next
                else:
                    prev.next = l.next
                break
            prev = l
            l = l.next
        return (l is not None)

    def iterator(self):
        l = self.head
        def _hx_local_2():
            def _hx_local_0():
                return (l is not None)
            def _hx_local_1():
                nonlocal l
                k = l
                l = k.next
                return k.elt
            return _hx_AnonObject({'hasNext': _hx_local_0, 'next': _hx_local_1})
        return _hx_local_2()

    def toString(self):
        a = list()
        l = self.head
        while (l is not None):
            x = l.elt
            a.append(x)
            l = l.next
        return (("{" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in a]))) + "}")

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.head = None
haxe_ds_GenericStack._hx_class = haxe_ds_GenericStack
_hx_classes["haxe.ds.GenericStack"] = haxe_ds_GenericStack


