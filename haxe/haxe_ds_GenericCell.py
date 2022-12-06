class haxe_ds_GenericCell:
    _hx_class_name = "haxe.ds.GenericCell"
    __slots__ = ("elt", "next")
    _hx_fields = ["elt", "next"]

    def __init__(self,elt,next):
        self.elt = elt
        self.next = next

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.elt = None
        _hx_o.next = None
haxe_ds_GenericCell._hx_class = haxe_ds_GenericCell
_hx_classes["haxe.ds.GenericCell"] = haxe_ds_GenericCell


