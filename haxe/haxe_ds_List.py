class haxe_ds_List:
    _hx_class_name = "haxe.ds.List"
    __slots__ = ("h", "q", "length")
    _hx_fields = ["h", "q", "length"]
    _hx_methods = ["add", "push", "first", "last", "pop", "isEmpty", "clear", "remove", "iterator", "keyValueIterator", "toString", "join", "filter", "map"]

    def __init__(self):
        self.q = None
        self.h = None
        self.length = 0

    def add(self,item):
        x = haxe_ds__List_ListNode(item,None)
        if (self.h is None):
            self.h = x
        else:
            self.q.next = x
        self.q = x
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 + 1)
        _hx_local_1

    def push(self,item):
        x = haxe_ds__List_ListNode(item,self.h)
        self.h = x
        if (self.q is None):
            self.q = x
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 + 1)
        _hx_local_1

    def first(self):
        if (self.h is None):
            return None
        else:
            return self.h.item

    def last(self):
        if (self.q is None):
            return None
        else:
            return self.q.item

    def pop(self):
        if (self.h is None):
            return None
        x = self.h.item
        self.h = self.h.next
        if (self.h is None):
            self.q = None
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 - 1)
        _hx_local_1
        return x

    def isEmpty(self):
        return (self.h is None)

    def clear(self):
        self.h = None
        self.q = None
        self.length = 0

    def remove(self,v):
        prev = None
        l = self.h
        while (l is not None):
            if HxOverrides.eq(l.item,v):
                if (prev is None):
                    self.h = l.next
                else:
                    prev.next = l.next
                if (self.q == l):
                    self.q = prev
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.length
                _hx_local_0.length = (_hx_local_1 - 1)
                _hx_local_1
                return True
            prev = l
            l = l.next
        return False

    def iterator(self):
        return haxe_ds__List_ListIterator(self.h)

    def keyValueIterator(self):
        return haxe_ds__List_ListKeyValueIterator(self.h)

    def toString(self):
        s_b = python_lib_io_StringIO()
        first = True
        l = self.h
        s_b.write("{")
        while (l is not None):
            if first:
                first = False
            else:
                s_b.write(", ")
            s_b.write(Std.string(Std.string(l.item)))
            l = l.next
        s_b.write("}")
        return s_b.getvalue()

    def join(self,sep):
        s_b = python_lib_io_StringIO()
        first = True
        l = self.h
        while (l is not None):
            if first:
                first = False
            else:
                s_b.write(Std.string(sep))
            s_b.write(Std.string(l.item))
            l = l.next
        return s_b.getvalue()

    def filter(self,f):
        l2 = haxe_ds_List()
        l = self.h
        while (l is not None):
            v = l.item
            l = l.next
            if f(v):
                l2.add(v)
        return l2

    def map(self,f):
        b = haxe_ds_List()
        l = self.h
        while (l is not None):
            v = l.item
            l = l.next
            b.add(f(v))
        return b

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
        _hx_o.q = None
        _hx_o.length = None
haxe_ds_List._hx_class = haxe_ds_List
_hx_classes["haxe.ds.List"] = haxe_ds_List


