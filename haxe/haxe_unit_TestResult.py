class haxe_unit_TestResult:
    _hx_class_name = "haxe.unit.TestResult"
    __slots__ = ("m_tests", "success")
    _hx_fields = ["m_tests", "success"]
    _hx_methods = ["add", "toString"]

    def __init__(self):
        self.m_tests = haxe_ds_List()
        self.success = True

    def add(self,t):
        self.m_tests.add(t)
        if (not t.success):
            self.success = False

    def toString(self):
        buf_b = python_lib_io_StringIO()
        failures = 0
        _g_head = self.m_tests.h
        while (_g_head is not None):
            val = _g_head.item
            _g_head = _g_head.next
            test = val
            if (test.success == False):
                buf_b.write("* ")
                buf_b.write(Std.string(test.classname))
                buf_b.write("::")
                buf_b.write(Std.string(test.method))
                buf_b.write("()")
                buf_b.write("\n")
                buf_b.write("ERR: ")
                if (test.posInfos is not None):
                    buf_b.write(Std.string(test.posInfos.fileName))
                    buf_b.write(":")
                    buf_b.write(Std.string(test.posInfos.lineNumber))
                    buf_b.write("(")
                    buf_b.write(Std.string(test.posInfos.className))
                    buf_b.write(".")
                    buf_b.write(Std.string(test.posInfos.methodName))
                    buf_b.write(") - ")
                buf_b.write(Std.string(test.error))
                buf_b.write("\n")
                if (test.backtrace is not None):
                    buf_b.write(Std.string(test.backtrace))
                    buf_b.write("\n")
                buf_b.write("\n")
                failures = (failures + 1)
        buf_b.write("\n")
        if (failures == 0):
            buf_b.write("OK ")
        else:
            buf_b.write("FAILED ")
        buf_b.write(Std.string(self.m_tests.length))
        buf_b.write(" tests, ")
        buf_b.write(Std.string(failures))
        buf_b.write(" failed, ")
        buf_b.write(Std.string((self.m_tests.length - failures)))
        buf_b.write(" success")
        buf_b.write("\n")
        return buf_b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.m_tests = None
        _hx_o.success = None
haxe_unit_TestResult._hx_class = haxe_unit_TestResult
_hx_classes["haxe.unit.TestResult"] = haxe_unit_TestResult


