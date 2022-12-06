class hscript__Checker_WithType(Enum):
    __slots__ = ()
    _hx_class_name = "hscript._Checker.WithType"
    _hx_constructs = ["NoValue", "Value", "WithType"]

    @staticmethod
    def WithType(t):
        return hscript__Checker_WithType("WithType", 2, (t,))
hscript__Checker_WithType.NoValue = hscript__Checker_WithType("NoValue", 0, ())
hscript__Checker_WithType.Value = hscript__Checker_WithType("Value", 1, ())
hscript__Checker_WithType._hx_class = hscript__Checker_WithType
_hx_classes["hscript._Checker.WithType"] = hscript__Checker_WithType

