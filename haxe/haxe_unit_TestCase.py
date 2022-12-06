class haxe_unit_TestCase:
    _hx_class_name = "haxe.unit.TestCase"
    __slots__ = ("currentTest",)
    _hx_fields = ["currentTest"]
    _hx_methods = ["setup", "tearDown", "print", "assertTrue", "assertFalse", "assertEquals"]

    def __init__(self):
        self.currentTest = None

    def setup(self):
        pass

    def tearDown(self):
        pass

    def print(self,v):
        haxe_unit_TestRunner.print(v)

    def assertTrue(self,b,c = None):
        self.currentTest.done = True
        if (b != True):
            self.currentTest.success = False
            self.currentTest.error = "expected true but was false"
            self.currentTest.posInfos = c
            raise haxe_Exception.thrown(self.currentTest)

    def assertFalse(self,b,c = None):
        self.currentTest.done = True
        if (b == True):
            self.currentTest.success = False
            self.currentTest.error = "expected false but was true"
            self.currentTest.posInfos = c
            raise haxe_Exception.thrown(self.currentTest)

    def assertEquals(self,expected,actual,c = None):
        self.currentTest.done = True
        if not HxOverrides.eq(actual,expected):
            self.currentTest.success = False
            tmp = ((("expected '" + Std.string(expected)) + "' but was '") + Std.string(actual))
            self.currentTest.error = (("null" if tmp is None else tmp) + "'")
            self.currentTest.posInfos = c
            raise haxe_Exception.thrown(self.currentTest)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.currentTest = None
haxe_unit_TestCase._hx_class = haxe_unit_TestCase
_hx_classes["haxe.unit.TestCase"] = haxe_unit_TestCase


