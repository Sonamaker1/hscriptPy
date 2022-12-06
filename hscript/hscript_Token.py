class hscript_Token(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.Token"
    _hx_constructs = ["TEof", "TConst", "TId", "TOp", "TPOpen", "TPClose", "TBrOpen", "TBrClose", "TDot", "TComma", "TSemicolon", "TBkOpen", "TBkClose", "TQuestion", "TDoubleDot", "TMeta", "TPrepro"]

    @staticmethod
    def TConst(c):
        return hscript_Token("TConst", 1, (c,))

    @staticmethod
    def TId(s):
        return hscript_Token("TId", 2, (s,))

    @staticmethod
    def TOp(s):
        return hscript_Token("TOp", 3, (s,))

    @staticmethod
    def TMeta(s):
        return hscript_Token("TMeta", 15, (s,))

    @staticmethod
    def TPrepro(s):
        return hscript_Token("TPrepro", 16, (s,))
hscript_Token.TEof = hscript_Token("TEof", 0, ())
hscript_Token.TPOpen = hscript_Token("TPOpen", 4, ())
hscript_Token.TPClose = hscript_Token("TPClose", 5, ())
hscript_Token.TBrOpen = hscript_Token("TBrOpen", 6, ())
hscript_Token.TBrClose = hscript_Token("TBrClose", 7, ())
hscript_Token.TDot = hscript_Token("TDot", 8, ())
hscript_Token.TComma = hscript_Token("TComma", 9, ())
hscript_Token.TSemicolon = hscript_Token("TSemicolon", 10, ())
hscript_Token.TBkOpen = hscript_Token("TBkOpen", 11, ())
hscript_Token.TBkClose = hscript_Token("TBkClose", 12, ())
hscript_Token.TQuestion = hscript_Token("TQuestion", 13, ())
hscript_Token.TDoubleDot = hscript_Token("TDoubleDot", 14, ())
hscript_Token._hx_class = hscript_Token
_hx_classes["hscript.Token"] = hscript_Token


