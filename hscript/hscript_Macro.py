class hscript_Macro:
    _hx_class_name = "hscript.Macro"
    __slots__ = ("p", "binops", "unops")
    _hx_fields = ["p", "binops", "unops"]
    _hx_methods = ["map", "convertType", "convert"]

    def __init__(self,pos):
        self.p = pos
        self.binops = haxe_ds_StringMap()
        self.unops = haxe_ds_StringMap()
        _g = 0
        _g1 = Type.getEnumConstructs(haxe_macro_Binop)
        while (_g < len(_g1)):
            c = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (c == "OpAssignOp"):
                continue
            op = Type.createEnum(haxe_macro_Binop,c)
            assign = False
            _hx_str = None
            str1 = op.index
            if (str1 == 0):
                assign = True
                _hx_str = "+"
            elif (str1 == 1):
                assign = True
                _hx_str = "*"
            elif (str1 == 2):
                assign = True
                _hx_str = "/"
            elif (str1 == 3):
                assign = True
                _hx_str = "-"
            elif (str1 == 4):
                _hx_str = "="
            elif (str1 == 5):
                _hx_str = "=="
            elif (str1 == 6):
                _hx_str = "!="
            elif (str1 == 7):
                _hx_str = ">"
            elif (str1 == 8):
                _hx_str = ">="
            elif (str1 == 9):
                _hx_str = "<"
            elif (str1 == 10):
                _hx_str = "<="
            elif (str1 == 11):
                assign = True
                _hx_str = "&"
            elif (str1 == 12):
                assign = True
                _hx_str = "|"
            elif (str1 == 13):
                assign = True
                _hx_str = "^"
            elif (str1 == 14):
                _hx_str = "&&"
            elif (str1 == 15):
                _hx_str = "||"
            elif (str1 == 16):
                assign = True
                _hx_str = "<<"
            elif (str1 == 17):
                assign = True
                _hx_str = ">>"
            elif (str1 == 18):
                assign = True
                _hx_str = ">>>"
            elif (str1 == 19):
                assign = True
                _hx_str = "%"
            elif (str1 == 20):
                _g2 = op.params[0]
                _hx_str = ""
            elif (str1 == 21):
                _hx_str = "..."
            elif (str1 == 22):
                _hx_str = "=>"
            elif (str1 == 23):
                _hx_str = "in"
            else:
                pass
            self.binops.h[_hx_str] = op
            if assign:
                self.binops.h[(("null" if _hx_str is None else _hx_str) + "=")] = haxe_macro_Binop.OpAssignOp(op)
        _g = 0
        _g1 = Type.getEnumConstructs(haxe_macro_Unop)
        while (_g < len(_g1)):
            c = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            op = Type.createEnum(haxe_macro_Unop,c)
            _hx_str = None
            str1 = op.index
            if (str1 == 0):
                _hx_str = "++"
            elif (str1 == 1):
                _hx_str = "--"
            elif (str1 == 2):
                _hx_str = "!"
            elif (str1 == 3):
                _hx_str = "-"
            elif (str1 == 4):
                _hx_str = "~"
            elif (str1 == 5):
                continue
            else:
                pass
            self.unops.h[_hx_str] = op

    def map(self,a,f):
        b = list()
        _g = 0
        while (_g < len(a)):
            x = (a[_g] if _g >= 0 and _g < len(a) else None)
            _g = (_g + 1)
            x1 = f(x)
            b.append(x1)
        return b

    def convertType(self,t):
        tmp = t.index
        if (tmp == 0):
            pack = t.params[0]
            args = t.params[1]
            params = []
            if (args is not None):
                _g = 0
                while (_g < len(args)):
                    t1 = (args[_g] if _g >= 0 and _g < len(args) else None)
                    _g = (_g + 1)
                    x = haxe_macro_TypeParam.TPType(self.convertType(t1))
                    params.append(x)
            return haxe_macro_ComplexType.TPath(_hx_AnonObject({'pack': pack, 'name': (None if ((len(pack) == 0)) else pack.pop()), 'params': params, 'sub': None}))
        elif (tmp == 1):
            args = t.params[0]
            ret = t.params[1]
            return haxe_macro_ComplexType.TFunction(self.map(args,self.convertType),self.convertType(ret))
        elif (tmp == 2):
            fields = t.params[0]
            tf = []
            _g = 0
            while (_g < len(fields)):
                f = (fields[_g] if _g >= 0 and _g < len(fields) else None)
                _g = (_g + 1)
                meta = None
                if (Reflect.field(f,"meta") is None):
                    meta = []
                else:
                    _g1 = []
                    _g2 = 0
                    _g3 = Reflect.field(f,"meta")
                    while (_g2 < len(_g3)):
                        m = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                        _g2 = (_g2 + 1)
                        m1 = m.name
                        x = None
                        if (m.params is None):
                            x = []
                        else:
                            _g4 = []
                            _g5 = 0
                            _g6 = m.params
                            while (_g5 < len(_g6)):
                                e = (_g6[_g5] if _g5 >= 0 and _g5 < len(_g6) else None)
                                _g5 = (_g5 + 1)
                                x1 = self.convert(e)
                                _g4.append(x1)
                            x = _g4
                        x2 = _hx_AnonObject({'name': m1, 'params': x, 'pos': self.p})
                        _g1.append(x2)
                    meta = _g1
                x3 = _hx_AnonObject({'name': f.name, 'meta': meta, 'doc': None, 'access': [], 'kind': haxe_macro_FieldType.FVar(self.convertType(f.t),None), 'pos': self.p})
                tf.append(x3)
            return haxe_macro_ComplexType.TAnonymous(tf)
        elif (tmp == 3):
            t1 = t.params[0]
            return haxe_macro_ComplexType.TParent(self.convertType(t1))
        elif (tmp == 4):
            t1 = t.params[0]
            return haxe_macro_ComplexType.TOptional(self.convertType(t1))
        elif (tmp == 5):
            name = t.params[0]
            ct = self.convertType(t.params[1])
            return haxe_macro_ComplexType.TNamed(name,ct)
        else:
            pass

    def convert(self,e):
        tmp = None
        tmp1 = e.index
        if (tmp1 == 0):
            c = e.params[0]
            tmp1 = None
            tmp2 = c.index
            if (tmp2 == 0):
                v = c.params[0]
                tmp1 = haxe_macro_Constant.CInt(Std.string(v))
            elif (tmp2 == 1):
                f = c.params[0]
                tmp1 = haxe_macro_Constant.CFloat(Std.string(f))
            elif (tmp2 == 2):
                s = c.params[0]
                tmp1 = haxe_macro_Constant.CString(s)
            else:
                pass
            tmp = haxe_macro_ExprDef.EConst(tmp1)
        elif (tmp1 == 1):
            v = e.params[0]
            tmp = haxe_macro_ExprDef.EConst(haxe_macro_Constant.CIdent(v))
        elif (tmp1 == 2):
            n = e.params[0]
            t = e.params[1]
            e1 = e.params[2]
            tmp = haxe_macro_ExprDef.EVars([_hx_AnonObject({'name': n, 'expr': (None if ((e1 is None)) else self.convert(e1)), 'type': (None if ((t is None)) else self.convertType(t))})])
        elif (tmp1 == 3):
            e1 = e.params[0]
            tmp = haxe_macro_ExprDef.EParenthesis(self.convert(e1))
        elif (tmp1 == 4):
            el = e.params[0]
            tmp = haxe_macro_ExprDef.EBlock(self.map(el,self.convert))
        elif (tmp1 == 5):
            e1 = e.params[0]
            f = e.params[1]
            tmp = haxe_macro_ExprDef.EField(self.convert(e1),f)
        elif (tmp1 == 6):
            op = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            b = self.binops.h.get(op,None)
            if (b is None):
                raise haxe_Exception.thrown(hscript_Error.EInvalidOp(op))
            tmp = haxe_macro_ExprDef.EBinop(b,self.convert(e1),self.convert(e2))
        elif (tmp1 == 7):
            op = e.params[0]
            prefix = e.params[1]
            e1 = e.params[2]
            u = self.unops.h.get(op,None)
            if (u is None):
                raise haxe_Exception.thrown(hscript_Error.EInvalidOp(op))
            tmp = haxe_macro_ExprDef.EUnop(u,(not prefix),self.convert(e1))
        elif (tmp1 == 8):
            e1 = e.params[0]
            params = e.params[1]
            tmp = haxe_macro_ExprDef.ECall(self.convert(e1),self.map(params,self.convert))
        elif (tmp1 == 9):
            c = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            tmp = haxe_macro_ExprDef.EIf(self.convert(c),self.convert(e1),(None if ((e2 is None)) else self.convert(e2)))
        elif (tmp1 == 10):
            c = e.params[0]
            e1 = e.params[1]
            tmp = haxe_macro_ExprDef.EWhile(self.convert(c),self.convert(e1),True)
        elif (tmp1 == 11):
            v = e.params[0]
            it = e.params[1]
            efor = e.params[2]
            p = self.p
            tmp1 = self.convert(it)
            tmp2 = self.convert(efor)
            tmp = haxe_macro_ExprDef.EFor(_hx_AnonObject({'expr': haxe_macro_ExprDef.EBinop(haxe_macro_Binop.OpIn,_hx_AnonObject({'expr': haxe_macro_ExprDef.EConst(haxe_macro_Constant.CIdent(v)), 'pos': p}),tmp1), 'pos': p}),tmp2)
        elif (tmp1 == 12):
            tmp = haxe_macro_ExprDef.EBreak
        elif (tmp1 == 13):
            tmp = haxe_macro_ExprDef.EContinue
        elif (tmp1 == 14):
            args = e.params[0]
            e1 = e.params[1]
            name = e.params[2]
            ret = e.params[3]
            targs = []
            _g = 0
            while (_g < len(args)):
                a = (args[_g] if _g >= 0 and _g < len(args) else None)
                _g = (_g + 1)
                a1 = a.name
                x = (None if ((Reflect.field(a,"t") is None)) else self.convertType(Reflect.field(a,"t")))
                targs.append(_hx_AnonObject({'name': a1, 'type': x, 'opt': False, 'value': None}))
            tmp = haxe_macro_ExprDef.EFunction(haxe_macro_FunctionKind.FNamed(name,False),_hx_AnonObject({'params': [], 'args': targs, 'expr': self.convert(e1), 'ret': (None if ((ret is None)) else self.convertType(ret))}))
        elif (tmp1 == 15):
            e1 = e.params[0]
            tmp = haxe_macro_ExprDef.EReturn((None if ((e1 is None)) else self.convert(e1)))
        elif (tmp1 == 16):
            e1 = e.params[0]
            index = e.params[1]
            tmp = haxe_macro_ExprDef.EArray(self.convert(e1),self.convert(index))
        elif (tmp1 == 17):
            el = e.params[0]
            tmp = haxe_macro_ExprDef.EArrayDecl(self.map(el,self.convert))
        elif (tmp1 == 18):
            cl = e.params[0]
            params = e.params[1]
            pack = cl.split(".")
            tmp1 = (None if ((len(pack) == 0)) else pack.pop())
            tmp2 = self.map(params,self.convert)
            tmp = haxe_macro_ExprDef.ENew(_hx_AnonObject({'pack': pack, 'name': tmp1, 'params': [], 'sub': None}),tmp2)
        elif (tmp1 == 19):
            e1 = e.params[0]
            tmp = haxe_macro_ExprDef.EThrow(self.convert(e1))
        elif (tmp1 == 20):
            e1 = e.params[0]
            v = e.params[1]
            t = e.params[2]
            ec = e.params[3]
            tmp = haxe_macro_ExprDef.ETry(self.convert(e1),[_hx_AnonObject({'type': self.convertType(t), 'name': v, 'expr': self.convert(ec)})])
        elif (tmp1 == 21):
            fields = e.params[0]
            tf = []
            _g = 0
            while (_g < len(fields)):
                f = (fields[_g] if _g >= 0 and _g < len(fields) else None)
                _g = (_g + 1)
                x = _hx_AnonObject({'field': f.name, 'expr': self.convert(f.e)})
                tf.append(x)
            tmp = haxe_macro_ExprDef.EObjectDecl(tf)
        elif (tmp1 == 22):
            cond = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            tmp = haxe_macro_ExprDef.ETernary(self.convert(cond),self.convert(e1),self.convert(e2))
        elif (tmp1 == 23):
            e1 = e.params[0]
            cases = e.params[1]
            edef = e.params[2]
            tmp1 = self.convert(e1)
            _g = []
            _g1 = 0
            while (_g1 < len(cases)):
                c = (cases[_g1] if _g1 >= 0 and _g1 < len(cases) else None)
                _g1 = (_g1 + 1)
                _g2 = []
                _g3 = 0
                _g4 = c.values
                while (_g3 < len(_g4)):
                    v = (_g4[_g3] if _g3 >= 0 and _g3 < len(_g4) else None)
                    _g3 = (_g3 + 1)
                    x = self.convert(v)
                    _g2.append(x)
                x1 = _hx_AnonObject({'values': _g2, 'expr': self.convert(c.expr)})
                _g.append(x1)
            tmp = haxe_macro_ExprDef.ESwitch(tmp1,_g,(None if ((edef is None)) else self.convert(edef)))
        elif (tmp1 == 24):
            c = e.params[0]
            e1 = e.params[1]
            tmp = haxe_macro_ExprDef.EWhile(self.convert(c),self.convert(e1),False)
        elif (tmp1 == 25):
            m = e.params[0]
            params = e.params[1]
            esub = e.params[2]
            mpos = self.p
            tmp1 = None
            if (params is None):
                tmp1 = []
            else:
                _g = []
                _g1 = 0
                while (_g1 < len(params)):
                    p = (params[_g1] if _g1 >= 0 and _g1 < len(params) else None)
                    _g1 = (_g1 + 1)
                    x = self.convert(p)
                    _g.append(x)
                tmp1 = _g
            tmp2 = self.convert(esub)
            tmp = haxe_macro_ExprDef.EMeta(_hx_AnonObject({'name': m, 'params': tmp1, 'pos': mpos}),tmp2)
        elif (tmp1 == 26):
            e1 = e.params[0]
            t = e.params[1]
            tmp = haxe_macro_ExprDef.ECheckType(self.convert(e1),self.convertType(t))
        else:
            pass
        return _hx_AnonObject({'expr': tmp, 'pos': self.p})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.p = None
        _hx_o.binops = None
        _hx_o.unops = None
hscript_Macro._hx_class = hscript_Macro
_hx_classes["hscript.Macro"] = hscript_Macro

