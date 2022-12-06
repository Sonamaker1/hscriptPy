class haxe_rtti_Rights(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.rtti.Rights"
    _hx_constructs = ["RNormal", "RNo", "RCall", "RMethod", "RDynamic", "RInline"]

    @staticmethod
    def RCall(m):
        return haxe_rtti_Rights("RCall", 2, (m,))
haxe_rtti_Rights.RNormal = haxe_rtti_Rights("RNormal", 0, ())
haxe_rtti_Rights.RNo = haxe_rtti_Rights("RNo", 1, ())
haxe_rtti_Rights.RMethod = haxe_rtti_Rights("RMethod", 3, ())
haxe_rtti_Rights.RDynamic = haxe_rtti_Rights("RDynamic", 4, ())
haxe_rtti_Rights.RInline = haxe_rtti_Rights("RInline", 5, ())
haxe_rtti_Rights._hx_class = haxe_rtti_Rights
_hx_classes["haxe.rtti.Rights"] = haxe_rtti_Rights

