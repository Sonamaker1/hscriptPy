class haxe_ds_TreeNode:
    _hx_class_name = "haxe.ds.TreeNode"
    __slots__ = ("left", "right", "key", "value", "_height")
    _hx_fields = ["left", "right", "key", "value", "_height"]
    _hx_methods = ["toString"]

    def __init__(self,l,k,v,r,h = None):
        if (h is None):
            h = -1
        self._height = None
        self.left = l
        self.key = k
        self.value = v
        self.right = r
        if (h == -1):
            tmp = None
            _this = self.left
            _this1 = self.right
            if (((0 if ((_this is None)) else _this._height)) > ((0 if ((_this1 is None)) else _this1._height))):
                _this = self.left
                tmp = (0 if ((_this is None)) else _this._height)
            else:
                _this = self.right
                tmp = (0 if ((_this is None)) else _this._height)
            self._height = (tmp + 1)
        else:
            self._height = h

    def toString(self):
        return ((HxOverrides.stringOrNull((("" if ((self.left is None)) else (HxOverrides.stringOrNull(self.left.toString()) + ", ")))) + (((("" + Std.string(self.key)) + "=") + Std.string(self.value)))) + HxOverrides.stringOrNull((("" if ((self.right is None)) else (", " + HxOverrides.stringOrNull(self.right.toString()))))))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.left = None
        _hx_o.right = None
        _hx_o.key = None
        _hx_o.value = None
        _hx_o._height = None
haxe_ds_TreeNode._hx_class = haxe_ds_TreeNode
_hx_classes["haxe.ds.TreeNode"] = haxe_ds_TreeNode


