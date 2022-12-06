class hscript_CType(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.CType"
    _hx_constructs = ["CTPath", "CTFun", "CTAnon", "CTParent", "CTOpt", "CTNamed"]

    @staticmethod
    def CTPath(path,params = None):
        return hscript_CType("CTPath", 0, (path,params))

    @staticmethod
    def CTFun(args,ret):
        return hscript_CType("CTFun", 1, (args,ret))

    @staticmethod
    def CTAnon(fields):
        return hscript_CType("CTAnon", 2, (fields,))

    @staticmethod
    def CTParent(t):
        return hscript_CType("CTParent", 3, (t,))

    @staticmethod
    def CTOpt(t):
        return hscript_CType("CTOpt", 4, (t,))

    @staticmethod
    def CTNamed(n,t):
        return hscript_CType("CTNamed", 5, (n,t))
hscript_CType._hx_class = hscript_CType
_hx_classes["hscript.CType"] = hscript_CType

