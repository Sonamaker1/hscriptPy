class haxe__CallStack_CallStack_Impl_:
    _hx_class_name = "haxe._CallStack.CallStack_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "callStack", "exceptionStack", "toString", "subtract", "copy", "get", "asArray", "equalItems", "exceptionToString", "itemToString"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def callStack():
        infos = python_lib_Traceback.extract_stack()
        if (len(infos) != 0):
            infos.pop()
        infos.reverse()
        return haxe_NativeStackTrace.toHaxe(infos)

    @staticmethod
    def exceptionStack(fullStack = None):
        if (fullStack is None):
            fullStack = False
        eStack = haxe_NativeStackTrace.toHaxe(haxe_NativeStackTrace.exceptionStack())
        return (eStack if fullStack else haxe__CallStack_CallStack_Impl_.subtract(eStack,haxe__CallStack_CallStack_Impl_.callStack()))

    @staticmethod
    def toString(stack):
        b = StringBuf()
        _g = 0
        _g1 = stack
        while (_g < len(_g1)):
            s = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            b.b.write("\nCalled from ")
            haxe__CallStack_CallStack_Impl_.itemToString(b,s)
        return b.b.getvalue()

    @staticmethod
    def subtract(this1,stack):
        startIndex = -1
        i = -1
        while True:
            i = (i + 1)
            tmp = i
            if (not ((tmp < len(this1)))):
                break
            _g = 0
            _g1 = len(stack)
            while (_g < _g1):
                j = _g
                _g = (_g + 1)
                if haxe__CallStack_CallStack_Impl_.equalItems((this1[i] if i >= 0 and i < len(this1) else None),python_internal_ArrayImpl._get(stack, j)):
                    if (startIndex < 0):
                        startIndex = i
                    i = (i + 1)
                    if (i >= len(this1)):
                        break
                else:
                    startIndex = -1
            if (startIndex >= 0):
                break
        if (startIndex >= 0):
            return this1[0:startIndex]
        else:
            return this1

    @staticmethod
    def copy(this1):
        return list(this1)

    @staticmethod
    def get(this1,index):
        return (this1[index] if index >= 0 and index < len(this1) else None)

    @staticmethod
    def asArray(this1):
        return this1

    @staticmethod
    def equalItems(item1,item2):
        if (item1 is None):
            if (item2 is None):
                return True
            else:
                return False
        else:
            tmp = item1.index
            if (tmp == 0):
                if (item2 is None):
                    return False
                elif (item2.index == 0):
                    return True
                else:
                    return False
            elif (tmp == 1):
                if (item2 is None):
                    return False
                elif (item2.index == 1):
                    m2 = item2.params[0]
                    m1 = item1.params[0]
                    return (m1 == m2)
                else:
                    return False
            elif (tmp == 2):
                if (item2 is None):
                    return False
                elif (item2.index == 2):
                    item21 = item2.params[0]
                    file2 = item2.params[1]
                    line2 = item2.params[2]
                    col2 = item2.params[3]
                    col1 = item1.params[3]
                    line1 = item1.params[2]
                    file1 = item1.params[1]
                    item11 = item1.params[0]
                    if (((file1 == file2) and ((line1 == line2))) and ((col1 == col2))):
                        return haxe__CallStack_CallStack_Impl_.equalItems(item11,item21)
                    else:
                        return False
                else:
                    return False
            elif (tmp == 3):
                if (item2 is None):
                    return False
                elif (item2.index == 3):
                    class2 = item2.params[0]
                    method2 = item2.params[1]
                    method1 = item1.params[1]
                    class1 = item1.params[0]
                    if (class1 == class2):
                        return (method1 == method2)
                    else:
                        return False
                else:
                    return False
            elif (tmp == 4):
                if (item2 is None):
                    return False
                elif (item2.index == 4):
                    v2 = item2.params[0]
                    v1 = item1.params[0]
                    return (v1 == v2)
                else:
                    return False
            else:
                pass

    @staticmethod
    def exceptionToString(e):
        if (e.get_previous() is None):
            tmp = ("Exception: " + HxOverrides.stringOrNull(e.toString()))
            tmp1 = e.get_stack()
            return (("null" if tmp is None else tmp) + HxOverrides.stringOrNull((("null" if ((tmp1 is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp1)))))
        result = ""
        e1 = e
        prev = None
        while (e1 is not None):
            if (prev is None):
                result1 = ("Exception: " + HxOverrides.stringOrNull(e1.get_message()))
                tmp = e1.get_stack()
                result = ((("null" if result1 is None else result1) + HxOverrides.stringOrNull((("null" if ((tmp is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp))))) + ("null" if result is None else result))
            else:
                prevStack = haxe__CallStack_CallStack_Impl_.subtract(e1.get_stack(),prev.get_stack())
                result = (((("Exception: " + HxOverrides.stringOrNull(e1.get_message())) + HxOverrides.stringOrNull((("null" if ((prevStack is None)) else haxe__CallStack_CallStack_Impl_.toString(prevStack))))) + "\n\nNext ") + ("null" if result is None else result))
            prev = e1
            e1 = e1.get_previous()
        return result

    @staticmethod
    def itemToString(b,s):
        tmp = s.index
        if (tmp == 0):
            b.b.write("a C function")
        elif (tmp == 1):
            m = s.params[0]
            b.b.write("module ")
            s1 = Std.string(m)
            b.b.write(s1)
        elif (tmp == 2):
            s1 = s.params[0]
            file = s.params[1]
            line = s.params[2]
            col = s.params[3]
            if (s1 is not None):
                haxe__CallStack_CallStack_Impl_.itemToString(b,s1)
                b.b.write(" (")
            s2 = Std.string(file)
            b.b.write(s2)
            b.b.write(" line ")
            s2 = Std.string(line)
            b.b.write(s2)
            if (col is not None):
                b.b.write(" column ")
                s2 = Std.string(col)
                b.b.write(s2)
            if (s1 is not None):
                b.b.write(")")
        elif (tmp == 3):
            cname = s.params[0]
            meth = s.params[1]
            s1 = Std.string(("<unknown>" if ((cname is None)) else cname))
            b.b.write(s1)
            b.b.write(".")
            s1 = Std.string(meth)
            b.b.write(s1)
        elif (tmp == 4):
            n = s.params[0]
            b.b.write("local function #")
            s = Std.string(n)
            b.b.write(s)
        else:
            pass
haxe__CallStack_CallStack_Impl_._hx_class = haxe__CallStack_CallStack_Impl_
_hx_classes["haxe._CallStack.CallStack_Impl_"] = haxe__CallStack_CallStack_Impl_


