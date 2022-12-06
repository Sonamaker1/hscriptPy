class haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_:
    _hx_class_name = "haxe.ds._ReadOnlyArray.ReadOnlyArray_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "get", "concat"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def get(this1,i):
        return (this1[i] if i >= 0 and i < len(this1) else None)

    @staticmethod
    def concat(this1,a):
        return (this1 + a)
haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_._hx_class = haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_
_hx_classes["haxe.ds._ReadOnlyArray.ReadOnlyArray_Impl_"] = haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_


