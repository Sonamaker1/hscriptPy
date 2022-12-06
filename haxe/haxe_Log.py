class haxe_Log:
    _hx_class_name = "haxe.Log"
    __slots__ = ()
    _hx_statics = ["formatOutput", "trace"]

    @staticmethod
    def formatOutput(v,infos):
        _hx_str = Std.string(v)
        if (infos is None):
            return _hx_str
        pstr = ((HxOverrides.stringOrNull(infos.fileName) + ":") + Std.string(infos.lineNumber))
        if (Reflect.field(infos,"customParams") is not None):
            _g = 0
            _g1 = Reflect.field(infos,"customParams")
            while (_g < len(_g1)):
                v = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                _hx_str = (("null" if _hx_str is None else _hx_str) + ((", " + Std.string(v))))
        return ((("null" if pstr is None else pstr) + ": ") + ("null" if _hx_str is None else _hx_str))

    @staticmethod
    def trace(v,infos = None):
        _hx_str = haxe_Log.formatOutput(v,infos)
        str1 = Std.string(_hx_str)
        python_Lib.printString((("" + ("null" if str1 is None else str1)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))
haxe_Log._hx_class = haxe_Log
_hx_classes["haxe.Log"] = haxe_Log


