class hscript_Printer:
    _hx_class_name = "hscript.Printer"
    __slots__ = ("buf", "tabs")
    _hx_fields = ["buf", "tabs"]
    _hx_methods = ["exprToString", "typeToString", "add", "type", "addType", "expr"]
    _hx_statics = ["toString", "errorToString"]

    def __init__(self):
        self.tabs = None
        self.buf = None

    def exprToString(self,e):
        self.buf = StringBuf()
        self.tabs = ""
        self.expr(e)
        return self.buf.b.getvalue()

    def typeToString(self,t):
        self.buf = StringBuf()
        self.tabs = ""
        self.type(t)
        return self.buf.b.getvalue()

    def add(self,s):
        _this = self.buf
        s1 = Std.string(s)
        _this.b.write(s1)

    def type(self,t):
        tmp = t.index
        if (tmp == 0):
            path = t.params[0]
            params = t.params[1]
            s = ".".join([python_Boot.toString1(x1,'') for x1 in path])
            _this = self.buf
            s1 = Std.string(s)
            _this.b.write(s1)
            if (params is not None):
                self.buf.b.write("<")
                first = True
                _g = 0
                while (_g < len(params)):
                    p = (params[_g] if _g >= 0 and _g < len(params) else None)
                    _g = (_g + 1)
                    if first:
                        first = False
                    else:
                        self.buf.b.write(", ")
                    self.type(p)
                self.buf.b.write(">")
        elif (tmp == 1):
            _g = t.params[0]
            _g1 = t.params[1]
            args = _g
            ret = _g1
            def _hx_local_1(a):
                if (a.index == 5):
                    _g = a.params[0]
                    _g = a.params[1]
                    return True
                else:
                    return False
            if Lambda.exists(args,_hx_local_1):
                self.buf.b.write("(")
                _g2 = 0
                while (_g2 < len(args)):
                    a = (args[_g2] if _g2 >= 0 and _g2 < len(args) else None)
                    _g2 = (_g2 + 1)
                    if (a.index == 5):
                        _g3 = a.params[0]
                        _g4 = a.params[1]
                        self.type(a)
                    else:
                        self.type(hscript_CType.CTNamed("_",a))
                self.buf.b.write(")->")
                self.type(ret)
            else:
                args = _g
                ret = _g1
                if (len(args) == 0):
                    self.buf.b.write("Void -> ")
                else:
                    _g = 0
                    while (_g < len(args)):
                        a = (args[_g] if _g >= 0 and _g < len(args) else None)
                        _g = (_g + 1)
                        self.type(a)
                        self.buf.b.write(" -> ")
                self.type(ret)
        elif (tmp == 2):
            fields = t.params[0]
            self.buf.b.write("{")
            first = True
            _g = 0
            while (_g < len(fields)):
                f = (fields[_g] if _g >= 0 and _g < len(fields) else None)
                _g = (_g + 1)
                if first:
                    first = False
                    self.buf.b.write(" ")
                else:
                    self.buf.b.write(", ")
                _this = self.buf
                s = Std.string((HxOverrides.stringOrNull(f.name) + " : "))
                _this.b.write(s)
                self.type(f.t)
            self.buf.b.write(("}" if first else " }"))
        elif (tmp == 3):
            t1 = t.params[0]
            self.buf.b.write("(")
            self.type(t1)
            self.buf.b.write(")")
        elif (tmp == 4):
            t1 = t.params[0]
            self.buf.b.write("?")
            self.type(t1)
        elif (tmp == 5):
            name = t.params[0]
            t1 = t.params[1]
            _this = self.buf
            s = Std.string(name)
            _this.b.write(s)
            self.buf.b.write(":")
            self.type(t1)
        else:
            pass

    def addType(self,t):
        if (t is not None):
            self.buf.b.write(" : ")
            self.type(t)

    def expr(self,e):
        if (e is None):
            self.buf.b.write("??NULL??")
            return
        tmp = e.index
        if (tmp == 0):
            c = e.params[0]
            tmp = c.index
            if (tmp == 0):
                i = c.params[0]
                _this = self.buf
                s = Std.string(i)
                _this.b.write(s)
            elif (tmp == 1):
                f = c.params[0]
                _this = self.buf
                s = Std.string(f)
                _this.b.write(s)
            elif (tmp == 2):
                s = c.params[0]
                self.buf.b.write("\"")
                _this = s.split("\"")
                _this1 = "\\\"".join([python_Boot.toString1(x1,'') for x1 in _this])
                _this = _this1.split("\n")
                _this1 = "\\n".join([python_Boot.toString1(x1,'') for x1 in _this])
                _this = _this1.split("\r")
                _this1 = "\\r".join([python_Boot.toString1(x1,'') for x1 in _this])
                _this = _this1.split("\t")
                s = "\\t".join([python_Boot.toString1(x1,'') for x1 in _this])
                _this = self.buf
                s1 = Std.string(s)
                _this.b.write(s1)
                self.buf.b.write("\"")
            else:
                pass
        elif (tmp == 1):
            v = e.params[0]
            _this = self.buf
            s = Std.string(v)
            _this.b.write(s)
        elif (tmp == 2):
            n = e.params[0]
            t = e.params[1]
            e1 = e.params[2]
            _this = self.buf
            s = Std.string(("var " + ("null" if n is None else n)))
            _this.b.write(s)
            self.addType(t)
            if (e1 is not None):
                self.buf.b.write(" = ")
                self.expr(e1)
        elif (tmp == 3):
            e1 = e.params[0]
            self.buf.b.write("(")
            self.expr(e1)
            self.buf.b.write(")")
        elif (tmp == 4):
            el = e.params[0]
            if (len(el) == 0):
                self.buf.b.write("{}")
            else:
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.tabs
                _hx_local_0.tabs = (("null" if _hx_local_1 is None else _hx_local_1) + "\t")
                _hx_local_0.tabs
                self.buf.b.write("{\n")
                _g = 0
                while (_g < len(el)):
                    e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                    _g = (_g + 1)
                    _this = self.buf
                    s = Std.string(self.tabs)
                    _this.b.write(s)
                    self.expr(e1)
                    self.buf.b.write(";\n")
                self.tabs = HxString.substr(self.tabs,1,None)
                self.buf.b.write("}")
        elif (tmp == 5):
            e1 = e.params[0]
            f = e.params[1]
            self.expr(e1)
            _this = self.buf
            s = Std.string(("." + ("null" if f is None else f)))
            _this.b.write(s)
        elif (tmp == 6):
            op = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            self.expr(e1)
            _this = self.buf
            s = Std.string(((" " + ("null" if op is None else op)) + " "))
            _this.b.write(s)
            self.expr(e2)
        elif (tmp == 7):
            op = e.params[0]
            pre = e.params[1]
            e1 = e.params[2]
            if pre:
                _this = self.buf
                s = Std.string(op)
                _this.b.write(s)
                self.expr(e1)
            else:
                self.expr(e1)
                _this = self.buf
                s = Std.string(op)
                _this.b.write(s)
        elif (tmp == 8):
            e1 = e.params[0]
            args = e.params[1]
            if (e1 is None):
                self.expr(e1)
            else:
                tmp = e1.index
                if (tmp == 0):
                    _g = e1.params[0]
                    self.expr(e1)
                elif (tmp == 1):
                    _g = e1.params[0]
                    self.expr(e1)
                elif (tmp == 5):
                    _g = e1.params[0]
                    _g = e1.params[1]
                    self.expr(e1)
                else:
                    self.buf.b.write("(")
                    self.expr(e1)
                    self.buf.b.write(")")
            self.buf.b.write("(")
            first = True
            _g = 0
            while (_g < len(args)):
                a = (args[_g] if _g >= 0 and _g < len(args) else None)
                _g = (_g + 1)
                if first:
                    first = False
                else:
                    self.buf.b.write(", ")
                self.expr(a)
            self.buf.b.write(")")
        elif (tmp == 9):
            cond = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            self.buf.b.write("if( ")
            self.expr(cond)
            self.buf.b.write(" ) ")
            self.expr(e1)
            if (e2 is not None):
                self.buf.b.write(" else ")
                self.expr(e2)
        elif (tmp == 10):
            cond = e.params[0]
            e1 = e.params[1]
            self.buf.b.write("while( ")
            self.expr(cond)
            self.buf.b.write(" ) ")
            self.expr(e1)
        elif (tmp == 11):
            v = e.params[0]
            it = e.params[1]
            e1 = e.params[2]
            _this = self.buf
            s = Std.string((("for( " + ("null" if v is None else v)) + " in "))
            _this.b.write(s)
            self.expr(it)
            self.buf.b.write(" ) ")
            self.expr(e1)
        elif (tmp == 12):
            self.buf.b.write("break")
        elif (tmp == 13):
            self.buf.b.write("continue")
        elif (tmp == 14):
            params = e.params[0]
            e1 = e.params[1]
            name = e.params[2]
            ret = e.params[3]
            self.buf.b.write("function")
            if (name is not None):
                _this = self.buf
                s = Std.string((" " + ("null" if name is None else name)))
                _this.b.write(s)
            self.buf.b.write("(")
            first = True
            _g = 0
            while (_g < len(params)):
                a = (params[_g] if _g >= 0 and _g < len(params) else None)
                _g = (_g + 1)
                if first:
                    first = False
                else:
                    self.buf.b.write(", ")
                if Reflect.field(a,"opt"):
                    self.buf.b.write("?")
                _this = self.buf
                s = Std.string(a.name)
                _this.b.write(s)
                self.addType(Reflect.field(a,"t"))
            self.buf.b.write(")")
            self.addType(ret)
            self.buf.b.write(" ")
            self.expr(e1)
        elif (tmp == 15):
            e1 = e.params[0]
            self.buf.b.write("return")
            if (e1 is not None):
                self.buf.b.write(" ")
                self.expr(e1)
        elif (tmp == 16):
            e1 = e.params[0]
            index = e.params[1]
            self.expr(e1)
            self.buf.b.write("[")
            self.expr(index)
            self.buf.b.write("]")
        elif (tmp == 17):
            el = e.params[0]
            self.buf.b.write("[")
            first = True
            _g = 0
            while (_g < len(el)):
                e1 = (el[_g] if _g >= 0 and _g < len(el) else None)
                _g = (_g + 1)
                if first:
                    first = False
                else:
                    self.buf.b.write(", ")
                self.expr(e1)
            self.buf.b.write("]")
        elif (tmp == 18):
            cl = e.params[0]
            args = e.params[1]
            _this = self.buf
            s = Std.string((("new " + ("null" if cl is None else cl)) + "("))
            _this.b.write(s)
            first = True
            _g = 0
            while (_g < len(args)):
                e1 = (args[_g] if _g >= 0 and _g < len(args) else None)
                _g = (_g + 1)
                if first:
                    first = False
                else:
                    self.buf.b.write(", ")
                self.expr(e1)
            self.buf.b.write(")")
        elif (tmp == 19):
            e1 = e.params[0]
            self.buf.b.write("throw ")
            self.expr(e1)
        elif (tmp == 20):
            e1 = e.params[0]
            v = e.params[1]
            t = e.params[2]
            ecatch = e.params[3]
            self.buf.b.write("try ")
            self.expr(e1)
            _this = self.buf
            s = Std.string((" catch( " + ("null" if v is None else v)))
            _this.b.write(s)
            self.addType(t)
            self.buf.b.write(") ")
            self.expr(ecatch)
        elif (tmp == 21):
            fl = e.params[0]
            if (len(fl) == 0):
                self.buf.b.write("{}")
            else:
                _hx_local_7 = self
                _hx_local_8 = _hx_local_7.tabs
                _hx_local_7.tabs = (("null" if _hx_local_8 is None else _hx_local_8) + "\t")
                _hx_local_7.tabs
                self.buf.b.write("{\n")
                _g = 0
                while (_g < len(fl)):
                    f = (fl[_g] if _g >= 0 and _g < len(fl) else None)
                    _g = (_g + 1)
                    _this = self.buf
                    s = Std.string(self.tabs)
                    _this.b.write(s)
                    _this1 = self.buf
                    s1 = Std.string((HxOverrides.stringOrNull(f.name) + " : "))
                    _this1.b.write(s1)
                    self.expr(f.e)
                    self.buf.b.write(",\n")
                self.tabs = HxString.substr(self.tabs,1,None)
                self.buf.b.write("}")
        elif (tmp == 22):
            c = e.params[0]
            e1 = e.params[1]
            e2 = e.params[2]
            self.expr(c)
            self.buf.b.write(" ? ")
            self.expr(e1)
            self.buf.b.write(" : ")
            self.expr(e2)
        elif (tmp == 23):
            e1 = e.params[0]
            cases = e.params[1]
            _hx_def = e.params[2]
            self.buf.b.write("switch( ")
            self.expr(e1)
            self.buf.b.write(") {")
            _g = 0
            while (_g < len(cases)):
                c = (cases[_g] if _g >= 0 and _g < len(cases) else None)
                _g = (_g + 1)
                self.buf.b.write("case ")
                first = True
                _g1 = 0
                _g2 = c.values
                while (_g1 < len(_g2)):
                    v = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
                    _g1 = (_g1 + 1)
                    if first:
                        first = False
                    else:
                        self.buf.b.write(", ")
                    self.expr(v)
                self.buf.b.write(": ")
                self.expr(c.expr)
                self.buf.b.write(";\n")
            if (_hx_def is not None):
                self.buf.b.write("default: ")
                self.expr(_hx_def)
                self.buf.b.write(";\n")
            self.buf.b.write("}")
        elif (tmp == 24):
            cond = e.params[0]
            e1 = e.params[1]
            self.buf.b.write("do ")
            self.expr(e1)
            self.buf.b.write(" while ( ")
            self.expr(cond)
            self.buf.b.write(" )")
        elif (tmp == 25):
            name = e.params[0]
            args = e.params[1]
            e1 = e.params[2]
            self.buf.b.write("@")
            _this = self.buf
            s = Std.string(name)
            _this.b.write(s)
            if ((args is not None) and ((len(args) > 0))):
                self.buf.b.write("(")
                first = True
                _g = 0
                while (_g < len(args)):
                    a = (args[_g] if _g >= 0 and _g < len(args) else None)
                    _g = (_g + 1)
                    if first:
                        first = False
                    else:
                        self.buf.b.write(", ")
                    self.expr(e1)
                self.buf.b.write(")")
            self.buf.b.write(" ")
            self.expr(e1)
        elif (tmp == 26):
            e1 = e.params[0]
            t = e.params[1]
            self.buf.b.write("(")
            self.expr(e1)
            self.buf.b.write(" : ")
            self.addType(t)
            self.buf.b.write(")")
        else:
            pass

    @staticmethod
    def toString(e):
        return hscript_Printer().exprToString(e)

    @staticmethod
    def errorToString(e):
        message = None
        message1 = e.index
        if (message1 == 0):
            c = e.params[0]
            message = (((("Invalid character: '" + HxOverrides.stringOrNull((("EOF" if ((c == -1)) else "".join(map(chr,[c])))))) + "' (") + Std.string(c)) + ")")
        elif (message1 == 1):
            s = e.params[0]
            message = (("Unexpected token: \"" + ("null" if s is None else s)) + "\"")
        elif (message1 == 2):
            message = "Unterminated string"
        elif (message1 == 3):
            message = "Unterminated comment"
        elif (message1 == 4):
            _hx_str = e.params[0]
            message = (("Invalid preprocessor (" + ("null" if _hx_str is None else _hx_str)) + ")")
        elif (message1 == 5):
            v = e.params[0]
            message = ("Unknown variable: " + ("null" if v is None else v))
        elif (message1 == 6):
            v = e.params[0]
            message = ("Invalid iterator: " + ("null" if v is None else v))
        elif (message1 == 7):
            op = e.params[0]
            message = ("Invalid operator: " + ("null" if op is None else op))
        elif (message1 == 8):
            f = e.params[0]
            message = ("Invalid access to field " + ("null" if f is None else f))
        elif (message1 == 9):
            msg = e.params[0]
            message = msg
        else:
            pass
        return message

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.buf = None
        _hx_o.tabs = None
hscript_Printer._hx_class = hscript_Printer
_hx_classes["hscript.Printer"] = hscript_Printer


