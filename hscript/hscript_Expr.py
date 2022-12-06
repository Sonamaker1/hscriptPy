class hscript_Expr(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.Expr"
    _hx_constructs = ["EConst", "EIdent", "EVar", "EParent", "EBlock", "EField", "EBinop", "EUnop", "ECall", "EIf", "EWhile", "EFor", "EBreak", "EContinue", "EFunction", "EReturn", "EArray", "EArrayDecl", "ENew", "EThrow", "ETry", "EObject", "ETernary", "ESwitch", "EDoWhile", "EMeta", "ECheckType"]

    @staticmethod
    def EConst(c):
        return hscript_Expr("EConst", 0, (c,))

    @staticmethod
    def EIdent(v):
        return hscript_Expr("EIdent", 1, (v,))

    @staticmethod
    def EVar(n,t = None,e= None):
        return hscript_Expr("EVar", 2, (n,t,e))

    @staticmethod
    def EParent(e):
        return hscript_Expr("EParent", 3, (e,))

    @staticmethod
    def EBlock(e):
        return hscript_Expr("EBlock", 4, (e,))

    @staticmethod
    def EField(e,f):
        return hscript_Expr("EField", 5, (e,f))

    @staticmethod
    def EBinop(op,e1,e2):
        return hscript_Expr("EBinop", 6, (op,e1,e2))

    @staticmethod
    def EUnop(op,prefix,e):
        return hscript_Expr("EUnop", 7, (op,prefix,e))

    @staticmethod
    def ECall(e,params):
        return hscript_Expr("ECall", 8, (e,params))

    @staticmethod
    def EIf(cond,e1,e2 = None):
        return hscript_Expr("EIf", 9, (cond,e1,e2))

    @staticmethod
    def EWhile(cond,e):
        return hscript_Expr("EWhile", 10, (cond,e))

    @staticmethod
    def EFor(v,it,e):
        return hscript_Expr("EFor", 11, (v,it,e))

    @staticmethod
    def EFunction(args,e,name = None,ret= None):
        return hscript_Expr("EFunction", 14, (args,e,name,ret))

    @staticmethod
    def EReturn(e = None):
        return hscript_Expr("EReturn", 15, (e,))

    @staticmethod
    def EArray(e,index):
        return hscript_Expr("EArray", 16, (e,index))

    @staticmethod
    def EArrayDecl(e):
        return hscript_Expr("EArrayDecl", 17, (e,))

    @staticmethod
    def ENew(cl,params):
        return hscript_Expr("ENew", 18, (cl,params))

    @staticmethod
    def EThrow(e):
        return hscript_Expr("EThrow", 19, (e,))

    @staticmethod
    def ETry(e,v,t,ecatch):
        return hscript_Expr("ETry", 20, (e,v,t,ecatch))

    @staticmethod
    def EObject(fl):
        return hscript_Expr("EObject", 21, (fl,))

    @staticmethod
    def ETernary(cond,e1,e2):
        return hscript_Expr("ETernary", 22, (cond,e1,e2))

    @staticmethod
    def ESwitch(e,cases,defaultExpr = None):
        return hscript_Expr("ESwitch", 23, (e,cases,defaultExpr))

    @staticmethod
    def EDoWhile(cond,e):
        return hscript_Expr("EDoWhile", 24, (cond,e))

    @staticmethod
    def EMeta(name,args,e):
        return hscript_Expr("EMeta", 25, (name,args,e))

    @staticmethod
    def ECheckType(e,t):
        return hscript_Expr("ECheckType", 26, (e,t))
hscript_Expr.EBreak = hscript_Expr("EBreak", 12, ())
hscript_Expr.EContinue = hscript_Expr("EContinue", 13, ())
hscript_Expr._hx_class = hscript_Expr
_hx_classes["hscript.Expr"] = hscript_Expr


