class HxOverrides:
    _hx_class_name = "HxOverrides"
    __slots__ = ()
    _hx_statics = ["iterator", "keyValueIterator", "eq", "stringOrNull", "shift", "pop", "push", "join", "filter", "map", "toUpperCase", "toLowerCase", "split", "length", "rshift", "modf", "mod", "arrayGet", "arraySet", "mapKwArgs", "reverseMapKwArgs"]

    @staticmethod
    def iterator(x):
        if isinstance(x,list):
            return haxe_iterators_ArrayIterator(x)
        return x.iterator()

    @staticmethod
    def keyValueIterator(x):
        if isinstance(x,list):
            return haxe_iterators_ArrayKeyValueIterator(x)
        return x.keyValueIterator()

    @staticmethod
    def eq(a,b):
        if (isinstance(a,list) or isinstance(b,list)):
            return a is b
        return (a == b)

    @staticmethod
    def stringOrNull(s):
        if (s is None):
            return "null"
        else:
            return s

    @staticmethod
    def shift(x):
        if isinstance(x,list):
            _this = x
            return (None if ((len(_this) == 0)) else _this.pop(0))
        return x.shift()

    @staticmethod
    def pop(x):
        if isinstance(x,list):
            _this = x
            return (None if ((len(_this) == 0)) else _this.pop())
        return x.pop()

    @staticmethod
    def push(x,e):
        if isinstance(x,list):
            _this = x
            _this.append(e)
            return len(_this)
        return x.push(e)

    @staticmethod
    def join(x,sep):
        if isinstance(x,list):
            return sep.join([python_Boot.toString1(x1,'') for x1 in x])
        return x.join(sep)

    @staticmethod
    def filter(x,f):
        if isinstance(x,list):
            return list(filter(f,x))
        return x.filter(f)

    @staticmethod
    def map(x,f):
        if isinstance(x,list):
            return list(map(f,x))
        return x.map(f)

    @staticmethod
    def toUpperCase(x):
        if isinstance(x,str):
            return x.upper()
        return x.toUpperCase()

    @staticmethod
    def toLowerCase(x):
        if isinstance(x,str):
            return x.lower()
        return x.toLowerCase()

    @staticmethod
    def split(x,delimiter):
        if isinstance(x,str):
            _this = x
            if (delimiter == ""):
                return list(_this)
            else:
                return _this.split(delimiter)
        return x.split(delimiter)

    @staticmethod
    def length(x):
        if isinstance(x,str):
            return len(x)
        elif isinstance(x,list):
            return len(x)
        return x.length

    @staticmethod
    def rshift(val,n):
        return ((val % 0x100000000) >> n)

    @staticmethod
    def modf(a,b):
        if (b == 0.0):
            return float('nan')
        elif (a < 0):
            if (b < 0):
                return -(-a % (-b))
            else:
                return -(-a % b)
        elif (b < 0):
            return a % (-b)
        else:
            return a % b

    @staticmethod
    def mod(a,b):
        if (a < 0):
            if (b < 0):
                return -(-a % (-b))
            else:
                return -(-a % b)
        elif (b < 0):
            return a % (-b)
        else:
            return a % b

    @staticmethod
    def arrayGet(a,i):
        if isinstance(a,list):
            x = a
            if ((i > -1) and ((i < len(x)))):
                return x[i]
            else:
                return None
        else:
            return a[i]

    @staticmethod
    def arraySet(a,i,v):
        if isinstance(a,list):
            x = a
            v1 = v
            l = len(x)
            while (l < i):
                x.append(None)
                l = (l + 1)
            if (l == i):
                x.append(v1)
            else:
                x[i] = v1
            return v1
        else:
            a[i] = v
            return v

    @staticmethod
    def mapKwArgs(a,v):
        a1 = _hx_AnonObject(python_Lib.anonToDict(a))
        k = python_HaxeIterator(iter(v.keys()))
        while k.hasNext():
            k1 = k.next()
            val = v.get(k1)
            if a1._hx_hasattr(k1):
                x = getattr(a1,k1)
                setattr(a1,val,x)
                delattr(a1,k1)
        return a1

    @staticmethod
    def reverseMapKwArgs(a,v):
        a1 = a.copy()
        k = python_HaxeIterator(iter(v.keys()))
        while k.hasNext():
            k1 = k.next()
            val = v.get(k1)
            if (val in a1):
                x = a1.get(val,None)
                a1[k1] = x
                del a1[val]
        return a1
HxOverrides._hx_class = HxOverrides
_hx_classes["HxOverrides"] = HxOverrides


