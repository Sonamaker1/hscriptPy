class hscript_TType(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.TType"
    _hx_constructs = ["TMono", "TVoid", "TInt", "TFloat", "TBool", "TDynamic", "TParam", "TUnresolved", "TNull", "TInst", "TEnum", "TType", "TAbstract", "TFun", "TAnon", "TLazy"]

    @staticmethod
    def TMono(r):
        return hscript_TType("TMono", 0, (r,))

    @staticmethod
    def TParam(name):
        return hscript_TType("TParam", 6, (name,))

    @staticmethod
    def TUnresolved(name):
        return hscript_TType("TUnresolved", 7, (name,))

    @staticmethod
    def TNull(t):
        return hscript_TType("TNull", 8, (t,))

    @staticmethod
    def TInst(c,args):
        return hscript_TType("TInst", 9, (c,args))

    @staticmethod
    def TEnum(e,args):
        return hscript_TType("TEnum", 10, (e,args))

    @staticmethod
    def TType(t,args):
        return hscript_TType("TType", 11, (t,args))

    @staticmethod
    def TAbstract(a,args):
        return hscript_TType("TAbstract", 12, (a,args))

    @staticmethod
    def TFun(args,ret):
        return hscript_TType("TFun", 13, (args,ret))

    @staticmethod
    def TAnon(fields):
        return hscript_TType("TAnon", 14, (fields,))

    @staticmethod
    def TLazy(f):
        return hscript_TType("TLazy", 15, (f,))
hscript_TType.TVoid = hscript_TType("TVoid", 1, ())
hscript_TType.TInt = hscript_TType("TInt", 2, ())
hscript_TType.TFloat = hscript_TType("TFloat", 3, ())
hscript_TType.TBool = hscript_TType("TBool", 4, ())
hscript_TType.TDynamic = hscript_TType("TDynamic", 5, ())
hscript_TType._hx_class = hscript_TType
_hx_classes["hscript.TType"] = hscript_TType

