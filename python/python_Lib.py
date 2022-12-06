class python_Lib:
    _hx_class_name = "python.Lib"
    __slots__ = ()
    _hx_statics = ["lineEnd", "get___name__", "print", "printString", "println", "dictToAnon", "anonToDict", "anonAsDict", "dictAsAnon", "toPythonIterable", "toHaxeIterable", "toHaxeIterator"]
    __name__ = None

    @staticmethod
    def get___name__():
        return __name__

    @staticmethod
    def print(v):
        python_Lib.printString(Std.string(v))

    @staticmethod
    def printString(_hx_str):
        encoding = "utf-8"
        if (encoding is None):
            encoding = "utf-8"
        python_lib_Sys.stdout.buffer.write(_hx_str.encode(encoding, "strict"))
        python_lib_Sys.stdout.flush()

    @staticmethod
    def println(v):
        _hx_str = Std.string(v)
        python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))

    @staticmethod
    def dictToAnon(v):
        return _hx_AnonObject(v.copy())

    @staticmethod
    def anonToDict(o):
        if isinstance(o,_hx_AnonObject):
            return o.__dict__.copy()
        else:
            return None

    @staticmethod
    def anonAsDict(o):
        if isinstance(o,_hx_AnonObject):
            return o.__dict__
        else:
            return None

    @staticmethod
    def dictAsAnon(d):
        return _hx_AnonObject(d)

    @staticmethod
    def toPythonIterable(it):
        def _hx_local_3():
            def _hx_local_2():
                it1 = HxOverrides.iterator(it)
                _hx_self = None
                def _hx_local_0():
                    if it1.hasNext():
                        return it1.next()
                    else:
                        raise haxe_Exception.thrown(StopIteration())
                def _hx_local_1():
                    return _hx_self
                this1 = _hx_AnonObject({'__next__': _hx_local_0, '__iter__': _hx_local_1})
                _hx_self = this1
                return _hx_self
            return _hx_AnonObject({'__iter__': _hx_local_2})
        return _hx_local_3()

    @staticmethod
    def toHaxeIterable(it):
        return python_HaxeIterable(it)

    @staticmethod
    def toHaxeIterator(it):
        return python_HaxeIterator(it)
python_Lib._hx_class = python_Lib
_hx_classes["python.Lib"] = python_Lib


