class hscript_CTypedecl(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.CTypedecl"
    _hx_constructs = ["CTClass", "CTEnum", "CTTypedef", "CTAlias", "CTAbstract"]

    @staticmethod
    def CTClass(c):
        return hscript_CTypedecl("CTClass", 0, (c,))

    @staticmethod
    def CTEnum(e):
        return hscript_CTypedecl("CTEnum", 1, (e,))

    @staticmethod
    def CTTypedef(t):
        return hscript_CTypedecl("CTTypedef", 2, (t,))

    @staticmethod
    def CTAlias(t):
        return hscript_CTypedecl("CTAlias", 3, (t,))

    @staticmethod
    def CTAbstract(a):
        return hscript_CTypedecl("CTAbstract", 4, (a,))
hscript_CTypedecl._hx_class = hscript_CTypedecl
_hx_classes["hscript.CTypedecl"] = hscript_CTypedecl


