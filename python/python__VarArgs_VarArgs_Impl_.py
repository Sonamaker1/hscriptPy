class python__VarArgs_VarArgs_Impl_:
    _hx_class_name = "python._VarArgs.VarArgs_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "raw", "toArray", "fromArray"]

    @staticmethod
    def _new(d):
        this1 = d
        return this1

    @staticmethod
    def raw(this1):
        return this1

    @staticmethod
    def toArray(this1):
        if (not Std.isOfType(this1,list)):
            return list(this1)
        else:
            return this1

    @staticmethod
    def fromArray(d):
        this1 = d
        return this1
python__VarArgs_VarArgs_Impl_._hx_class = python__VarArgs_VarArgs_Impl_
_hx_classes["python._VarArgs.VarArgs_Impl_"] = python__VarArgs_VarArgs_Impl_


