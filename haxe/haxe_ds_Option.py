class haxe_ds_Option(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.ds.Option"
    _hx_constructs = ["Some", "None"]

    @staticmethod
    def Some(v):
        return haxe_ds_Option("Some", 0, (v,))
haxe_ds_Option._hx_None = haxe_ds_Option("None", 1, ())
haxe_ds_Option._hx_class = haxe_ds_Option
_hx_classes["haxe.ds.Option"] = haxe_ds_Option


