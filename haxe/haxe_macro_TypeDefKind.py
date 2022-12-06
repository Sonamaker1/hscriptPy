class haxe_macro_TypeDefKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.TypeDefKind"
    _hx_constructs = ["TDEnum", "TDStructure", "TDClass", "TDAlias", "TDAbstract", "TDField"]

    @staticmethod
    def TDClass(superClass = None,interfaces= None,isInterface= None,isFinal= None,isAbstract= None):
        return haxe_macro_TypeDefKind("TDClass", 2, (superClass,interfaces,isInterface,isFinal,isAbstract))

    @staticmethod
    def TDAlias(t):
        return haxe_macro_TypeDefKind("TDAlias", 3, (t,))

    @staticmethod
    def TDAbstract(tthis,_hx_from = None,to= None):
        return haxe_macro_TypeDefKind("TDAbstract", 4, (tthis,_hx_from,to))

    @staticmethod
    def TDField(kind,access = None):
        return haxe_macro_TypeDefKind("TDField", 5, (kind,access))
haxe_macro_TypeDefKind.TDEnum = haxe_macro_TypeDefKind("TDEnum", 0, ())
haxe_macro_TypeDefKind.TDStructure = haxe_macro_TypeDefKind("TDStructure", 1, ())
haxe_macro_TypeDefKind._hx_class = haxe_macro_TypeDefKind
_hx_classes["haxe.macro.TypeDefKind"] = haxe_macro_TypeDefKind


