class haxe_rtti_CType(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.rtti.CType"
    _hx_constructs = ["CUnknown", "CEnum", "CClass", "CTypedef", "CFunction", "CAnonymous", "CDynamic", "CAbstract"]

    @staticmethod
    def CEnum(name,params):
        return haxe_rtti_CType("CEnum", 1, (name,params))

    @staticmethod
    def CClass(name,params):
        return haxe_rtti_CType("CClass", 2, (name,params))

    @staticmethod
    def CTypedef(name,params):
        return haxe_rtti_CType("CTypedef", 3, (name,params))

    @staticmethod
    def CFunction(args,ret):
        return haxe_rtti_CType("CFunction", 4, (args,ret))

    @staticmethod
    def CAnonymous(fields):
        return haxe_rtti_CType("CAnonymous", 5, (fields,))

    @staticmethod
    def CDynamic(t = None):
        return haxe_rtti_CType("CDynamic", 6, (t,))

    @staticmethod
    def CAbstract(name,params):
        return haxe_rtti_CType("CAbstract", 7, (name,params))
haxe_rtti_CType.CUnknown = haxe_rtti_CType("CUnknown", 0, ())
haxe_rtti_CType._hx_class = haxe_rtti_CType
_hx_classes["haxe.rtti.CType"] = haxe_rtti_CType

