class haxe_SysTools:
    _hx_class_name = "haxe.SysTools"
    __slots__ = ()
    _hx_statics = ["winMetaCharacters", "quoteUnixArg", "quoteWinArg"]

    @staticmethod
    def quoteUnixArg(argument):
        if (argument == ""):
            return "''"
        _this = EReg("[^a-zA-Z0-9_@%+=:,./-]","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument)
        if (_this.matchObj is None):
            return argument
        return (("'" + HxOverrides.stringOrNull(StringTools.replace(argument,"'","'\"'\"'"))) + "'")

    @staticmethod
    def quoteWinArg(argument,escapeMetaCharacters):
        _this = EReg("^[^ \t\\\\\"]+$","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument)
        if (_this.matchObj is None):
            result_b = python_lib_io_StringIO()
            needquote = None
            startIndex = None
            if (((argument.find(" ") if ((startIndex is None)) else HxString.indexOfImpl(argument," ",startIndex))) == -1):
                startIndex = None
                needquote = (((argument.find("\t") if ((startIndex is None)) else HxString.indexOfImpl(argument,"\t",startIndex))) != -1)
            else:
                needquote = True
            needquote1 = (needquote or ((argument == "")))
            if needquote1:
                result_b.write("\"")
            bs_buf = StringBuf()
            _g = 0
            _g1 = len(argument)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _g2 = HxString.charCodeAt(argument,i)
                if (_g2 is None):
                    c = _g2
                    if (bs_buf.get_length() > 0):
                        result_b.write(Std.string(bs_buf.b.getvalue()))
                        bs_buf = StringBuf()
                    result_b.write("".join(map(chr,[c])))
                else:
                    _g3 = _g2
                    if (_g3 == 34):
                        bs = bs_buf.b.getvalue()
                        result_b.write(Std.string(bs))
                        result_b.write(Std.string(bs))
                        bs_buf = StringBuf()
                        result_b.write("\\\"")
                    elif (_g3 == 92):
                        bs_buf.b.write("\\")
                    else:
                        c1 = _g2
                        if (bs_buf.get_length() > 0):
                            result_b.write(Std.string(bs_buf.b.getvalue()))
                            bs_buf = StringBuf()
                        result_b.write("".join(map(chr,[c1])))
            result_b.write(Std.string(bs_buf.b.getvalue()))
            if needquote1:
                result_b.write(Std.string(bs_buf.b.getvalue()))
                result_b.write("\"")
            argument = result_b.getvalue()
        if escapeMetaCharacters:
            result_b = python_lib_io_StringIO()
            _g = 0
            _g1 = len(argument)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = HxString.charCodeAt(argument,i)
                if (python_internal_ArrayImpl.indexOf(haxe_SysTools.winMetaCharacters,c,None) >= 0):
                    result_b.write("".join(map(chr,[94])))
                result_b.write("".join(map(chr,[c])))
            return result_b.getvalue()
        else:
            return argument
haxe_SysTools._hx_class = haxe_SysTools
_hx_classes["haxe.SysTools"] = haxe_SysTools


