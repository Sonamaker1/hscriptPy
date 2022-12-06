class python__NativeIterable_NativeIterable_Impl_:
    _hx_class_name = "python._NativeIterable.NativeIterable_Impl_"
    __slots__ = ()
    _hx_statics = ["toHaxeIterable", "iterator"]

    @staticmethod
    def toHaxeIterable(this1):
        return python_HaxeIterable(this1)

    @staticmethod
    def iterator(this1):
        return python_HaxeIterator(this1.__iter__())
python__NativeIterable_NativeIterable_Impl_._hx_class = python__NativeIterable_NativeIterable_Impl_
_hx_classes["python._NativeIterable.NativeIterable_Impl_"] = python__NativeIterable_NativeIterable_Impl_


