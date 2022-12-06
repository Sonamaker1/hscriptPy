class Lambda:
    _hx_class_name = "Lambda"
    __slots__ = ()
    _hx_statics = ["array", "list", "map", "mapi", "flatten", "flatMap", "has", "exists", "foreach", "iter", "filter", "fold", "count", "empty", "indexOf", "find", "concat"]

    @staticmethod
    def array(it):
        a = list()
        i = HxOverrides.iterator(it)
        while i.hasNext():
            i1 = i.next()
            a.append(i1)
        return a

    @staticmethod
    def list(it):
        l = haxe_ds_List()
        i = HxOverrides.iterator(it)
        while i.hasNext():
            i1 = i.next()
            l.add(i1)
        return l

    @staticmethod
    def map(it,f):
        l = haxe_ds_List()
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            l.add(f(x1))
        return l

    @staticmethod
    def mapi(it,f):
        l = haxe_ds_List()
        i = 0
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            tmp = i
            i = (i + 1)
            l.add(f(tmp,x1))
        return l

    @staticmethod
    def flatten(it):
        l = haxe_ds_List()
        e = HxOverrides.iterator(it)
        while e.hasNext():
            e1 = e.next()
            x = HxOverrides.iterator(e1)
            while x.hasNext():
                x1 = x.next()
                l.add(x1)
        return l

    @staticmethod
    def flatMap(it,f):
        return Lambda.flatten(Lambda.map(it,f))

    @staticmethod
    def has(it,elt):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if HxOverrides.eq(x1,elt):
                return True
        return False

    @staticmethod
    def exists(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if f(x1):
                return True
        return False

    @staticmethod
    def foreach(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if (not f(x1)):
                return False
        return True

    @staticmethod
    def iter(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            f(x1)

    @staticmethod
    def filter(it,f):
        l = haxe_ds_List()
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if f(x1):
                l.add(x1)
        return l

    @staticmethod
    def fold(it,f,first):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            first = f(x1,first)
        return first

    @staticmethod
    def count(it,pred = None):
        n = 0
        if (pred is None):
            _ = HxOverrides.iterator(it)
            while _.hasNext():
                _1 = _.next()
                n = (n + 1)
        else:
            x = HxOverrides.iterator(it)
            while x.hasNext():
                x1 = x.next()
                if pred(x1):
                    n = (n + 1)
        return n

    @staticmethod
    def empty(it):
        return (not HxOverrides.iterator(it).hasNext())

    @staticmethod
    def indexOf(it,v):
        i = 0
        v2 = HxOverrides.iterator(it)
        while v2.hasNext():
            v21 = v2.next()
            if HxOverrides.eq(v,v21):
                return i
            i = (i + 1)
        return -1

    @staticmethod
    def find(it,f):
        v = HxOverrides.iterator(it)
        while v.hasNext():
            v1 = v.next()
            if f(v1):
                return v1
        return None

    @staticmethod
    def concat(a,b):
        l = haxe_ds_List()
        x = HxOverrides.iterator(a)
        while x.hasNext():
            x1 = x.next()
            l.add(x1)
        x = HxOverrides.iterator(b)
        while x.hasNext():
            x1 = x.next()
            l.add(x1)
        return l
Lambda._hx_class = Lambda
_hx_classes["Lambda"] = Lambda


