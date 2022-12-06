class haxe_macro_DisplayKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.DisplayKind"
    _hx_constructs = ["DKCall", "DKDot", "DKStructure", "DKMarked", "DKPattern"]

    @staticmethod
    def DKPattern(outermost):
        return haxe_macro_DisplayKind("DKPattern", 4, (outermost,))
haxe_macro_DisplayKind.DKCall = haxe_macro_DisplayKind("DKCall", 0, ())
haxe_macro_DisplayKind.DKDot = haxe_macro_DisplayKind("DKDot", 1, ())
haxe_macro_DisplayKind.DKStructure = haxe_macro_DisplayKind("DKStructure", 2, ())
haxe_macro_DisplayKind.DKMarked = haxe_macro_DisplayKind("DKMarked", 3, ())
haxe_macro_DisplayKind._hx_class = haxe_macro_DisplayKind
_hx_classes["haxe.macro.DisplayKind"] = haxe_macro_DisplayKind

