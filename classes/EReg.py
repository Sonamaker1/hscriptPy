class EReg:
    _hx_class_name = "EReg"
    __slots__ = ("pattern", "matchObj", "_hx_global")
    _hx_fields = ["pattern", "matchObj", "global"]
    _hx_methods = ["match", "matched", "matchedLeft", "matchedRight", "matchedPos", "matchSub", "split", "replace", "map"]
    _hx_statics = ["escape"]

    def __init__(self,r,opt):
        self.matchObj = None
        self._hx_global = False
        options = 0
        _g = 0
        _g1 = len(opt)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = (-1 if ((i >= len(opt))) else ord(opt[i]))
            if (c == 109):
                options = (options | python_lib_Re.M)
            if (c == 105):
                options = (options | python_lib_Re.I)
            if (c == 115):
                options = (options | python_lib_Re.S)
            if (c == 117):
                options = (options | python_lib_Re.U)
            if (c == 103):
                self._hx_global = True
        self.pattern = python_lib_Re.compile(r,options)

    def match(self,s):
        self.matchObj = python_lib_Re.search(self.pattern,s)
        return (self.matchObj is not None)

    def matched(self,n):
        return self.matchObj.group(n)

    def matchedLeft(self):
        return HxString.substr(self.matchObj.string,0,self.matchObj.start())

    def matchedRight(self):
        return HxString.substr(self.matchObj.string,self.matchObj.end(),None)

    def matchedPos(self):
        return _hx_AnonObject({'pos': self.matchObj.start(), 'len': (self.matchObj.end() - self.matchObj.start())})

    def matchSub(self,s,pos,_hx_len = None):
        if (_hx_len is None):
            _hx_len = -1
        if (_hx_len != -1):
            self.matchObj = self.pattern.search(s,pos,(pos + _hx_len))
        else:
            self.matchObj = self.pattern.search(s,pos)
        return (self.matchObj is not None)

    def split(self,s):
        if self._hx_global:
            ret = []
            lastEnd = 0
            x = python_HaxeIterator(python_lib_Re.finditer(self.pattern,s))
            while x.hasNext():
                x1 = x.next()
                x2 = HxString.substring(s,lastEnd,x1.start())
                ret.append(x2)
                lastEnd = x1.end()
            x = HxString.substr(s,lastEnd,None)
            ret.append(x)
            return ret
        else:
            self.matchObj = python_lib_Re.search(self.pattern,s)
            if (self.matchObj is None):
                return [s]
            else:
                return [HxString.substring(s,0,self.matchObj.start()), HxString.substr(s,self.matchObj.end(),None)]

    def replace(self,s,by):
        _this = by.split("$$")
        by = "_hx_#repl#__".join([python_Boot.toString1(x1,'') for x1 in _this])
        def _hx_local_0(x):
            res = by
            g = x.groups()
            _g = 0
            _g1 = len(g)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                gs = g[i]
                if (gs is None):
                    continue
                delimiter = ("$" + HxOverrides.stringOrNull(str((i + 1))))
                _this = (list(res) if ((delimiter == "")) else res.split(delimiter))
                res = gs.join([python_Boot.toString1(x1,'') for x1 in _this])
            _this = res.split("_hx_#repl#__")
            res = "$".join([python_Boot.toString1(x1,'') for x1 in _this])
            return res
        replace = _hx_local_0
        return python_lib_Re.sub(self.pattern,replace,s,(0 if (self._hx_global) else 1))

    def map(self,s,f):
        buf_b = python_lib_io_StringIO()
        pos = 0
        right = s
        cur = self
        while (pos < len(s)):
            if (self.matchObj is None):
                self.matchObj = python_lib_Re.search(self.pattern,s)
            else:
                self.matchObj = self.matchObj.re.search(s,pos)
            if (self.matchObj is None):
                break
            pos1 = self.matchObj.end()
            curPos_pos = cur.matchObj.start()
            curPos_len = (cur.matchObj.end() - cur.matchObj.start())
            buf_b.write(Std.string(HxString.substr(HxString.substr(cur.matchObj.string,0,cur.matchObj.start()),pos,None)))
            buf_b.write(Std.string(f(cur)))
            right = HxString.substr(cur.matchObj.string,cur.matchObj.end(),None)
            if (not self._hx_global):
                buf_b.write(Std.string(right))
                return buf_b.getvalue()
            if (curPos_len == 0):
                buf_b.write(Std.string(("" if (((pos1 < 0) or ((pos1 >= len(s))))) else s[pos1])))
                right = HxString.substr(right,1,None)
                pos = (pos1 + 1)
            else:
                pos = pos1
        buf_b.write(Std.string(right))
        return buf_b.getvalue()

    @staticmethod
    def escape(s):
        return python_lib_Re.escape(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.pattern = None
        _hx_o.matchObj = None
        _hx_o._hx_global = None
EReg._hx_class = EReg
_hx_classes["EReg"] = EReg


