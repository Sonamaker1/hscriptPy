class haxe_macro_ExprDef(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ExprDef"
    _hx_constructs = ["EConst", "EArray", "EBinop", "EField", "EParenthesis", "EObjectDecl", "EArrayDecl", "ECall", "ENew", "EUnop", "EVars", "EFunction", "EBlock", "EFor", "EIf", "EWhile", "ESwitch", "ETry", "EReturn", "EBreak", "EContinue", "EUntyped", "EThrow", "ECast", "EDisplay", "EDisplayNew", "ETernary", "ECheckType", "EMeta", "EIs"]

    @staticmethod
    def EConst(c):
        return haxe_macro_ExprDef("EConst", 0, (c,))

    @staticmethod
    def EArray(e1,e2):
        return haxe_macro_ExprDef("EArray", 1, (e1,e2))

    @staticmethod
    def EBinop(op,e1,e2):
        return haxe_macro_ExprDef("EBinop", 2, (op,e1,e2))

    @staticmethod
    def EField(e,field):
        return haxe_macro_ExprDef("EField", 3, (e,field))

    @staticmethod
    def EParenthesis(e):
        return haxe_macro_ExprDef("EParenthesis", 4, (e,))

    @staticmethod
    def EObjectDecl(fields):
        return haxe_macro_ExprDef("EObjectDecl", 5, (fields,))

    @staticmethod
    def EArrayDecl(values):
        return haxe_macro_ExprDef("EArrayDecl", 6, (values,))

    @staticmethod
    def ECall(e,params):
        return haxe_macro_ExprDef("ECall", 7, (e,params))

    @staticmethod
    def ENew(t,params):
        return haxe_macro_ExprDef("ENew", 8, (t,params))

    @staticmethod
    def EUnop(op,postFix,e):
        return haxe_macro_ExprDef("EUnop", 9, (op,postFix,e))

    @staticmethod
    def EVars(vars):
        return haxe_macro_ExprDef("EVars", 10, (vars,))

    @staticmethod
    def EFunction(kind,f):
        return haxe_macro_ExprDef("EFunction", 11, (kind,f))

    @staticmethod
    def EBlock(exprs):
        return haxe_macro_ExprDef("EBlock", 12, (exprs,))

    @staticmethod
    def EFor(it,expr):
        return haxe_macro_ExprDef("EFor", 13, (it,expr))

    @staticmethod
    def EIf(econd,eif,eelse):
        return haxe_macro_ExprDef("EIf", 14, (econd,eif,eelse))

    @staticmethod
    def EWhile(econd,e,normalWhile):
        return haxe_macro_ExprDef("EWhile", 15, (econd,e,normalWhile))

    @staticmethod
    def ESwitch(e,cases,edef):
        return haxe_macro_ExprDef("ESwitch", 16, (e,cases,edef))

    @staticmethod
    def ETry(e,catches):
        return haxe_macro_ExprDef("ETry", 17, (e,catches))

    @staticmethod
    def EReturn(e = None):
        return haxe_macro_ExprDef("EReturn", 18, (e,))

    @staticmethod
    def EUntyped(e):
        return haxe_macro_ExprDef("EUntyped", 21, (e,))

    @staticmethod
    def EThrow(e):
        return haxe_macro_ExprDef("EThrow", 22, (e,))

    @staticmethod
    def ECast(e,t):
        return haxe_macro_ExprDef("ECast", 23, (e,t))

    @staticmethod
    def EDisplay(e,displayKind):
        return haxe_macro_ExprDef("EDisplay", 24, (e,displayKind))

    @staticmethod
    def EDisplayNew(t):
        return haxe_macro_ExprDef("EDisplayNew", 25, (t,))

    @staticmethod
    def ETernary(econd,eif,eelse):
        return haxe_macro_ExprDef("ETernary", 26, (econd,eif,eelse))

    @staticmethod
    def ECheckType(e,t):
        return haxe_macro_ExprDef("ECheckType", 27, (e,t))

    @staticmethod
    def EMeta(s,e):
        return haxe_macro_ExprDef("EMeta", 28, (s,e))

    @staticmethod
    def EIs(e,t):
        return haxe_macro_ExprDef("EIs", 29, (e,t))
haxe_macro_ExprDef.EBreak = haxe_macro_ExprDef("EBreak", 19, ())
haxe_macro_ExprDef.EContinue = haxe_macro_ExprDef("EContinue", 20, ())
haxe_macro_ExprDef._hx_class = haxe_macro_ExprDef
_hx_classes["haxe.macro.ExprDef"] = haxe_macro_ExprDef

