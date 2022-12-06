class hscript_Bytes:
    _hx_class_name = "hscript.Bytes"
    __slots__ = ("bin", "bout", "pin", "hstrings", "strings", "nstrings")
    _hx_fields = ["bin", "bout", "pin", "hstrings", "strings", "nstrings"]
    _hx_methods = ["doEncodeString", "doDecodeString", "doEncodeInt", "doEncodeConst", "doDecodeInt", "doDecodeConst", "doEncode", "doDecode"]
    _hx_statics = ["encode", "decode"]

    def __init__(self,bin = None):
        self.bin = bin
        self.pin = 0
        self.bout = haxe_io_BytesBuffer()
        self.hstrings = haxe_ds_StringMap()
        self.strings = [None]
        self.nstrings = 1

    def doEncodeString(self,v):
        vid = self.hstrings.h.get(v,None)
        if (vid is None):
            if (self.nstrings == 256):
                self.hstrings = haxe_ds_StringMap()
                self.nstrings = 1
            self.hstrings.h[v] = self.nstrings
            self.bout.b.append(0)
            vb = haxe_io_Bytes.ofString(v)
            self.bout.b.append(vb.length)
            self.bout.b.extend(vb.b)
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.nstrings
            _hx_local_0.nstrings = (_hx_local_1 + 1)
            _hx_local_1
        else:
            self.bout.b.append(vid)

    def doDecodeString(self):
        pos = self.pin
        self.pin = (self.pin + 1)
        id = self.bin.b[pos]
        if (id == 0):
            _hx_len = self.bin.b[self.pin]
            _hx_str = self.bin.getString((self.pin + 1),_hx_len)
            _hx_local_0 = self
            _hx_local_1 = _hx_local_0.pin
            _hx_local_0.pin = (_hx_local_1 + ((_hx_len + 1)))
            _hx_local_0.pin
            if (len(self.strings) == 255):
                self.strings = [None]
            _this = self.strings
            _this.append(_hx_str)
            return _hx_str
        return (self.strings[id] if id >= 0 and id < len(self.strings) else None)

    def doEncodeInt(self,v):
        self.bout.addInt32(v)

    def doEncodeConst(self,c):
        tmp = c.index
        if (tmp == 0):
            v = c.params[0]
            if ((v >= 0) and ((v <= 255))):
                self.bout.b.append(0)
                self.bout.b.append(v)
            else:
                self.bout.b.append(1)
                self.doEncodeInt(v)
        elif (tmp == 1):
            f = c.params[0]
            self.bout.b.append(2)
            self.doEncodeString(Std.string(f))
        elif (tmp == 2):
            s = c.params[0]
            self.bout.b.append(3)
            self.doEncodeString(s)
        else:
            pass

    def doDecodeInt(self):
        _this = self.bin
        pos = self.pin
        v = (((_this.b[pos] | ((_this.b[(pos + 1)] << 8))) | ((_this.b[(pos + 2)] << 16))) | ((_this.b[(pos + 3)] << 24)))
        i = ((v | -2147483648) if ((((v & -2147483648)) != 0)) else v)
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.pin
        _hx_local_0.pin = (_hx_local_1 + 4)
        _hx_local_0.pin
        return i

    def doDecodeConst(self):
        pos = self.pin
        self.pin = (self.pin + 1)
        _g = self.bin.b[pos]
        if (_g == 0):
            pos = self.pin
            self.pin = (self.pin + 1)
            return hscript_Const.CInt(self.bin.b[pos])
        elif (_g == 1):
            i = self.doDecodeInt()
            return hscript_Const.CInt(i)
        elif (_g == 2):
            return hscript_Const.CFloat(Std.parseFloat(self.doDecodeString()))
        elif (_g == 3):
            return hscript_Const.CString(self.doDecodeString())
        else:
            raise haxe_Exception.thrown(("Invalid code " + Std.string(self.bin.b[(self.pin - 1)])))

    def doEncode(self,e):
        self.bout.b.append(e.index)
        tmp = e.index
        if (tmp == 0):
            c = e.params[0]
            self.doEncodeConst(c)
        elif (tmp == 1):
            v = e.params[0]
            self.doEncodeString(v)
        elif (tmp == 2):
            _g = e.params[1]
            n = e.params[0]
            e1 = e.params[2]
            self.doEncodeString(n)
            if (e1 is None):
                self.bout.b.append(255)
            else:
                self.doEncode(e1)
        elif (tmp == 3):
            e1 = e.params[0]
            self.doEncode(e1)
        elif (tmp == 4):
            el = e.params[0]
            self.bout.b.append(len(el))
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                self.doEncode(e1)
        elif (tmp == 5):
            e1 = e.params[0]
            f = e.params[1]
            self.doEncode(e1)
            self.doEncodeString(f)
        elif (tmp == 6):
            op = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            self.doEncodeString(op)
            self.doEncode(e1)
            self.doEncode(e2)
        elif (tmp == 7):
            op = e.params[0]
            prefix = e.params[1]
            e1 = e.params[2]
            self.doEncodeString(op)
            self.bout.b.append((1 if prefix else 0))
            self.doEncode(e1)
        elif (tmp == 8):
            e1 = e.params[0]
            el = e.params[1]
            self.doEncode(e1)
            self.bout.b.append(len(el))
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                self.doEncode(e1)
        elif (tmp == 9):
            cond = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            self.doEncode(cond)
            self.doEncode(e1)
            if (e2 is None):
                self.bout.b.append(255)
            else:
                self.doEncode(e2)
        elif (tmp == 10):
            cond = e.params[0]
            e1 = e.params[1]
            self.doEncode(cond)
            self.doEncode(e1)
        elif (tmp == 11):
            v = e.params[0]
            it = e.params[1]
            e1 = e.params[2]
            self.doEncodeString(v)
            self.doEncode(it)
            self.doEncode(e1)
        elif ((tmp == 13) or ((tmp == 12))):
            pass
        elif (tmp == 14):
            _g = e.params[3]
            params = e.params[0]
            e1 = e.params[1]
            name = e.params[2]
            self.bout.b.append(len(params))
            _g = 0
            while (_g < len(params)):
                p = (params[_g] if _g >= 0 and _g < len(params) else None)
                _g = (_g + 1)
                self.doEncodeString(p.name)
            self.doEncode(e1)
            self.doEncodeString(("" if ((name is None)) else name))
        elif (tmp == 15):
            e1 = e.params[0]
            if (e1 is None):
                self.bout.b.append(255)
            else:
                self.doEncode(e1)
        elif (tmp == 16):
            e1 = e.params[0]
            index = e.params[1]
            self.doEncode(e1)
            self.doEncode(index)
        elif (tmp == 17):
            el = e.params[0]
            if (len(el) >= 255):
                raise haxe_Exception.thrown("assert")
            self.bout.b.append(len(el))
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                self.doEncode(e1)
        elif (tmp == 18):
            cl = e.params[0]
            params = e.params[1]
            self.doEncodeString(cl)
            self.bout.b.append(len(params))
            _g = 0
            while (_g < len(params)):
                e1 = (params[_g] if _g >= 0 and _g < len(params) else None)
                _g = (_g + 1)
                self.doEncode(e1)
        elif (tmp == 19):
            e1 = e.params[0]
            self.doEncode(e1)
        elif (tmp == 20):
            _g = e.params[2]
            e1 = e.params[0]
            v = e.params[1]
            ecatch = e.params[3]
            self.doEncode(e1)
            self.doEncodeString(v)
            self.doEncode(ecatch)
        elif (tmp == 21):
            fl = e.params[0]
            self.bout.b.append(len(fl))
            _g = 0
            while (_g < len(fl)):
                f = (fl[_g] if _g >= 0 and _g < len(fl) else None)
                _g = (_g + 1)
                self.doEncodeString(f.name)
                self.doEncode(f.e)
        elif (tmp == 22):
            cond = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            self.doEncode(cond)
            self.doEncode(e1)
            self.doEncode(e2)
        elif (tmp == 23):
            e1 = e.params[0]
            cases = e.params[1]
            _hx_def = e.params[2]
            self.doEncode(e1)
            _g = 0
            while (_g < len(cases)):
                c = (cases[_g] if _g >= 0 and _g < len(cases) else None)
                _g = (_g + 1)
                if (len(c.values) == 0):
                    raise haxe_Exception.thrown("assert")
                _g1 = 0
                _g2 = c.values
                while (_g1 < len(_g2)):
                    v = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    self.doEncode(v)
                self.bout.b.append(255)
                self.doEncode(c.expr)
            self.bout.b.append(255)
            if (_hx_def is None):
                self.bout.b.append(255)
            else:
                self.doEncode(_hx_def)
        elif (tmp == 24):
            cond = e.params[0]
            e1 = e.params[1]
            self.doEncode(cond)
            self.doEncode(e1)
        elif (tmp == 25):
            name = e.params[0]
            args = e.params[1]
            e1 = e.params[2]
            self.doEncodeString(name)
            self.bout.b.append((0 if ((args is None)) else (len(args) + 1)))
            if (args is not None):
                _g = 0
                while (_g < len(args)):
                    e2 = (args[_g] if _g >= 0 and _g < len(args) else None)
                    _g = (_g + 1)
                    self.doEncode(e2)
            self.doEncode(e1)
        elif (tmp == 26):
            _g = e.params[1]
            e1 = e.params[0]
            self.doEncode(e1)
        else:
            pass

    def doDecode(self):
        pos = self.pin
        self.pin = (self.pin + 1)
        _g = self.bin.b[pos]
        if (_g == 0):
            return hscript_Expr.EConst(self.doDecodeConst())
        elif (_g == 1):
            return hscript_Expr.EIdent(self.doDecodeString())
        elif (_g == 2):
            v = self.doDecodeString()
            return hscript_Expr.EVar(v,None,self.doDecode())
        elif (_g == 3):
            return hscript_Expr.EParent(self.doDecode())
        elif (_g == 4):
            a = list()
            _g = 0
            pos = self.pin
            self.pin = (self.pin + 1)
            _g1 = self.bin.b[pos]
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                x = self.doDecode()
                a.append(x)
            return hscript_Expr.EBlock(a)
        elif (_g == 5):
            e = self.doDecode()
            return hscript_Expr.EField(e,self.doDecodeString())
        elif (_g == 6):
            op = self.doDecodeString()
            e1 = self.doDecode()
            return hscript_Expr.EBinop(op,e1,self.doDecode())
        elif (_g == 7):
            op = self.doDecodeString()
            pos = self.pin
            self.pin = (self.pin + 1)
            prefix = (self.bin.b[pos] != 0)
            return hscript_Expr.EUnop(op,prefix,self.doDecode())
        elif (_g == 8):
            e = self.doDecode()
            params = list()
            _g = 0
            pos = self.pin
            self.pin = (self.pin + 1)
            _g1 = self.bin.b[pos]
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                x = self.doDecode()
                params.append(x)
            return hscript_Expr.ECall(e,params)
        elif (_g == 9):
            cond = self.doDecode()
            e1 = self.doDecode()
            return hscript_Expr.EIf(cond,e1,self.doDecode())
        elif (_g == 10):
            cond = self.doDecode()
            return hscript_Expr.EWhile(cond,self.doDecode())
        elif (_g == 11):
            v = self.doDecodeString()
            it = self.doDecode()
            return hscript_Expr.EFor(v,it,self.doDecode())
        elif (_g == 12):
            return hscript_Expr.EBreak
        elif (_g == 13):
            return hscript_Expr.EContinue
        elif (_g == 14):
            params = list()
            _g = 0
            pos = self.pin
            self.pin = (self.pin + 1)
            _g1 = self.bin.b[pos]
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                x = _hx_AnonObject({'name': self.doDecodeString()})
                params.append(x)
            e = self.doDecode()
            name = self.doDecodeString()
            return hscript_Expr.EFunction(params,e,(None if ((name == "")) else name))
        elif (_g == 15):
            return hscript_Expr.EReturn(self.doDecode())
        elif (_g == 16):
            e = self.doDecode()
            return hscript_Expr.EArray(e,self.doDecode())
        elif (_g == 17):
            el = list()
            _g = 0
            pos = self.pin
            self.pin = (self.pin + 1)
            _g1 = self.bin.b[pos]
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                x = self.doDecode()
                el.append(x)
            return hscript_Expr.EArrayDecl(el)
        elif (_g == 18):
            cl = self.doDecodeString()
            el = list()
            _g = 0
            pos = self.pin
            self.pin = (self.pin + 1)
            _g1 = self.bin.b[pos]
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                x = self.doDecode()
                el.append(x)
            return hscript_Expr.ENew(cl,el)
        elif (_g == 19):
            return hscript_Expr.EThrow(self.doDecode())
        elif (_g == 20):
            e = self.doDecode()
            v = self.doDecodeString()
            return hscript_Expr.ETry(e,v,None,self.doDecode())
        elif (_g == 21):
            fl = list()
            _g = 0
            pos = self.pin
            self.pin = (self.pin + 1)
            _g1 = self.bin.b[pos]
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                name = self.doDecodeString()
                e = self.doDecode()
                fl.append(_hx_AnonObject({'name': name, 'e': e}))
            return hscript_Expr.EObject(fl)
        elif (_g == 22):
            cond = self.doDecode()
            e1 = self.doDecode()
            e2 = self.doDecode()
            return hscript_Expr.ETernary(cond,e1,e2)
        elif (_g == 23):
            e = self.doDecode()
            cases = []
            while True:
                v = self.doDecode()
                if (v is None):
                    break
                values = [v]
                while True:
                    v = self.doDecode()
                    if (v is None):
                        break
                    values.append(v)
                x = _hx_AnonObject({'values': values, 'expr': self.doDecode()})
                cases.append(x)
            _hx_def = self.doDecode()
            return hscript_Expr.ESwitch(e,cases,_hx_def)
        elif (_g == 24):
            cond = self.doDecode()
            return hscript_Expr.EDoWhile(cond,self.doDecode())
        elif (_g == 25):
            name = self.doDecodeString()
            pos = self.pin
            self.pin = (self.pin + 1)
            count = self.bin.b[pos]
            args = None
            if (count == 0):
                args = None
            else:
                _g = []
                _g1 = 0
                _g2 = (count - 1)
                while (_g1 < _g2):
                    i = _g1
                    _g1 = (_g1 + 1)
                    x = self.doDecode()
                    _g.append(x)
                args = _g
            return hscript_Expr.EMeta(name,args,self.doDecode())
        elif (_g == 26):
            return hscript_Expr.ECheckType(self.doDecode(),hscript_CType.CTPath(["Void"]))
        elif (_g == 255):
            return None
        else:
            raise haxe_Exception.thrown(("Invalid code " + Std.string(self.bin.b[(self.pin - 1)])))

    @staticmethod
    def encode(e):
        b = hscript_Bytes()
        b.doEncode(e)
        return b.bout.getBytes()

    @staticmethod
    def decode(_hx_bytes):
        b = hscript_Bytes(_hx_bytes)
        return b.doDecode()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bin = None
        _hx_o.bout = None
        _hx_o.pin = None
        _hx_o.hstrings = None
        _hx_o.strings = None
        _hx_o.nstrings = None
hscript_Bytes._hx_class = hscript_Bytes
_hx_classes["hscript.Bytes"] = hscript_Bytes

