class haxe_Exception(Exception):
    _hx_class_name = "haxe.Exception"
    __slots__ = ("_hx___exceptionStack", "_hx___nativeStack", "_hx___skipStack", "_hx___nativeException", "_hx___previousException")
    _hx_fields = ["__exceptionStack", "__nativeStack", "__skipStack", "__nativeException", "__previousException"]
    _hx_methods = ["unwrap", "toString", "details", "__shiftStack", "get_message", "get_previous", "get_native", "get_stack"]
    _hx_statics = ["caught", "thrown"]
    _hx_interfaces = []
    _hx_super = Exception


    def __init__(self,message,previous = None,native = None):
        self._hx___previousException = None
        self._hx___nativeException = None
        self._hx___nativeStack = None
        self._hx___exceptionStack = None
        self._hx___skipStack = 0
        super().__init__(message)
        self._hx___previousException = previous
        if ((native is not None) and Std.isOfType(native,BaseException)):
            self._hx___nativeException = native
            self._hx___nativeStack = haxe_NativeStackTrace.exceptionStack()
        else:
            self._hx___nativeException = self
            infos = python_lib_Traceback.extract_stack()
            if (len(infos) != 0):
                infos.pop()
            infos.reverse()
            self._hx___nativeStack = infos

    def unwrap(self):
        return self._hx___nativeException

    def toString(self):
        return self.get_message()

    def details(self):
        if (self.get_previous() is None):
            tmp = ("Exception: " + HxOverrides.stringOrNull(self.toString()))
            tmp1 = self.get_stack()
            return (("null" if tmp is None else tmp) + HxOverrides.stringOrNull((("null" if ((tmp1 is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp1)))))
        else:
            result = ""
            e = self
            prev = None
            while (e is not None):
                if (prev is None):
                    result1 = ("Exception: " + HxOverrides.stringOrNull(e.get_message()))
                    tmp = e.get_stack()
                    result = ((("null" if result1 is None else result1) + HxOverrides.stringOrNull((("null" if ((tmp is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp))))) + ("null" if result is None else result))
                else:
                    prevStack = haxe__CallStack_CallStack_Impl_.subtract(e.get_stack(),prev.get_stack())
                    result = (((("Exception: " + HxOverrides.stringOrNull(e.get_message())) + HxOverrides.stringOrNull((("null" if ((prevStack is None)) else haxe__CallStack_CallStack_Impl_.toString(prevStack))))) + "\n\nNext ") + ("null" if result is None else result))
                prev = e
                e = e.get_previous()
            return result

    def _hx___shiftStack(self):
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def get_message(self):
        return str(self)

    def get_previous(self):
        return self._hx___previousException

    def get_native(self):
        return self._hx___nativeException

    def get_stack(self):
        _g = self._hx___exceptionStack
        if (_g is None):
            def _hx_local_1():
                def _hx_local_0():
                    self._hx___exceptionStack = haxe_NativeStackTrace.toHaxe(self._hx___nativeStack,self._hx___skipStack)
                    return self._hx___exceptionStack
                return _hx_local_0()
            return _hx_local_1()
        else:
            s = _g
            return s

    @staticmethod
    def caught(value):
        if Std.isOfType(value,haxe_Exception):
            return value
        elif Std.isOfType(value,BaseException):
            return haxe_Exception(str(value),None,value)
        else:
            return haxe_ValueException(value,None,value)

    @staticmethod
    def thrown(value):
        if Std.isOfType(value,haxe_Exception):
            return value.get_native()
        elif Std.isOfType(value,BaseException):
            return value
        else:
            e = haxe_ValueException(value)
            e._hx___skipStack = (e._hx___skipStack + 1)
            return e

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o._hx___exceptionStack = None
        _hx_o._hx___nativeStack = None
        _hx_o._hx___skipStack = None
        _hx_o._hx___nativeException = None
        _hx_o._hx___previousException = None
haxe_Exception._hx_class = haxe_Exception
_hx_classes["haxe.Exception"] = haxe_Exception


