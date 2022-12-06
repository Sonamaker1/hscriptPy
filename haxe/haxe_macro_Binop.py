class haxe_macro_Binop(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Binop"
    _hx_constructs = ["OpAdd", "OpMult", "OpDiv", "OpSub", "OpAssign", "OpEq", "OpNotEq", "OpGt", "OpGte", "OpLt", "OpLte", "OpAnd", "OpOr", "OpXor", "OpBoolAnd", "OpBoolOr", "OpShl", "OpShr", "OpUShr", "OpMod", "OpAssignOp", "OpInterval", "OpArrow", "OpIn"]

    @staticmethod
    def OpAssignOp(op):
        return haxe_macro_Binop("OpAssignOp", 20, (op,))
haxe_macro_Binop.OpAdd = haxe_macro_Binop("OpAdd", 0, ())
haxe_macro_Binop.OpMult = haxe_macro_Binop("OpMult", 1, ())
haxe_macro_Binop.OpDiv = haxe_macro_Binop("OpDiv", 2, ())
haxe_macro_Binop.OpSub = haxe_macro_Binop("OpSub", 3, ())
haxe_macro_Binop.OpAssign = haxe_macro_Binop("OpAssign", 4, ())
haxe_macro_Binop.OpEq = haxe_macro_Binop("OpEq", 5, ())
haxe_macro_Binop.OpNotEq = haxe_macro_Binop("OpNotEq", 6, ())
haxe_macro_Binop.OpGt = haxe_macro_Binop("OpGt", 7, ())
haxe_macro_Binop.OpGte = haxe_macro_Binop("OpGte", 8, ())
haxe_macro_Binop.OpLt = haxe_macro_Binop("OpLt", 9, ())
haxe_macro_Binop.OpLte = haxe_macro_Binop("OpLte", 10, ())
haxe_macro_Binop.OpAnd = haxe_macro_Binop("OpAnd", 11, ())
haxe_macro_Binop.OpOr = haxe_macro_Binop("OpOr", 12, ())
haxe_macro_Binop.OpXor = haxe_macro_Binop("OpXor", 13, ())
haxe_macro_Binop.OpBoolAnd = haxe_macro_Binop("OpBoolAnd", 14, ())
haxe_macro_Binop.OpBoolOr = haxe_macro_Binop("OpBoolOr", 15, ())
haxe_macro_Binop.OpShl = haxe_macro_Binop("OpShl", 16, ())
haxe_macro_Binop.OpShr = haxe_macro_Binop("OpShr", 17, ())
haxe_macro_Binop.OpUShr = haxe_macro_Binop("OpUShr", 18, ())
haxe_macro_Binop.OpMod = haxe_macro_Binop("OpMod", 19, ())
haxe_macro_Binop.OpInterval = haxe_macro_Binop("OpInterval", 21, ())
haxe_macro_Binop.OpArrow = haxe_macro_Binop("OpArrow", 22, ())
haxe_macro_Binop.OpIn = haxe_macro_Binop("OpIn", 23, ())
haxe_macro_Binop._hx_class = haxe_macro_Binop
_hx_classes["haxe.macro.Binop"] = haxe_macro_Binop

