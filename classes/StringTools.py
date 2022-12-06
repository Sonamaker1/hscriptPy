class StringTools:
    _hx_class_name = "StringTools"
    __slots__ = ()
    _hx_statics = ["urlEncode", "urlDecode", "htmlEscape", "htmlUnescape", "contains", "startsWith", "endsWith", "isSpace", "ltrim", "rtrim", "trim", "lpad", "rpad", "replace", "hex", "fastCodeAt", "unsafeCodeAt", "iterator", "keyValueIterator", "isEof", "quoteUnixArg", "winMetaCharacters", "quoteWinArg"]

    @staticmethod
    def urlEncode(s):
        return python_lib_urllib_Parse.quote(s,"")

    @staticmethod
    def urlDecode(s):
        return python_lib_urllib_Parse.unquote(s)

    @staticmethod
    def htmlEscape(s,quotes = None):
        buf_b = python_lib_io_StringIO()
        _g_offset = 0
        _g_s = s
        while (_g_offset < len(_g_s)):
            index = _g_offset
            _g_offset = (_g_offset + 1)
            code = ord(_g_s[index])
            code1 = code
            if (code1 == 34):
                if quotes:
                    buf_b.write("&quot;")
                else:
                    buf_b.write("".join(map(chr,[code])))
            elif (code1 == 38):
                buf_b.write("&amp;")
            elif (code1 == 39):
                if quotes:
                    buf_b.write("&#039;")
                else:
                    buf_b.write("".join(map(chr,[code])))
            elif (code1 == 60):
                buf_b.write("&lt;")
            elif (code1 == 62):
                buf_b.write("&gt;")
            else:
                buf_b.write("".join(map(chr,[code])))
        return buf_b.getvalue()

    @staticmethod
    def htmlUnescape(s):
        _this = s.split("&gt;")
        _this1 = ">".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&lt;")
        _this1 = "<".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&quot;")
        _this1 = "\"".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&#039;")
        _this1 = "'".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&amp;")
        return "&".join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def contains(s,value):
        startIndex = None
        return (((s.find(value) if ((startIndex is None)) else HxString.indexOfImpl(s,value,startIndex))) != -1)

    @staticmethod
    def startsWith(s,start):
        return s.startswith(start)

    @staticmethod
    def endsWith(s,end):
        return s.endswith(end)

    @staticmethod
    def isSpace(s,pos):
        if (((len(s) == 0) or ((pos < 0))) or ((pos >= len(s)))):
            return False
        c = HxString.charCodeAt(s,pos)
        if (not (((c > 8) and ((c < 14))))):
            return (c == 32)
        else:
            return True

    @staticmethod
    def ltrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,r)):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,r,(l - r))
        else:
            return s

    @staticmethod
    def rtrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,((l - r) - 1))):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,0,(l - r))
        else:
            return s

    @staticmethod
    def trim(s):
        return StringTools.ltrim(StringTools.rtrim(s))

    @staticmethod
    def lpad(s,c,l):
        if (len(c) <= 0):
            return s
        buf = StringBuf()
        l = (l - len(s))
        while (buf.get_length() < l):
            s1 = Std.string(c)
            buf.b.write(s1)
        s1 = Std.string(s)
        buf.b.write(s1)
        return buf.b.getvalue()

    @staticmethod
    def rpad(s,c,l):
        if (len(c) <= 0):
            return s
        buf = StringBuf()
        s1 = Std.string(s)
        buf.b.write(s1)
        while (buf.get_length() < l):
            s = Std.string(c)
            buf.b.write(s)
        return buf.b.getvalue()

    @staticmethod
    def replace(s,sub,by):
        _this = (list(s) if ((sub == "")) else s.split(sub))
        return by.join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def hex(n,digits = None):
        s = ""
        hexChars = "0123456789ABCDEF"
        while True:
            index = (n & 15)
            s = (HxOverrides.stringOrNull((("" if (((index < 0) or ((index >= len(hexChars))))) else hexChars[index]))) + ("null" if s is None else s))
            n = HxOverrides.rshift(n, 4)
            if (not ((n > 0))):
                break
        if ((digits is not None) and ((len(s) < digits))):
            diff = (digits - len(s))
            _g = 0
            _g1 = diff
            while (_g < _g1):
                _ = _g
                _g = (_g + 1)
                s = ("0" + ("null" if s is None else s))
        return s

    @staticmethod
    def fastCodeAt(s,index):
        if (index >= len(s)):
            return -1
        else:
            return ord(s[index])

    @staticmethod
    def unsafeCodeAt(s,index):
        return ord(s[index])

    @staticmethod
    def iterator(s):
        return haxe_iterators_StringIterator(s)

    @staticmethod
    def keyValueIterator(s):
        return haxe_iterators_StringKeyValueIterator(s)

    @staticmethod
    def isEof(c):
        return (c == -1)

    @staticmethod
    def quoteUnixArg(argument):
        if (argument == ""):
            return "''"
        else:
            _this = EReg("[^a-zA-Z0-9_@%+=:,./-]","")
            _this.matchObj = python_lib_Re.search(_this.pattern,argument)
            if (_this.matchObj is None):
                return argument
            else:
                return (("'" + HxOverrides.stringOrNull(StringTools.replace(argument,"'","'\"'\"'"))) + "'")

    @staticmethod
    def quoteWinArg(argument,escapeMetaCharacters):
        argument1 = argument
        _this = EReg("^[^ \t\\\\\"]+$","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument1)
        if (_this.matchObj is None):
            result_b = python_lib_io_StringIO()
            needquote = None
            startIndex = None
            if (((argument1.find(" ") if ((startIndex is None)) else HxString.indexOfImpl(argument1," ",startIndex))) == -1):
                startIndex = None
                needquote = (((argument1.find("\t") if ((startIndex is None)) else HxString.indexOfImpl(argument1,"\t",startIndex))) != -1)
            else:
                needquote = True
            needquote1 = (needquote or ((argument1 == "")))
            if needquote1:
                result_b.write("\"")
            bs_buf = StringBuf()
            _g = 0
            _g1 = len(argument1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _g2 = HxString.charCodeAt(argument1,i)
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
            argument1 = result_b.getvalue()
        if escapeMetaCharacters:
            result_b = python_lib_io_StringIO()
            _g = 0
            _g1 = len(argument1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = HxString.charCodeAt(argument1,i)
                if (python_internal_ArrayImpl.indexOf(haxe_SysTools.winMetaCharacters,c,None) >= 0):
                    result_b.write("".join(map(chr,[94])))
                result_b.write("".join(map(chr,[c])))
            return result_b.getvalue()
        else:
            return argument1
StringTools._hx_class = StringTools
_hx_classes["StringTools"] = StringTools


