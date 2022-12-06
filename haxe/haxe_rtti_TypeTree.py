class haxe_rtti_TypeTree(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.rtti.TypeTree"
    _hx_constructs = ["TPackage", "TClassdecl", "TEnumdecl", "TTypedecl", "TAbstractdecl"]

    @staticmethod
    def TPackage(name,full,subs):
        return haxe_rtti_TypeTree("TPackage", 0, (name,full,subs))

    @staticmethod
    def TClassdecl(c):
        return haxe_rtti_TypeTree("TClassdecl", 1, (c,))

    @staticmethod
    def TEnumdecl(e):
        return haxe_rtti_TypeTree("TEnumdecl", 2, (e,))

    @staticmethod
    def TTypedecl(t):
        return haxe_rtti_TypeTree("TTypedecl", 3, (t,))

    @staticmethod
    def TAbstractdecl(a):
        return haxe_rtti_TypeTree("TAbstractdecl", 4, (a,))
haxe_rtti_TypeTree._hx_class = haxe_rtti_TypeTree
_hx_classes["haxe.rtti.TypeTree"] = haxe_rtti_TypeTree


