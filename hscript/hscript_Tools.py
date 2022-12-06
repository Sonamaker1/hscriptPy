class hscript_Tools:
    _hx_class_name = "hscript.Tools"
    __slots__ = ()
    _hx_statics = ["iter", "map", "expr", "mk"]

    @staticmethod
    def iter(e,f):
        tmp = e.index
        if (tmp == 0):
            _g = e.params[0]
        elif (tmp == 1):
            _g = e.params[0]
        elif (tmp == 2):
            _g = e.params[0]
            _g = e.params[1]
            e1 = e.params[2]
            if (e1 is not None):
                f(e1)
        elif (tmp == 3):
            e1 = e.params[0]
            f(e1)
        elif (tmp == 4):
            el = e.params[0]
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                f(e1)
        elif (tmp == 5):
            _g = e.params[1]
            e1 = e.params[0]
            f(e1)
        elif (tmp == 6):
            _g = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            f(e1)
            f(e2)
        elif (tmp == 7):
            _g = e.params[0]
            _g = e.params[1]
            e1 = e.params[2]
            f(e1)
        elif (tmp == 8):
            e1 = e.params[0]
            args = e.params[1]
            f(e1)
            _g = 0
            while (_g < len(args)):
                a = (args[_g] if _g >= 0 and _g < len(args) else None)
                _g = (_g + 1)
                f(a)
        elif (tmp == 9):
            c = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            f(c)
            f(e1)
            if (e2 is not None):
                f(e2)
        elif (tmp == 10):
            c = e.params[0]
            e1 = e.params[1]
            f(c)
            f(e1)
        elif (tmp == 11):
            _g = e.params[0]
            it = e.params[1]
            e1 = e.params[2]
            f(it)
            f(e1)
        elif ((tmp == 13) or ((tmp == 12))):
            pass
        elif (tmp == 14):
            _g = e.params[0]
            _g = e.params[2]
            _g = e.params[3]
            e1 = e.params[1]
            f(e1)
        elif (tmp == 15):
            e1 = e.params[0]
            if (e1 is not None):
                f(e1)
        elif (tmp == 16):
            e1 = e.params[0]
            i = e.params[1]
            f(e1)
            f(i)
        elif (tmp == 17):
            el = e.params[0]
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                f(e1)
        elif (tmp == 18):
            _g = e.params[0]
            el = e.params[1]
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                f(e1)
        elif (tmp == 19):
            e1 = e.params[0]
            f(e1)
        elif (tmp == 20):
            _g = e.params[1]
            _g = e.params[2]
            e1 = e.params[0]
            c = e.params[3]
            f(e1)
            f(c)
        elif (tmp == 21):
            fl = e.params[0]
            _g = 0
            while (_g < len(fl)):
                fi = (fl[_g] if _g >= 0 and _g < len(fl) else None)
                _g = (_g + 1)
                f(fi.e)
        elif (tmp == 22):
            c = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            f(c)
            f(e1)
            f(e2)
        elif (tmp == 23):
            e1 = e.params[0]
            cases = e.params[1]
            _hx_def = e.params[2]
            f(e1)
            _g = 0
            while (_g < len(cases)):
                c = (cases[_g] if _g >= 0 and _g < len(cases) else None)
                _g = (_g + 1)
                _g1 = 0
                _g2 = c.values
                while (_g1 < len(_g2)):
                    v = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    f(v)
                f(c.expr)
            if (_hx_def is not None):
                f(_hx_def)
        elif (tmp == 24):
            c = e.params[0]
            e1 = e.params[1]
            f(c)
            f(e1)
        elif (tmp == 25):
            name = e.params[0]
            args = e.params[1]
            e1 = e.params[2]
            if (args is not None):
                _g = 0
                while (_g < len(args)):
                    a = (args[_g] if _g >= 0 and _g < len(args) else None)
                    _g = (_g + 1)
                    f(a)
            f(e1)
        elif (tmp == 26):
            _g = e.params[1]
            e1 = e.params[0]
            f(e1)
        else:
            pass

    @staticmethod
    def map(e,f):
        edef = None
        edef1 = e.index
        if (edef1 == 0):
            _g = e.params[0]
            edef = e
        elif (edef1 == 1):
            _g = e.params[0]
            edef = e
        elif (edef1 == 2):
            n = e.params[0]
            t = e.params[1]
            e1 = e.params[2]
            edef = hscript_Expr.EVar(n,t,(f(e1) if ((e1 is not None)) else None))
        elif (edef1 == 3):
            e1 = e.params[0]
            edef = hscript_Expr.EParent(f(e1))
        elif (edef1 == 4):
            el = e.params[0]
            _g = []
            _g1 = 0
            while (_g1 < len(el)):
                e1 = (el[_g1] if _g1 >= 0 and _g1 < len(el) else None)
                _g1 = (_g1 + 1)
                x = f(e1)
                _g.append(x)
            edef = hscript_Expr.EBlock(_g)
        elif (edef1 == 5):
            e1 = e.params[0]
            fi = e.params[1]
            edef = hscript_Expr.EField(f(e1),fi)
        elif (edef1 == 6):
            op = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            edef = hscript_Expr.EBinop(op,f(e1),f(e2))
        elif (edef1 == 7):
            op = e.params[0]
            pre = e.params[1]
            e1 = e.params[2]
            edef = hscript_Expr.EUnop(op,pre,f(e1))
        elif (edef1 == 8):
            e1 = e.params[0]
            args = e.params[1]
            edef1 = f(e1)
            _g = []
            _g1 = 0
            while (_g1 < len(args)):
                a = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                _g1 = (_g1 + 1)
                x = f(a)
                _g.append(x)
            edef = hscript_Expr.ECall(edef1,_g)
        elif (edef1 == 9):
            c = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            edef = hscript_Expr.EIf(f(c),f(e1),(f(e2) if ((e2 is not None)) else None))
        elif (edef1 == 10):
            c = e.params[0]
            e1 = e.params[1]
            edef = hscript_Expr.EWhile(f(c),f(e1))
        elif (edef1 == 11):
            v = e.params[0]
            it = e.params[1]
            e1 = e.params[2]
            edef = hscript_Expr.EFor(v,f(it),f(e1))
        elif ((edef1 == 13) or ((edef1 == 12))):
            edef = e
        elif (edef1 == 14):
            args = e.params[0]
            e1 = e.params[1]
            name = e.params[2]
            t = e.params[3]
            edef = hscript_Expr.EFunction(args,f(e1),name,t)
        elif (edef1 == 15):
            e1 = e.params[0]
            edef = hscript_Expr.EReturn((f(e1) if ((e1 is not None)) else None))
        elif (edef1 == 16):
            e1 = e.params[0]
            i = e.params[1]
            edef = hscript_Expr.EArray(f(e1),f(i))
        elif (edef1 == 17):
            el = e.params[0]
            _g = []
            _g1 = 0
            while (_g1 < len(el)):
                e1 = (el[_g1] if _g1 >= 0 and _g1 < len(el) else None)
                _g1 = (_g1 + 1)
                x = f(e1)
                _g.append(x)
            edef = hscript_Expr.EArrayDecl(_g)
        elif (edef1 == 18):
            cl = e.params[0]
            el = e.params[1]
            _g = []
            _g1 = 0
            while (_g1 < len(el)):
                e1 = (el[_g1] if _g1 >= 0 and _g1 < len(el) else None)
                _g1 = (_g1 + 1)
                x = f(e1)
                _g.append(x)
            edef = hscript_Expr.ENew(cl,_g)
        elif (edef1 == 19):
            e1 = e.params[0]
            edef = hscript_Expr.EThrow(f(e1))
        elif (edef1 == 20):
            e1 = e.params[0]
            v = e.params[1]
            t = e.params[2]
            c = e.params[3]
            edef = hscript_Expr.ETry(f(e1),v,t,f(c))
        elif (edef1 == 21):
            fl = e.params[0]
            _g = []
            _g1 = 0
            while (_g1 < len(fl)):
                fi = (fl[_g1] if _g1 >= 0 and _g1 < len(fl) else None)
                _g1 = (_g1 + 1)
                x = _hx_AnonObject({'name': fi.name, 'e': f(fi.e)})
                _g.append(x)
            edef = hscript_Expr.EObject(_g)
        elif (edef1 == 22):
            c = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            edef = hscript_Expr.ETernary(f(c),f(e1),f(e2))
        elif (edef1 == 23):
            e1 = e.params[0]
            cases = e.params[1]
            _hx_def = e.params[2]
            edef1 = f(e1)
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
                    x = f(v)
                    _g2.append(x)
                x1 = _hx_AnonObject({'values': _g2, 'expr': f(c.expr)})
                _g.append(x1)
            edef = hscript_Expr.ESwitch(edef1,_g,(None if ((_hx_def is None)) else f(_hx_def)))
        elif (edef1 == 24):
            c = e.params[0]
            e1 = e.params[1]
            edef = hscript_Expr.EDoWhile(f(c),f(e1))
        elif (edef1 == 25):
            name = e.params[0]
            args = e.params[1]
            e1 = e.params[2]
            edef1 = None
            if (args is None):
                edef1 = None
            else:
                _g = []
                _g1 = 0
                while (_g1 < len(args)):
                    a = (args[_g1] if _g1 >= 0 and _g1 < len(args) else None)
                    _g1 = (_g1 + 1)
                    x = f(a)
                    _g.append(x)
                edef1 = _g
            edef = hscript_Expr.EMeta(name,edef1,f(e1))
        elif (edef1 == 26):
            e1 = e.params[0]
            t = e.params[1]
            edef = hscript_Expr.ECheckType(f(e1),t)
        else:
            pass
        return edef

    @staticmethod
    def expr(e):
        return e

    @staticmethod
    def mk(e,p):
        return e
hscript_Tools._hx_class = hscript_Tools
_hx_classes["hscript.Tools"] = hscript_Tools


