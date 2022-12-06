class haxe_unit_TestRunner:
    _hx_class_name = "haxe.unit.TestRunner"
    __slots__ = ("result", "cases")
    _hx_fields = ["result", "cases"]
    _hx_methods = ["add", "run", "runCase"]
    _hx_statics = ["print", "customTrace"]

    def __init__(self):
        self.result = haxe_unit_TestResult()
        self.cases = haxe_ds_List()

    def add(self,c):
        self.cases.add(c)

    def run(self):
        self.result = haxe_unit_TestResult()
        _g_head = self.cases.h
        while (_g_head is not None):
            val = _g_head.item
            _g_head = _g_head.next
            c = val
            self.runCase(c)
        haxe_unit_TestRunner.print(self.result.toString())
        return self.result.success

    def runCase(self,t):
        old = haxe_Log.trace
        haxe_Log.trace = haxe_unit_TestRunner.customTrace
        cl = Type.getClass(t)
        fields = python_Boot.getInstanceFields(cl)
        haxe_unit_TestRunner.print((("Class: " + HxOverrides.stringOrNull(Type.getClassName(cl))) + " "))
        _g = 0
        while (_g < len(fields)):
            f = (fields[_g] if _g >= 0 and _g < len(fields) else None)
            _g = (_g + 1)
            fname = f
            field = Reflect.field(t,f)
            if (fname.startswith("test") and Reflect.isFunction(field)):
                t.currentTest = haxe_unit_TestStatus()
                t.currentTest.classname = Type.getClassName(cl)
                t.currentTest.method = fname
                t.setup()
                try:
                    Reflect.callMethod(t,field,list())
                    if t.currentTest.done:
                        t.currentTest.success = True
                        haxe_unit_TestRunner.print(".")
                    else:
                        t.currentTest.success = False
                        t.currentTest.error = "(warning) no assert"
                        haxe_unit_TestRunner.print("W")
                except BaseException as _g1:
                    None
                    _g2 = haxe_Exception.caught(_g1).unwrap()
                    if Std.isOfType(_g2,haxe_unit_TestStatus):
                        haxe_unit_TestRunner.print("F")
                        tmp = haxe__CallStack_CallStack_Impl_.exceptionStack()
                        t.currentTest.backtrace = haxe__CallStack_CallStack_Impl_.toString(tmp)
                    else:
                        e = _g2
                        haxe_unit_TestRunner.print("E")
                        tmp1 = Std.string(e)
                        t.currentTest.error = ("exception thrown : " + ("null" if tmp1 is None else tmp1))
                        tmp2 = haxe__CallStack_CallStack_Impl_.exceptionStack()
                        t.currentTest.backtrace = haxe__CallStack_CallStack_Impl_.toString(tmp2)
                self.result.add(t.currentTest)
                t.tearDown()
        haxe_unit_TestRunner.print("\n")
        haxe_Log.trace = old

    @staticmethod
    def print(v):
        python_Lib.printString(Std.string(v))

    @staticmethod
    def customTrace(v,p = None):
        haxe_unit_TestRunner.print((((((HxOverrides.stringOrNull(p.fileName) + ":") + Std.string(p.lineNumber)) + ": ") + Std.string(v)) + "\n"))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.result = None
        _hx_o.cases = None
haxe_unit_TestRunner._hx_class = haxe_unit_TestRunner
_hx_classes["haxe.unit.TestRunner"] = haxe_unit_TestRunner


