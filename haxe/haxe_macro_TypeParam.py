class haxe_macro_TypeParam(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.TypeParam"
    _hx_constructs = ["TPType", "TPExpr"]

    @staticmethod
    def TPType(t):
        return haxe_macro_TypeParam("TPType", 0, (t,))

    @staticmethod
    def TPExpr(e):
        return haxe_macro_TypeParam("TPExpr", 1, (e,))
haxe_macro_TypeParam._hx_class = haxe_macro_TypeParam
_hx_classes["haxe.macro.TypeParam"] = haxe_macro_TypeParam

