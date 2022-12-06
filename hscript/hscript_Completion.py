class hscript_Completion:
    _hx_class_name = "hscript.Completion"
    __slots__ = ("expr", "t")
    _hx_fields = ["expr", "t"]

    def __init__(self,expr,t):
        self.expr = expr
        self.t = t

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.expr = None
        _hx_o.t = None
hscript_Completion._hx_class = hscript_Completion
_hx_classes["hscript.Completion"] = hscript_Completion


