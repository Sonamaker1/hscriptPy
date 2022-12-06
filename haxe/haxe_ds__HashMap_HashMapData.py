class haxe_ds__HashMap_HashMapData:
    _hx_class_name = "haxe.ds._HashMap.HashMapData"
    __slots__ = ("keys", "values")
    _hx_fields = ["keys", "values"]

    def __init__(self):
        self.keys = haxe_ds_IntMap()
        self.values = haxe_ds_IntMap()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.keys = None
        _hx_o.values = None
haxe_ds__HashMap_HashMapData._hx_class = haxe_ds__HashMap_HashMapData
_hx_classes["haxe.ds._HashMap.HashMapData"] = haxe_ds__HashMap_HashMapData


