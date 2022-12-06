class haxe_ds__HashMap_HashMap_Impl_:
    _hx_class_name = "haxe.ds._HashMap.HashMap_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "set", "get", "exists", "remove", "keys", "copy", "iterator", "keyValueIterator", "clear"]

    @staticmethod
    def _new():
        this1 = haxe_ds__HashMap_HashMapData()
        return this1

    @staticmethod
    def set(this1,k,v):
        this1.keys.set(k.hashCode(),k)
        this1.values.set(k.hashCode(),v)

    @staticmethod
    def get(this1,k):
        _this = this1.values
        key = k.hashCode()
        return _this.h.get(key,None)

    @staticmethod
    def exists(this1,k):
        _this = this1.values
        return (k.hashCode() in _this.h)

    @staticmethod
    def remove(this1,k):
        this1.values.remove(k.hashCode())
        return this1.keys.remove(k.hashCode())

    @staticmethod
    def keys(this1):
        return this1.keys.iterator()

    @staticmethod
    def copy(this1):
        copied = haxe_ds__HashMap_HashMapData()
        copied.keys = this1.keys.copy()
        copied.values = this1.values.copy()
        return copied

    @staticmethod
    def iterator(this1):
        return this1.values.iterator()

    @staticmethod
    def keyValueIterator(this1):
        return haxe_iterators_HashMapKeyValueIterator(this1)

    @staticmethod
    def clear(this1):
        this1.keys.h.clear()
        this1.values.h.clear()
haxe_ds__HashMap_HashMap_Impl_._hx_class = haxe_ds__HashMap_HashMap_Impl_
_hx_classes["haxe.ds._HashMap.HashMap_Impl_"] = haxe_ds__HashMap_HashMap_Impl_


