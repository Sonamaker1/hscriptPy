class haxe_NativeStackTrace:
    _hx_class_name = "haxe.NativeStackTrace"
    __slots__ = ()
    _hx_statics = ["saveStack", "callStack", "exceptionStack", "toHaxe"]

    @staticmethod
    def saveStack(exception):
        pass

    @staticmethod
    def callStack():
        infos = python_lib_Traceback.extract_stack()
        if (len(infos) != 0):
            infos.pop()
        infos.reverse()
        return infos

    @staticmethod
    def exceptionStack():
        exc = python_lib_Sys.exc_info()
        if (exc[2] is not None):
            infos = python_lib_Traceback.extract_tb(exc[2])
            infos.reverse()
            return infos
        else:
            return []

    @staticmethod
    def toHaxe(native,skip = None):
        if (skip is None):
            skip = 0
        stack = []
        _g = 0
        _g1 = len(native)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (skip > i):
                continue
            elem = (native[i] if i >= 0 and i < len(native) else None)
            x = haxe_StackItem.FilePos(haxe_StackItem.Method(None,elem[2]),elem[0],elem[1])
            stack.append(x)
        return stack
haxe_NativeStackTrace._hx_class = haxe_NativeStackTrace
_hx_classes["haxe.NativeStackTrace"] = haxe_NativeStackTrace


