class haxe_macro_ComplexType(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ComplexType"
    _hx_constructs = ["TPath", "TFunction", "TAnonymous", "TParent", "TExtend", "TOptional", "TNamed", "TIntersection"]

    @staticmethod
    def TPath(p):
        return haxe_macro_ComplexType("TPath", 0, (p,))

    @staticmethod
    def TFunction(args,ret):
        return haxe_macro_ComplexType("TFunction", 1, (args,ret))

    @staticmethod
    def TAnonymous(fields):
        return haxe_macro_ComplexType("TAnonymous", 2, (fields,))

    @staticmethod
    def TParent(t):
        return haxe_macro_ComplexType("TParent", 3, (t,))

    @staticmethod
    def TExtend(p,fields):
        return haxe_macro_ComplexType("TExtend", 4, (p,fields))

    @staticmethod
    def TOptional(t):
        return haxe_macro_ComplexType("TOptional", 5, (t,))

    @staticmethod
    def TNamed(n,t):
        return haxe_macro_ComplexType("TNamed", 6, (n,t))

    @staticmethod
    def TIntersection(tl):
        return haxe_macro_ComplexType("TIntersection", 7, (tl,))
haxe_macro_ComplexType._hx_class = haxe_macro_ComplexType
_hx_classes["haxe.macro.ComplexType"] = haxe_macro_ComplexType

