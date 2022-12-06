class haxe_unit_TestStatus:
    _hx_class_name = "haxe.unit.TestStatus"
    __slots__ = ("done", "success", "error", "method", "classname", "posInfos", "backtrace")
    _hx_fields = ["done", "success", "error", "method", "classname", "posInfos", "backtrace"]

    def __init__(self):
        self.backtrace = None
        self.posInfos = None
        self.classname = None
        self.method = None
        self.error = None
        self.done = False
        self.success = False

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.done = None
        _hx_o.success = None
        _hx_o.error = None
        _hx_o.method = None
        _hx_o.classname = None
        _hx_o.posInfos = None
        _hx_o.backtrace = None
haxe_unit_TestStatus._hx_class = haxe_unit_TestStatus
_hx_classes["haxe.unit.TestStatus"] = haxe_unit_TestStatus


