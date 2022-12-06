class python__KwArgs_KwArgs_Impl_:
    _hx_class_name = "python._KwArgs.KwArgs_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "toDict", "toDictHelper", "fromDict", "fromT", "typed", "get"]

    @staticmethod
    def _new(d):
        this1 = d
        return this1

    @staticmethod
    def toDict(this1):
        return python__KwArgs_KwArgs_Impl_.toDictHelper(this1,None)

    @staticmethod
    def toDictHelper(this1,x):
        return this1

    @staticmethod
    def fromDict(d):
        this1 = d
        return this1

    @staticmethod
    def fromT(d):
        this1 = python_Lib.anonAsDict(d)
        return this1

    @staticmethod
    def typed(this1):
        return _hx_AnonObject(python__KwArgs_KwArgs_Impl_.toDictHelper(this1,None))

    @staticmethod
    def get(this1,key,_hx_def):
        return this1.get(key,_hx_def)
python__KwArgs_KwArgs_Impl_._hx_class = python__KwArgs_KwArgs_Impl_
_hx_classes["python._KwArgs.KwArgs_Impl_"] = python__KwArgs_KwArgs_Impl_


