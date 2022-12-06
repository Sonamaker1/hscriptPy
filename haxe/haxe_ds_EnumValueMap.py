class haxe_ds_EnumValueMap(haxe_ds_BalancedTree):
    _hx_class_name = "haxe.ds.EnumValueMap"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["compare", "compareArgs", "compareArg", "copy"]
    _hx_statics = []
    _hx_interfaces = [haxe_IMap]
    _hx_super = haxe_ds_BalancedTree


    def __init__(self):
        super().__init__()

    def compare(self,k1,k2):
        d = (k1.index - k2.index)
        if (d != 0):
            return d
        p1 = list(k1.params)
        p2 = list(k2.params)
        if ((len(p1) == 0) and ((len(p2) == 0))):
            return 0
        return self.compareArgs(p1,p2)

    def compareArgs(self,a1,a2):
        ld = (len(a1) - len(a2))
        if (ld != 0):
            return ld
        _g = 0
        _g1 = len(a1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            d = self.compareArg((a1[i] if i >= 0 and i < len(a1) else None),(a2[i] if i >= 0 and i < len(a2) else None))
            if (d != 0):
                return d
        return 0

    def compareArg(self,v1,v2):
        if (Reflect.isEnumValue(v1) and Reflect.isEnumValue(v2)):
            return self.compare(v1,v2)
        elif (Std.isOfType(v1,list) and Std.isOfType(v2,list)):
            return self.compareArgs(v1,v2)
        else:
            return Reflect.compare(v1,v2)

    def copy(self):
        copied = haxe_ds_EnumValueMap()
        copied.root = self.root
        return copied

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
haxe_ds_EnumValueMap._hx_class = haxe_ds_EnumValueMap
_hx_classes["haxe.ds.EnumValueMap"] = haxe_ds_EnumValueMap


