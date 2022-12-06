class ValueType(Enum):
    __slots__ = ()
    _hx_class_name = "ValueType"
    _hx_constructs = ["TNull", "TInt", "TFloat", "TBool", "TObject", "TFunction", "TClass", "TEnum", "TUnknown"]

    @staticmethod
    def TClass(c):
        return ValueType("TClass", 6, (c,))

    @staticmethod
    def TEnum(e):
        return ValueType("TEnum", 7, (e,))
ValueType.TNull = ValueType("TNull", 0, ())
ValueType.TInt = ValueType("TInt", 1, ())
ValueType.TFloat = ValueType("TFloat", 2, ())
ValueType.TBool = ValueType("TBool", 3, ())
ValueType.TObject = ValueType("TObject", 4, ())
ValueType.TFunction = ValueType("TFunction", 5, ())
ValueType.TUnknown = ValueType("TUnknown", 8, ())
ValueType._hx_class = ValueType
_hx_classes["ValueType"] = ValueType


