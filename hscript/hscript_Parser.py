class hscript_Parser:
    _hx_class_name = "hscript.Parser"
    __slots__ = ("line", "opChars", "identChars", "opPriority", "opRightAssoc", "preprocesorValues", "allowJSON", "allowTypes", "allowMetadata", "resumeErrors", "input", "readPos", "char", "ops", "idents", "uid", "tokens", "preprocStack")
    _hx_fields = ["line", "opChars", "identChars", "opPriority", "opRightAssoc", "preprocesorValues", "allowJSON", "allowTypes", "allowMetadata", "resumeErrors", "input", "readPos", "char", "ops", "idents", "uid", "tokens", "preprocStack"]
    _hx_methods = ["error", "invalidChar", "initParser", "parseString", "unexpected", "push", "ensure", "ensureToken", "maybe", "getIdent", "expr", "pmin", "pmax", "mk", "isBlock", "parseFullExpr", "parseObject", "parseExpr", "parseLambda", "parseMetaArgs", "mapCompr", "makeUnop", "makeBinop", "parseStructure", "parseExprNext", "parseFunctionArgs", "parseFunctionDecl", "parsePath", "parseType", "parseTypeNext", "parseExprList", "parseModule", "parseMetadata", "parseParams", "parseModuleDecl", "parseField", "readChar", "readString", "token", "preprocValue", "parsePreproCond", "evalPreproCond", "preprocess", "skipTokens", "tokenComment", "constString", "tokenString"]
    _hx_statics = ["p1", "tokenMin", "tokenMax"]

    def __init__(self):
        self.preprocStack = None
        self.tokens = None
        self.idents = None
        self.ops = None
        self.char = None
        self.readPos = None
        self.input = None
        self.resumeErrors = None
        self.allowMetadata = None
        self.allowTypes = None
        self.allowJSON = None
        self.uid = 0
        self.preprocesorValues = haxe_ds_StringMap()
        self.line = 1
        self.opChars = "+*/-=!><&|^%~"
        self.identChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"
        priorities = [["%"], ["*", "/"], ["+", "-"], ["<<", ">>", ">>>"], ["|", "&", "^"], ["==", "!=", ">", "<", ">=", "<="], ["..."], ["&&"], ["||"], ["=", "+=", "-=", "*=", "/=", "%=", "<<=", ">>=", ">>>=", "|=", "&=", "^=", "=>"], ["->"]]
        self.opPriority = haxe_ds_StringMap()
        self.opRightAssoc = haxe_ds_StringMap()
        _g = 0
        _g1 = len(priorities)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _g2 = 0
            _g3 = (priorities[i] if i >= 0 and i < len(priorities) else None)
            while (_g2 < len(_g3)):
                x = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                _g2 = (_g2 + 1)
                self.opPriority.h[x] = i
                if (i == 9):
                    self.opRightAssoc.h[x] = True
        x = "!"
        self.opPriority.h[x] = (-1 if (((x == "++") or ((x == "--")))) else -2)
        x = "++"
        self.opPriority.h[x] = (-1 if (((x == "++") or ((x == "--")))) else -2)
        x = "--"
        self.opPriority.h[x] = (-1 if (((x == "++") or ((x == "--")))) else -2)
        x = "~"
        self.opPriority.h[x] = (-1 if (((x == "++") or ((x == "--")))) else -2)

    def error(self,err,pmin,pmax):
        if (not self.resumeErrors):
            raise haxe_Exception.thrown(err)

    def invalidChar(self,c):
        if (not self.resumeErrors):
            raise haxe_Exception.thrown(hscript_Error.EInvalidChar(c))

    def initParser(self,origin):
        self.preprocStack = []
        self.tokens = haxe_ds_GenericStack()
        self.char = -1
        self.ops = list()
        self.idents = list()
        self.uid = 0
        _g = 0
        _g1 = len(self.opChars)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            python_internal_ArrayImpl._set(self.ops, HxString.charCodeAt(self.opChars,i), True)
        _g = 0
        _g1 = len(self.identChars)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            python_internal_ArrayImpl._set(self.idents, HxString.charCodeAt(self.identChars,i), True)

    def parseString(self,s,origin = None):
        if (origin is None):
            origin = "hscript"
        self.initParser(origin)
        self.input = s
        self.readPos = 0
        a = list()
        while True:
            tk = self.token()
            if (tk == hscript_Token.TEof):
                break
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            self.parseFullExpr(a)
        if (len(a) == 1):
            return (a[0] if 0 < len(a) else None)
        else:
            return hscript_Expr.EBlock(a)

    def unexpected(self,tk):
        err = hscript_Error.EUnexpected(self.tokenString(tk))
        if (not self.resumeErrors):
            raise haxe_Exception.thrown(err)
        return None

    def push(self,tk):
        _this = self.tokens
        _this.head = haxe_ds_GenericCell(tk,_this.head)

    def ensure(self,tk):
        t = self.token()
        if (t != tk):
            self.unexpected(t)

    def ensureToken(self,tk):
        t = self.token()
        if (not Type.enumEq(t,tk)):
            self.unexpected(t)

    def maybe(self,tk):
        t = self.token()
        if Type.enumEq(t,tk):
            return True
        _this = self.tokens
        _this.head = haxe_ds_GenericCell(t,_this.head)
        return False

    def getIdent(self):
        tk = self.token()
        if (tk is None):
            self.unexpected(tk)
            return None
        elif (tk.index == 2):
            id = tk.params[0]
            return id
        else:
            self.unexpected(tk)
            return None

    def expr(self,e):
        return e

    def pmin(self,e):
        return 0

    def pmax(self,e):
        return 0

    def mk(self,e,pmin = None,pmax = None):
        return e

    def isBlock(self,e):
        if (e is None):
            return False
        tmp = e.index
        if (tmp == 2):
            _g = e.params[0]
            t = e.params[1]
            e1 = e.params[2]
            if (e1 is not None):
                return self.isBlock(e1)
            elif (t is not None):
                if (t is None):
                    return False
                elif (t.index == 2):
                    _g = t.params[0]
                    return True
                else:
                    return False
            else:
                return False
        elif (tmp == 4):
            _g = e.params[0]
            return True
        elif (tmp == 6):
            _g = e.params[0]
            _g = e.params[1]
            e1 = e.params[2]
            return self.isBlock(e1)
        elif (tmp == 7):
            _g = e.params[0]
            prefix = e.params[1]
            e1 = e.params[2]
            if (not prefix):
                return self.isBlock(e1)
            else:
                return False
        elif (tmp == 9):
            _g = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            if (e2 is not None):
                return self.isBlock(e2)
            else:
                return self.isBlock(e1)
        elif (tmp == 10):
            _g = e.params[0]
            e1 = e.params[1]
            return self.isBlock(e1)
        elif (tmp == 11):
            _g = e.params[0]
            _g = e.params[1]
            e1 = e.params[2]
            return self.isBlock(e1)
        elif (tmp == 14):
            _g = e.params[0]
            _g = e.params[2]
            _g = e.params[3]
            e1 = e.params[1]
            return self.isBlock(e1)
        elif (tmp == 15):
            e1 = e.params[0]
            if (e1 is not None):
                return self.isBlock(e1)
            else:
                return False
        elif (tmp == 20):
            _g = e.params[0]
            _g = e.params[1]
            _g = e.params[2]
            e1 = e.params[3]
            return self.isBlock(e1)
        elif (tmp == 21):
            _g = e.params[0]
            return True
        elif (tmp == 23):
            _g = e.params[0]
            _g = e.params[1]
            _g = e.params[2]
            return True
        elif (tmp == 24):
            _g = e.params[0]
            e1 = e.params[1]
            return self.isBlock(e1)
        elif (tmp == 25):
            _g = e.params[0]
            _g = e.params[1]
            e1 = e.params[2]
            return self.isBlock(e1)
        else:
            return False

    def parseFullExpr(self,exprs):
        e = self.parseExpr()
        exprs.append(e)
        tk = self.token()
        while True:
            tmp = None
            if ((tk == hscript_Token.TComma) and ((e is not None))):
                if (e.index == 2):
                    _g = e.params[0]
                    _g1 = e.params[1]
                    _g2 = e.params[2]
                    tmp = True
                else:
                    tmp = False
            else:
                tmp = False
            if (not tmp):
                break
            e = self.parseStructure("var")
            exprs.append(e)
            tk = self.token()
        if ((tk != hscript_Token.TSemicolon) and ((tk != hscript_Token.TEof))):
            if self.isBlock(e):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
            else:
                self.unexpected(tk)

    def parseObject(self,p1):
        fl = list()
        while True:
            tk = self.token()
            id = None
            if (tk is None):
                self.unexpected(tk)
                break
            else:
                tmp = tk.index
                if (tmp == 1):
                    c = tk.params[0]
                    if (not self.allowJSON):
                        self.unexpected(tk)
                    if (c.index == 2):
                        s = c.params[0]
                        id = s
                    else:
                        self.unexpected(tk)
                elif (tmp == 2):
                    i = tk.params[0]
                    id = i
                elif (tmp == 7):
                    break
                else:
                    self.unexpected(tk)
                    break
            t = self.token()
            if (t != hscript_Token.TDoubleDot):
                self.unexpected(t)
            x = _hx_AnonObject({'name': id, 'e': self.parseExpr()})
            fl.append(x)
            tk = self.token()
            if (tk is None):
                self.unexpected(tk)
            else:
                tmp1 = tk.index
                if (tmp1 == 7):
                    break
                elif (tmp1 == 9):
                    pass
                else:
                    self.unexpected(tk)
        return self.parseExprNext(hscript_Expr.EObject(fl))

    def parseExpr(self):
        tk = self.token()
        if (tk is None):
            return self.unexpected(tk)
        else:
            tmp = tk.index
            if (tmp == 1):
                c = tk.params[0]
                return self.parseExprNext(hscript_Expr.EConst(c))
            elif (tmp == 2):
                id = tk.params[0]
                e = self.parseStructure(id)
                if (e is None):
                    e = hscript_Expr.EIdent(id)
                return self.parseExprNext(e)
            elif (tmp == 3):
                op = tk.params[0]
                if (op == "-"):
                    start = 0
                    e = self.parseExpr()
                    if (e is None):
                        return self.makeUnop(op,e)
                    if (e.index == 0):
                        _g = e.params[0]
                        tmp = _g.index
                        if (tmp == 0):
                            i = _g.params[0]
                            return hscript_Expr.EConst(hscript_Const.CInt(-i))
                        elif (tmp == 1):
                            f = _g.params[0]
                            return hscript_Expr.EConst(hscript_Const.CFloat(-f))
                        else:
                            return self.makeUnop(op,e)
                    else:
                        return self.makeUnop(op,e)
                if (self.opPriority.h.get(op,None) < 0):
                    return self.makeUnop(op,self.parseExpr())
                return self.unexpected(tk)
            elif (tmp == 4):
                tk = self.token()
                if (tk == hscript_Token.TPClose):
                    t = self.token()
                    if (not Type.enumEq(t,hscript_Token.TOp("->"))):
                        self.unexpected(t)
                    eret = self.parseExpr()
                    return hscript_Expr.EFunction([],hscript_Expr.EReturn(eret))
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
                e = self.parseExpr()
                tk = self.token()
                if (tk is not None):
                    tmp = tk.index
                    if (tmp == 5):
                        return self.parseExprNext(hscript_Expr.EParent(e))
                    elif (tmp == 9):
                        if (e.index == 1):
                            v = e.params[0]
                            return self.parseLambda([_hx_AnonObject({'name': v})],0)
                    elif (tmp == 14):
                        t = self.parseType()
                        tk = self.token()
                        if (tk is not None):
                            tmp = tk.index
                            if (tmp == 5):
                                return self.parseExprNext(hscript_Expr.ECheckType(e,t))
                            elif (tmp == 9):
                                if (e.index == 1):
                                    v = e.params[0]
                                    return self.parseLambda([_hx_AnonObject({'name': v, 't': t})],0)
                            else:
                                pass
                    else:
                        pass
                return self.unexpected(tk)
            elif (tmp == 6):
                tk = self.token()
                if (tk is None):
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                else:
                    tmp = tk.index
                    if (tmp == 1):
                        c = tk.params[0]
                        if self.allowJSON:
                            if (c.index == 2):
                                _g = c.params[0]
                                tk2 = self.token()
                                _this = self.tokens
                                _this.head = haxe_ds_GenericCell(tk2,_this.head)
                                _this = self.tokens
                                _this.head = haxe_ds_GenericCell(tk,_this.head)
                                if (tk2 is not None):
                                    if (tk2.index == 14):
                                        return self.parseExprNext(self.parseObject(0))
                            else:
                                _this = self.tokens
                                _this.head = haxe_ds_GenericCell(tk,_this.head)
                        else:
                            _this = self.tokens
                            _this.head = haxe_ds_GenericCell(tk,_this.head)
                    elif (tmp == 2):
                        _g = tk.params[0]
                        tk2 = self.token()
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(tk2,_this.head)
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(tk,_this.head)
                        if (tk2 is not None):
                            if (tk2.index == 14):
                                return self.parseExprNext(self.parseObject(0))
                    elif (tmp == 7):
                        return self.parseExprNext(hscript_Expr.EObject([]))
                    else:
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(tk,_this.head)
                a = list()
                while True:
                    self.parseFullExpr(a)
                    tk = self.token()
                    if ((tk == hscript_Token.TBrClose) or ((self.resumeErrors and ((tk == hscript_Token.TEof))))):
                        break
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                return hscript_Expr.EBlock(a)
            elif (tmp == 11):
                a = list()
                tk = self.token()
                while ((tk != hscript_Token.TBkClose) and (((not self.resumeErrors) or ((tk != hscript_Token.TEof))))):
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                    x = self.parseExpr()
                    a.append(x)
                    tk = self.token()
                    if (tk == hscript_Token.TComma):
                        tk = self.token()
                if ((len(a) == 1) and (((a[0] if 0 < len(a) else None) is not None))):
                    _g = (a[0] if 0 < len(a) else None)
                    tmp = _g.index
                    if (tmp == 10):
                        _g1 = _g.params[0]
                        _g1 = _g.params[1]
                        def _hx_local_2():
                            _hx_local_0 = self
                            _hx_local_1 = _hx_local_0.uid
                            _hx_local_0.uid = (_hx_local_1 + 1)
                            return _hx_local_1
                        tmp = ("__a_" + Std.string(_hx_local_2()))
                        e = hscript_Expr.EBlock([hscript_Expr.EVar(tmp,None,hscript_Expr.EArrayDecl([])), self.mapCompr(tmp,(a[0] if 0 < len(a) else None)), hscript_Expr.EIdent(tmp)])
                        return self.parseExprNext(e)
                    elif (tmp == 11):
                        _g1 = _g.params[0]
                        _g1 = _g.params[1]
                        _g1 = _g.params[2]
                        def _hx_local_5():
                            _hx_local_3 = self
                            _hx_local_4 = _hx_local_3.uid
                            _hx_local_3.uid = (_hx_local_4 + 1)
                            return _hx_local_4
                        tmp = ("__a_" + Std.string(_hx_local_5()))
                        e = hscript_Expr.EBlock([hscript_Expr.EVar(tmp,None,hscript_Expr.EArrayDecl([])), self.mapCompr(tmp,(a[0] if 0 < len(a) else None)), hscript_Expr.EIdent(tmp)])
                        return self.parseExprNext(e)
                    elif (tmp == 24):
                        _g1 = _g.params[0]
                        _g1 = _g.params[1]
                        def _hx_local_8():
                            _hx_local_6 = self
                            _hx_local_7 = _hx_local_6.uid
                            _hx_local_6.uid = (_hx_local_7 + 1)
                            return _hx_local_7
                        tmp = ("__a_" + Std.string(_hx_local_8()))
                        e = hscript_Expr.EBlock([hscript_Expr.EVar(tmp,None,hscript_Expr.EArrayDecl([])), self.mapCompr(tmp,(a[0] if 0 < len(a) else None)), hscript_Expr.EIdent(tmp)])
                        return self.parseExprNext(e)
                    else:
                        pass
                return self.parseExprNext(hscript_Expr.EArrayDecl(a))
            elif (tmp == 15):
                id = tk.params[0]
                if self.allowMetadata:
                    args = self.parseMetaArgs()
                    return hscript_Expr.EMeta(id,args,self.parseExpr())
                else:
                    return self.unexpected(tk)
            else:
                return self.unexpected(tk)

    def parseLambda(self,args,pmin):
        while True:
            id = self.getIdent()
            t = (self.parseType() if (self.maybe(hscript_Token.TDoubleDot)) else None)
            args.append(_hx_AnonObject({'name': id, 't': t}))
            tk = self.token()
            if (tk is None):
                self.unexpected(tk)
                break
            else:
                tmp = tk.index
                if (tmp == 5):
                    break
                elif (tmp == 9):
                    pass
                else:
                    self.unexpected(tk)
                    break
        t = self.token()
        if (not Type.enumEq(t,hscript_Token.TOp("->"))):
            self.unexpected(t)
        eret = self.parseExpr()
        return hscript_Expr.EFunction(args,hscript_Expr.EReturn(eret))

    def parseMetaArgs(self):
        tk = self.token()
        if (tk != hscript_Token.TPOpen):
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            return None
        args = []
        tk = self.token()
        if (tk != hscript_Token.TPClose):
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            while True:
                x = self.parseExpr()
                args.append(x)
                _g = self.token()
                if (_g is None):
                    tk = _g
                    self.unexpected(tk)
                else:
                    tmp = _g.index
                    if (tmp == 5):
                        break
                    elif (tmp == 9):
                        pass
                    else:
                        tk1 = _g
                        self.unexpected(tk1)
        return args

    def mapCompr(self,tmp,e):
        if (e is None):
            return None
        edef = None
        edef1 = e.index
        if (edef1 == 3):
            e2 = e.params[0]
            edef = hscript_Expr.EParent(self.mapCompr(tmp,e2))
        elif (edef1 == 4):
            _g = e.params[0]
            if (len(_g) == 1):
                e1 = (_g[0] if 0 < len(_g) else None)
                edef = hscript_Expr.EBlock([self.mapCompr(tmp,e1)])
            else:
                edef = hscript_Expr.ECall(hscript_Expr.EField(hscript_Expr.EIdent(tmp),"push"),[e])
        elif (edef1 == 9):
            cond = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            edef = (hscript_Expr.EIf(cond,self.mapCompr(tmp,e1),None) if ((e2 is None)) else hscript_Expr.ECall(hscript_Expr.EField(hscript_Expr.EIdent(tmp),"push"),[e]))
        elif (edef1 == 10):
            cond = e.params[0]
            e2 = e.params[1]
            edef = hscript_Expr.EWhile(cond,self.mapCompr(tmp,e2))
        elif (edef1 == 11):
            v = e.params[0]
            it = e.params[1]
            e2 = e.params[2]
            edef = hscript_Expr.EFor(v,it,self.mapCompr(tmp,e2))
        elif (edef1 == 24):
            cond = e.params[0]
            e2 = e.params[1]
            edef = hscript_Expr.EDoWhile(cond,self.mapCompr(tmp,e2))
        else:
            edef = hscript_Expr.ECall(hscript_Expr.EField(hscript_Expr.EIdent(tmp),"push"),[e])
        return edef

    def makeUnop(self,op,e):
        if ((e is None) and self.resumeErrors):
            return None
        tmp = e.index
        if (tmp == 6):
            bop = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            return hscript_Expr.EBinop(bop,self.makeUnop(op,e1),e2)
        elif (tmp == 22):
            e1 = e.params[0]
            e2 = e.params[1]
            e3 = e.params[2]
            return hscript_Expr.ETernary(self.makeUnop(op,e1),e2,e3)
        else:
            return hscript_Expr.EUnop(op,True,e)

    def makeBinop(self,op,e1,e):
        if ((e is None) and self.resumeErrors):
            return hscript_Expr.EBinop(op,e1,e)
        tmp = e.index
        if (tmp == 6):
            op2 = e.params[0]
            e2 = e.params[1]
            e3 = e.params[2]
            if ((self.opPriority.h.get(op,None) <= self.opPriority.h.get(op2,None)) and (not (op in self.opRightAssoc.h))):
                return hscript_Expr.EBinop(op2,self.makeBinop(op,e1,e2),e3)
            else:
                return hscript_Expr.EBinop(op,e1,e)
        elif (tmp == 22):
            e2 = e.params[0]
            e3 = e.params[1]
            e4 = e.params[2]
            if (op in self.opRightAssoc.h):
                return hscript_Expr.EBinop(op,e1,e)
            else:
                return hscript_Expr.ETernary(self.makeBinop(op,e1,e2),e3,e4)
        else:
            return hscript_Expr.EBinop(op,e1,e)

    def parseStructure(self,id):
        id1 = id
        _hx_local_0 = len(id1)
        if (_hx_local_0 == 5):
            if (id1 == "break"):
                return hscript_Expr.EBreak
            elif (id1 == "throw"):
                e = self.parseExpr()
                return hscript_Expr.EThrow(e)
            elif (id1 == "while"):
                econd = self.parseExpr()
                e = self.parseExpr()
                return hscript_Expr.EWhile(econd,e)
            else:
                return None
        elif (_hx_local_0 == 4):
            if (id1 == "else"):
                return self.unexpected(hscript_Token.TId(id))
            else:
                return None
        elif (_hx_local_0 == 3):
            if (id1 == "for"):
                t = self.token()
                if (t != hscript_Token.TPOpen):
                    self.unexpected(t)
                vname = self.getIdent()
                t = self.token()
                if (not Type.enumEq(t,hscript_Token.TId("in"))):
                    self.unexpected(t)
                eiter = self.parseExpr()
                t = self.token()
                if (t != hscript_Token.TPClose):
                    self.unexpected(t)
                e = self.parseExpr()
                return hscript_Expr.EFor(vname,eiter,e)
            elif (id1 == "new"):
                a = list()
                x = self.getIdent()
                a.append(x)
                while True:
                    tk = self.token()
                    if (tk is None):
                        self.unexpected(tk)
                        break
                    else:
                        tmp = tk.index
                        if (tmp == 4):
                            break
                        elif (tmp == 8):
                            x = self.getIdent()
                            a.append(x)
                        else:
                            self.unexpected(tk)
                            break
                args = self.parseExprList(hscript_Token.TPClose)
                return hscript_Expr.ENew(".".join([python_Boot.toString1(x1,'') for x1 in a]),args)
            elif (id1 == "try"):
                e = self.parseExpr()
                t = self.token()
                if (not Type.enumEq(t,hscript_Token.TId("catch"))):
                    self.unexpected(t)
                t = self.token()
                if (t != hscript_Token.TPOpen):
                    self.unexpected(t)
                vname = self.getIdent()
                t = self.token()
                if (t != hscript_Token.TDoubleDot):
                    self.unexpected(t)
                t = None
                if self.allowTypes:
                    t = self.parseType()
                else:
                    t1 = self.token()
                    if (not Type.enumEq(t1,hscript_Token.TId("Dynamic"))):
                        self.unexpected(t1)
                t1 = self.token()
                if (t1 != hscript_Token.TPClose):
                    self.unexpected(t1)
                ec = self.parseExpr()
                return hscript_Expr.ETry(e,vname,t,ec)
            elif (id1 == "var"):
                ident = self.getIdent()
                tk = self.token()
                t = None
                if ((tk == hscript_Token.TDoubleDot) and self.allowTypes):
                    t = self.parseType()
                    tk = self.token()
                e = None
                if Type.enumEq(tk,hscript_Token.TOp("=")):
                    e = self.parseExpr()
                else:
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                return hscript_Expr.EVar(ident,t,e)
            else:
                return None
        elif (_hx_local_0 == 8):
            if (id1 == "continue"):
                return hscript_Expr.EContinue
            elif (id1 == "function"):
                tk = self.token()
                name = None
                if (tk is None):
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                elif (tk.index == 2):
                    id = tk.params[0]
                    name = id
                else:
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                inf = self.parseFunctionDecl()
                return hscript_Expr.EFunction(inf.args,inf.body,name,inf.ret)
            else:
                return None
        elif (_hx_local_0 == 2):
            if (id1 == "do"):
                e = self.parseExpr()
                tk = self.token()
                if (tk is None):
                    self.unexpected(tk)
                elif (tk.index == 2):
                    if (tk.params[0] != "while"):
                        self.unexpected(tk)
                else:
                    self.unexpected(tk)
                econd = self.parseExpr()
                return hscript_Expr.EDoWhile(econd,e)
            elif (id1 == "if"):
                t = self.token()
                if (t != hscript_Token.TPOpen):
                    self.unexpected(t)
                cond = self.parseExpr()
                t = self.token()
                if (t != hscript_Token.TPClose):
                    self.unexpected(t)
                e1 = self.parseExpr()
                e2 = None
                semic = False
                tk = self.token()
                if (tk == hscript_Token.TSemicolon):
                    semic = True
                    tk = self.token()
                if Type.enumEq(tk,hscript_Token.TId("else")):
                    e2 = self.parseExpr()
                else:
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(tk,_this.head)
                    if semic:
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(hscript_Token.TSemicolon,_this.head)
                return hscript_Expr.EIf(cond,e1,e2)
            else:
                return None
        elif (_hx_local_0 == 6):
            if (id1 == "inline"):
                if (not self.maybe(hscript_Token.TId("function"))):
                    self.unexpected(hscript_Token.TId("inline"))
                return self.parseStructure("function")
            elif (id1 == "return"):
                tk = self.token()
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
                e = (None if ((tk == hscript_Token.TSemicolon)) else self.parseExpr())
                return hscript_Expr.EReturn(e)
            elif (id1 == "switch"):
                e = self.parseExpr()
                _hx_def = None
                cases = []
                t = self.token()
                if (t != hscript_Token.TBrOpen):
                    self.unexpected(t)
                while True:
                    tk = self.token()
                    if (tk is None):
                        self.unexpected(tk)
                        break
                    else:
                        tmp = tk.index
                        if (tmp == 2):
                            _g = tk.params[0]
                            _hx_local_1 = len(_g)
                            if (_hx_local_1 == 4):
                                if (_g == "case"):
                                    c = _hx_AnonObject({'values': [], 'expr': None})
                                    cases.append(c)
                                    while True:
                                        e1 = self.parseExpr()
                                        _this = c.values
                                        _this.append(e1)
                                        tk = self.token()
                                        if (tk is None):
                                            self.unexpected(tk)
                                            break
                                        else:
                                            tmp1 = tk.index
                                            if (tmp1 == 9):
                                                pass
                                            elif (tmp1 == 14):
                                                break
                                            else:
                                                self.unexpected(tk)
                                                break
                                    exprs = []
                                    while True:
                                        tk = self.token()
                                        _this1 = self.tokens
                                        _this1.head = haxe_ds_GenericCell(tk,_this1.head)
                                        if (tk is None):
                                            self.parseFullExpr(exprs)
                                        else:
                                            tmp2 = tk.index
                                            if (tmp2 == 0):
                                                if self.resumeErrors:
                                                    break
                                                else:
                                                    self.parseFullExpr(exprs)
                                            elif (tmp2 == 2):
                                                _g1 = tk.params[0]
                                                _hx_local_2 = len(_g1)
                                                if (_hx_local_2 == 4):
                                                    if (_g1 == "case"):
                                                        break
                                                    else:
                                                        self.parseFullExpr(exprs)
                                                elif (_hx_local_2 == 7):
                                                    if (_g1 == "default"):
                                                        break
                                                    else:
                                                        self.parseFullExpr(exprs)
                                                else:
                                                    self.parseFullExpr(exprs)
                                            elif (tmp2 == 7):
                                                break
                                            else:
                                                self.parseFullExpr(exprs)
                                    c.expr = ((exprs[0] if 0 < len(exprs) else None) if ((len(exprs) == 1)) else (hscript_Expr.EBlock([]) if ((len(exprs) == 0)) else hscript_Expr.EBlock(exprs)))
                                else:
                                    self.unexpected(tk)
                                    break
                            elif (_hx_local_1 == 7):
                                if (_g == "default"):
                                    if (_hx_def is not None):
                                        self.unexpected(tk)
                                    t = self.token()
                                    if (t != hscript_Token.TDoubleDot):
                                        self.unexpected(t)
                                    exprs1 = []
                                    while True:
                                        tk = self.token()
                                        _this2 = self.tokens
                                        _this2.head = haxe_ds_GenericCell(tk,_this2.head)
                                        if (tk is None):
                                            self.parseFullExpr(exprs1)
                                        else:
                                            tmp3 = tk.index
                                            if (tmp3 == 0):
                                                if self.resumeErrors:
                                                    break
                                                else:
                                                    self.parseFullExpr(exprs1)
                                            elif (tmp3 == 2):
                                                _g2 = tk.params[0]
                                                _hx_local_3 = len(_g2)
                                                if (_hx_local_3 == 4):
                                                    if (_g2 == "case"):
                                                        break
                                                    else:
                                                        self.parseFullExpr(exprs1)
                                                elif (_hx_local_3 == 7):
                                                    if (_g2 == "default"):
                                                        break
                                                    else:
                                                        self.parseFullExpr(exprs1)
                                                else:
                                                    self.parseFullExpr(exprs1)
                                            elif (tmp3 == 7):
                                                break
                                            else:
                                                self.parseFullExpr(exprs1)
                                    _hx_def = ((exprs1[0] if 0 < len(exprs1) else None) if ((len(exprs1) == 1)) else (hscript_Expr.EBlock([]) if ((len(exprs1) == 0)) else hscript_Expr.EBlock(exprs1)))
                                else:
                                    self.unexpected(tk)
                                    break
                            else:
                                self.unexpected(tk)
                                break
                        elif (tmp == 7):
                            break
                        else:
                            self.unexpected(tk)
                            break
                return hscript_Expr.ESwitch(e,cases,_hx_def)
            else:
                return None
        else:
            return None

    def parseExprNext(self,e1):
        tk = self.token()
        if (tk is None):
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            return e1
        else:
            tmp = tk.index
            if (tmp == 3):
                op = tk.params[0]
                if (op == "->"):
                    tmp = e1.index
                    if (tmp == 1):
                        i = e1.params[0]
                        eret = self.parseExpr()
                        return hscript_Expr.EFunction([_hx_AnonObject({'name': i})],hscript_Expr.EReturn(eret))
                    elif (tmp == 3):
                        _hx_tmp = e1.params[0]
                        if (_hx_tmp.index == 1):
                            i = _hx_tmp.params[0]
                            eret = self.parseExpr()
                            return hscript_Expr.EFunction([_hx_AnonObject({'name': i})],hscript_Expr.EReturn(eret))
                    elif (tmp == 26):
                        _hx_tmp = e1.params[0]
                        if (_hx_tmp.index == 1):
                            i = _hx_tmp.params[0]
                            t = e1.params[1]
                            eret = self.parseExpr()
                            return hscript_Expr.EFunction([_hx_AnonObject({'name': i, 't': t})],hscript_Expr.EReturn(eret))
                    else:
                        pass
                    self.unexpected(tk)
                if (self.opPriority.h.get(op,None) == -1):
                    tmp = None
                    if (not self.isBlock(e1)):
                        if (e1.index == 3):
                            _g = e1.params[0]
                            tmp = True
                        else:
                            tmp = False
                    else:
                        tmp = True
                    if tmp:
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(tk,_this.head)
                        return e1
                    return self.parseExprNext(hscript_Expr.EUnop(op,False,e1))
                return self.makeBinop(op,e1,self.parseExpr())
            elif (tmp == 4):
                return self.parseExprNext(hscript_Expr.ECall(e1,self.parseExprList(hscript_Token.TPClose)))
            elif (tmp == 8):
                field = self.getIdent()
                return self.parseExprNext(hscript_Expr.EField(e1,field))
            elif (tmp == 11):
                e2 = self.parseExpr()
                t = self.token()
                if (t != hscript_Token.TBkClose):
                    self.unexpected(t)
                return self.parseExprNext(hscript_Expr.EArray(e1,e2))
            elif (tmp == 13):
                e2 = self.parseExpr()
                t = self.token()
                if (t != hscript_Token.TDoubleDot):
                    self.unexpected(t)
                e3 = self.parseExpr()
                return hscript_Expr.ETernary(e1,e2,e3)
            else:
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
                return e1

    def parseFunctionArgs(self):
        args = list()
        tk = self.token()
        if (tk != hscript_Token.TPClose):
            done = False
            while (not done):
                name = None
                opt = False
                if (tk is not None):
                    if (tk.index == 13):
                        opt = True
                        tk = self.token()
                if (tk is None):
                    self.unexpected(tk)
                    break
                elif (tk.index == 2):
                    id = tk.params[0]
                    name = id
                else:
                    self.unexpected(tk)
                    break
                arg = _hx_AnonObject({'name': name})
                args.append(arg)
                if opt:
                    Reflect.setField(arg,"opt",True)
                if self.allowTypes:
                    if self.maybe(hscript_Token.TDoubleDot):
                        Reflect.setField(arg,"t",self.parseType())
                    if self.maybe(hscript_Token.TOp("=")):
                        Reflect.setField(arg,"value",self.parseExpr())
                tk = self.token()
                if (tk is None):
                    self.unexpected(tk)
                else:
                    tmp = tk.index
                    if (tmp == 5):
                        done = True
                    elif (tmp == 9):
                        tk = self.token()
                    else:
                        self.unexpected(tk)
        return args

    def parseFunctionDecl(self):
        t = self.token()
        if (t != hscript_Token.TPOpen):
            self.unexpected(t)
        args = self.parseFunctionArgs()
        ret = None
        if self.allowTypes:
            tk = self.token()
            if (tk != hscript_Token.TDoubleDot):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
            else:
                ret = self.parseType()
        return _hx_AnonObject({'args': args, 'ret': ret, 'body': self.parseExpr()})

    def parsePath(self):
        path = [self.getIdent()]
        while True:
            t = self.token()
            if (t != hscript_Token.TDot):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(t,_this.head)
                break
            x = self.getIdent()
            path.append(x)
        return path

    def parseType(self):
        _gthis = self
        t = self.token()
        if (t is None):
            return self.unexpected(t)
        else:
            tmp = t.index
            if (tmp == 2):
                v = t.params[0]
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(t,_this.head)
                path = self.parsePath()
                params = None
                t = self.token()
                if (t is None):
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(t,_this.head)
                elif (t.index == 3):
                    op = t.params[0]
                    if (op == "<"):
                        params = []
                        while True:
                            x = self.parseType()
                            params.append(x)
                            t = self.token()
                            if (t is not None):
                                tmp = t.index
                                if (tmp == 3):
                                    op = t.params[0]
                                    if (op == ">"):
                                        break
                                    if (HxString.charCodeAt(op,0) == 62):
                                        _this = self.tokens
                                        _this.head = haxe_ds_GenericCell(hscript_Token.TOp(HxString.substr(op,1,None)),_this.head)
                                        break
                                elif (tmp == 9):
                                    continue
                                else:
                                    pass
                            self.unexpected(t)
                            break
                    else:
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(t,_this.head)
                else:
                    _this = self.tokens
                    _this.head = haxe_ds_GenericCell(t,_this.head)
                return self.parseTypeNext(hscript_CType.CTPath(path,params))
            elif (tmp == 4):
                a = self.token()
                b = self.token()
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(b,_this.head)
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(a,_this.head)
                def _hx_local_0(args):
                    _g = _gthis.token()
                    if (_g is None):
                        t = _g
                        _gthis.unexpected(t)
                    elif (_g.index == 3):
                        if (_g.params[0] != "->"):
                            t = _g
                            _gthis.unexpected(t)
                    else:
                        t = _g
                        _gthis.unexpected(t)
                    return hscript_CType.CTFun(args,_gthis.parseType())
                withReturn = _hx_local_0
                if (a is None):
                    t1 = self.parseType()
                    _g = self.token()
                    if (_g is None):
                        t2 = _g
                        return self.unexpected(t2)
                    else:
                        tmp = _g.index
                        if (tmp == 5):
                            return self.parseTypeNext(hscript_CType.CTParent(t1))
                        elif (tmp == 9):
                            args = [t1]
                            while True:
                                x = self.parseType()
                                args.append(x)
                                if (not self.maybe(hscript_Token.TComma)):
                                    break
                            t1 = self.token()
                            if (t1 != hscript_Token.TPClose):
                                self.unexpected(t1)
                            return withReturn(args)
                        else:
                            t1 = _g
                            return self.unexpected(t1)
                else:
                    tmp = a.index
                    if (tmp == 2):
                        _g = a.params[0]
                        if (b is None):
                            t1 = self.parseType()
                            _g = self.token()
                            if (_g is None):
                                t2 = _g
                                return self.unexpected(t2)
                            else:
                                tmp = _g.index
                                if (tmp == 5):
                                    return self.parseTypeNext(hscript_CType.CTParent(t1))
                                elif (tmp == 9):
                                    args = [t1]
                                    while True:
                                        x = self.parseType()
                                        args.append(x)
                                        if (not self.maybe(hscript_Token.TComma)):
                                            break
                                    t1 = self.token()
                                    if (t1 != hscript_Token.TPClose):
                                        self.unexpected(t1)
                                    return withReturn(args)
                                else:
                                    t1 = _g
                                    return self.unexpected(t1)
                        elif (b.index == 14):
                            _g = []
                            _g1 = 0
                            _g2 = self.parseFunctionArgs()
                            while (_g1 < len(_g2)):
                                arg = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                                _g1 = (_g1 + 1)
                                _g3 = Reflect.field(arg,"value")
                                if (_g3 is not None):
                                    v = _g3
                                    if (not self.resumeErrors):
                                        raise haxe_Exception.thrown(hscript_Error.ECustom("Default values not allowed in function types"))
                                x = hscript_CType.CTNamed(arg.name,(hscript_CType.CTOpt(Reflect.field(arg,"t")) if (Reflect.field(arg,"opt")) else Reflect.field(arg,"t")))
                                _g.append(x)
                            args = _g
                            return withReturn(args)
                        else:
                            t1 = self.parseType()
                            _g = self.token()
                            if (_g is None):
                                t2 = _g
                                return self.unexpected(t2)
                            else:
                                tmp = _g.index
                                if (tmp == 5):
                                    return self.parseTypeNext(hscript_CType.CTParent(t1))
                                elif (tmp == 9):
                                    args = [t1]
                                    while True:
                                        x = self.parseType()
                                        args.append(x)
                                        if (not self.maybe(hscript_Token.TComma)):
                                            break
                                    t1 = self.token()
                                    if (t1 != hscript_Token.TPClose):
                                        self.unexpected(t1)
                                    return withReturn(args)
                                else:
                                    t1 = _g
                                    return self.unexpected(t1)
                    elif (tmp == 5):
                        _g = []
                        _g1 = 0
                        _g2 = self.parseFunctionArgs()
                        while (_g1 < len(_g2)):
                            arg = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                            _g1 = (_g1 + 1)
                            _g3 = Reflect.field(arg,"value")
                            if (_g3 is not None):
                                v = _g3
                                if (not self.resumeErrors):
                                    raise haxe_Exception.thrown(hscript_Error.ECustom("Default values not allowed in function types"))
                            x = hscript_CType.CTNamed(arg.name,(hscript_CType.CTOpt(Reflect.field(arg,"t")) if (Reflect.field(arg,"opt")) else Reflect.field(arg,"t")))
                            _g.append(x)
                        args = _g
                        return withReturn(args)
                    else:
                        t1 = self.parseType()
                        _g = self.token()
                        if (_g is None):
                            t2 = _g
                            return self.unexpected(t2)
                        else:
                            tmp = _g.index
                            if (tmp == 5):
                                return self.parseTypeNext(hscript_CType.CTParent(t1))
                            elif (tmp == 9):
                                args = [t1]
                                while True:
                                    x = self.parseType()
                                    args.append(x)
                                    if (not self.maybe(hscript_Token.TComma)):
                                        break
                                t1 = self.token()
                                if (t1 != hscript_Token.TPClose):
                                    self.unexpected(t1)
                                return withReturn(args)
                            else:
                                t1 = _g
                                return self.unexpected(t1)
            elif (tmp == 6):
                fields = []
                meta = None
                while True:
                    t = self.token()
                    if (t is None):
                        self.unexpected(t)
                        break
                    else:
                        tmp = t.index
                        if (tmp == 2):
                            _g = t.params[0]
                            if (_g == "var"):
                                name = self.getIdent()
                                t1 = self.token()
                                if (t1 != hscript_Token.TDoubleDot):
                                    self.unexpected(t1)
                                x = _hx_AnonObject({'name': name, 't': self.parseType(), 'meta': meta})
                                fields.append(x)
                                meta = None
                                t2 = self.token()
                                if (t2 != hscript_Token.TSemicolon):
                                    self.unexpected(t2)
                            else:
                                name1 = _g
                                t3 = self.token()
                                if (t3 != hscript_Token.TDoubleDot):
                                    self.unexpected(t3)
                                x1 = _hx_AnonObject({'name': name1, 't': self.parseType(), 'meta': meta})
                                fields.append(x1)
                                t = self.token()
                                if (t is None):
                                    self.unexpected(t)
                                else:
                                    tmp1 = t.index
                                    if (tmp1 == 7):
                                        break
                                    elif (tmp1 == 9):
                                        pass
                                    else:
                                        self.unexpected(t)
                        elif (tmp == 7):
                            break
                        elif (tmp == 15):
                            name2 = t.params[0]
                            if (meta is None):
                                meta = []
                            x2 = _hx_AnonObject({'name': name2, 'params': self.parseMetaArgs()})
                            meta.append(x2)
                        else:
                            self.unexpected(t)
                            break
                return self.parseTypeNext(hscript_CType.CTAnon(fields))
            else:
                return self.unexpected(t)

    def parseTypeNext(self,t):
        tk = self.token()
        if (tk is None):
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            return t
        elif (tk.index == 3):
            op = tk.params[0]
            if (op != "->"):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
                return t
        else:
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            return t
        t2 = self.parseType()
        if (t2.index == 1):
            _g = t2.params[1]
            args = t2.params[0]
            args.insert(0, t)
            return t2
        else:
            return hscript_CType.CTFun([t],t2)

    def parseExprList(self,etk):
        args = list()
        tk = self.token()
        if (tk == etk):
            return args
        _this = self.tokens
        _this.head = haxe_ds_GenericCell(tk,_this.head)
        while True:
            x = self.parseExpr()
            args.append(x)
            tk = self.token()
            if (tk is None):
                if (tk == etk):
                    break
                self.unexpected(tk)
                break
            elif (tk.index != 9):
                if (tk == etk):
                    break
                self.unexpected(tk)
                break
        return args

    def parseModule(self,content,origin = None):
        if (origin is None):
            origin = "hscript"
        self.initParser(origin)
        self.input = content
        self.readPos = 0
        self.allowTypes = True
        self.allowMetadata = True
        decls = []
        while True:
            tk = self.token()
            if (tk == hscript_Token.TEof):
                break
            _this = self.tokens
            _this.head = haxe_ds_GenericCell(tk,_this.head)
            x = self.parseModuleDecl()
            decls.append(x)
        return decls

    def parseMetadata(self):
        meta = []
        while True:
            tk = self.token()
            if (tk is None):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
                break
            elif (tk.index == 15):
                name = tk.params[0]
                x = _hx_AnonObject({'name': name, 'params': self.parseMetaArgs()})
                meta.append(x)
            else:
                _this1 = self.tokens
                _this1.head = haxe_ds_GenericCell(tk,_this1.head)
                break
        return meta

    def parseParams(self):
        if self.maybe(hscript_Token.TOp("<")):
            if (not self.resumeErrors):
                raise haxe_Exception.thrown(hscript_Error.EInvalidOp("Unsupported class type parameters"))
        return _hx_AnonObject({})

    def parseModuleDecl(self):
        meta = self.parseMetadata()
        ident = self.getIdent()
        isPrivate = False
        isExtern = False
        while True:
            ident1 = ident
            _hx_local_0 = len(ident1)
            if (_hx_local_0 == 7):
                if (ident1 == "private"):
                    isPrivate = True
                else:
                    break
            elif (_hx_local_0 == 6):
                if (ident1 == "extern"):
                    isExtern = True
                else:
                    break
            else:
                break
            ident = self.getIdent()
        ident1 = ident
        _hx_local_1 = len(ident1)
        if (_hx_local_1 == 5):
            if (ident1 == "class"):
                name = self.getIdent()
                params = self.parseParams()
                extend = None
                implement = []
                while True:
                    t = self.token()
                    if (t is None):
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(t,_this.head)
                        break
                    elif (t.index == 2):
                        _g = t.params[0]
                        _hx_local_2 = len(_g)
                        if (_hx_local_2 == 10):
                            if (_g == "implements"):
                                x = self.parseType()
                                implement.append(x)
                            else:
                                _this1 = self.tokens
                                _this1.head = haxe_ds_GenericCell(t,_this1.head)
                                break
                        elif (_hx_local_2 == 7):
                            if (_g == "extends"):
                                extend = self.parseType()
                            else:
                                _this1 = self.tokens
                                _this1.head = haxe_ds_GenericCell(t,_this1.head)
                                break
                        else:
                            _this1 = self.tokens
                            _this1.head = haxe_ds_GenericCell(t,_this1.head)
                            break
                    else:
                        _this2 = self.tokens
                        _this2.head = haxe_ds_GenericCell(t,_this2.head)
                        break
                fields = []
                t = self.token()
                if (t != hscript_Token.TBrOpen):
                    self.unexpected(t)
                while (not self.maybe(hscript_Token.TBrClose)):
                    x = self.parseField()
                    fields.append(x)
                return hscript_ModuleDecl.DClass(_hx_AnonObject({'name': name, 'meta': meta, 'params': params, 'extend': extend, 'implement': implement, 'fields': fields, 'isPrivate': isPrivate, 'isExtern': isExtern}))
            else:
                self.unexpected(hscript_Token.TId(ident))
        elif (_hx_local_1 == 7):
            if (ident1 == "package"):
                path = self.parsePath()
                t = self.token()
                if (t != hscript_Token.TSemicolon):
                    self.unexpected(t)
                return hscript_ModuleDecl.DPackage(path)
            elif (ident1 == "typedef"):
                name = self.getIdent()
                params = self.parseParams()
                t = self.token()
                if (not Type.enumEq(t,hscript_Token.TOp("="))):
                    self.unexpected(t)
                t = self.parseType()
                return hscript_ModuleDecl.DTypedef(_hx_AnonObject({'name': name, 'meta': meta, 'params': params, 'isPrivate': isPrivate, 't': t}))
            else:
                self.unexpected(hscript_Token.TId(ident))
        elif (_hx_local_1 == 6):
            if (ident1 == "import"):
                path = [self.getIdent()]
                star = False
                while True:
                    t = self.token()
                    if (t != hscript_Token.TDot):
                        _this = self.tokens
                        _this.head = haxe_ds_GenericCell(t,_this.head)
                        break
                    t = self.token()
                    if (t is None):
                        self.unexpected(t)
                    else:
                        tmp = t.index
                        if (tmp == 2):
                            id = t.params[0]
                            path.append(id)
                        elif (tmp == 3):
                            if (t.params[0] == "*"):
                                star = True
                            else:
                                self.unexpected(t)
                        else:
                            self.unexpected(t)
                t = self.token()
                if (t != hscript_Token.TSemicolon):
                    self.unexpected(t)
                return hscript_ModuleDecl.DImport(path,star)
            else:
                self.unexpected(hscript_Token.TId(ident))
        else:
            self.unexpected(hscript_Token.TId(ident))
        return None

    def parseField(self):
        meta = self.parseMetadata()
        access = []
        while True:
            id = self.getIdent()
            id1 = id
            _hx_local_0 = len(id1)
            if (_hx_local_0 == 5):
                if (id1 == "macro"):
                    access.append(hscript_FieldAccess.AMacro)
                else:
                    self.unexpected(hscript_Token.TId(id))
                    break
            elif (_hx_local_0 == 7):
                if (id1 == "private"):
                    access.append(hscript_FieldAccess.APrivate)
                else:
                    self.unexpected(hscript_Token.TId(id))
                    break
            elif (_hx_local_0 == 3):
                if (id1 == "var"):
                    name1 = self.getIdent()
                    get = None
                    _hx_set = None
                    if self.maybe(hscript_Token.TPOpen):
                        get = self.getIdent()
                        t = self.token()
                        if (t != hscript_Token.TComma):
                            self.unexpected(t)
                        _hx_set = self.getIdent()
                        t1 = self.token()
                        if (t1 != hscript_Token.TPClose):
                            self.unexpected(t1)
                    _hx_type = (self.parseType() if (self.maybe(hscript_Token.TDoubleDot)) else None)
                    expr = (self.parseExpr() if (self.maybe(hscript_Token.TOp("="))) else None)
                    if (expr is not None):
                        if self.isBlock(expr):
                            self.maybe(hscript_Token.TSemicolon)
                        else:
                            t2 = self.token()
                            if (t2 != hscript_Token.TSemicolon):
                                self.unexpected(t2)
                    else:
                        tmp = None
                        if (_hx_type is not None):
                            if (_hx_type is None):
                                tmp = False
                            elif (_hx_type.index == 2):
                                _g = _hx_type.params[0]
                                tmp = True
                            else:
                                tmp = False
                        else:
                            tmp = False
                        if tmp:
                            self.maybe(hscript_Token.TSemicolon)
                        else:
                            t3 = self.token()
                            if (t3 != hscript_Token.TSemicolon):
                                self.unexpected(t3)
                    return _hx_AnonObject({'name': name1, 'meta': meta, 'access': access, 'kind': hscript_FieldKind.KVar(_hx_AnonObject({'get': get, 'set': _hx_set, 'type': _hx_type, 'expr': expr}))})
                else:
                    self.unexpected(hscript_Token.TId(id))
                    break
            elif (_hx_local_0 == 8):
                if (id1 == "function"):
                    name = self.getIdent()
                    inf = self.parseFunctionDecl()
                    return _hx_AnonObject({'name': name, 'meta': meta, 'access': access, 'kind': hscript_FieldKind.KFunction(_hx_AnonObject({'args': inf.args, 'expr': inf.body, 'ret': inf.ret}))})
                elif (id1 == "override"):
                    access.append(hscript_FieldAccess.AOverride)
                else:
                    self.unexpected(hscript_Token.TId(id))
                    break
            elif (_hx_local_0 == 6):
                if (id1 == "inline"):
                    access.append(hscript_FieldAccess.AInline)
                elif (id1 == "public"):
                    access.append(hscript_FieldAccess.APublic)
                elif (id1 == "static"):
                    access.append(hscript_FieldAccess.AStatic)
                else:
                    self.unexpected(hscript_Token.TId(id))
                    break
            else:
                self.unexpected(hscript_Token.TId(id))
                break
        return None

    def readChar(self):
        s = self.input
        index = self.readPos
        self.readPos = (self.readPos + 1)
        if (index >= len(s)):
            return -1
        else:
            return ord(s[index])

    def readString(self,until):
        c = 0
        b_b = python_lib_io_StringIO()
        esc = False
        old = self.line
        s = self.input
        while True:
            s = self.input
            index = self.readPos
            self.readPos = (self.readPos + 1)
            c = (-1 if ((index >= len(s))) else ord(s[index]))
            if (c == -1):
                self.line = old
                if (not self.resumeErrors):
                    raise haxe_Exception.thrown(hscript_Error.EUnterminatedString)
                break
            if esc:
                esc = False
                c1 = c
                if (((c1 == 92) or ((c1 == 39))) or ((c1 == 34))):
                    b_b.write("".join(map(chr,[c])))
                elif (c1 == 47):
                    if self.allowJSON:
                        b_b.write("".join(map(chr,[c])))
                    else:
                        self.invalidChar(c)
                elif (c1 == 110):
                    b_b.write("".join(map(chr,[10])))
                elif (c1 == 114):
                    b_b.write("".join(map(chr,[13])))
                elif (c1 == 116):
                    b_b.write("".join(map(chr,[9])))
                elif (c1 == 117):
                    if (not self.allowJSON):
                        self.invalidChar(c)
                    k = 0
                    _g = 0
                    while (_g < 4):
                        i = _g
                        _g = (_g + 1)
                        k = (k << 4)
                        s1 = self.input
                        index1 = self.readPos
                        self.readPos = (self.readPos + 1)
                        char = (-1 if ((index1 >= len(s1))) else ord(s1[index1]))
                        char1 = char
                        if ((((((((((char1 == 57) or ((char1 == 56))) or ((char1 == 55))) or ((char1 == 54))) or ((char1 == 53))) or ((char1 == 52))) or ((char1 == 51))) or ((char1 == 50))) or ((char1 == 49))) or ((char1 == 48))):
                            k = (k + ((char - 48)))
                        elif ((((((char1 == 70) or ((char1 == 69))) or ((char1 == 68))) or ((char1 == 67))) or ((char1 == 66))) or ((char1 == 65))):
                            k = (k + ((char - 55)))
                        elif ((((((char1 == 102) or ((char1 == 101))) or ((char1 == 100))) or ((char1 == 99))) or ((char1 == 98))) or ((char1 == 97))):
                            k = (k + ((char - 87)))
                        else:
                            if (char == -1):
                                self.line = old
                                if (not self.resumeErrors):
                                    raise haxe_Exception.thrown(hscript_Error.EUnterminatedString)
                            self.invalidChar(char)
                    b_b.write("".join(map(chr,[k])))
                else:
                    self.invalidChar(c)
            elif (c == 92):
                esc = True
            elif (c == until):
                break
            else:
                if (c == 10):
                    _hx_local_4 = self
                    _hx_local_5 = _hx_local_4.line
                    _hx_local_4.line = (_hx_local_5 + 1)
                    _hx_local_5
                b_b.write("".join(map(chr,[c])))
        return b_b.getvalue()

    def token(self):
        if (self.tokens.head is not None):
            _this = self.tokens
            k = _this.head
            if (k is None):
                return None
            else:
                _this.head = k.next
                return k.elt
        char = None
        if (self.char < 0):
            s = self.input
            index = self.readPos
            self.readPos = (self.readPos + 1)
            char = (-1 if ((index >= len(s))) else ord(s[index]))
        else:
            char = self.char
            self.char = -1
        while True:
            if (char == -1):
                self.char = char
                return hscript_Token.TEof
            char1 = char
            if (char1 == 0):
                return hscript_Token.TEof
            elif (char1 == 10):
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.line
                _hx_local_0.line = (_hx_local_1 + 1)
                _hx_local_1
            elif (((char1 == 32) or ((char1 == 13))) or ((char1 == 9))):
                pass
            elif (char1 == 35):
                s = self.input
                index = self.readPos
                self.readPos = (self.readPos + 1)
                char = (-1 if ((index >= len(s))) else ord(s[index]))
                if (self.idents[char] if char >= 0 and char < len(self.idents) else None):
                    id = "".join(map(chr,[char]))
                    while True:
                        s1 = self.input
                        index1 = self.readPos
                        self.readPos = (self.readPos + 1)
                        char = (-1 if ((index1 >= len(s1))) else ord(s1[index1]))
                        if (not (self.idents[char] if char >= 0 and char < len(self.idents) else None)):
                            self.char = char
                            return self.preprocess(id)
                        id = (("null" if id is None else id) + HxOverrides.stringOrNull("".join(map(chr,[char]))))
                self.invalidChar(char)
            elif ((char1 == 39) or ((char1 == 34))):
                return hscript_Token.TConst(hscript_Const.CString(self.readString(char)))
            elif (char1 == 40):
                return hscript_Token.TPOpen
            elif (char1 == 41):
                return hscript_Token.TPClose
            elif (char1 == 44):
                return hscript_Token.TComma
            elif (char1 == 46):
                s2 = self.input
                index2 = self.readPos
                self.readPos = (self.readPos + 1)
                char = (-1 if ((index2 >= len(s2))) else ord(s2[index2]))
                char2 = char
                if (char2 == 46):
                    s3 = self.input
                    index3 = self.readPos
                    self.readPos = (self.readPos + 1)
                    char = (-1 if ((index3 >= len(s3))) else ord(s3[index3]))
                    if (char != 46):
                        self.invalidChar(char)
                    return hscript_Token.TOp("...")
                elif ((((((((((char2 == 57) or ((char2 == 56))) or ((char2 == 55))) or ((char2 == 54))) or ((char2 == 53))) or ((char2 == 52))) or ((char2 == 51))) or ((char2 == 50))) or ((char2 == 49))) or ((char2 == 48))):
                    n = (char - 48)
                    exp = 1
                    while True:
                        s4 = self.input
                        index4 = self.readPos
                        self.readPos = (self.readPos + 1)
                        char = (-1 if ((index4 >= len(s4))) else ord(s4[index4]))
                        exp = (exp * 10)
                        char3 = char
                        if ((((((((((char3 == 57) or ((char3 == 56))) or ((char3 == 55))) or ((char3 == 54))) or ((char3 == 53))) or ((char3 == 52))) or ((char3 == 51))) or ((char3 == 50))) or ((char3 == 49))) or ((char3 == 48))):
                            n = ((n * 10) + ((char - 48)))
                        else:
                            self.char = char
                            return hscript_Token.TConst(hscript_Const.CFloat((n / exp)))
                else:
                    self.char = char
                    return hscript_Token.TDot
            elif ((((((((((char1 == 57) or ((char1 == 56))) or ((char1 == 55))) or ((char1 == 54))) or ((char1 == 53))) or ((char1 == 52))) or ((char1 == 51))) or ((char1 == 50))) or ((char1 == 49))) or ((char1 == 48))):
                n1 = (((char - 48)) * 1.0)
                exp1 = 0.
                while True:
                    s5 = self.input
                    index5 = self.readPos
                    self.readPos = (self.readPos + 1)
                    char = (-1 if ((index5 >= len(s5))) else ord(s5[index5]))
                    exp1 = (exp1 * 10)
                    char4 = char
                    if (char4 == 46):
                        if (exp1 > 0):
                            tmp = None
                            if (exp1 == 10):
                                s6 = self.input
                                index6 = self.readPos
                                self.readPos = (self.readPos + 1)
                                tmp = (((-1 if ((index6 >= len(s6))) else ord(s6[index6]))) == 46)
                            else:
                                tmp = False
                            if tmp:
                                _this = self.tokens
                                _this.head = haxe_ds_GenericCell(hscript_Token.TOp("..."),_this.head)
                                i = None
                                try:
                                    i = int(n1)
                                except BaseException as _g:
                                    None
                                    i = None
                                i1 = i
                                return hscript_Token.TConst((hscript_Const.CInt(i1) if ((i1 == n1)) else hscript_Const.CFloat(n1)))
                            self.invalidChar(char)
                        exp1 = 1.
                    elif ((((((((((char4 == 57) or ((char4 == 56))) or ((char4 == 55))) or ((char4 == 54))) or ((char4 == 53))) or ((char4 == 52))) or ((char4 == 51))) or ((char4 == 50))) or ((char4 == 49))) or ((char4 == 48))):
                        n1 = ((n1 * 10) + ((char - 48)))
                    elif ((char4 == 101) or ((char4 == 69))):
                        tk = self.token()
                        pow = None
                        if (tk is None):
                            _this1 = self.tokens
                            _this1.head = haxe_ds_GenericCell(tk,_this1.head)
                        else:
                            tmp1 = tk.index
                            if (tmp1 == 1):
                                _g1 = tk.params[0]
                                if (_g1.index == 0):
                                    e = _g1.params[0]
                                    pow = e
                                else:
                                    _this2 = self.tokens
                                    _this2.head = haxe_ds_GenericCell(tk,_this2.head)
                            elif (tmp1 == 3):
                                if (tk.params[0] == "-"):
                                    tk = self.token()
                                    if (tk is None):
                                        _this3 = self.tokens
                                        _this3.head = haxe_ds_GenericCell(tk,_this3.head)
                                    elif (tk.index == 1):
                                        _g2 = tk.params[0]
                                        if (_g2.index == 0):
                                            e1 = _g2.params[0]
                                            pow = -e1
                                        else:
                                            _this4 = self.tokens
                                            _this4.head = haxe_ds_GenericCell(tk,_this4.head)
                                    else:
                                        _this5 = self.tokens
                                        _this5.head = haxe_ds_GenericCell(tk,_this5.head)
                                else:
                                    _this6 = self.tokens
                                    _this6.head = haxe_ds_GenericCell(tk,_this6.head)
                            else:
                                _this7 = self.tokens
                                _this7.head = haxe_ds_GenericCell(tk,_this7.head)
                        if (pow is None):
                            self.invalidChar(char)
                        return hscript_Token.TConst(hscript_Const.CFloat((((Math.pow(10,pow) / exp1) * n1) * 10)))
                    elif (char4 == 120):
                        if ((n1 > 0) or ((exp1 > 0))):
                            self.invalidChar(char)
                        n2 = 0
                        while True:
                            s7 = self.input
                            index7 = self.readPos
                            self.readPos = (self.readPos + 1)
                            char = (-1 if ((index7 >= len(s7))) else ord(s7[index7]))
                            char5 = char
                            if ((((((((((char5 == 57) or ((char5 == 56))) or ((char5 == 55))) or ((char5 == 54))) or ((char5 == 53))) or ((char5 == 52))) or ((char5 == 51))) or ((char5 == 50))) or ((char5 == 49))) or ((char5 == 48))):
                                n2 = ((((n2 << 4)) + char) - 48)
                            elif ((((((char5 == 70) or ((char5 == 69))) or ((char5 == 68))) or ((char5 == 67))) or ((char5 == 66))) or ((char5 == 65))):
                                n2 = (((n2 << 4)) + ((char - 55)))
                            elif ((((((char5 == 102) or ((char5 == 101))) or ((char5 == 100))) or ((char5 == 99))) or ((char5 == 98))) or ((char5 == 97))):
                                n2 = (((n2 << 4)) + ((char - 87)))
                            else:
                                self.char = char
                                return hscript_Token.TConst(hscript_Const.CInt(n2))
                    else:
                        self.char = char
                        i2 = None
                        try:
                            i2 = int(n1)
                        except BaseException as _g3:
                            None
                            i2 = None
                        i3 = i2
                        return hscript_Token.TConst((hscript_Const.CFloat(((n1 * 10) / exp1)) if ((exp1 > 0)) else (hscript_Const.CInt(i3) if ((i3 == n1)) else hscript_Const.CFloat(n1))))
            elif (char1 == 58):
                return hscript_Token.TDoubleDot
            elif (char1 == 59):
                return hscript_Token.TSemicolon
            elif (char1 == 61):
                s8 = self.input
                index8 = self.readPos
                self.readPos = (self.readPos + 1)
                char = (-1 if ((index8 >= len(s8))) else ord(s8[index8]))
                if (char == 61):
                    return hscript_Token.TOp("==")
                elif (char == 62):
                    return hscript_Token.TOp("=>")
                self.char = char
                return hscript_Token.TOp("=")
            elif (char1 == 63):
                return hscript_Token.TQuestion
            elif (char1 == 64):
                s9 = self.input
                index9 = self.readPos
                self.readPos = (self.readPos + 1)
                char = (-1 if ((index9 >= len(s9))) else ord(s9[index9]))
                if ((self.idents[char] if char >= 0 and char < len(self.idents) else None) or ((char == 58))):
                    id1 = "".join(map(chr,[char]))
                    while True:
                        s10 = self.input
                        index10 = self.readPos
                        self.readPos = (self.readPos + 1)
                        char = (-1 if ((index10 >= len(s10))) else ord(s10[index10]))
                        if (not (self.idents[char] if char >= 0 and char < len(self.idents) else None)):
                            self.char = char
                            return hscript_Token.TMeta(id1)
                        id1 = (("null" if id1 is None else id1) + HxOverrides.stringOrNull("".join(map(chr,[char]))))
                self.invalidChar(char)
            elif (char1 == 91):
                return hscript_Token.TBkOpen
            elif (char1 == 93):
                return hscript_Token.TBkClose
            elif (char1 == 123):
                return hscript_Token.TBrOpen
            elif (char1 == 125):
                return hscript_Token.TBrClose
            else:
                if (self.ops[char] if char >= 0 and char < len(self.ops) else None):
                    op = "".join(map(chr,[char]))
                    while True:
                        s11 = self.input
                        index11 = self.readPos
                        self.readPos = (self.readPos + 1)
                        char = (-1 if ((index11 >= len(s11))) else ord(s11[index11]))
                        if (char == -1):
                            char = 0
                        if (not (self.ops[char] if char >= 0 and char < len(self.ops) else None)):
                            self.char = char
                            return hscript_Token.TOp(op)
                        pop = op
                        op = (("null" if op is None else op) + HxOverrides.stringOrNull("".join(map(chr,[char]))))
                        if ((not (op in self.opPriority.h)) and (pop in self.opPriority.h)):
                            if ((op == "//") or ((op == "/*"))):
                                return self.tokenComment(op,char)
                            self.char = char
                            return hscript_Token.TOp(pop)
                if (self.idents[char] if char >= 0 and char < len(self.idents) else None):
                    id2 = "".join(map(chr,[char]))
                    while True:
                        s12 = self.input
                        index12 = self.readPos
                        self.readPos = (self.readPos + 1)
                        char = (-1 if ((index12 >= len(s12))) else ord(s12[index12]))
                        if (char == -1):
                            char = 0
                        if (not (self.idents[char] if char >= 0 and char < len(self.idents) else None)):
                            self.char = char
                            return hscript_Token.TId(id2)
                        id2 = (("null" if id2 is None else id2) + HxOverrides.stringOrNull("".join(map(chr,[char]))))
                self.invalidChar(char)
            s13 = self.input
            index13 = self.readPos
            self.readPos = (self.readPos + 1)
            char = (-1 if ((index13 >= len(s13))) else ord(s13[index13]))

    def preprocValue(self,id):
        return self.preprocesorValues.h.get(id,None)

    def parsePreproCond(self):
        tk = self.token()
        if (tk is None):
            return self.unexpected(tk)
        else:
            tmp = tk.index
            if (tmp == 2):
                id = tk.params[0]
                return hscript_Expr.EIdent(id)
            elif (tmp == 3):
                if (tk.params[0] == "!"):
                    return hscript_Expr.EUnop("!",True,self.parsePreproCond())
                else:
                    return self.unexpected(tk)
            elif (tmp == 4):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(hscript_Token.TPOpen,_this.head)
                return self.parseExpr()
            else:
                return self.unexpected(tk)

    def evalPreproCond(self,e):
        tmp = e.index
        if (tmp == 1):
            id = e.params[0]
            return (self.preprocValue(id) is not None)
        elif (tmp == 3):
            e1 = e.params[0]
            return self.evalPreproCond(e1)
        elif (tmp == 6):
            _g = e.params[1]
            _g1 = e.params[2]
            _g2 = e.params[0]
            if (_g2 == "&&"):
                e1 = _g
                e2 = _g1
                if self.evalPreproCond(e1):
                    return self.evalPreproCond(e2)
                else:
                    return False
            elif (_g2 == "||"):
                e1 = _g
                e2 = _g1
                if (not self.evalPreproCond(e1)):
                    return self.evalPreproCond(e2)
                else:
                    return True
            else:
                if (not self.resumeErrors):
                    raise haxe_Exception.thrown(hscript_Error.EInvalidPreprocessor(("Can't eval " + HxOverrides.stringOrNull(e.tag))))
                return False
        elif (tmp == 7):
            _g = e.params[1]
            if (e.params[0] == "!"):
                e1 = e.params[2]
                return (not self.evalPreproCond(e1))
            else:
                if (not self.resumeErrors):
                    raise haxe_Exception.thrown(hscript_Error.EInvalidPreprocessor(("Can't eval " + HxOverrides.stringOrNull(e.tag))))
                return False
        else:
            if (not self.resumeErrors):
                raise haxe_Exception.thrown(hscript_Error.EInvalidPreprocessor(("Can't eval " + HxOverrides.stringOrNull(e.tag))))
            return False

    def preprocess(self,id):
        id1 = id
        _hx_local_0 = len(id1)
        if (_hx_local_0 == 4):
            if (id1 == "else"):
                if (len(self.preprocStack) > 0):
                    if python_internal_ArrayImpl._get(self.preprocStack, (len(self.preprocStack) - 1)).r:
                        python_internal_ArrayImpl._get(self.preprocStack, (len(self.preprocStack) - 1)).r = False
                        self.skipTokens()
                        return self.token()
                    elif (id == "else"):
                        _this = self.preprocStack
                        if (len(_this) != 0):
                            _this.pop()
                        _this = self.preprocStack
                        _this.append(_hx_AnonObject({'r': True}))
                        return self.token()
                    else:
                        _this = self.preprocStack
                        if (len(_this) != 0):
                            _this.pop()
                        return self.preprocess("if")
                else:
                    return hscript_Token.TPrepro(id)
            else:
                return hscript_Token.TPrepro(id)
        elif (_hx_local_0 == 3):
            if (id1 == "end"):
                if (len(self.preprocStack) > 0):
                    _this = self.preprocStack
                    if (len(_this) != 0):
                        _this.pop()
                    return self.token()
                else:
                    return hscript_Token.TPrepro(id)
            else:
                return hscript_Token.TPrepro(id)
        elif (_hx_local_0 == 6):
            if (id1 == "elseif"):
                if (len(self.preprocStack) > 0):
                    if python_internal_ArrayImpl._get(self.preprocStack, (len(self.preprocStack) - 1)).r:
                        python_internal_ArrayImpl._get(self.preprocStack, (len(self.preprocStack) - 1)).r = False
                        self.skipTokens()
                        return self.token()
                    elif (id == "else"):
                        _this = self.preprocStack
                        if (len(_this) != 0):
                            _this.pop()
                        _this = self.preprocStack
                        _this.append(_hx_AnonObject({'r': True}))
                        return self.token()
                    else:
                        _this = self.preprocStack
                        if (len(_this) != 0):
                            _this.pop()
                        return self.preprocess("if")
                else:
                    return hscript_Token.TPrepro(id)
            else:
                return hscript_Token.TPrepro(id)
        elif (_hx_local_0 == 2):
            if (id1 == "if"):
                e = self.parsePreproCond()
                if self.evalPreproCond(e):
                    _this = self.preprocStack
                    _this.append(_hx_AnonObject({'r': True}))
                    return self.token()
                _this = self.preprocStack
                _this.append(_hx_AnonObject({'r': False}))
                self.skipTokens()
                return self.token()
            else:
                return hscript_Token.TPrepro(id)
        else:
            return hscript_Token.TPrepro(id)

    def skipTokens(self):
        spos = (len(self.preprocStack) - 1)
        obj = (self.preprocStack[spos] if spos >= 0 and spos < len(self.preprocStack) else None)
        pos = self.readPos
        while True:
            tk = self.token()
            if (tk == hscript_Token.TEof):
                if (not self.resumeErrors):
                    raise haxe_Exception.thrown(hscript_Error.EInvalidPreprocessor("Unclosed"))
            if ((self.preprocStack[spos] if spos >= 0 and spos < len(self.preprocStack) else None) != obj):
                _this = self.tokens
                _this.head = haxe_ds_GenericCell(tk,_this.head)
                break

    def tokenComment(self,op,char):
        c = HxString.charCodeAt(op,1)
        s = self.input
        if (c == 47):
            while ((char != 13) and ((char != 10))):
                s = self.input
                index = self.readPos
                self.readPos = (self.readPos + 1)
                char = (-1 if ((index >= len(s))) else ord(s[index]))
                if (char == -1):
                    break
            self.char = char
            return self.token()
        if (c == 42):
            old = self.line
            if (op == "/**/"):
                self.char = char
                return self.token()
            while True:
                while (char != 42):
                    if (char == 10):
                        _hx_local_0 = self
                        _hx_local_1 = _hx_local_0.line
                        _hx_local_0.line = (_hx_local_1 + 1)
                        _hx_local_1
                    s = self.input
                    index = self.readPos
                    self.readPos = (self.readPos + 1)
                    char = (-1 if ((index >= len(s))) else ord(s[index]))
                    if (char == -1):
                        self.line = old
                        if (not self.resumeErrors):
                            raise haxe_Exception.thrown(hscript_Error.EUnterminatedComment)
                        break
                s1 = self.input
                index1 = self.readPos
                self.readPos = (self.readPos + 1)
                char = (-1 if ((index1 >= len(s1))) else ord(s1[index1]))
                if (char == -1):
                    self.line = old
                    if (not self.resumeErrors):
                        raise haxe_Exception.thrown(hscript_Error.EUnterminatedComment)
                    break
                if (char == 47):
                    break
            return self.token()
        self.char = char
        return hscript_Token.TOp(op)

    def constString(self,c):
        tmp = c.index
        if (tmp == 0):
            v = c.params[0]
            return Std.string(v)
        elif (tmp == 1):
            f = c.params[0]
            return Std.string(f)
        elif (tmp == 2):
            s = c.params[0]
            return s
        else:
            pass

    def tokenString(self,t):
        tmp = t.index
        if (tmp == 0):
            return "<eof>"
        elif (tmp == 1):
            c = t.params[0]
            return self.constString(c)
        elif (tmp == 2):
            s = t.params[0]
            return s
        elif (tmp == 3):
            s = t.params[0]
            return s
        elif (tmp == 4):
            return "("
        elif (tmp == 5):
            return ")"
        elif (tmp == 6):
            return "{"
        elif (tmp == 7):
            return "}"
        elif (tmp == 8):
            return "."
        elif (tmp == 9):
            return ","
        elif (tmp == 10):
            return ";"
        elif (tmp == 11):
            return "["
        elif (tmp == 12):
            return "]"
        elif (tmp == 13):
            return "?"
        elif (tmp == 14):
            return ":"
        elif (tmp == 15):
            id = t.params[0]
            return ("@" + ("null" if id is None else id))
        elif (tmp == 16):
            id = t.params[0]
            return ("#" + ("null" if id is None else id))
        else:
            pass

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.line = None
        _hx_o.opChars = None
        _hx_o.identChars = None
        _hx_o.opPriority = None
        _hx_o.opRightAssoc = None
        _hx_o.preprocesorValues = None
        _hx_o.allowJSON = None
        _hx_o.allowTypes = None
        _hx_o.allowMetadata = None
        _hx_o.resumeErrors = None
        _hx_o.input = None
        _hx_o.readPos = None
        _hx_o.char = None
        _hx_o.ops = None
        _hx_o.idents = None
        _hx_o.uid = None
        _hx_o.tokens = None
        _hx_o.preprocStack = None
hscript_Parser._hx_class = hscript_Parser
_hx_classes["hscript.Parser"] = hscript_Parser


