class haxe__Rest_Rest_Impl_:
    _hx_class_name = "haxe._Rest.Rest_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "of", "_new", "get", "toArray", "iterator", "keyValueIterator", "append", "prepend", "toString"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def of(array):
        this1 = array
        return this1

    @staticmethod
    def _new(array):
        this1 = array
        return this1

    @staticmethod
    def get(this1,index):
        return (this1[index] if index >= 0 and index < len(this1) else None)

    @staticmethod
    def toArray(this1):
        return list(this1)

    @staticmethod
    def iterator(this1):
        return haxe_iterators_RestIterator(this1)

    @staticmethod
    def keyValueIterator(this1):
        return haxe_iterators_RestKeyValueIterator(this1)

    @staticmethod
    def append(this1,item):
        result = list(this1)
        result.append(item)
        this1 = result
        return this1

    @staticmethod
    def prepend(this1,item):
        result = list(this1)
        result.insert(0, item)
        this1 = result
        return this1

    @staticmethod
    def toString(this1):
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in this1]))) + "]")
haxe__Rest_Rest_Impl_._hx_class = haxe__Rest_Rest_Impl_
_hx_classes["haxe._Rest.Rest_Impl_"] = haxe__Rest_Rest_Impl_


