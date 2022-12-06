class haxe_macro_ImportMode(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ImportMode"
    _hx_constructs = ["INormal", "IAsName", "IAll"]

    @staticmethod
    def IAsName(alias):
        return haxe_macro_ImportMode("IAsName", 1, (alias,))
haxe_macro_ImportMode.INormal = haxe_macro_ImportMode("INormal", 0, ())
haxe_macro_ImportMode.IAll = haxe_macro_ImportMode("IAll", 2, ())
haxe_macro_ImportMode._hx_class = haxe_macro_ImportMode
_hx_classes["haxe.macro.ImportMode"] = haxe_macro_ImportMode

