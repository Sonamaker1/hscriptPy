class haxe_ds_StringMap:
    _hx_class_name = "haxe.ds.StringMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        has = (key in self.h)
        if has:
            del self.h[key]
        return has

    def keys(self):
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_StringMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            value = self.h.get(key1,None)
            copied.h[key1] = value
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(i1))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_StringMap._hx_class = haxe_ds_StringMap
_hx_classes["haxe.ds.StringMap"] = haxe_ds_StringMap


