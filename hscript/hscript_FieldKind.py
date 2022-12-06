class hscript_FieldKind(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.FieldKind"
    _hx_constructs = ["KFunction", "KVar"]

    @staticmethod
    def KFunction(f):
        return hscript_FieldKind("KFunction", 0, (f,))

    @staticmethod
    def KVar(v):
        return hscript_FieldKind("KVar", 1, (v,))
hscript_FieldKind._hx_class = hscript_FieldKind
_hx_classes["hscript.FieldKind"] = hscript_FieldKind

