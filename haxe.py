from _hx_AnonObject import _hx_AnonObject
import sys
import _hx_AnonObject as anon
import globalClasses
 
import sys
from classes_hscript import _Xml_XmlType_Impl_, StringBuf, StringTools, Xml 
from classes_hscript import Enum
from classes_hscript import EReg
from classes_hscript import HxOverrides
from classes_hscript import HxString
from classes_hscript import Std
from classes_hscript import Type

from io import StringIO as python_lib_io_StringIO


import functools as python_lib_Functools
from classes_hscript import HxString
import math as Math
import math as python_lib_Math
import re as python_lib_Re
from classes_hscript import Reflect
import sys as python_lib_Sys
import traceback as python_lib_Traceback

class haxe_Exception(Exception):
    _hx_class_name = "haxe.Exception"
    __slots__ = ("_hx___exceptionStack", "_hx___nativeStack", "_hx___skipStack", "_hx___nativeException", "_hx___previousException")
    _hx_fields = ["__exceptionStack", "__nativeStack", "__skipStack", "__nativeException", "__previousException"]
    _hx_methods = ["unwrap", "toString", "details", "__shiftStack", "get_message", "get_previous", "get_native", "get_stack"]
    _hx_statics = ["caught", "thrown"]
    _hx_interfaces = []
    _hx_super = Exception


    def __init__(self,message,previous = None,native = None):
        self._hx___previousException = None
        self._hx___nativeException = None
        self._hx___nativeStack = None
        self._hx___exceptionStack = None
        self._hx___skipStack = 0
        super().__init__(message)
        self._hx___previousException = previous
        if ((native is not None) and Std.isOfType(native,BaseException)):
            self._hx___nativeException = native
            self._hx___nativeStack = haxe_NativeStackTrace.exceptionStack()
        else:
            self._hx___nativeException = self
            infos = python_lib_Traceback.extract_stack()
            if (len(infos) != 0):
                infos.pop()
            infos.reverse()
            self._hx___nativeStack = infos

    def unwrap(self):
        return self._hx___nativeException

    def toString(self):
        return self.get_message()

    def details(self):
        if (self.get_previous() is None):
            tmp = ("Exception: " + HxOverrides.stringOrNull(self.toString()))
            tmp1 = self.get_stack()
            return (("null" if tmp is None else tmp) + HxOverrides.stringOrNull((("null" if ((tmp1 is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp1)))))
        else:
            result = ""
            e = self
            prev = None
            while (e is not None):
                if (prev is None):
                    result1 = ("Exception: " + HxOverrides.stringOrNull(e.get_message()))
                    tmp = e.get_stack()
                    result = ((("null" if result1 is None else result1) + HxOverrides.stringOrNull((("null" if ((tmp is None)) else haxe__CallStack_CallStack_Impl_.toString(tmp))))) + ("null" if result is None else result))
                else:
                    prevStack = haxe__CallStack_CallStack_Impl_.subtract(e.get_stack(),prev.get_stack())
                    result = (((("Exception: " + HxOverrides.stringOrNull(e.get_message())) + HxOverrides.stringOrNull((("null" if ((prevStack is None)) else haxe__CallStack_CallStack_Impl_.toString(prevStack))))) + "\n\nNext ") + ("null" if result is None else result))
                prev = e
                e = e.get_previous()
            return result

    def _hx___shiftStack(self):
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def get_message(self):
        return str(self)

    def get_previous(self):
        return self._hx___previousException

    def get_native(self):
        return self._hx___nativeException

    def get_stack(self):
        _g = self._hx___exceptionStack
        if (_g is None):
            def _hx_local_1():
                def _hx_local_0():
                    self._hx___exceptionStack = haxe_NativeStackTrace.toHaxe(self._hx___nativeStack,self._hx___skipStack)
                    return self._hx___exceptionStack
                return _hx_local_0()
            return _hx_local_1()
        else:
            s = _g
            return s

    @staticmethod
    def caught(value):
        if Std.isOfType(value,haxe_Exception):
            return value
        elif Std.isOfType(value,BaseException):
            return haxe_Exception(str(value),None,value)
        else:
            return haxe_ValueException(value,None,value)

    @staticmethod
    def thrown(value):
        if Std.isOfType(value,haxe_Exception):
            return value.get_native()
        elif Std.isOfType(value,BaseException):
            return value
        else:
            e = haxe_ValueException(value)
            e._hx___skipStack = (e._hx___skipStack + 1)
            return e

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o._hx___exceptionStack = None
        _hx_o._hx___nativeStack = None
        _hx_o._hx___skipStack = None
        _hx_o._hx___nativeException = None
        _hx_o._hx___previousException = None
haxe_Exception._hx_class = haxe_Exception
globalClasses._hx_classes["haxe.Exception"] = haxe_Exception


class haxe_IMap:
    _hx_class_name = "haxe.IMap"
    __slots__ = ()
    _hx_methods = ["get", "set", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
haxe_IMap._hx_class = haxe_IMap
globalClasses._hx_classes["haxe.IMap"] = haxe_IMap


class haxe_Int64Helper:
    _hx_class_name = "haxe.Int64Helper"
    __slots__ = ()
    _hx_statics = ["parseString", "fromFloat"]

    @staticmethod
    def parseString(sParam):
        base_high = 0
        base_low = 10
        this1 = haxe__Int64____Int64(0,0)
        current = this1
        this1 = haxe__Int64____Int64(0,1)
        multiplier = this1
        sIsNegative = False
        s = StringTools.trim(sParam)
        if ((("" if ((0 >= len(s))) else s[0])) == "-"):
            sIsNegative = True
            s = HxString.substring(s,1,len(s))
        _hx_len = len(s)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            digitInt = (HxString.charCodeAt(s,((_hx_len - 1) - i)) - 48)
            if ((digitInt < 0) or ((digitInt > 9))):
                raise haxe_Exception.thrown("NumberFormatError")
            if (digitInt != 0):
                digit_high = (digitInt >> 31)
                digit_low = digitInt
                if sIsNegative:
                    mask = 65535
                    al = (multiplier.low & mask)
                    ah = HxOverrides.rshift(multiplier.low, 16)
                    bl = (digit_low & mask)
                    bh = HxOverrides.rshift(digit_low, 16)
                    p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
                    p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
                    p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
                    p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
                    low = p00
                    high = ((((((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
                        ret = high
                        high = (high + 1)
                        high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
                        ret1 = high
                        high = (high + 1)
                        high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    high = (((high + ((((haxe__Int32_Int32_Impl_.mul(multiplier.low,digit_high) + haxe__Int32_Int32_Impl_.mul(multiplier.high,digit_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    b_high = high
                    b_low = low
                    high1 = (((current.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low1 = (((current.low - b_low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(current.low,b_low) < 0):
                        ret2 = high1
                        high1 = (high1 - 1)
                        high1 = ((high1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    this1 = haxe__Int64____Int64(high1,low1)
                    current = this1
                    if (not ((current.high < 0))):
                        raise haxe_Exception.thrown("NumberFormatError: Underflow")
                else:
                    mask1 = 65535
                    al1 = (multiplier.low & mask1)
                    ah1 = HxOverrides.rshift(multiplier.low, 16)
                    bl1 = (digit_low & mask1)
                    bh1 = HxOverrides.rshift(digit_low, 16)
                    p001 = haxe__Int32_Int32_Impl_.mul(al1,bl1)
                    p101 = haxe__Int32_Int32_Impl_.mul(ah1,bl1)
                    p011 = haxe__Int32_Int32_Impl_.mul(al1,bh1)
                    p111 = haxe__Int32_Int32_Impl_.mul(ah1,bh1)
                    low2 = p001
                    high2 = ((((((p111 + (HxOverrides.rshift(p011, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p101, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p011 = ((((p011 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low2 = (((low2 + p011) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low2,p011) < 0):
                        ret3 = high2
                        high2 = (high2 + 1)
                        high2 = ((high2 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    p101 = ((((p101 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low2 = (((low2 + p101) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low2,p101) < 0):
                        ret4 = high2
                        high2 = (high2 + 1)
                        high2 = ((high2 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    high2 = (((high2 + ((((haxe__Int32_Int32_Impl_.mul(multiplier.low,digit_high) + haxe__Int32_Int32_Impl_.mul(multiplier.high,digit_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    b_high1 = high2
                    b_low1 = low2
                    high3 = (((current.high + b_high1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    low3 = (((current.low + b_low1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    if (haxe__Int32_Int32_Impl_.ucompare(low3,current.low) < 0):
                        ret5 = high3
                        high3 = (high3 + 1)
                        high3 = ((high3 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                    this2 = haxe__Int64____Int64(high3,low3)
                    current = this2
                    if (current.high < 0):
                        raise haxe_Exception.thrown("NumberFormatError: Overflow")
            mask2 = 65535
            al2 = (multiplier.low & mask2)
            ah2 = HxOverrides.rshift(multiplier.low, 16)
            bl2 = (base_low & mask2)
            bh2 = HxOverrides.rshift(base_low, 16)
            p002 = haxe__Int32_Int32_Impl_.mul(al2,bl2)
            p102 = haxe__Int32_Int32_Impl_.mul(ah2,bl2)
            p012 = haxe__Int32_Int32_Impl_.mul(al2,bh2)
            p112 = haxe__Int32_Int32_Impl_.mul(ah2,bh2)
            low4 = p002
            high4 = ((((((p112 + (HxOverrides.rshift(p012, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p102, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            p012 = ((((p012 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low4 = (((low4 + p012) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (haxe__Int32_Int32_Impl_.ucompare(low4,p012) < 0):
                ret6 = high4
                high4 = (high4 + 1)
                high4 = ((high4 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            p102 = ((((p102 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low4 = (((low4 + p102) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (haxe__Int32_Int32_Impl_.ucompare(low4,p102) < 0):
                ret7 = high4
                high4 = (high4 + 1)
                high4 = ((high4 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            high4 = (((high4 + ((((haxe__Int32_Int32_Impl_.mul(multiplier.low,base_high) + haxe__Int32_Int32_Impl_.mul(multiplier.high,base_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this3 = haxe__Int64____Int64(high4,low4)
            multiplier = this3
        return current

    @staticmethod
    def fromFloat(f):
        if (python_lib_Math.isnan(f) or (not ((((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))))):
            raise haxe_Exception.thrown("Number is NaN or Infinite")
        noFractions = (f - (HxOverrides.modf(f, 1)))
        if (noFractions > 9007199254740991):
            raise haxe_Exception.thrown("Conversion overflow")
        if (noFractions < -9007199254740991):
            raise haxe_Exception.thrown("Conversion underflow")
        this1 = haxe__Int64____Int64(0,0)
        result = this1
        neg = (noFractions < 0)
        rest = (-noFractions if neg else noFractions)
        i = 0
        while (rest >= 1):
            curr = HxOverrides.modf(rest, 2)
            rest = (rest / 2)
            if (curr >= 1):
                a_high = 0
                a_low = 1
                b = i
                b = (b & 63)
                b1 = None
                if (b == 0):
                    this1 = haxe__Int64____Int64(a_high,a_low)
                    b1 = this1
                elif (b < 32):
                    this2 = haxe__Int64____Int64(((((((((a_high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a_low, ((32 - b))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a_low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                    b1 = this2
                else:
                    this3 = haxe__Int64____Int64(((((a_low << ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
                    b1 = this3
                high = (((result.high + b1.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low = (((result.low + b1.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (haxe__Int32_Int32_Impl_.ucompare(low,result.low) < 0):
                    ret = high
                    high = (high + 1)
                    high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this4 = haxe__Int64____Int64(high,low)
                result = this4
            i = (i + 1)
        if neg:
            high = ((~result.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~result.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            result = this1
        return result
haxe_Int64Helper._hx_class = haxe_Int64Helper
globalClasses._hx_classes["haxe.Int64Helper"] = haxe_Int64Helper


class haxe_Log:
    _hx_class_name = "haxe.Log"
    __slots__ = ()
    _hx_statics = ["formatOutput", "trace"]

    @staticmethod
    def formatOutput(v,infos):
        _hx_str = Std.string(v)
        if (infos is None):
            return _hx_str
        pstr = ((HxOverrides.stringOrNull(infos.fileName) + ":") + Std.string(infos.lineNumber))
        if (Reflect.field(infos,"customParams") is not None):
            _g = 0
            _g1 = Reflect.field(infos,"customParams")
            while (_g < len(_g1)):
                v = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
                _g = (_g + 1)
                _hx_str = (("null" if _hx_str is None else _hx_str) + ((", " + Std.string(v))))
        return ((("null" if pstr is None else pstr) + ": ") + ("null" if _hx_str is None else _hx_str))

    @staticmethod
    def trace(v,infos = None):
        from python import python_Lib 
        _hx_str = haxe_Log.formatOutput(v,infos)
        str1 = Std.string(_hx_str)
        python_Lib.printString((("" + ("null" if str1 is None else str1)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))
haxe_Log._hx_class = haxe_Log
globalClasses._hx_classes["haxe.Log"] = haxe_Log


class haxe_NativeStackTrace:
    _hx_class_name = "haxe.NativeStackTrace"
    __slots__ = ()
    _hx_statics = ["saveStack", "callStack", "exceptionStack", "toHaxe"]

    @staticmethod
    def saveStack(exception):
        pass

    @staticmethod
    def callStack():
        infos = python_lib_Traceback.extract_stack()
        if (len(infos) != 0):
            infos.pop()
        infos.reverse()
        return infos

    @staticmethod
    def exceptionStack():
        exc = python_lib_Sys.exc_info()
        if (exc[2] is not None):
            infos = python_lib_Traceback.extract_tb(exc[2])
            infos.reverse()
            return infos
        else:
            return []

    @staticmethod
    def toHaxe(native,skip = None):
        if (skip is None):
            skip = 0
        stack = []
        _g = 0
        _g1 = len(native)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (skip > i):
                continue
            elem = (native[i] if i >= 0 and i < len(native) else None)
            x = haxe_StackItem.FilePos(haxe_StackItem.Method(None,elem[2]),elem[0],elem[1])
            stack.append(x)
        return stack
haxe_NativeStackTrace._hx_class = haxe_NativeStackTrace
globalClasses._hx_classes["haxe.NativeStackTrace"] = haxe_NativeStackTrace


class haxe_StackItem(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.StackItem"
    _hx_constructs = ["CFunction", "Module", "FilePos", "Method", "LocalFunction"]

    @staticmethod
    def Module(m):
        return haxe_StackItem("Module", 1, (m,))

    @staticmethod
    def FilePos(s,file,line,column = None):
        return haxe_StackItem("FilePos", 2, (s,file,line,column))

    @staticmethod
    def Method(classname,method):
        return haxe_StackItem("Method", 3, (classname,method))

    @staticmethod
    def LocalFunction(v = None):
        return haxe_StackItem("LocalFunction", 4, (v,))
haxe_StackItem.CFunction = haxe_StackItem("CFunction", 0, ())
haxe_StackItem._hx_class = haxe_StackItem
globalClasses._hx_classes["haxe.StackItem"] = haxe_StackItem


class haxe_SysTools:
    _hx_class_name = "haxe.SysTools"
    __slots__ = ()
    _hx_statics = ["winMetaCharacters", "quoteUnixArg", "quoteWinArg"]

    @staticmethod
    def quoteUnixArg(argument):
        if (argument == ""):
            return "''"
        _this = EReg("[^a-zA-Z0-9_@%+=:,./-]","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument)
        if (_this.matchObj is None):
            return argument
        return (("'" + HxOverrides.stringOrNull(StringTools.replace(argument,"'","'\"'\"'"))) + "'")

    @staticmethod
    def quoteWinArg(argument,escapeMetaCharacters):
        _this = EReg("^[^ \t\\\\\"]+$","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument)
        if (_this.matchObj is None):
            result_b = python_lib_io_StringIO()
            needquote = None
            startIndex = None
            if (((argument.find(" ") if ((startIndex is None)) else HxString.indexOfImpl(argument," ",startIndex))) == -1):
                startIndex = None
                needquote = (((argument.find("\t") if ((startIndex is None)) else HxString.indexOfImpl(argument,"\t",startIndex))) != -1)
            else:
                needquote = True
            needquote1 = (needquote or ((argument == "")))
            if needquote1:
                result_b.write("\"")
            bs_buf = StringBuf()
            _g = 0
            _g1 = len(argument)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _g2 = HxString.charCodeAt(argument,i)
                if (_g2 is None):
                    c = _g2
                    if (bs_buf.get_length() > 0):
                        result_b.write(Std.string(bs_buf.b.getvalue()))
                        bs_buf = StringBuf()
                    result_b.write("".join(map(chr,[c])))
                else:
                    _g3 = _g2
                    if (_g3 == 34):
                        bs = bs_buf.b.getvalue()
                        result_b.write(Std.string(bs))
                        result_b.write(Std.string(bs))
                        bs_buf = StringBuf()
                        result_b.write("\\\"")
                    elif (_g3 == 92):
                        bs_buf.b.write("\\")
                    else:
                        c1 = _g2
                        if (bs_buf.get_length() > 0):
                            result_b.write(Std.string(bs_buf.b.getvalue()))
                            bs_buf = StringBuf()
                        result_b.write("".join(map(chr,[c1])))
            result_b.write(Std.string(bs_buf.b.getvalue()))
            if needquote1:
                result_b.write(Std.string(bs_buf.b.getvalue()))
                result_b.write("\"")
            argument = result_b.getvalue()
        if escapeMetaCharacters:
            from python import python_internal_ArrayImpl
            result_b = python_lib_io_StringIO()
            _g = 0
            _g1 = len(argument)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = HxString.charCodeAt(argument,i)
                if (python_internal_ArrayImpl.indexOf(haxe_SysTools.winMetaCharacters,c,None) >= 0):
                    result_b.write("".join(map(chr,[94])))
                result_b.write("".join(map(chr,[c])))
            return result_b.getvalue()
        else:
            return argument
haxe_SysTools._hx_class = haxe_SysTools
globalClasses._hx_classes["haxe.SysTools"] = haxe_SysTools


class haxe_ValueException(haxe_Exception):
    _hx_class_name = "haxe.ValueException"
    __slots__ = ("value",)
    _hx_fields = ["value"]
    _hx_methods = ["unwrap"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,value,previous = None,native = None):
        self.value = None
        super().__init__(Std.string(value),previous,native)
        self.value = value
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def unwrap(self):
        return self.value

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.value = None
haxe_ValueException._hx_class = haxe_ValueException
globalClasses._hx_classes["haxe.ValueException"] = haxe_ValueException


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
        from python import python_internal_ArrayImpl
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
globalClasses._hx_classes["haxe._CallStack.CallStack_Impl_"] = haxe__CallStack_CallStack_Impl_


class haxe__Int32_Int32_Impl_:
    _hx_class_name = "haxe._Int32.Int32_Impl_"
    __slots__ = ()
    _hx_statics = ["negate", "preIncrement", "postIncrement", "preDecrement", "postDecrement", "add", "addInt", "sub", "subInt", "intSub", "mul", "mulInt", "complement", "or", "orInt", "xor", "xorInt", "shr", "shrInt", "intShr", "shl", "shlInt", "intShl", "toFloat", "ucompare", "clamp"]

    @staticmethod
    def negate(this1):
        return (((~this1 + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def preIncrement(this1):
        this1 = (this1 + 1)
        x = this1
        this1 = ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postIncrement(this1):
        ret = this1
        this1 = (this1 + 1)
        this1 = ((this1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def preDecrement(this1):
        this1 = (this1 - 1)
        x = this1
        this1 = ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postDecrement(this1):
        ret = this1
        this1 = (this1 - 1)
        this1 = ((this1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def add(a,b):
        return (((a + b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def addInt(a,b):
        return (((a + b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def sub(a,b):
        return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def subInt(a,b):
        return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def intSub(a,b):
        return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def mul(a,b):
        return ((((a * ((b & 65535))) + ((((((a * (HxOverrides.rshift(b, 16))) << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def mulInt(a,b):
        return haxe__Int32_Int32_Impl_.mul(a,b)

    @staticmethod
    def complement(a):
        return ((~a + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def _hx_or(a,b):
        return ((((a | b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def orInt(a,b):
        return ((((a | b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def xor(a,b):
        return ((((a ^ b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def xorInt(a,b):
        return ((((a ^ b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shr(a,b):
        return ((((a >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shrInt(a,b):
        return ((((a >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def intShr(a,b):
        return ((((a >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shl(a,b):
        return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def shlInt(a,b):
        return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def intShl(a,b):
        return ((((a << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def toFloat(this1):
        return this1

    @staticmethod
    def ucompare(a,b):
        if (a < 0):
            if (b < 0):
                return (((((~b + (2 ** 31)) % (2 ** 32) - (2 ** 31)) - (((~a + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            else:
                return 1
        if (b < 0):
            return -1
        else:
            return (((a - b) + (2 ** 31)) % (2 ** 32) - (2 ** 31))

    @staticmethod
    def clamp(x):
        return ((x + (2 ** 31)) % (2 ** 32) - (2 ** 31))
haxe__Int32_Int32_Impl_._hx_class = haxe__Int32_Int32_Impl_
globalClasses._hx_classes["haxe._Int32.Int32_Impl_"] = haxe__Int32_Int32_Impl_


class haxe__Int64_Int64_Impl_:
    _hx_class_name = "haxe._Int64.Int64_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "copy", "make", "ofInt", "toInt", "is", "isInt64", "getHigh", "getLow", "isNeg", "isZero", "compare", "ucompare", "toStr", "toString", "parseString", "fromFloat", "divMod", "neg", "preIncrement", "postIncrement", "preDecrement", "postDecrement", "add", "addInt", "sub", "subInt", "intSub", "mul", "mulInt", "div", "divInt", "intDiv", "mod", "modInt", "intMod", "eq", "eqInt", "neq", "neqInt", "lt", "ltInt", "intLt", "lte", "lteInt", "intLte", "gt", "gtInt", "intGt", "gte", "gteInt", "intGte", "complement", "and", "or", "xor", "shl", "shr", "ushr", "get_high", "set_high", "get_low", "set_low"]
    high = None
    low = None

    @staticmethod
    def _new(x):
        this1 = x
        return this1

    @staticmethod
    def copy(this1):
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        return this2

    @staticmethod
    def make(high,low):
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def ofInt(x):
        this1 = haxe__Int64____Int64((x >> 31),x)
        return this1

    @staticmethod
    def toInt(x):
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        return x.low

    @staticmethod
    def _hx_is(val):
        return Std.isOfType(val,haxe__Int64____Int64)

    @staticmethod
    def isInt64(val):
        return Std.isOfType(val,haxe__Int64____Int64)

    @staticmethod
    def getHigh(x):
        return x.high

    @staticmethod
    def getLow(x):
        return x.low

    @staticmethod
    def isNeg(x):
        return (x.high < 0)

    @staticmethod
    def isZero(x):
        b_high = 0
        b_low = 0
        if (x.high == b_high):
            return (x.low == b_low)
        else:
            return False

    @staticmethod
    def compare(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        if (a.high < 0):
            if (b.high < 0):
                return v
            else:
                return -1
        elif (b.high >= 0):
            return v
        else:
            return 1

    @staticmethod
    def ucompare(a,b):
        v = haxe__Int32_Int32_Impl_.ucompare(a.high,b.high)
        if (v != 0):
            return v
        else:
            return haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)

    @staticmethod
    def toStr(x):
        return haxe__Int64_Int64_Impl_.toString(x)

    @staticmethod
    def toString(this1):
        i = this1
        b_high = 0
        b_low = 0
        if ((i.high == b_high) and ((i.low == b_low))):
            return "0"
        _hx_str = ""
        neg = False
        if (i.high < 0):
            neg = True
        this1 = haxe__Int64____Int64(0,10)
        ten = this1
        while True:
            b_high = 0
            b_low = 0
            if (not (((i.high != b_high) or ((i.low != b_low))))):
                break
            r = haxe__Int64_Int64_Impl_.divMod(i,ten)
            if (r.modulus.high < 0):
                x = r.modulus
                high = ((~x.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low = (((~x.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (low == 0):
                    ret = high
                    high = (high + 1)
                    high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this_high = high
                this_low = low
                _hx_str = (Std.string(this_low) + ("null" if _hx_str is None else _hx_str))
                x1 = r.quotient
                high1 = ((~x1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low1 = (((~x1.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (low1 == 0):
                    ret1 = high1
                    high1 = (high1 + 1)
                    high1 = ((high1 + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this1 = haxe__Int64____Int64(high1,low1)
                i = this1
            else:
                _hx_str = (Std.string(r.modulus.low) + ("null" if _hx_str is None else _hx_str))
                i = r.quotient
        if neg:
            _hx_str = ("-" + ("null" if _hx_str is None else _hx_str))
        return _hx_str

    @staticmethod
    def parseString(sParam):
        return haxe_Int64Helper.parseString(sParam)

    @staticmethod
    def fromFloat(f):
        return haxe_Int64Helper.fromFloat(f)

    @staticmethod
    def divMod(dividend,divisor):
        if (divisor.high == 0):
            _g = divisor.low
            if (_g == 0):
                raise haxe_Exception.thrown("divide by zero")
            elif (_g == 1):
                this1 = haxe__Int64____Int64(dividend.high,dividend.low)
                this2 = haxe__Int64____Int64(0,0)
                return _hx_AnonObject({'quotient': this1, 'modulus': this2})
            else:
                pass
        divSign = ((dividend.high < 0) != ((divisor.high < 0)))
        modulus = None
        if (dividend.high < 0):
            high = ((~dividend.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~dividend.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            modulus = this1
        else:
            this1 = haxe__Int64____Int64(dividend.high,dividend.low)
            modulus = this1
        if (divisor.high < 0):
            high = ((~divisor.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~divisor.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            divisor = this1
        this1 = haxe__Int64____Int64(0,0)
        quotient = this1
        this1 = haxe__Int64____Int64(0,1)
        mask = this1
        while (not ((divisor.high < 0))):
            v = haxe__Int32_Int32_Impl_.ucompare(divisor.high,modulus.high)
            cmp = (v if ((v != 0)) else haxe__Int32_Int32_Impl_.ucompare(divisor.low,modulus.low))
            b = 1
            b = (b & 63)
            if (b == 0):
                this1 = haxe__Int64____Int64(divisor.high,divisor.low)
                divisor = this1
            elif (b < 32):
                this2 = haxe__Int64____Int64(((((((((divisor.high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(divisor.low, ((32 - b))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((divisor.low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                divisor = this2
            else:
                this3 = haxe__Int64____Int64(((((divisor.low << ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
                divisor = this3
            b1 = 1
            b1 = (b1 & 63)
            if (b1 == 0):
                this4 = haxe__Int64____Int64(mask.high,mask.low)
                mask = this4
            elif (b1 < 32):
                this5 = haxe__Int64____Int64(((((((((mask.high << b1)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(mask.low, ((32 - b1))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((mask.low << b1)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                mask = this5
            else:
                this6 = haxe__Int64____Int64(((((mask.low << ((b1 - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
                mask = this6
            if (cmp >= 0):
                break
        while True:
            b_high = 0
            b_low = 0
            if (not (((mask.high != b_high) or ((mask.low != b_low))))):
                break
            v = haxe__Int32_Int32_Impl_.ucompare(modulus.high,divisor.high)
            if (((v if ((v != 0)) else haxe__Int32_Int32_Impl_.ucompare(modulus.low,divisor.low))) >= 0):
                this1 = haxe__Int64____Int64(((((quotient.high | mask.high)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((quotient.low | mask.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                quotient = this1
                high = (((modulus.high - divisor.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                low = (((modulus.low - divisor.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                if (haxe__Int32_Int32_Impl_.ucompare(modulus.low,divisor.low) < 0):
                    ret = high
                    high = (high - 1)
                    high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
                this2 = haxe__Int64____Int64(high,low)
                modulus = this2
            b = 1
            b = (b & 63)
            if (b == 0):
                this3 = haxe__Int64____Int64(mask.high,mask.low)
                mask = this3
            elif (b < 32):
                this4 = haxe__Int64____Int64(HxOverrides.rshift(mask.high, b),((((((((mask.high << ((32 - b)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(mask.low, b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                mask = this4
            else:
                this5 = haxe__Int64____Int64(0,HxOverrides.rshift(mask.high, ((b - 32))))
                mask = this5
            b1 = 1
            b1 = (b1 & 63)
            if (b1 == 0):
                this6 = haxe__Int64____Int64(divisor.high,divisor.low)
                divisor = this6
            elif (b1 < 32):
                this7 = haxe__Int64____Int64(HxOverrides.rshift(divisor.high, b1),((((((((divisor.high << ((32 - b1)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(divisor.low, b1))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
                divisor = this7
            else:
                this8 = haxe__Int64____Int64(0,HxOverrides.rshift(divisor.high, ((b1 - 32))))
                divisor = this8
        if divSign:
            high = ((~quotient.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~quotient.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            quotient = this1
        if (dividend.high < 0):
            high = ((~modulus.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            low = (((~modulus.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            if (low == 0):
                ret = high
                high = (high + 1)
                high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
            this1 = haxe__Int64____Int64(high,low)
            modulus = this1
        return _hx_AnonObject({'quotient': quotient, 'modulus': modulus})

    @staticmethod
    def neg(x):
        high = ((~x.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((~x.low + 1) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (low == 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def preIncrement(this1):
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        def _hx_local_1():
            _hx_local_0 = this1.low
            this1.low = (this1.low + 1)
            return _hx_local_0
        ret = _hx_local_1()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (this1.low == 0):
            def _hx_local_3():
                _hx_local_2 = this1.high
                this1.high = (this1.high + 1)
                return _hx_local_2
            ret = _hx_local_3()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postIncrement(this1):
        ret = this1
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        def _hx_local_2():
            _hx_local_0 = this1
            _hx_local_1 = _hx_local_0.low
            _hx_local_0.low = (_hx_local_1 + 1)
            return _hx_local_1
        ret1 = _hx_local_2()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (this1.low == 0):
            def _hx_local_5():
                _hx_local_3 = this1
                _hx_local_4 = _hx_local_3.high
                _hx_local_3.high = (_hx_local_4 + 1)
                return _hx_local_4
            ret1 = _hx_local_5()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def preDecrement(this1):
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        if (this1.low == 0):
            def _hx_local_1():
                _hx_local_0 = this1.high
                this1.high = (this1.high - 1)
                return _hx_local_0
            ret = _hx_local_1()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        def _hx_local_3():
            _hx_local_2 = this1.low
            this1.low = (this1.low - 1)
            return _hx_local_2
        ret = _hx_local_3()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return this1

    @staticmethod
    def postDecrement(this1):
        ret = this1
        this2 = haxe__Int64____Int64(this1.high,this1.low)
        this1 = this2
        if (this1.low == 0):
            def _hx_local_2():
                _hx_local_0 = this1
                _hx_local_1 = _hx_local_0.high
                _hx_local_0.high = (_hx_local_1 - 1)
                return _hx_local_1
            ret1 = _hx_local_2()
            this1.high = ((this1.high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        def _hx_local_5():
            _hx_local_3 = this1
            _hx_local_4 = _hx_local_3.low
            _hx_local_3.low = (_hx_local_4 - 1)
            return _hx_local_4
        ret1 = _hx_local_5()
        this1.low = ((this1.low + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        return ret

    @staticmethod
    def add(a,b):
        high = (((a.high + b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low + b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,a.low) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def addInt(a,b):
        b_high = (b >> 31)
        b_low = b
        high = (((a.high + b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low + b_low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,a.low) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def sub(a,b):
        high = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low - b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(a.low,b.low) < 0):
            ret = high
            high = (high - 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def subInt(a,b):
        b_high = (b >> 31)
        b_low = b
        high = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a.low - b_low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(a.low,b_low) < 0):
            ret = high
            high = (high - 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def intSub(a,b):
        a_high = (a >> 31)
        a_low = a
        high = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((a_low - b.low) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(a_low,b.low) < 0):
            ret = high
            high = (high - 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def mul(a,b):
        mask = 65535
        al = (a.low & mask)
        ah = HxOverrides.rshift(a.low, 16)
        bl = (b.low & mask)
        bh = HxOverrides.rshift(b.low, 16)
        p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
        p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
        p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
        p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
        low = p00
        high = ((((((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        high = (((high + ((((haxe__Int32_Int32_Impl_.mul(a.low,b.high) + haxe__Int32_Int32_Impl_.mul(a.high,b.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def mulInt(a,b):
        b_high = (b >> 31)
        b_low = b
        mask = 65535
        al = (a.low & mask)
        ah = HxOverrides.rshift(a.low, 16)
        bl = (b_low & mask)
        bh = HxOverrides.rshift(b_low, 16)
        p00 = haxe__Int32_Int32_Impl_.mul(al,bl)
        p10 = haxe__Int32_Int32_Impl_.mul(ah,bl)
        p01 = haxe__Int32_Int32_Impl_.mul(al,bh)
        p11 = haxe__Int32_Int32_Impl_.mul(ah,bh)
        low = p00
        high = ((((((p11 + (HxOverrides.rshift(p01, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) + (HxOverrides.rshift(p10, 16))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p01 = ((((p01 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p01) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p01) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        p10 = ((((p10 << 16)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        low = (((low + p10) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (haxe__Int32_Int32_Impl_.ucompare(low,p10) < 0):
            ret = high
            high = (high + 1)
            high = ((high + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        high = (((high + ((((haxe__Int32_Int32_Impl_.mul(a.low,b_high) + haxe__Int32_Int32_Impl_.mul(a.high,b_low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        this1 = haxe__Int64____Int64(high,low)
        return this1

    @staticmethod
    def div(a,b):
        return haxe__Int64_Int64_Impl_.divMod(a,b).quotient

    @staticmethod
    def divInt(a,b):
        this1 = haxe__Int64____Int64((b >> 31),b)
        return haxe__Int64_Int64_Impl_.divMod(a,this1).quotient

    @staticmethod
    def intDiv(a,b):
        this1 = haxe__Int64____Int64((a >> 31),a)
        x = haxe__Int64_Int64_Impl_.divMod(this1,b).quotient
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        x1 = x.low
        this1 = haxe__Int64____Int64((x1 >> 31),x1)
        return this1

    @staticmethod
    def mod(a,b):
        return haxe__Int64_Int64_Impl_.divMod(a,b).modulus

    @staticmethod
    def modInt(a,b):
        this1 = haxe__Int64____Int64((b >> 31),b)
        x = haxe__Int64_Int64_Impl_.divMod(a,this1).modulus
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        x1 = x.low
        this1 = haxe__Int64____Int64((x1 >> 31),x1)
        return this1

    @staticmethod
    def intMod(a,b):
        this1 = haxe__Int64____Int64((a >> 31),a)
        x = haxe__Int64_Int64_Impl_.divMod(this1,b).modulus
        if (x.high != ((((x.low >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31))):
            raise haxe_Exception.thrown("Overflow")
        x1 = x.low
        this1 = haxe__Int64____Int64((x1 >> 31),x1)
        return this1

    @staticmethod
    def eq(a,b):
        if (a.high == b.high):
            return (a.low == b.low)
        else:
            return False

    @staticmethod
    def eqInt(a,b):
        b_high = (b >> 31)
        b_low = b
        if (a.high == b_high):
            return (a.low == b_low)
        else:
            return False

    @staticmethod
    def neq(a,b):
        if (a.high == b.high):
            return (a.low != b.low)
        else:
            return True

    @staticmethod
    def neqInt(a,b):
        b_high = (b >> 31)
        b_low = b
        if (a.high == b_high):
            return (a.low != b_low)
        else:
            return True

    @staticmethod
    def lt(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) < 0)

    @staticmethod
    def ltInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) < 0)

    @staticmethod
    def intLt(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) < 0)

    @staticmethod
    def lte(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) <= 0)

    @staticmethod
    def lteInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) <= 0)

    @staticmethod
    def intLte(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) <= 0)

    @staticmethod
    def gt(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) > 0)

    @staticmethod
    def gtInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) > 0)

    @staticmethod
    def intGt(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) > 0)

    @staticmethod
    def gte(a,b):
        v = (((a.high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a.high < 0)) else (v if ((b.high >= 0)) else 1))) >= 0)

    @staticmethod
    def gteInt(a,b):
        b_high = (b >> 31)
        b_low = b
        v = (((a.high - b_high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a.low,b_low)
        return ((((v if ((b_high < 0)) else -1) if ((a.high < 0)) else (v if ((b_high >= 0)) else 1))) >= 0)

    @staticmethod
    def intGte(a,b):
        a_high = (a >> 31)
        a_low = a
        v = (((a_high - b.high) + (2 ** 31)) % (2 ** 32) - (2 ** 31))
        if (v == 0):
            v = haxe__Int32_Int32_Impl_.ucompare(a_low,b.low)
        return ((((v if ((b.high < 0)) else -1) if ((a_high < 0)) else (v if ((b.high >= 0)) else 1))) >= 0)

    @staticmethod
    def complement(a):
        this1 = haxe__Int64____Int64(((~a.high + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((~a.low + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
        return this1

    @staticmethod
    def _hx_and(a,b):
        this1 = haxe__Int64____Int64((a.high & b.high),(a.low & b.low))
        return this1

    @staticmethod
    def _hx_or(a,b):
        this1 = haxe__Int64____Int64(((((a.high | b.high)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.low | b.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
        return this1

    @staticmethod
    def xor(a,b):
        this1 = haxe__Int64____Int64(((((a.high ^ b.high)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.low ^ b.low)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
        return this1

    @staticmethod
    def shl(a,b):
        b = (b & 63)
        if (b == 0):
            this1 = haxe__Int64____Int64(a.high,a.low)
            return this1
        elif (b < 32):
            this1 = haxe__Int64____Int64(((((((((a.high << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, ((32 - b))))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.low << b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1
        else:
            this1 = haxe__Int64____Int64(((((a.low << ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),0)
            return this1

    @staticmethod
    def shr(a,b):
        b = (b & 63)
        if (b == 0):
            this1 = haxe__Int64____Int64(a.high,a.low)
            return this1
        elif (b < 32):
            this1 = haxe__Int64____Int64(((((a.high >> b)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((((((a.high << ((32 - b)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1
        else:
            this1 = haxe__Int64____Int64(((((a.high >> 31)) + (2 ** 31)) % (2 ** 32) - (2 ** 31)),((((a.high >> ((b - 32)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1

    @staticmethod
    def ushr(a,b):
        b = (b & 63)
        if (b == 0):
            this1 = haxe__Int64____Int64(a.high,a.low)
            return this1
        elif (b < 32):
            this1 = haxe__Int64____Int64(HxOverrides.rshift(a.high, b),((((((((a.high << ((32 - b)))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)) | HxOverrides.rshift(a.low, b))) + (2 ** 31)) % (2 ** 32) - (2 ** 31)))
            return this1
        else:
            this1 = haxe__Int64____Int64(0,HxOverrides.rshift(a.high, ((b - 32))))
            return this1

    @staticmethod
    def get_high(this1):
        return this1.high

    @staticmethod
    def set_high(this1,x):
        def _hx_local_1():
            def _hx_local_0():
                this1.high = x
                return this1.high
            return _hx_local_0()
        return _hx_local_1()

    @staticmethod
    def get_low(this1):
        return this1.low

    @staticmethod
    def set_low(this1,x):
        def _hx_local_1():
            def _hx_local_0():
                this1.low = x
                return this1.low
            return _hx_local_0()
        return _hx_local_1()
haxe__Int64_Int64_Impl_._hx_class = haxe__Int64_Int64_Impl_
globalClasses._hx_classes["haxe._Int64.Int64_Impl_"] = haxe__Int64_Int64_Impl_


class haxe__Int64____Int64:
    _hx_class_name = "haxe._Int64.___Int64"
    __slots__ = ("high", "low")
    _hx_fields = ["high", "low"]
    _hx_methods = ["toString"]

    def __init__(self,high,low):
        self.high = high
        self.low = low

    def toString(self):
        return haxe__Int64_Int64_Impl_.toString(self)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.high = None
        _hx_o.low = None
haxe__Int64____Int64._hx_class = haxe__Int64____Int64
globalClasses._hx_classes["haxe._Int64.___Int64"] = haxe__Int64____Int64


class haxe__Rest_Rest_Impl_:
    _hx_class_name = "haxe._Rest.Rest_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "of", "_new", "get", "toArray", "iterator", "keyValueIterator", "append", "prepend", "toString"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def of(array):
        this1 = array
        return this1

    @staticmethod
    def _new(array):
        this1 = array
        return this1

    @staticmethod
    def get(this1,index):
        return (this1[index] if index >= 0 and index < len(this1) else None)

    @staticmethod
    def toArray(this1):
        return list(this1)

    @staticmethod
    def iterator(this1):
        return haxe_iterators_RestIterator(this1)

    @staticmethod
    def keyValueIterator(this1):
        return haxe_iterators_RestKeyValueIterator(this1)

    @staticmethod
    def append(this1,item):
        result = list(this1)
        result.append(item)
        this1 = result
        return this1

    @staticmethod
    def prepend(this1,item):
        result = list(this1)
        result.insert(0, item)
        this1 = result
        return this1

    @staticmethod
    def toString(this1):
        from python import python_Boot
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in this1]))) + "]")
haxe__Rest_Rest_Impl_._hx_class = haxe__Rest_Rest_Impl_
globalClasses._hx_classes["haxe._Rest.Rest_Impl_"] = haxe__Rest_Rest_Impl_


class haxe_ds_BalancedTree:
    _hx_class_name = "haxe.ds.BalancedTree"
    __slots__ = ("root",)
    _hx_fields = ["root"]
    _hx_methods = ["set", "get", "remove", "exists", "iterator", "keyValueIterator", "keys", "copy", "setLoop", "removeLoop", "keysLoop", "merge", "minBinding", "removeMinBinding", "balance", "compare", "toString", "clear"]
    _hx_statics = ["iteratorLoop"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.root = None

    def set(self,key,value):
        self.root = self.setLoop(key,value,self.root)

    def get(self,key):
        node = self.root
        while (node is not None):
            c = self.compare(key,node.key)
            if (c == 0):
                return node.value
            if (c < 0):
                node = node.left
            else:
                node = node.right
        return None

    def remove(self,key):
        try:
            self.root = self.removeLoop(key,self.root)
            return True
        except BaseException as _g:
            None
            if Std.isOfType(haxe_Exception.caught(_g).unwrap(),str):
                return False
            else:
                raise _g

    def exists(self,key):
        node = self.root
        while (node is not None):
            c = self.compare(key,node.key)
            if (c == 0):
                return True
            elif (c < 0):
                node = node.left
            else:
                node = node.right
        return False

    def iterator(self):
        ret = []
        haxe_ds_BalancedTree.iteratorLoop(self.root,ret)
        return haxe_iterators_ArrayIterator(ret)

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def keys(self):
        ret = []
        self.keysLoop(self.root,ret)
        return haxe_iterators_ArrayIterator(ret)

    def copy(self):
        copied = haxe_ds_BalancedTree()
        copied.root = self.root
        return copied

    def setLoop(self,k,v,node):
        if (node is None):
            return haxe_ds_TreeNode(None,k,v,None)
        c = self.compare(k,node.key)
        if (c == 0):
            return haxe_ds_TreeNode(node.left,k,v,node.right,(0 if ((node is None)) else node._height))
        elif (c < 0):
            nl = self.setLoop(k,v,node.left)
            return self.balance(nl,node.key,node.value,node.right)
        else:
            nr = self.setLoop(k,v,node.right)
            return self.balance(node.left,node.key,node.value,nr)

    def removeLoop(self,k,node):
        if (node is None):
            raise haxe_Exception.thrown("Not_found")
        c = self.compare(k,node.key)
        if (c == 0):
            return self.merge(node.left,node.right)
        elif (c < 0):
            return self.balance(self.removeLoop(k,node.left),node.key,node.value,node.right)
        else:
            return self.balance(node.left,node.key,node.value,self.removeLoop(k,node.right))

    def keysLoop(self,node,acc):
        if (node is not None):
            self.keysLoop(node.left,acc)
            x = node.key
            acc.append(x)
            self.keysLoop(node.right,acc)

    def merge(self,t1,t2):
        if (t1 is None):
            return t2
        if (t2 is None):
            return t1
        t = self.minBinding(t2)
        return self.balance(t1,t.key,t.value,self.removeMinBinding(t2))

    def minBinding(self,t):
        if (t is None):
            raise haxe_Exception.thrown("Not_found")
        elif (t.left is None):
            return t
        else:
            return self.minBinding(t.left)

    def removeMinBinding(self,t):
        if (t.left is None):
            return t.right
        else:
            return self.balance(self.removeMinBinding(t.left),t.key,t.value,t.right)

    def balance(self,l,k,v,r):
        hl = (0 if ((l is None)) else l._height)
        hr = (0 if ((r is None)) else r._height)
        if (hl > ((hr + 2))):
            _this = l.left
            _this1 = l.right
            if (((0 if ((_this is None)) else _this._height)) >= ((0 if ((_this1 is None)) else _this1._height))):
                return haxe_ds_TreeNode(l.left,l.key,l.value,haxe_ds_TreeNode(l.right,k,v,r))
            else:
                return haxe_ds_TreeNode(haxe_ds_TreeNode(l.left,l.key,l.value,l.right.left),l.right.key,l.right.value,haxe_ds_TreeNode(l.right.right,k,v,r))
        elif (hr > ((hl + 2))):
            _this = r.right
            _this1 = r.left
            if (((0 if ((_this is None)) else _this._height)) > ((0 if ((_this1 is None)) else _this1._height))):
                return haxe_ds_TreeNode(haxe_ds_TreeNode(l,k,v,r.left),r.key,r.value,r.right)
            else:
                return haxe_ds_TreeNode(haxe_ds_TreeNode(l,k,v,r.left.left),r.left.key,r.left.value,haxe_ds_TreeNode(r.left.right,r.key,r.value,r.right))
        else:
            return haxe_ds_TreeNode(l,k,v,r,(((hl if ((hl > hr)) else hr)) + 1))

    def compare(self,k1,k2):
        return Reflect.compare(k1,k2)

    def toString(self):
        if (self.root is None):
            return "{}"
        else:
            return (("{" + HxOverrides.stringOrNull(self.root.toString())) + "}")

    def clear(self):
        self.root = None

    @staticmethod
    def iteratorLoop(node,acc):
        if (node is not None):
            haxe_ds_BalancedTree.iteratorLoop(node.left,acc)
            x = node.value
            acc.append(x)
            haxe_ds_BalancedTree.iteratorLoop(node.right,acc)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.root = None
haxe_ds_BalancedTree._hx_class = haxe_ds_BalancedTree
globalClasses._hx_classes["haxe.ds.BalancedTree"] = haxe_ds_BalancedTree


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
globalClasses._hx_classes["haxe.ds.EnumValueMap"] = haxe_ds_EnumValueMap


class haxe_ds_GenericCell:
    _hx_class_name = "haxe.ds.GenericCell"
    __slots__ = ("elt", "next")
    _hx_fields = ["elt", "next"]

    def __init__(self,elt,next):
        self.elt = elt
        self.next = next

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.elt = None
        _hx_o.next = None
haxe_ds_GenericCell._hx_class = haxe_ds_GenericCell
globalClasses._hx_classes["haxe.ds.GenericCell"] = haxe_ds_GenericCell


class haxe_ds_GenericStack:
    _hx_class_name = "haxe.ds.GenericStack"
    __slots__ = ("head",)
    _hx_fields = ["head"]
    _hx_methods = ["add", "first", "pop", "isEmpty", "remove", "iterator", "toString"]

    def __init__(self):
        self.head = None

    def add(self,item):
        self.head = haxe_ds_GenericCell(item,self.head)

    def first(self):
        if (self.head is None):
            return None
        else:
            return self.head.elt

    def pop(self):
        k = self.head
        if (k is None):
            return None
        else:
            self.head = k.next
            return k.elt

    def isEmpty(self):
        return (self.head is None)

    def remove(self,v):
        prev = None
        l = self.head
        while (l is not None):
            if HxOverrides.eq(l.elt,v):
                if (prev is None):
                    self.head = l.next
                else:
                    prev.next = l.next
                break
            prev = l
            l = l.next
        return (l is not None)

    def iterator(self):
        l = self.head
        def _hx_local_2():
            def _hx_local_0():
                return (l is not None)
            def _hx_local_1():
                nonlocal l
                k = l
                l = k.next
                return k.elt
            return _hx_AnonObject({'hasNext': _hx_local_0, 'next': _hx_local_1})
        return _hx_local_2()

    def toString(self):
        from python import python_Boot
        a = list()
        l = self.head
        while (l is not None):
            x = l.elt
            a.append(x)
            l = l.next
        return (("{" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in a]))) + "}")

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.head = None
haxe_ds_GenericStack._hx_class = haxe_ds_GenericStack
globalClasses._hx_classes["haxe.ds.GenericStack"] = haxe_ds_GenericStack


class haxe_ds_IntMap:
    _hx_class_name = "haxe.ds.IntMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        if (not (key in self.h)):
            return False
        del self.h[key]
        return True

    def keys(self):
        from python import python_HaxeIterator
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        from python import python_HaxeIterator
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_IntMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            copied.set(key1,self.h.get(key1,None))
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(i1))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_IntMap._hx_class = haxe_ds_IntMap
globalClasses._hx_classes["haxe.ds.IntMap"] = haxe_ds_IntMap


class haxe_ds_List:
    _hx_class_name = "haxe.ds.List"
    __slots__ = ("h", "q", "length")
    _hx_fields = ["h", "q", "length"]
    _hx_methods = ["add", "push", "first", "last", "pop", "isEmpty", "clear", "remove", "iterator", "keyValueIterator", "toString", "join", "filter", "map"]

    def __init__(self):
        self.q = None
        self.h = None
        self.length = 0

    def add(self,item):
        x = haxe_ds__List_ListNode(item,None)
        if (self.h is None):
            self.h = x
        else:
            self.q.next = x
        self.q = x
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 + 1)
        _hx_local_1

    def push(self,item):
        x = haxe_ds__List_ListNode(item,self.h)
        self.h = x
        if (self.q is None):
            self.q = x
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 + 1)
        _hx_local_1

    def first(self):
        if (self.h is None):
            return None
        else:
            return self.h.item

    def last(self):
        if (self.q is None):
            return None
        else:
            return self.q.item

    def pop(self):
        if (self.h is None):
            return None
        x = self.h.item
        self.h = self.h.next
        if (self.h is None):
            self.q = None
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0.length
        _hx_local_0.length = (_hx_local_1 - 1)
        _hx_local_1
        return x

    def isEmpty(self):
        return (self.h is None)

    def clear(self):
        self.h = None
        self.q = None
        self.length = 0

    def remove(self,v):
        prev = None
        l = self.h
        while (l is not None):
            if HxOverrides.eq(l.item,v):
                if (prev is None):
                    self.h = l.next
                else:
                    prev.next = l.next
                if (self.q == l):
                    self.q = prev
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.length
                _hx_local_0.length = (_hx_local_1 - 1)
                _hx_local_1
                return True
            prev = l
            l = l.next
        return False

    def iterator(self):
        return haxe_ds__List_ListIterator(self.h)

    def keyValueIterator(self):
        return haxe_ds__List_ListKeyValueIterator(self.h)

    def toString(self):
        s_b = python_lib_io_StringIO()
        first = True
        l = self.h
        s_b.write("{")
        while (l is not None):
            if first:
                first = False
            else:
                s_b.write(", ")
            s_b.write(Std.string(Std.string(l.item)))
            l = l.next
        s_b.write("}")
        return s_b.getvalue()

    def join(self,sep):
        s_b = python_lib_io_StringIO()
        first = True
        l = self.h
        while (l is not None):
            if first:
                first = False
            else:
                s_b.write(Std.string(sep))
            s_b.write(Std.string(l.item))
            l = l.next
        return s_b.getvalue()

    def filter(self,f):
        l2 = haxe_ds_List()
        l = self.h
        while (l is not None):
            v = l.item
            l = l.next
            if f(v):
                l2.add(v)
        return l2

    def map(self,f):
        b = haxe_ds_List()
        l = self.h
        while (l is not None):
            v = l.item
            l = l.next
            b.add(f(v))
        return b

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
        _hx_o.q = None
        _hx_o.length = None
haxe_ds_List._hx_class = haxe_ds_List
globalClasses._hx_classes["haxe.ds.List"] = haxe_ds_List


class haxe_ds_ObjectMap:
    _hx_class_name = "haxe.ds.ObjectMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        r = (key in self.h)
        if r:
            del self.h[key]
        return r

    def keys(self):
        from python import python_HaxeIterator
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        from python import python_HaxeIterator
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_ObjectMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            copied.set(key1,self.h.get(key1,None))
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(Std.string(i1)))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_ObjectMap._hx_class = haxe_ds_ObjectMap
globalClasses._hx_classes["haxe.ds.ObjectMap"] = haxe_ds_ObjectMap

class haxe_ds_Option(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.ds.Option"
    _hx_constructs = ["Some", "None"]

    @staticmethod
    def Some(v):
        return haxe_ds_Option("Some", 0, (v,))
haxe_ds_Option._hx_None = haxe_ds_Option("None", 1, ())
haxe_ds_Option._hx_class = haxe_ds_Option
globalClasses._hx_classes["haxe.ds.Option"] = haxe_ds_Option


class haxe_ds_StringMap:
    _hx_class_name = "haxe.ds.StringMap"
    __slots__ = ("h",)
    _hx_fields = ["h"]
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        self.h = dict()

    def set(self,key,value):
        self.h[key] = value

    def get(self,key):
        return self.h.get(key,None)

    def exists(self,key):
        return (key in self.h)

    def remove(self,key):
        has = (key in self.h)
        if has:
            del self.h[key]
        return has

    def keys(self):
        from python import python_HaxeIterator
        return python_HaxeIterator(iter(self.h.keys()))

    def iterator(self):
        from python import python_HaxeIterator
        return python_HaxeIterator(iter(self.h.values()))

    def keyValueIterator(self):
        return haxe_iterators_MapKeyValueIterator(self)

    def copy(self):
        copied = haxe_ds_StringMap()
        key = self.keys()
        while key.hasNext():
            key1 = key.next()
            value = self.h.get(key1,None)
            copied.h[key1] = value
        return copied

    def toString(self):
        s_b = python_lib_io_StringIO()
        s_b.write("{")
        it = self.keys()
        i = it
        while i.hasNext():
            i1 = i.next()
            s_b.write(Std.string(i1))
            s_b.write(" => ")
            s_b.write(Std.string(Std.string(self.h.get(i1,None))))
            if it.hasNext():
                s_b.write(", ")
        s_b.write("}")
        return s_b.getvalue()

    def clear(self):
        self.h.clear()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.h = None
haxe_ds_StringMap._hx_class = haxe_ds_StringMap
globalClasses._hx_classes["haxe.ds.StringMap"] = haxe_ds_StringMap


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
globalClasses._hx_classes["haxe.ds.TreeNode"] = haxe_ds_TreeNode


class haxe_ds_WeakMap:
    _hx_class_name = "haxe.ds.WeakMap"
    __slots__ = ()
    _hx_methods = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear"]
    _hx_interfaces = [haxe_IMap]

    def __init__(self):
        raise haxe_exceptions_NotImplementedException("Not implemented for this platform",None,_hx_AnonObject({'fileName': "haxe/ds/WeakMap.hx", 'lineNumber': 39, 'className': "haxe.ds.WeakMap", 'methodName': "new"}))

    def set(self,key,value):
        pass

    def get(self,key):
        return None

    def exists(self,key):
        return False

    def remove(self,key):
        return False

    def keys(self):
        return None

    def iterator(self):
        return None

    def keyValueIterator(self):
        return None

    def copy(self):
        return None

    def toString(self):
        return None

    def clear(self):
        pass

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
haxe_ds_WeakMap._hx_class = haxe_ds_WeakMap
globalClasses._hx_classes["haxe.ds.WeakMap"] = haxe_ds_WeakMap


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
globalClasses._hx_classes["haxe.ds._HashMap.HashMapData"] = haxe_ds__HashMap_HashMapData


class haxe_ds__HashMap_HashMap_Impl_:
    _hx_class_name = "haxe.ds._HashMap.HashMap_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "set", "get", "exists", "remove", "keys", "copy", "iterator", "keyValueIterator", "clear"]

    @staticmethod
    def _new():
        this1 = haxe_ds__HashMap_HashMapData()
        return this1

    @staticmethod
    def set(this1,k,v):
        this1.keys.set(k.hashCode(),k)
        this1.values.set(k.hashCode(),v)

    @staticmethod
    def get(this1,k):
        _this = this1.values
        key = k.hashCode()
        return _this.h.get(key,None)

    @staticmethod
    def exists(this1,k):
        _this = this1.values
        return (k.hashCode() in _this.h)

    @staticmethod
    def remove(this1,k):
        this1.values.remove(k.hashCode())
        return this1.keys.remove(k.hashCode())

    @staticmethod
    def keys(this1):
        return this1.keys.iterator()

    @staticmethod
    def copy(this1):
        copied = haxe_ds__HashMap_HashMapData()
        copied.keys = this1.keys.copy()
        copied.values = this1.values.copy()
        return copied

    @staticmethod
    def iterator(this1):
        return this1.values.iterator()

    @staticmethod
    def keyValueIterator(this1):
        return haxe_iterators_HashMapKeyValueIterator(this1)

    @staticmethod
    def clear(this1):
        this1.keys.h.clear()
        this1.values.h.clear()
haxe_ds__HashMap_HashMap_Impl_._hx_class = haxe_ds__HashMap_HashMap_Impl_
globalClasses._hx_classes["haxe.ds._HashMap.HashMap_Impl_"] = haxe_ds__HashMap_HashMap_Impl_


class haxe_ds__List_ListIterator:
    _hx_class_name = "haxe.ds._List.ListIterator"
    __slots__ = ("head",)
    _hx_fields = ["head"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,head):
        self.head = head

    def hasNext(self):
        return (self.head is not None)

    def next(self):
        val = self.head.item
        self.head = self.head.next
        return val

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.head = None
haxe_ds__List_ListIterator._hx_class = haxe_ds__List_ListIterator
globalClasses._hx_classes["haxe.ds._List.ListIterator"] = haxe_ds__List_ListIterator


class haxe_ds__List_ListKeyValueIterator:
    _hx_class_name = "haxe.ds._List.ListKeyValueIterator"
    __slots__ = ("idx", "head")
    _hx_fields = ["idx", "head"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,head):
        self.head = head
        self.idx = 0

    def hasNext(self):
        return (self.head is not None)

    def next(self):
        val = self.head.item
        self.head = self.head.next
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.idx
                _hx_local_0.idx = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_AnonObject({'value': val, 'key': _hx_local_2()})
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.idx = None
        _hx_o.head = None
haxe_ds__List_ListKeyValueIterator._hx_class = haxe_ds__List_ListKeyValueIterator
globalClasses._hx_classes["haxe.ds._List.ListKeyValueIterator"] = haxe_ds__List_ListKeyValueIterator


class haxe_ds__List_ListNode:
    _hx_class_name = "haxe.ds._List.ListNode"
    __slots__ = ("item", "next")
    _hx_fields = ["item", "next"]

    def __init__(self,item,next):
        self.item = item
        self.next = next

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.item = None
        _hx_o.next = None
haxe_ds__List_ListNode._hx_class = haxe_ds__List_ListNode
globalClasses._hx_classes["haxe.ds._List.ListNode"] = haxe_ds__List_ListNode


class haxe_ds__Map_Map_Impl_:
    _hx_class_name = "haxe.ds._Map.Map_Impl_"
    __slots__ = ()
    _hx_statics = ["set", "get", "exists", "remove", "keys", "iterator", "keyValueIterator", "copy", "toString", "clear", "arrayWrite", "toStringMap", "toIntMap", "toEnumValueMapMap", "toObjectMap", "fromStringMap", "fromIntMap", "fromObjectMap"]

    @staticmethod
    def set(this1,key,value):
        this1.set(key,value)

    @staticmethod
    def get(this1,key):
        return this1.get(key)

    @staticmethod
    def exists(this1,key):
        return this1.exists(key)

    @staticmethod
    def remove(this1,key):
        return this1.remove(key)

    @staticmethod
    def keys(this1):
        return this1.keys()

    @staticmethod
    def iterator(this1):
        return this1.iterator()

    @staticmethod
    def keyValueIterator(this1):
        return this1.keyValueIterator()

    @staticmethod
    def copy(this1):
        return this1.copy()

    @staticmethod
    def toString(this1):
        return this1.toString()

    @staticmethod
    def clear(this1):
        this1.clear()

    @staticmethod
    def arrayWrite(this1,k,v):
        this1.set(k,v)
        return v

    @staticmethod
    def toStringMap(t):
        return haxe_ds_StringMap()

    @staticmethod
    def toIntMap(t):
        return haxe_ds_IntMap()

    @staticmethod
    def toEnumValueMapMap(t):
        return haxe_ds_EnumValueMap()

    @staticmethod
    def toObjectMap(t):
        return haxe_ds_ObjectMap()

    @staticmethod
    def fromStringMap(_hx_map):
        return _hx_map

    @staticmethod
    def fromIntMap(_hx_map):
        return _hx_map

    @staticmethod
    def fromObjectMap(_hx_map):
        return _hx_map
haxe_ds__Map_Map_Impl_._hx_class = haxe_ds__Map_Map_Impl_
globalClasses._hx_classes["haxe.ds._Map.Map_Impl_"] = haxe_ds__Map_Map_Impl_


class haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_:
    _hx_class_name = "haxe.ds._ReadOnlyArray.ReadOnlyArray_Impl_"
    __slots__ = ()
    _hx_statics = ["get_length", "get", "concat"]
    length = None

    @staticmethod
    def get_length(this1):
        return len(this1)

    @staticmethod
    def get(this1,i):
        return (this1[i] if i >= 0 and i < len(this1) else None)

    @staticmethod
    def concat(this1,a):
        return (this1 + a)
haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_._hx_class = haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_
globalClasses._hx_classes["haxe.ds._ReadOnlyArray.ReadOnlyArray_Impl_"] = haxe_ds__ReadOnlyArray_ReadOnlyArray_Impl_

class haxe_exceptions_PosException(haxe_Exception):
    _hx_class_name = "haxe.exceptions.PosException"
    __slots__ = ("posInfos",)
    _hx_fields = ["posInfos"]
    _hx_methods = ["toString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,message,previous = None,pos = None):
        self.posInfos = None
        super().__init__(message,previous)
        if (pos is None):
            self.posInfos = _hx_AnonObject({'fileName': "(unknown)", 'lineNumber': 0, 'className': "(unknown)", 'methodName': "(unknown)"})
        else:
            self.posInfos = pos
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    def toString(self):
        return ((((((((("" + HxOverrides.stringOrNull(super().toString())) + " in ") + HxOverrides.stringOrNull(self.posInfos.className)) + ".") + HxOverrides.stringOrNull(self.posInfos.methodName)) + " at ") + HxOverrides.stringOrNull(self.posInfos.fileName)) + ":") + Std.string(self.posInfos.lineNumber))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.posInfos = None
haxe_exceptions_PosException._hx_class = haxe_exceptions_PosException
globalClasses._hx_classes["haxe.exceptions.PosException"] = haxe_exceptions_PosException

class haxe_exceptions_NotImplementedException(haxe_exceptions_PosException):
    _hx_class_name = "haxe.exceptions.NotImplementedException"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_exceptions_PosException


    def __init__(self,message = None,previous = None,pos = None):
        if (message is None):
            message = "Not implemented"
        super().__init__(message,previous,pos)
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1
haxe_exceptions_NotImplementedException._hx_class = haxe_exceptions_NotImplementedException
globalClasses._hx_classes["haxe.exceptions.NotImplementedException"] = haxe_exceptions_NotImplementedException





class haxe_io_Bytes:
    _hx_class_name = "haxe.io.Bytes"
    __slots__ = ("length", "b")
    _hx_fields = ["length", "b"]
    _hx_methods = ["get", "set", "blit", "fill", "sub", "compare", "getDouble", "getFloat", "setDouble", "setFloat", "getUInt16", "setUInt16", "getInt32", "getInt64", "setInt32", "setInt64", "getString", "readString", "toString", "toHex", "getData"]
    _hx_statics = ["alloc", "ofString", "ofData", "ofHex", "fastGet"]

    def __init__(self,length,b):
        self.length = length
        self.b = b

    def get(self,pos):
        return self.b[pos]

    def set(self,pos,v):
        self.b[pos] = (v & 255)

    def blit(self,pos,src,srcpos,_hx_len):
        if (((((pos < 0) or ((srcpos < 0))) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))) or (((srcpos + _hx_len) > src.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        self.b[pos:pos+_hx_len] = src.b[srcpos:srcpos+_hx_len]

    def fill(self,pos,_hx_len,value):
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            pos1 = pos
            pos = (pos + 1)
            self.b[pos1] = (value & 255)

    def sub(self,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return haxe_io_Bytes(_hx_len,self.b[pos:(pos + _hx_len)])

    def compare(self,other):
        b1 = self.b
        b2 = other.b
        _hx_len = (self.length if ((self.length < other.length)) else other.length)
        _g = 0
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (b1[i] != b2[i]):
                return (b1[i] - b2[i])
        return (self.length - other.length)

    def getDouble(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        pos1 = (pos + 4)
        v1 = (((self.b[pos1] | ((self.b[(pos1 + 1)] << 8))) | ((self.b[(pos1 + 2)] << 16))) | ((self.b[(pos1 + 3)] << 24)))
        return haxe_io_FPHelper.i64ToDouble(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v),((v1 | -2147483648) if ((((v1 & -2147483648)) != 0)) else v1))

    def getFloat(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        return haxe_io_FPHelper.i32ToFloat(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v))

    def setDouble(self,pos,v):
        i = haxe_io_FPHelper.doubleToI64(v)
        v = i.low
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)
        self.b[(pos + 2)] = ((v >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v, 24) & 255)
        pos1 = (pos + 4)
        v = i.high
        self.b[pos1] = (v & 255)
        self.b[(pos1 + 1)] = ((v >> 8) & 255)
        self.b[(pos1 + 2)] = ((v >> 16) & 255)
        self.b[(pos1 + 3)] = (HxOverrides.rshift(v, 24) & 255)

    def setFloat(self,pos,v):
        v1 = haxe_io_FPHelper.floatToI32(v)
        self.b[pos] = (v1 & 255)
        self.b[(pos + 1)] = ((v1 >> 8) & 255)
        self.b[(pos + 2)] = ((v1 >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)

    def getUInt16(self,pos):
        return (self.b[pos] | ((self.b[(pos + 1)] << 8)))

    def setUInt16(self,pos,v):
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)

    def getInt32(self,pos):
        v = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        if (((v & -2147483648)) != 0):
            return (v | -2147483648)
        else:
            return v

    def getInt64(self,pos):
        pos1 = (pos + 4)
        v = (((self.b[pos1] | ((self.b[(pos1 + 1)] << 8))) | ((self.b[(pos1 + 2)] << 16))) | ((self.b[(pos1 + 3)] << 24)))
        v1 = (((self.b[pos] | ((self.b[(pos + 1)] << 8))) | ((self.b[(pos + 2)] << 16))) | ((self.b[(pos + 3)] << 24)))
        this1 = haxe__Int64____Int64(((v | -2147483648) if ((((v & -2147483648)) != 0)) else v),((v1 | -2147483648) if ((((v1 & -2147483648)) != 0)) else v1))
        return this1

    def setInt32(self,pos,v):
        self.b[pos] = (v & 255)
        self.b[(pos + 1)] = ((v >> 8) & 255)
        self.b[(pos + 2)] = ((v >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v, 24) & 255)

    def setInt64(self,pos,v):
        v1 = v.low
        self.b[pos] = (v1 & 255)
        self.b[(pos + 1)] = ((v1 >> 8) & 255)
        self.b[(pos + 2)] = ((v1 >> 16) & 255)
        self.b[(pos + 3)] = (HxOverrides.rshift(v1, 24) & 255)
        pos1 = (pos + 4)
        v1 = v.high
        self.b[pos1] = (v1 & 255)
        self.b[(pos1 + 1)] = ((v1 >> 8) & 255)
        self.b[(pos1 + 2)] = ((v1 >> 16) & 255)
        self.b[(pos1 + 3)] = (HxOverrides.rshift(v1, 24) & 255)

    def getString(self,pos,_hx_len,encoding = None):
        tmp = (encoding is None)
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > self.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        return self.b[pos:pos+_hx_len].decode('UTF-8','replace')

    def readString(self,pos,_hx_len):
        return self.getString(pos,_hx_len)

    def toString(self):
        return self.getString(0,self.length)

    def toHex(self):
        from python import python_internal_ArrayImpl
        s_b = python_lib_io_StringIO()
        chars = []
        _hx_str = "0123456789abcdef"
        _g = 0
        _g1 = len(_hx_str)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            x = HxString.charCodeAt(_hx_str,i)
            chars.append(x)
        _g = 0
        _g1 = self.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = self.b[i]
            s_b.write("".join(map(chr,[python_internal_ArrayImpl._get(chars, (c >> 4))])))
            s_b.write("".join(map(chr,[python_internal_ArrayImpl._get(chars, (c & 15))])))
        return s_b.getvalue()

    def getData(self):
        return self.b

    @staticmethod
    def alloc(length):
        return haxe_io_Bytes(length,bytearray(length))

    @staticmethod
    def ofString(s,encoding = None):
        b = bytearray(s,"UTF-8")
        return haxe_io_Bytes(len(b),b)

    @staticmethod
    def ofData(b):
        return haxe_io_Bytes(len(b),b)

    @staticmethod
    def ofHex(s):
        _hx_len = len(s)
        if (((_hx_len & 1)) != 0):
            raise haxe_Exception.thrown("Not a hex string (odd number of digits)")
        ret = haxe_io_Bytes.alloc((_hx_len >> 1))
        _g = 0
        _g1 = ret.length
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            index = (i * 2)
            high = (-1 if ((index >= len(s))) else ord(s[index]))
            index1 = ((i * 2) + 1)
            low = (-1 if ((index1 >= len(s))) else ord(s[index1]))
            high = (((high & 15)) + ((((((high & 64)) >> 6)) * 9)))
            low = (((low & 15)) + ((((((low & 64)) >> 6)) * 9)))
            ret.b[i] = (((((high << 4) | low)) & 255) & 255)
        return ret

    @staticmethod
    def fastGet(b,pos):
        return b[pos]

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.length = None
        _hx_o.b = None
haxe_io_Bytes._hx_class = haxe_io_Bytes
globalClasses._hx_classes["haxe.io.Bytes"] = haxe_io_Bytes


class haxe_io_BytesBuffer:
    _hx_class_name = "haxe.io.BytesBuffer"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length", "addByte", "add", "addString", "addInt32", "addInt64", "addFloat", "addDouble", "addBytes", "getBytes"]

    def __init__(self):
        self.b = bytearray()

    def get_length(self):
        return len(self.b)

    def addByte(self,byte):
        self.b.append(byte)

    def add(self,src):
        self.b.extend(src.b)

    def addString(self,v,encoding = None):
        self.b.extend(bytearray(v,"UTF-8"))

    def addInt32(self,v):
        self.b.append((v & 255))
        self.b.append(((v >> 8) & 255))
        self.b.append(((v >> 16) & 255))
        self.b.append(HxOverrides.rshift(v, 24))

    def addInt64(self,v):
        self.addInt32(v.low)
        self.addInt32(v.high)

    def addFloat(self,v):
        self.addInt32(haxe_io_FPHelper.floatToI32(v))

    def addDouble(self,v):
        self.addInt64(haxe_io_FPHelper.doubleToI64(v))

    def addBytes(self,src,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > src.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        self.b.extend(src.b[pos:(pos + _hx_len)])

    def getBytes(self):
        _hx_bytes = haxe_io_Bytes(len(self.b),self.b)
        self.b = None
        return _hx_bytes

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
haxe_io_BytesBuffer._hx_class = haxe_io_BytesBuffer
globalClasses._hx_classes["haxe.io.BytesBuffer"] = haxe_io_BytesBuffer

class haxe_io_Encoding(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Encoding"
    _hx_constructs = ["UTF8", "RawNative"]
haxe_io_Encoding.UTF8 = haxe_io_Encoding("UTF8", 0, ())
haxe_io_Encoding.RawNative = haxe_io_Encoding("RawNative", 1, ())
haxe_io_Encoding._hx_class = haxe_io_Encoding
globalClasses._hx_classes["haxe.io.Encoding"] = haxe_io_Encoding


class haxe_io_Eof:
    _hx_class_name = "haxe.io.Eof"
    __slots__ = ()
    _hx_methods = ["toString"]

    def __init__(self):
        pass

    def toString(self):
        return "Eof"

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
haxe_io_Eof._hx_class = haxe_io_Eof
globalClasses._hx_classes["haxe.io.Eof"] = haxe_io_Eof

class haxe_io_Error(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.io.Error"
    _hx_constructs = ["Blocked", "Overflow", "OutsideBounds", "Custom"]

    @staticmethod
    def Custom(e):
        return haxe_io_Error("Custom", 3, (e,))
haxe_io_Error.Blocked = haxe_io_Error("Blocked", 0, ())
haxe_io_Error.Overflow = haxe_io_Error("Overflow", 1, ())
haxe_io_Error.OutsideBounds = haxe_io_Error("OutsideBounds", 2, ())
haxe_io_Error._hx_class = haxe_io_Error
globalClasses._hx_classes["haxe.io.Error"] = haxe_io_Error


class haxe_io_FPHelper:
    _hx_class_name = "haxe.io.FPHelper"
    __slots__ = ()
    _hx_statics = ["i64tmp", "LN2", "_i32ToFloat", "_i64ToDouble", "_floatToI32", "_doubleToI64", "i32ToFloat", "floatToI32", "i64ToDouble", "doubleToI64"]

    @staticmethod
    def _i32ToFloat(i):
        sign = (1 - ((HxOverrides.rshift(i, 31) << 1)))
        e = ((i >> 23) & 255)
        if (e == 255):
            if (((i & 8388607)) == 0):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        m = ((((i & 8388607)) << 1) if ((e == 0)) else ((i & 8388607) | 8388608))
        return ((sign * m) * Math.pow(2,(e - 150)))

    @staticmethod
    def _i64ToDouble(lo,hi):
        sign = (1 - ((HxOverrides.rshift(hi, 31) << 1)))
        e = ((hi >> 20) & 2047)
        if (e == 2047):
            if ((lo == 0) and ((((hi & 1048575)) == 0))):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        m = (2.220446049250313e-16 * ((((((hi & 1048575)) * 4294967296.) + (((HxOverrides.rshift(lo, 31)) * 2147483648.))) + ((lo & 2147483647)))))
        if (e == 0):
            m = (m * 2.0)
        else:
            m = (m + 1.0)
        return ((sign * m) * Math.pow(2,(e - 1023)))

    @staticmethod
    def _floatToI32(f):
        if (f == 0):
            return 0
        af = (-f if ((f < 0)) else f)
        exp = Math.floor((((Math.NEGATIVE_INFINITY if ((af == 0.0)) else (Math.NaN if ((af < 0.0)) else python_lib_Math.log(af)))) / 0.6931471805599453))
        if (exp > 127):
            return 2139095040
        else:
            if (exp <= -127):
                exp = -127
                af = (af * 7.1362384635298e+44)
            else:
                af = ((((af / Math.pow(2,exp)) - 1.0)) * 8388608)
            return ((((-2147483648 if ((f < 0)) else 0)) | (((exp + 127) << 23))) | Math.floor((af + 0.5)))

    @staticmethod
    def _doubleToI64(v):
        i64 = haxe_io_FPHelper.i64tmp
        if (v == 0):
            i64.low = 0
            i64.high = 0
        elif (not ((((v != Math.POSITIVE_INFINITY) and ((v != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(v))))):
            i64.low = 0
            i64.high = (2146435072 if ((v > 0)) else -1048576)
        else:
            av = (-v if ((v < 0)) else v)
            exp = Math.floor((((Math.NEGATIVE_INFINITY if ((av == 0.0)) else (Math.NaN if ((av < 0.0)) else python_lib_Math.log(av)))) / 0.6931471805599453))
            if (exp > 1023):
                i64.low = -1
                i64.high = 2146435071
            else:
                if (exp <= -1023):
                    exp = -1023
                    av = (av / 2.2250738585072014e-308)
                else:
                    av = ((av / Math.pow(2,exp)) - 1.0)
                v1 = (av * 4503599627370496.)
                sig = (v1 if (((v1 == Math.POSITIVE_INFINITY) or ((v1 == Math.NEGATIVE_INFINITY)))) else (Math.NaN if (python_lib_Math.isnan(v1)) else Math.floor((v1 + 0.5))))
                sig_l = None
                try:
                    sig_l = int(sig)
                except BaseException as _g:
                    None
                    sig_l = None
                sig_l1 = sig_l
                sig_h = None
                try:
                    sig_h = int((sig / 4294967296.0))
                except BaseException as _g:
                    None
                    sig_h = None
                sig_h1 = sig_h
                i64.low = sig_l1
                i64.high = ((((-2147483648 if ((v < 0)) else 0)) | (((exp + 1023) << 20))) | sig_h1)
        return i64

    @staticmethod
    def i32ToFloat(i):
        sign = (1 - ((HxOverrides.rshift(i, 31) << 1)))
        e = ((i >> 23) & 255)
        if (e == 255):
            if (((i & 8388607)) == 0):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        else:
            m = ((((i & 8388607)) << 1) if ((e == 0)) else ((i & 8388607) | 8388608))
            return ((sign * m) * Math.pow(2,(e - 150)))

    @staticmethod
    def floatToI32(f):
        if (f == 0):
            return 0
        else:
            af = (-f if ((f < 0)) else f)
            exp = Math.floor((((Math.NEGATIVE_INFINITY if ((af == 0.0)) else (Math.NaN if ((af < 0.0)) else python_lib_Math.log(af)))) / 0.6931471805599453))
            if (exp > 127):
                return 2139095040
            else:
                if (exp <= -127):
                    exp = -127
                    af = (af * 7.1362384635298e+44)
                else:
                    af = ((((af / Math.pow(2,exp)) - 1.0)) * 8388608)
                return ((((-2147483648 if ((f < 0)) else 0)) | (((exp + 127) << 23))) | Math.floor((af + 0.5)))

    @staticmethod
    def i64ToDouble(low,high):
        sign = (1 - ((HxOverrides.rshift(high, 31) << 1)))
        e = ((high >> 20) & 2047)
        if (e == 2047):
            if ((low == 0) and ((((high & 1048575)) == 0))):
                if (sign > 0):
                    return Math.POSITIVE_INFINITY
                else:
                    return Math.NEGATIVE_INFINITY
            else:
                return Math.NaN
        else:
            m = (2.220446049250313e-16 * ((((((high & 1048575)) * 4294967296.) + (((HxOverrides.rshift(low, 31)) * 2147483648.))) + ((low & 2147483647)))))
            if (e == 0):
                m = (m * 2.0)
            else:
                m = (m + 1.0)
            return ((sign * m) * Math.pow(2,(e - 1023)))

    @staticmethod
    def doubleToI64(v):
        i64 = haxe_io_FPHelper.i64tmp
        if (v == 0):
            i64.low = 0
            i64.high = 0
        elif (not ((((v != Math.POSITIVE_INFINITY) and ((v != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(v))))):
            i64.low = 0
            i64.high = (2146435072 if ((v > 0)) else -1048576)
        else:
            av = (-v if ((v < 0)) else v)
            exp = Math.floor((((Math.NEGATIVE_INFINITY if ((av == 0.0)) else (Math.NaN if ((av < 0.0)) else python_lib_Math.log(av)))) / 0.6931471805599453))
            if (exp > 1023):
                i64.low = -1
                i64.high = 2146435071
            else:
                if (exp <= -1023):
                    exp = -1023
                    av = (av / 2.2250738585072014e-308)
                else:
                    av = ((av / Math.pow(2,exp)) - 1.0)
                v1 = (av * 4503599627370496.)
                sig = (v1 if (((v1 == Math.POSITIVE_INFINITY) or ((v1 == Math.NEGATIVE_INFINITY)))) else (Math.NaN if (python_lib_Math.isnan(v1)) else Math.floor((v1 + 0.5))))
                sig_l = None
                try:
                    sig_l = int(sig)
                except BaseException as _g:
                    None
                    sig_l = None
                sig_l1 = sig_l
                sig_h = None
                try:
                    sig_h = int((sig / 4294967296.0))
                except BaseException as _g:
                    None
                    sig_h = None
                sig_h1 = sig_h
                i64.low = sig_l1
                i64.high = ((((-2147483648 if ((v < 0)) else 0)) | (((exp + 1023) << 20))) | sig_h1)
        return i64
haxe_io_FPHelper._hx_class = haxe_io_FPHelper
globalClasses._hx_classes["haxe.io.FPHelper"] = haxe_io_FPHelper


class haxe_io_Input:
    _hx_class_name = "haxe.io.Input"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["readByte", "readBytes", "close", "set_bigEndian", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString", "getDoubleSig"]

    def readByte(self):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Input.hx", 'lineNumber': 53, 'className': "haxe.io.Input", 'methodName': "readByte"}))

    def readBytes(self,s,pos,_hx_len):
        k = _hx_len
        b = s.b
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        try:
            while (k > 0):
                b[pos] = self.readByte()
                pos = (pos + 1)
                k = (k - 1)
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g
        return (_hx_len - k)

    def close(self):
        pass

    def set_bigEndian(self,b):
        self.bigEndian = b
        return b

    def readAll(self,bufsize = None):
        if (bufsize is None):
            bufsize = 16384
        buf = haxe_io_Bytes.alloc(bufsize)
        total = haxe_io_BytesBuffer()
        try:
            while True:
                _hx_len = self.readBytes(buf,0,bufsize)
                if (_hx_len == 0):
                    raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                if ((_hx_len < 0) or ((_hx_len > buf.length))):
                    raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
                total.b.extend(buf.b[0:_hx_len])
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g
        return total.getBytes()

    def readFullBytes(self,s,pos,_hx_len):
        while (_hx_len > 0):
            k = self.readBytes(s,pos,_hx_len)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            pos = (pos + k)
            _hx_len = (_hx_len - k)

    def read(self,nbytes):
        s = haxe_io_Bytes.alloc(nbytes)
        p = 0
        while (nbytes > 0):
            k = self.readBytes(s,p,nbytes)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            p = (p + k)
            nbytes = (nbytes - k)
        return s

    def readUntil(self,end):
        buf = haxe_io_BytesBuffer()
        last = None
        while True:
            last = self.readByte()
            if (not ((last != end))):
                break
            buf.b.append(last)
        return buf.getBytes().toString()

    def readLine(self):
        buf = haxe_io_BytesBuffer()
        last = None
        s = None
        try:
            while True:
                last = self.readByte()
                if (not ((last != 10))):
                    break
                buf.b.append(last)
            s = buf.getBytes().toString()
            if (HxString.charCodeAt(s,(len(s) - 1)) == 13):
                s = HxString.substr(s,0,-1)
        except BaseException as _g:
            None
            _g1 = haxe_Exception.caught(_g).unwrap()
            if Std.isOfType(_g1,haxe_io_Eof):
                e = _g1
                s = buf.getBytes().toString()
                if (len(s) == 0):
                    raise haxe_Exception.thrown(e)
            else:
                raise _g
        return s

    def readFloat(self):
        return haxe_io_FPHelper.i32ToFloat(self.readInt32())

    def readDouble(self):
        i1 = self.readInt32()
        i2 = self.readInt32()
        if self.bigEndian:
            return haxe_io_FPHelper.i64ToDouble(i2,i1)
        else:
            return haxe_io_FPHelper.i64ToDouble(i1,i2)

    def readInt8(self):
        n = self.readByte()
        if (n >= 128):
            return (n - 256)
        return n

    def readInt16(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        n = ((ch2 | ((ch1 << 8))) if (self.bigEndian) else (ch1 | ((ch2 << 8))))
        if (((n & 32768)) != 0):
            return (n - 65536)
        return n

    def readUInt16(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        if self.bigEndian:
            return (ch2 | ((ch1 << 8)))
        else:
            return (ch1 | ((ch2 << 8)))

    def readInt24(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        n = (((ch3 | ((ch2 << 8))) | ((ch1 << 16))) if (self.bigEndian) else ((ch1 | ((ch2 << 8))) | ((ch3 << 16))))
        if (((n & 8388608)) != 0):
            return (n - 16777216)
        return n

    def readUInt24(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        if self.bigEndian:
            return ((ch3 | ((ch2 << 8))) | ((ch1 << 16)))
        else:
            return ((ch1 | ((ch2 << 8))) | ((ch3 << 16)))

    def readInt32(self):
        ch1 = self.readByte()
        ch2 = self.readByte()
        ch3 = self.readByte()
        ch4 = self.readByte()
        n = ((((ch4 | ((ch3 << 8))) | ((ch2 << 16))) | ((ch1 << 24))) if (self.bigEndian) else (((ch1 | ((ch2 << 8))) | ((ch3 << 16))) | ((ch4 << 24))))
        if (((n & -2147483648)) != 0):
            return (n | -2147483648)
        else:
            return n

    def readString(self,_hx_len,encoding = None):
        b = haxe_io_Bytes.alloc(_hx_len)
        self.readFullBytes(b,0,_hx_len)
        return b.getString(0,_hx_len,encoding)

    def getDoubleSig(self,_hx_bytes):
        return ((((((((((_hx_bytes[1] if 1 < len(_hx_bytes) else None) & 15)) << 16) | (((_hx_bytes[2] if 2 < len(_hx_bytes) else None) << 8))) | (_hx_bytes[3] if 3 < len(_hx_bytes) else None))) * 4294967296.) + (((((_hx_bytes[4] if 4 < len(_hx_bytes) else None) >> 7)) * 2147483648))) + ((((((((_hx_bytes[4] if 4 < len(_hx_bytes) else None) & 127)) << 24) | (((_hx_bytes[5] if 5 < len(_hx_bytes) else None) << 16))) | (((_hx_bytes[6] if 6 < len(_hx_bytes) else None) << 8))) | (_hx_bytes[7] if 7 < len(_hx_bytes) else None))))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bigEndian = None
haxe_io_Input._hx_class = haxe_io_Input
globalClasses._hx_classes["haxe.io.Input"] = haxe_io_Input


class haxe_io_Output:
    _hx_class_name = "haxe.io.Output"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["writeByte", "writeBytes", "flush", "close", "set_bigEndian", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]

    def writeByte(self,c):
        raise haxe_exceptions_NotImplementedException(None,None,_hx_AnonObject({'fileName': "haxe/io/Output.hx", 'lineNumber': 47, 'className': "haxe.io.Output", 'methodName': "writeByte"}))

    def writeBytes(self,s,pos,_hx_len):
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        b = s.b
        k = _hx_len
        while (k > 0):
            self.writeByte(b[pos])
            pos = (pos + 1)
            k = (k - 1)
        return _hx_len

    def flush(self):
        pass

    def close(self):
        pass

    def set_bigEndian(self,b):
        self.bigEndian = b
        return b

    def write(self,s):
        l = s.length
        p = 0
        while (l > 0):
            k = self.writeBytes(s,p,l)
            if (k == 0):
                raise haxe_Exception.thrown(haxe_io_Error.Blocked)
            p = (p + k)
            l = (l - k)

    def writeFullBytes(self,s,pos,_hx_len):
        while (_hx_len > 0):
            k = self.writeBytes(s,pos,_hx_len)
            pos = (pos + k)
            _hx_len = (_hx_len - k)

    def writeFloat(self,x):
        self.writeInt32(haxe_io_FPHelper.floatToI32(x))

    def writeDouble(self,x):
        i64 = haxe_io_FPHelper.doubleToI64(x)
        if self.bigEndian:
            self.writeInt32(i64.high)
            self.writeInt32(i64.low)
        else:
            self.writeInt32(i64.low)
            self.writeInt32(i64.high)

    def writeInt8(self,x):
        if ((x < -128) or ((x >= 128))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeByte((x & 255))

    def writeInt16(self,x):
        if ((x < -32768) or ((x >= 32768))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeUInt16((x & 65535))

    def writeUInt16(self,x):
        if ((x < 0) or ((x >= 65536))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        if self.bigEndian:
            self.writeByte((x >> 8))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte((x >> 8))

    def writeInt24(self,x):
        if ((x < -8388608) or ((x >= 8388608))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        self.writeUInt24((x & 16777215))

    def writeUInt24(self,x):
        if ((x < 0) or ((x >= 16777216))):
            raise haxe_Exception.thrown(haxe_io_Error.Overflow)
        if self.bigEndian:
            self.writeByte((x >> 16))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x >> 16))

    def writeInt32(self,x):
        if self.bigEndian:
            self.writeByte(HxOverrides.rshift(x, 24))
            self.writeByte(((x >> 16) & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte((x & 255))
        else:
            self.writeByte((x & 255))
            self.writeByte(((x >> 8) & 255))
            self.writeByte(((x >> 16) & 255))
            self.writeByte(HxOverrides.rshift(x, 24))

    def prepare(self,nbytes):
        pass

    def writeInput(self,i,bufsize = None):
        if (bufsize is None):
            bufsize = 4096
        buf = haxe_io_Bytes.alloc(bufsize)
        try:
            while True:
                _hx_len = i.readBytes(buf,0,bufsize)
                if (_hx_len == 0):
                    raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                p = 0
                while (_hx_len > 0):
                    k = self.writeBytes(buf,p,_hx_len)
                    if (k == 0):
                        raise haxe_Exception.thrown(haxe_io_Error.Blocked)
                    p = (p + k)
                    _hx_len = (_hx_len - k)
        except BaseException as _g:
            None
            if (not Std.isOfType(haxe_Exception.caught(_g).unwrap(),haxe_io_Eof)):
                raise _g

    def writeString(self,s,encoding = None):
        b = haxe_io_Bytes.ofString(s,encoding)
        self.writeFullBytes(b,0,b.length)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.bigEndian = None
haxe_io_Output._hx_class = haxe_io_Output
globalClasses._hx_classes["haxe.io.Output"] = haxe_io_Output


class haxe_io_Path:
    _hx_class_name = "haxe.io.Path"
    __slots__ = ("dir", "file", "ext", "backslash")
    _hx_fields = ["dir", "file", "ext", "backslash"]
    _hx_methods = ["toString"]
    _hx_statics = ["withoutExtension", "withoutDirectory", "directory", "extension", "withExtension", "join", "normalize", "addTrailingSlash", "removeTrailingSlashes", "isAbsolute", "unescape", "escape"]

    def __init__(self,path):
        self.backslash = None
        self.ext = None
        self.file = None
        self.dir = None
        path1 = path
        _hx_local_0 = len(path1)
        if (_hx_local_0 == 1):
            if (path1 == "."):
                self.dir = path
                self.file = ""
                return
        elif (_hx_local_0 == 2):
            if (path1 == ".."):
                self.dir = path
                self.file = ""
                return
        else:
            pass
        startIndex = None
        c1 = None
        if (startIndex is None):
            c1 = path.rfind("/", 0, len(path))
        else:
            i = path.rfind("/", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("/"))) if ((i == -1)) else (i + 1))
            check = path.find("/", startLeft, len(path))
            c1 = (check if (((check > i) and ((check <= startIndex)))) else i)
        startIndex = None
        c2 = None
        if (startIndex is None):
            c2 = path.rfind("\\", 0, len(path))
        else:
            i = path.rfind("\\", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("\\"))) if ((i == -1)) else (i + 1))
            check = path.find("\\", startLeft, len(path))
            c2 = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (c1 < c2):
            self.dir = HxString.substr(path,0,c2)
            path = HxString.substr(path,(c2 + 1),None)
            self.backslash = True
        elif (c2 < c1):
            self.dir = HxString.substr(path,0,c1)
            path = HxString.substr(path,(c1 + 1),None)
        else:
            self.dir = None
        startIndex = None
        cp = None
        if (startIndex is None):
            cp = path.rfind(".", 0, len(path))
        else:
            i = path.rfind(".", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("."))) if ((i == -1)) else (i + 1))
            check = path.find(".", startLeft, len(path))
            cp = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (cp != -1):
            self.ext = HxString.substr(path,(cp + 1),None)
            self.file = HxString.substr(path,0,cp)
        else:
            self.ext = None
            self.file = path

    def toString(self):
        return ((HxOverrides.stringOrNull((("" if ((self.dir is None)) else (HxOverrides.stringOrNull(self.dir) + HxOverrides.stringOrNull((("\\" if (self.backslash) else "/"))))))) + HxOverrides.stringOrNull(self.file)) + HxOverrides.stringOrNull((("" if ((self.ext is None)) else ("." + HxOverrides.stringOrNull(self.ext))))))

    @staticmethod
    def withoutExtension(path):
        s = haxe_io_Path(path)
        s.ext = None
        return s.toString()

    @staticmethod
    def withoutDirectory(path):
        s = haxe_io_Path(path)
        s.dir = None
        return s.toString()

    @staticmethod
    def directory(path):
        s = haxe_io_Path(path)
        if (s.dir is None):
            return ""
        return s.dir

    @staticmethod
    def extension(path):
        s = haxe_io_Path(path)
        if (s.ext is None):
            return ""
        return s.ext

    @staticmethod
    def withExtension(path,ext):
        s = haxe_io_Path(path)
        s.ext = ext
        return s.toString()

    @staticmethod
    def join(paths):
        def _hx_local_0(s):
            if (s is not None):
                return (s != "")
            else:
                return False
        paths1 = list(filter(_hx_local_0,paths))
        if (len(paths1) == 0):
            return ""
        path = (paths1[0] if 0 < len(paths1) else None)
        _g = 1
        _g1 = len(paths1)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            path = haxe_io_Path.addTrailingSlash(path)
            path = (("null" if path is None else path) + HxOverrides.stringOrNull((paths1[i] if i >= 0 and i < len(paths1) else None)))
        return haxe_io_Path.normalize(path)

    @staticmethod
    def normalize(path):
        from python import python_Boot
        from python import python_internal_ArrayImpl
        slash = "/"
        _this = path.split("\\")
        path = slash.join([python_Boot.toString1(x1,'') for x1 in _this])
        if (path == slash):
            return slash
        target = []
        _g = 0
        _g1 = (list(path) if ((slash == "")) else path.split(slash))
        while (_g < len(_g1)):
            token = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (((token == "..") and ((len(target) > 0))) and ((python_internal_ArrayImpl._get(target, (len(target) - 1)) != ".."))):
                if (len(target) != 0):
                    target.pop()
            elif (token == ""):
                if ((len(target) > 0) or ((HxString.charCodeAt(path,0) == 47))):
                    target.append(token)
            elif (token != "."):
                target.append(token)
        tmp = slash.join([python_Boot.toString1(x1,'') for x1 in target])
        acc_b = python_lib_io_StringIO()
        colon = False
        slashes = False
        _g = 0
        _g1 = len(tmp)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            _g2 = (-1 if ((i >= len(tmp))) else ord(tmp[i]))
            _g3 = _g2
            if (_g3 == 47):
                if (not colon):
                    slashes = True
                else:
                    i1 = _g2
                    colon = False
                    if slashes:
                        acc_b.write("/")
                        slashes = False
                    acc_b.write("".join(map(chr,[i1])))
            elif (_g3 == 58):
                acc_b.write(":")
                colon = True
            else:
                i2 = _g2
                colon = False
                if slashes:
                    acc_b.write("/")
                    slashes = False
                acc_b.write("".join(map(chr,[i2])))
        return acc_b.getvalue()

    @staticmethod
    def addTrailingSlash(path):
        if (len(path) == 0):
            return "/"
        startIndex = None
        c1 = None
        if (startIndex is None):
            c1 = path.rfind("/", 0, len(path))
        else:
            i = path.rfind("/", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("/"))) if ((i == -1)) else (i + 1))
            check = path.find("/", startLeft, len(path))
            c1 = (check if (((check > i) and ((check <= startIndex)))) else i)
        startIndex = None
        c2 = None
        if (startIndex is None):
            c2 = path.rfind("\\", 0, len(path))
        else:
            i = path.rfind("\\", 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len("\\"))) if ((i == -1)) else (i + 1))
            check = path.find("\\", startLeft, len(path))
            c2 = (check if (((check > i) and ((check <= startIndex)))) else i)
        if (c1 < c2):
            if (c2 != ((len(path) - 1))):
                return (("null" if path is None else path) + "\\")
            else:
                return path
        elif (c1 != ((len(path) - 1))):
            return (("null" if path is None else path) + "/")
        else:
            return path

    @staticmethod
    def removeTrailingSlashes(path):
        while True:
            _g = HxString.charCodeAt(path,(len(path) - 1))
            if (_g is None):
                break
            else:
                _g1 = _g
                if ((_g1 == 92) or ((_g1 == 47))):
                    path = HxString.substr(path,0,-1)
                else:
                    break
        return path

    @staticmethod
    def isAbsolute(path):
        if path.startswith("/"):
            return True
        if ((("" if ((1 >= len(path))) else path[1])) == ":"):
            return True
        if path.startswith("\\\\"):
            return True
        return False

    @staticmethod
    def unescape(path):
        regex = EReg("-x([0-9][0-9])","g")
        def _hx_local_1():
            def _hx_local_0(regex):
                code = Std.parseInt(regex.matchObj.group(1))
                return "".join(map(chr,[code]))
            return regex.map(path,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def escape(path,allowSlashes = None):
        if (allowSlashes is None):
            allowSlashes = False
        regex = (EReg("[^A-Za-z0-9_/\\\\\\.]","g") if allowSlashes else EReg("[^A-Za-z0-9_\\.]","g"))
        def _hx_local_1():
            def _hx_local_0(v):
                return ("-x" + Std.string(HxString.charCodeAt(v.matchObj.group(0),0)))
            return regex.map(path,_hx_local_0)
        return _hx_local_1()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.dir = None
        _hx_o.file = None
        _hx_o.ext = None
        _hx_o.backslash = None
haxe_io_Path._hx_class = haxe_io_Path
globalClasses._hx_classes["haxe.io.Path"] = haxe_io_Path


class haxe_iterators_ArrayIterator:
    _hx_class_name = "haxe.iterators.ArrayIterator"
    __slots__ = ("array", "current")
    _hx_fields = ["array", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        from python import python_internal_ArrayImpl
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return python_internal_ArrayImpl._get(self.array, _hx_local_2())
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.array = None
        _hx_o.current = None
haxe_iterators_ArrayIterator._hx_class = haxe_iterators_ArrayIterator
globalClasses._hx_classes["haxe.iterators.ArrayIterator"] = haxe_iterators_ArrayIterator


class haxe_iterators_ArrayKeyValueIterator:
    _hx_class_name = "haxe.iterators.ArrayKeyValueIterator"
    __slots__ = ("current", "array")
    _hx_fields = ["current", "array"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,array):
        self.current = 0
        self.array = array

    def hasNext(self):
        return (self.current < len(self.array))

    def next(self):
        def _hx_local_3():
            from python import python_internal_ArrayImpl
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.current
                _hx_local_0.current = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_AnonObject({'value': python_internal_ArrayImpl._get(self.array, self.current), 'key': _hx_local_2()})
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.current = None
        _hx_o.array = None
haxe_iterators_ArrayKeyValueIterator._hx_class = haxe_iterators_ArrayKeyValueIterator
globalClasses._hx_classes["haxe.iterators.ArrayKeyValueIterator"] = haxe_iterators_ArrayKeyValueIterator


class haxe_iterators_HashMapKeyValueIterator:
    _hx_class_name = "haxe.iterators.HashMapKeyValueIterator"
    __slots__ = ("map", "keys")
    _hx_fields = ["map", "keys"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_map):
        self.map = _hx_map
        self.keys = _hx_map.keys.iterator()

    def hasNext(self):
        return self.keys.hasNext()

    def next(self):
        key = self.keys.next()
        _this = self.map.values
        key1 = key.hashCode()
        return _hx_AnonObject({'value': _this.h.get(key1,None), 'key': key})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.map = None
        _hx_o.keys = None
haxe_iterators_HashMapKeyValueIterator._hx_class = haxe_iterators_HashMapKeyValueIterator
globalClasses._hx_classes["haxe.iterators.HashMapKeyValueIterator"] = haxe_iterators_HashMapKeyValueIterator


class haxe_iterators_MapKeyValueIterator:
    _hx_class_name = "haxe.iterators.MapKeyValueIterator"
    __slots__ = ("map", "keys")
    _hx_fields = ["map", "keys"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_map):
        self.map = _hx_map
        self.keys = _hx_map.keys()

    def hasNext(self):
        return self.keys.hasNext()

    def next(self):
        key = self.keys.next()
        return _hx_AnonObject({'value': self.map.get(key), 'key': key})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.map = None
        _hx_o.keys = None
haxe_iterators_MapKeyValueIterator._hx_class = haxe_iterators_MapKeyValueIterator
globalClasses._hx_classes["haxe.iterators.MapKeyValueIterator"] = haxe_iterators_MapKeyValueIterator


class haxe_iterators_RestIterator:
    _hx_class_name = "haxe.iterators.RestIterator"
    __slots__ = ("args", "current")
    _hx_fields = ["args", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,args):
        self.current = 0
        self.args = args

    def hasNext(self):
        return (self.current < len(self.args))

    def next(self):
        from python import python_internal_ArrayImpl
        index = self.current
        self.current = (self.current + 1)
        return python_internal_ArrayImpl._get(self.args, index)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.args = None
        _hx_o.current = None
haxe_iterators_RestIterator._hx_class = haxe_iterators_RestIterator
globalClasses._hx_classes["haxe.iterators.RestIterator"] = haxe_iterators_RestIterator


class haxe_iterators_RestKeyValueIterator:
    _hx_class_name = "haxe.iterators.RestKeyValueIterator"
    __slots__ = ("args", "current")
    _hx_fields = ["args", "current"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,args):
        self.current = 0
        self.args = args

    def hasNext(self):
        return (self.current < len(self.args))

    def next(self):
        from python import python_internal_ArrayImpl
        tmp = self.current
        index = self.current
        self.current = (self.current + 1)
        return _hx_AnonObject({'key': tmp, 'value': python_internal_ArrayImpl._get(self.args, index)})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.args = None
        _hx_o.current = None
haxe_iterators_RestKeyValueIterator._hx_class = haxe_iterators_RestKeyValueIterator
globalClasses._hx_classes["haxe.iterators.RestKeyValueIterator"] = haxe_iterators_RestKeyValueIterator


class haxe_iterators_StringIterator:
    _hx_class_name = "haxe.iterators.StringIterator"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        index = self.offset
        self.offset = (self.offset + 1)
        return ord(self.s[index])

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringIterator._hx_class = haxe_iterators_StringIterator
globalClasses._hx_classes["haxe.iterators.StringIterator"] = haxe_iterators_StringIterator


class haxe_iterators_StringIteratorUnicode:
    _hx_class_name = "haxe.iterators.StringIteratorUnicode"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]
    _hx_statics = ["unicodeIterator"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        index = self.offset
        self.offset = (self.offset + 1)
        return ord(self.s[index])

    @staticmethod
    def unicodeIterator(s):
        return haxe_iterators_StringIteratorUnicode(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringIteratorUnicode._hx_class = haxe_iterators_StringIteratorUnicode
globalClasses._hx_classes["haxe.iterators.StringIteratorUnicode"] = haxe_iterators_StringIteratorUnicode


class haxe_iterators_StringKeyValueIterator:
    _hx_class_name = "haxe.iterators.StringKeyValueIterator"
    __slots__ = ("offset", "s")
    _hx_fields = ["offset", "s"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,s):
        self.offset = 0
        self.s = s

    def hasNext(self):
        return (self.offset < len(self.s))

    def next(self):
        tmp = self.offset
        s = self.s
        index = self.offset
        self.offset = (self.offset + 1)
        return _hx_AnonObject({'key': tmp, 'value': (-1 if ((index >= len(s))) else ord(s[index]))})

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.offset = None
        _hx_o.s = None
haxe_iterators_StringKeyValueIterator._hx_class = haxe_iterators_StringKeyValueIterator
globalClasses._hx_classes["haxe.iterators.StringKeyValueIterator"] = haxe_iterators_StringKeyValueIterator

class haxe_macro_Access(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Access"
    _hx_constructs = ["APublic", "APrivate", "AStatic", "AOverride", "ADynamic", "AInline", "AMacro", "AFinal", "AExtern", "AAbstract", "AOverload"]
haxe_macro_Access.APublic = haxe_macro_Access("APublic", 0, ())
haxe_macro_Access.APrivate = haxe_macro_Access("APrivate", 1, ())
haxe_macro_Access.AStatic = haxe_macro_Access("AStatic", 2, ())
haxe_macro_Access.AOverride = haxe_macro_Access("AOverride", 3, ())
haxe_macro_Access.ADynamic = haxe_macro_Access("ADynamic", 4, ())
haxe_macro_Access.AInline = haxe_macro_Access("AInline", 5, ())
haxe_macro_Access.AMacro = haxe_macro_Access("AMacro", 6, ())
haxe_macro_Access.AFinal = haxe_macro_Access("AFinal", 7, ())
haxe_macro_Access.AExtern = haxe_macro_Access("AExtern", 8, ())
haxe_macro_Access.AAbstract = haxe_macro_Access("AAbstract", 9, ())
haxe_macro_Access.AOverload = haxe_macro_Access("AOverload", 10, ())
haxe_macro_Access._hx_class = haxe_macro_Access
globalClasses._hx_classes["haxe.macro.Access"] = haxe_macro_Access

class haxe_macro_Binop(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Binop"
    _hx_constructs = ["OpAdd", "OpMult", "OpDiv", "OpSub", "OpAssign", "OpEq", "OpNotEq", "OpGt", "OpGte", "OpLt", "OpLte", "OpAnd", "OpOr", "OpXor", "OpBoolAnd", "OpBoolOr", "OpShl", "OpShr", "OpUShr", "OpMod", "OpAssignOp", "OpInterval", "OpArrow", "OpIn"]

    @staticmethod
    def OpAssignOp(op):
        return haxe_macro_Binop("OpAssignOp", 20, (op,))
haxe_macro_Binop.OpAdd = haxe_macro_Binop("OpAdd", 0, ())
haxe_macro_Binop.OpMult = haxe_macro_Binop("OpMult", 1, ())
haxe_macro_Binop.OpDiv = haxe_macro_Binop("OpDiv", 2, ())
haxe_macro_Binop.OpSub = haxe_macro_Binop("OpSub", 3, ())
haxe_macro_Binop.OpAssign = haxe_macro_Binop("OpAssign", 4, ())
haxe_macro_Binop.OpEq = haxe_macro_Binop("OpEq", 5, ())
haxe_macro_Binop.OpNotEq = haxe_macro_Binop("OpNotEq", 6, ())
haxe_macro_Binop.OpGt = haxe_macro_Binop("OpGt", 7, ())
haxe_macro_Binop.OpGte = haxe_macro_Binop("OpGte", 8, ())
haxe_macro_Binop.OpLt = haxe_macro_Binop("OpLt", 9, ())
haxe_macro_Binop.OpLte = haxe_macro_Binop("OpLte", 10, ())
haxe_macro_Binop.OpAnd = haxe_macro_Binop("OpAnd", 11, ())
haxe_macro_Binop.OpOr = haxe_macro_Binop("OpOr", 12, ())
haxe_macro_Binop.OpXor = haxe_macro_Binop("OpXor", 13, ())
haxe_macro_Binop.OpBoolAnd = haxe_macro_Binop("OpBoolAnd", 14, ())
haxe_macro_Binop.OpBoolOr = haxe_macro_Binop("OpBoolOr", 15, ())
haxe_macro_Binop.OpShl = haxe_macro_Binop("OpShl", 16, ())
haxe_macro_Binop.OpShr = haxe_macro_Binop("OpShr", 17, ())
haxe_macro_Binop.OpUShr = haxe_macro_Binop("OpUShr", 18, ())
haxe_macro_Binop.OpMod = haxe_macro_Binop("OpMod", 19, ())
haxe_macro_Binop.OpInterval = haxe_macro_Binop("OpInterval", 21, ())
haxe_macro_Binop.OpArrow = haxe_macro_Binop("OpArrow", 22, ())
haxe_macro_Binop.OpIn = haxe_macro_Binop("OpIn", 23, ())
haxe_macro_Binop._hx_class = haxe_macro_Binop
globalClasses._hx_classes["haxe.macro.Binop"] = haxe_macro_Binop

class haxe_macro_ComplexType(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ComplexType"
    _hx_constructs = ["TPath", "TFunction", "TAnonymous", "TParent", "TExtend", "TOptional", "TNamed", "TIntersection"]

    @staticmethod
    def TPath(p):
        return haxe_macro_ComplexType("TPath", 0, (p,))

    @staticmethod
    def TFunction(args,ret):
        return haxe_macro_ComplexType("TFunction", 1, (args,ret))

    @staticmethod
    def TAnonymous(fields):
        return haxe_macro_ComplexType("TAnonymous", 2, (fields,))

    @staticmethod
    def TParent(t):
        return haxe_macro_ComplexType("TParent", 3, (t,))

    @staticmethod
    def TExtend(p,fields):
        return haxe_macro_ComplexType("TExtend", 4, (p,fields))

    @staticmethod
    def TOptional(t):
        return haxe_macro_ComplexType("TOptional", 5, (t,))

    @staticmethod
    def TNamed(n,t):
        return haxe_macro_ComplexType("TNamed", 6, (n,t))

    @staticmethod
    def TIntersection(tl):
        return haxe_macro_ComplexType("TIntersection", 7, (tl,))
haxe_macro_ComplexType._hx_class = haxe_macro_ComplexType
globalClasses._hx_classes["haxe.macro.ComplexType"] = haxe_macro_ComplexType

class haxe_macro_Constant(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Constant"
    _hx_constructs = ["CInt", "CFloat", "CString", "CIdent", "CRegexp"]

    @staticmethod
    def CInt(v):
        return haxe_macro_Constant("CInt", 0, (v,))

    @staticmethod
    def CFloat(f):
        return haxe_macro_Constant("CFloat", 1, (f,))

    @staticmethod
    def CString(s,kind = None):
        return haxe_macro_Constant("CString", 2, (s,kind))

    @staticmethod
    def CIdent(s):
        return haxe_macro_Constant("CIdent", 3, (s,))

    @staticmethod
    def CRegexp(r,opt):
        return haxe_macro_Constant("CRegexp", 4, (r,opt))
haxe_macro_Constant._hx_class = haxe_macro_Constant
globalClasses._hx_classes["haxe.macro.Constant"] = haxe_macro_Constant

class haxe_macro_DisplayKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.DisplayKind"
    _hx_constructs = ["DKCall", "DKDot", "DKStructure", "DKMarked", "DKPattern"]

    @staticmethod
    def DKPattern(outermost):
        return haxe_macro_DisplayKind("DKPattern", 4, (outermost,))
haxe_macro_DisplayKind.DKCall = haxe_macro_DisplayKind("DKCall", 0, ())
haxe_macro_DisplayKind.DKDot = haxe_macro_DisplayKind("DKDot", 1, ())
haxe_macro_DisplayKind.DKStructure = haxe_macro_DisplayKind("DKStructure", 2, ())
haxe_macro_DisplayKind.DKMarked = haxe_macro_DisplayKind("DKMarked", 3, ())
haxe_macro_DisplayKind._hx_class = haxe_macro_DisplayKind
globalClasses._hx_classes["haxe.macro.DisplayKind"] = haxe_macro_DisplayKind

class haxe_macro_Error(haxe_Exception):
    _hx_class_name = "haxe.macro.Error"
    __slots__ = ("pos",)
    _hx_fields = ["pos"]
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_Exception


    def __init__(self,message,pos,previous = None):
        self.pos = None
        super().__init__(message,previous)
        self.pos = pos
        _hx_local_0 = self
        _hx_local_1 = _hx_local_0._hx___skipStack
        _hx_local_0._hx___skipStack = (_hx_local_1 + 1)
        _hx_local_1

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.pos = None
haxe_macro_Error._hx_class = haxe_macro_Error
globalClasses._hx_classes["haxe.macro.Error"] = haxe_macro_Error

class haxe_macro_ExprDef(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ExprDef"
    _hx_constructs = ["EConst", "EArray", "EBinop", "EField", "EParenthesis", "EObjectDecl", "EArrayDecl", "ECall", "ENew", "EUnop", "EVars", "EFunction", "EBlock", "EFor", "EIf", "EWhile", "ESwitch", "ETry", "EReturn", "EBreak", "EContinue", "EUntyped", "EThrow", "ECast", "EDisplay", "EDisplayNew", "ETernary", "ECheckType", "EMeta", "EIs"]

    @staticmethod
    def EConst(c):
        return haxe_macro_ExprDef("EConst", 0, (c,))

    @staticmethod
    def EArray(e1,e2):
        return haxe_macro_ExprDef("EArray", 1, (e1,e2))

    @staticmethod
    def EBinop(op,e1,e2):
        return haxe_macro_ExprDef("EBinop", 2, (op,e1,e2))

    @staticmethod
    def EField(e,field):
        return haxe_macro_ExprDef("EField", 3, (e,field))

    @staticmethod
    def EParenthesis(e):
        return haxe_macro_ExprDef("EParenthesis", 4, (e,))

    @staticmethod
    def EObjectDecl(fields):
        return haxe_macro_ExprDef("EObjectDecl", 5, (fields,))

    @staticmethod
    def EArrayDecl(values):
        return haxe_macro_ExprDef("EArrayDecl", 6, (values,))

    @staticmethod
    def ECall(e,params):
        return haxe_macro_ExprDef("ECall", 7, (e,params))

    @staticmethod
    def ENew(t,params):
        return haxe_macro_ExprDef("ENew", 8, (t,params))

    @staticmethod
    def EUnop(op,postFix,e):
        return haxe_macro_ExprDef("EUnop", 9, (op,postFix,e))

    @staticmethod
    def EVars(vars):
        return haxe_macro_ExprDef("EVars", 10, (vars,))

    @staticmethod
    def EFunction(kind,f):
        return haxe_macro_ExprDef("EFunction", 11, (kind,f))

    @staticmethod
    def EBlock(exprs):
        return haxe_macro_ExprDef("EBlock", 12, (exprs,))

    @staticmethod
    def EFor(it,expr):
        return haxe_macro_ExprDef("EFor", 13, (it,expr))

    @staticmethod
    def EIf(econd,eif,eelse):
        return haxe_macro_ExprDef("EIf", 14, (econd,eif,eelse))

    @staticmethod
    def EWhile(econd,e,normalWhile):
        return haxe_macro_ExprDef("EWhile", 15, (econd,e,normalWhile))

    @staticmethod
    def ESwitch(e,cases,edef):
        return haxe_macro_ExprDef("ESwitch", 16, (e,cases,edef))

    @staticmethod
    def ETry(e,catches):
        return haxe_macro_ExprDef("ETry", 17, (e,catches))

    @staticmethod
    def EReturn(e = None):
        return haxe_macro_ExprDef("EReturn", 18, (e,))

    @staticmethod
    def EUntyped(e):
        return haxe_macro_ExprDef("EUntyped", 21, (e,))

    @staticmethod
    def EThrow(e):
        return haxe_macro_ExprDef("EThrow", 22, (e,))

    @staticmethod
    def ECast(e,t):
        return haxe_macro_ExprDef("ECast", 23, (e,t))

    @staticmethod
    def EDisplay(e,displayKind):
        return haxe_macro_ExprDef("EDisplay", 24, (e,displayKind))

    @staticmethod
    def EDisplayNew(t):
        return haxe_macro_ExprDef("EDisplayNew", 25, (t,))

    @staticmethod
    def ETernary(econd,eif,eelse):
        return haxe_macro_ExprDef("ETernary", 26, (econd,eif,eelse))

    @staticmethod
    def ECheckType(e,t):
        return haxe_macro_ExprDef("ECheckType", 27, (e,t))

    @staticmethod
    def EMeta(s,e):
        return haxe_macro_ExprDef("EMeta", 28, (s,e))

    @staticmethod
    def EIs(e,t):
        return haxe_macro_ExprDef("EIs", 29, (e,t))
haxe_macro_ExprDef.EBreak = haxe_macro_ExprDef("EBreak", 19, ())
haxe_macro_ExprDef.EContinue = haxe_macro_ExprDef("EContinue", 20, ())
haxe_macro_ExprDef._hx_class = haxe_macro_ExprDef
globalClasses._hx_classes["haxe.macro.ExprDef"] = haxe_macro_ExprDef

class haxe_macro_FieldType(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.FieldType"
    _hx_constructs = ["FVar", "FFun", "FProp"]

    @staticmethod
    def FVar(t,e = None):
        return haxe_macro_FieldType("FVar", 0, (t,e))

    @staticmethod
    def FFun(f):
        return haxe_macro_FieldType("FFun", 1, (f,))

    @staticmethod
    def FProp(get,set,t = None,e= None):
        return haxe_macro_FieldType("FProp", 2, (get,set,t,e))
haxe_macro_FieldType._hx_class = haxe_macro_FieldType
globalClasses._hx_classes["haxe.macro.FieldType"] = haxe_macro_FieldType

class haxe_macro_FunctionKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.FunctionKind"
    _hx_constructs = ["FAnonymous", "FNamed", "FArrow"]

    @staticmethod
    def FNamed(name,inlined = None):
        return haxe_macro_FunctionKind("FNamed", 1, (name,inlined))
haxe_macro_FunctionKind.FAnonymous = haxe_macro_FunctionKind("FAnonymous", 0, ())
haxe_macro_FunctionKind.FArrow = haxe_macro_FunctionKind("FArrow", 2, ())
haxe_macro_FunctionKind._hx_class = haxe_macro_FunctionKind
globalClasses._hx_classes["haxe.macro.FunctionKind"] = haxe_macro_FunctionKind

class haxe_macro_ImportMode(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.ImportMode"
    _hx_constructs = ["INormal", "IAsName", "IAll"]

    @staticmethod
    def IAsName(alias):
        return haxe_macro_ImportMode("IAsName", 1, (alias,))
haxe_macro_ImportMode.INormal = haxe_macro_ImportMode("INormal", 0, ())
haxe_macro_ImportMode.IAll = haxe_macro_ImportMode("IAll", 2, ())
haxe_macro_ImportMode._hx_class = haxe_macro_ImportMode
globalClasses._hx_classes["haxe.macro.ImportMode"] = haxe_macro_ImportMode

class haxe_macro_QuoteStatus(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.QuoteStatus"
    _hx_constructs = ["Unquoted", "Quoted"]
haxe_macro_QuoteStatus.Unquoted = haxe_macro_QuoteStatus("Unquoted", 0, ())
haxe_macro_QuoteStatus.Quoted = haxe_macro_QuoteStatus("Quoted", 1, ())
haxe_macro_QuoteStatus._hx_class = haxe_macro_QuoteStatus
globalClasses._hx_classes["haxe.macro.QuoteStatus"] = haxe_macro_QuoteStatus

class haxe_macro_StringLiteralKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.StringLiteralKind"
    _hx_constructs = ["DoubleQuotes", "SingleQuotes"]
haxe_macro_StringLiteralKind.DoubleQuotes = haxe_macro_StringLiteralKind("DoubleQuotes", 0, ())
haxe_macro_StringLiteralKind.SingleQuotes = haxe_macro_StringLiteralKind("SingleQuotes", 1, ())
haxe_macro_StringLiteralKind._hx_class = haxe_macro_StringLiteralKind
globalClasses._hx_classes["haxe.macro.StringLiteralKind"] = haxe_macro_StringLiteralKind

class haxe_macro_TypeDefKind(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.TypeDefKind"
    _hx_constructs = ["TDEnum", "TDStructure", "TDClass", "TDAlias", "TDAbstract", "TDField"]

    @staticmethod
    def TDClass(superClass = None,interfaces= None,isInterface= None,isFinal= None,isAbstract= None):
        return haxe_macro_TypeDefKind("TDClass", 2, (superClass,interfaces,isInterface,isFinal,isAbstract))

    @staticmethod
    def TDAlias(t):
        return haxe_macro_TypeDefKind("TDAlias", 3, (t,))

    @staticmethod
    def TDAbstract(tthis,_hx_from = None,to= None):
        return haxe_macro_TypeDefKind("TDAbstract", 4, (tthis,_hx_from,to))

    @staticmethod
    def TDField(kind,access = None):
        return haxe_macro_TypeDefKind("TDField", 5, (kind,access))
haxe_macro_TypeDefKind.TDEnum = haxe_macro_TypeDefKind("TDEnum", 0, ())
haxe_macro_TypeDefKind.TDStructure = haxe_macro_TypeDefKind("TDStructure", 1, ())
haxe_macro_TypeDefKind._hx_class = haxe_macro_TypeDefKind
globalClasses._hx_classes["haxe.macro.TypeDefKind"] = haxe_macro_TypeDefKind


class haxe_macro_TypeParam(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.TypeParam"
    _hx_constructs = ["TPType", "TPExpr"]

    @staticmethod
    def TPType(t):
        return haxe_macro_TypeParam("TPType", 0, (t,))

    @staticmethod
    def TPExpr(e):
        return haxe_macro_TypeParam("TPExpr", 1, (e,))
haxe_macro_TypeParam._hx_class = haxe_macro_TypeParam
globalClasses._hx_classes["haxe.macro.TypeParam"] = haxe_macro_TypeParam

class haxe_macro_Unop(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.macro.Unop"
    _hx_constructs = ["OpIncrement", "OpDecrement", "OpNot", "OpNeg", "OpNegBits", "OpSpread"]
haxe_macro_Unop.OpIncrement = haxe_macro_Unop("OpIncrement", 0, ())
haxe_macro_Unop.OpDecrement = haxe_macro_Unop("OpDecrement", 1, ())
haxe_macro_Unop.OpNot = haxe_macro_Unop("OpNot", 2, ())
haxe_macro_Unop.OpNeg = haxe_macro_Unop("OpNeg", 3, ())
haxe_macro_Unop.OpNegBits = haxe_macro_Unop("OpNegBits", 4, ())
haxe_macro_Unop.OpSpread = haxe_macro_Unop("OpSpread", 5, ())
haxe_macro_Unop._hx_class = haxe_macro_Unop
globalClasses._hx_classes["haxe.macro.Unop"] = haxe_macro_Unop

class haxe_rtti_CType(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.rtti.CType"
    _hx_constructs = ["CUnknown", "CEnum", "CClass", "CTypedef", "CFunction", "CAnonymous", "CDynamic", "CAbstract"]

    @staticmethod
    def CEnum(name,params):
        return haxe_rtti_CType("CEnum", 1, (name,params))

    @staticmethod
    def CClass(name,params):
        return haxe_rtti_CType("CClass", 2, (name,params))

    @staticmethod
    def CTypedef(name,params):
        return haxe_rtti_CType("CTypedef", 3, (name,params))

    @staticmethod
    def CFunction(args,ret):
        return haxe_rtti_CType("CFunction", 4, (args,ret))

    @staticmethod
    def CAnonymous(fields):
        return haxe_rtti_CType("CAnonymous", 5, (fields,))

    @staticmethod
    def CDynamic(t = None):
        return haxe_rtti_CType("CDynamic", 6, (t,))

    @staticmethod
    def CAbstract(name,params):
        return haxe_rtti_CType("CAbstract", 7, (name,params))
haxe_rtti_CType.CUnknown = haxe_rtti_CType("CUnknown", 0, ())
haxe_rtti_CType._hx_class = haxe_rtti_CType
globalClasses._hx_classes["haxe.rtti.CType"] = haxe_rtti_CType

class haxe_rtti_CTypeTools:
    _hx_class_name = "haxe.rtti.CTypeTools"
    __slots__ = ()
    _hx_statics = ["toString", "nameWithParams", "functionArgumentName", "classField"]

    @staticmethod
    def toString(t):
        from python import python_Boot
        tmp = t.index
        if (tmp == 0):
            return "unknown"
        elif (tmp == 1):
            name = t.params[0]
            params = t.params[1]
            return haxe_rtti_CTypeTools.nameWithParams(name,params)
        elif (tmp == 2):
            name = t.params[0]
            params = t.params[1]
            return haxe_rtti_CTypeTools.nameWithParams(name,params)
        elif (tmp == 3):
            name = t.params[0]
            params = t.params[1]
            return haxe_rtti_CTypeTools.nameWithParams(name,params)
        elif (tmp == 4):
            args = t.params[0]
            ret = t.params[1]
            if (len(args) == 0):
                return ("Void -> " + HxOverrides.stringOrNull(haxe_rtti_CTypeTools.toString(ret)))
            else:
                _this = list(map(haxe_rtti_CTypeTools.functionArgumentName,args))
                return ((HxOverrides.stringOrNull(" -> ".join([python_Boot.toString1(x1,'') for x1 in _this])) + " -> ") + HxOverrides.stringOrNull(haxe_rtti_CTypeTools.toString(ret)))
        elif (tmp == 5):
            fields = t.params[0]
            _this = list(map(haxe_rtti_CTypeTools.classField,fields))
            return (("{ " + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + "}")
        elif (tmp == 6):
            d = t.params[0]
            if (d is None):
                return "Dynamic"
            else:
                return (("Dynamic<" + HxOverrides.stringOrNull(haxe_rtti_CTypeTools.toString(d))) + ">")
        elif (tmp == 7):
            name = t.params[0]
            params = t.params[1]
            return haxe_rtti_CTypeTools.nameWithParams(name,params)
        else:
            pass

    @staticmethod
    def nameWithParams(name,params):
        from python import python_Boot
        if (len(params) == 0):
            return name
        _this = list(map(haxe_rtti_CTypeTools.toString,params))
        return (((("null" if name is None else name) + "<") + HxOverrides.stringOrNull(", ".join([python_Boot.toString1(x1,'') for x1 in _this]))) + ">")

    @staticmethod
    def functionArgumentName(arg):
        return (((HxOverrides.stringOrNull((("?" if (arg.opt) else ""))) + HxOverrides.stringOrNull((("" if ((arg.name == "")) else (HxOverrides.stringOrNull(arg.name) + ":"))))) + HxOverrides.stringOrNull(haxe_rtti_CTypeTools.toString(arg.t))) + HxOverrides.stringOrNull((("" if ((Reflect.field(arg,"value") is None)) else (" = " + HxOverrides.stringOrNull(Reflect.field(arg,"value")))))))

    @staticmethod
    def classField(cf):
        return ((HxOverrides.stringOrNull(cf.name) + ":") + HxOverrides.stringOrNull(haxe_rtti_CTypeTools.toString(cf.type)))
haxe_rtti_CTypeTools._hx_class = haxe_rtti_CTypeTools
globalClasses._hx_classes["haxe.rtti.CTypeTools"] = haxe_rtti_CTypeTools


class haxe_rtti_Rights(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.rtti.Rights"
    _hx_constructs = ["RNormal", "RNo", "RCall", "RMethod", "RDynamic", "RInline"]

    @staticmethod
    def RCall(m):
        return haxe_rtti_Rights("RCall", 2, (m,))
haxe_rtti_Rights.RNormal = haxe_rtti_Rights("RNormal", 0, ())
haxe_rtti_Rights.RNo = haxe_rtti_Rights("RNo", 1, ())
haxe_rtti_Rights.RMethod = haxe_rtti_Rights("RMethod", 3, ())
haxe_rtti_Rights.RDynamic = haxe_rtti_Rights("RDynamic", 4, ())
haxe_rtti_Rights.RInline = haxe_rtti_Rights("RInline", 5, ())
haxe_rtti_Rights._hx_class = haxe_rtti_Rights
globalClasses._hx_classes["haxe.rtti.Rights"] = haxe_rtti_Rights

class haxe_rtti_TypeApi:
    _hx_class_name = "haxe.rtti.TypeApi"
    __slots__ = ()
    _hx_statics = ["typeInfos", "isVar", "leq", "rightsEq", "typeEq", "fieldEq", "constructorEq"]

    @staticmethod
    def typeInfos(t):
        inf = None
        tmp = t.index
        if (tmp == 0):
            _g = t.params[0]
            _g = t.params[1]
            _g = t.params[2]
            raise haxe_Exception.thrown("Unexpected Package")
        elif (tmp == 1):
            c = t.params[0]
            inf = c
        elif (tmp == 2):
            e = t.params[0]
            inf = e
        elif (tmp == 3):
            t1 = t.params[0]
            inf = t1
        elif (tmp == 4):
            a = t.params[0]
            inf = a
        else:
            pass
        return inf

    @staticmethod
    def isVar(t):
        if (t.index == 4):
            _g = t.params[0]
            _g = t.params[1]
            return False
        else:
            return True

    @staticmethod
    def leq(f,l1,l2):
        it_current = 0
        it_array = l2
        _g = 0
        while (_g < len(l1)):
            e1 = (l1[_g] if _g >= 0 and _g < len(l1) else None)
            _g = (_g + 1)
            if (it_current >= len(it_array)):
                return False
            e2 = it_current
            it_current = (it_current + 1)
            e21 = (it_array[e2] if e2 >= 0 and e2 < len(it_array) else None)
            if (not f(e1,e21)):
                return False
        if (it_current < len(it_array)):
            return False
        return True

    @staticmethod
    def rightsEq(r1,r2):
        if (r1 == r2):
            return True
        if (r1.index == 2):
            m1 = r1.params[0]
            if (r2.index == 2):
                m2 = r2.params[0]
                return (m1 == m2)
        return False

    @staticmethod
    def typeEq(t1,t2):
        tmp = t1.index
        if (tmp == 0):
            return (t2 == haxe_rtti_CType.CUnknown)
        elif (tmp == 1):
            name = t1.params[0]
            params = t1.params[1]
            if (t2.index == 1):
                name2 = t2.params[0]
                params2 = t2.params[1]
                if (name == name2):
                    return haxe_rtti_TypeApi.leq(haxe_rtti_TypeApi.typeEq,params,params2)
                else:
                    return False
        elif (tmp == 2):
            name = t1.params[0]
            params = t1.params[1]
            if (t2.index == 2):
                name2 = t2.params[0]
                params2 = t2.params[1]
                if (name == name2):
                    return haxe_rtti_TypeApi.leq(haxe_rtti_TypeApi.typeEq,params,params2)
                else:
                    return False
        elif (tmp == 3):
            name = t1.params[0]
            params = t1.params[1]
            if (t2.index == 3):
                name2 = t2.params[0]
                params2 = t2.params[1]
                if (name == name2):
                    return haxe_rtti_TypeApi.leq(haxe_rtti_TypeApi.typeEq,params,params2)
                else:
                    return False
        elif (tmp == 4):
            args = t1.params[0]
            ret = t1.params[1]
            if (t2.index == 4):
                args2 = t2.params[0]
                ret2 = t2.params[1]
                def _hx_local_0(a,b):
                    if ((a.name == b.name) and ((a.opt == b.opt))):
                        return haxe_rtti_TypeApi.typeEq(a.t,b.t)
                    else:
                        return False
                if haxe_rtti_TypeApi.leq(_hx_local_0,args,args2):
                    return haxe_rtti_TypeApi.typeEq(ret,ret2)
                else:
                    return False
        elif (tmp == 5):
            fields = t1.params[0]
            if (t2.index == 5):
                fields2 = t2.params[0]
                def _hx_local_2():
                    def _hx_local_1(a,b):
                        return haxe_rtti_TypeApi.fieldEq(a,b)
                    return haxe_rtti_TypeApi.leq(_hx_local_1,fields,fields2)
                return _hx_local_2()
        elif (tmp == 6):
            t = t1.params[0]
            if (t2.index == 6):
                t21 = t2.params[0]
                if ((t is None) != ((t21 is None))):
                    return False
                if (t is not None):
                    return haxe_rtti_TypeApi.typeEq(t,t21)
                else:
                    return True
        elif (tmp == 7):
            name = t1.params[0]
            params = t1.params[1]
            if (t2.index == 7):
                name2 = t2.params[0]
                params2 = t2.params[1]
                if (name == name2):
                    return haxe_rtti_TypeApi.leq(haxe_rtti_TypeApi.typeEq,params,params2)
                else:
                    return False
        else:
            pass
        return False

    @staticmethod
    def fieldEq(f1,f2):
        if (f1.name != f2.name):
            return False
        if (not haxe_rtti_TypeApi.typeEq(f1.type,f2.type)):
            return False
        if (f1.isPublic != f2.isPublic):
            return False
        if (f1.doc != f2.doc):
            return False
        if (not haxe_rtti_TypeApi.rightsEq(f1.get,f2.get)):
            return False
        if (not haxe_rtti_TypeApi.rightsEq(f1.set,f2.set)):
            return False
        if ((f1.params is None) != ((f2.params is None))):
            return False
        tmp = None
        if (f1.params is not None):
            from python import python_Boot
            _this = f1.params
            tmp1 = ":".join([python_Boot.toString1(x1,'') for x1 in _this])
            _this = f2.params
            tmp = (tmp1 != ":".join([python_Boot.toString1(x1,'') for x1 in _this]))
        else:
            tmp = False
        if tmp:
            return False
        return True

    @staticmethod
    def constructorEq(c1,c2):
        if (c1.name != c2.name):
            return False
        if (c1.doc != c2.doc):
            return False
        if ((c1.args is None) != ((c2.args is None))):
            return False
        def _hx_local_0(a,b):
            if ((a.name == b.name) and ((a.opt == b.opt))):
                return haxe_rtti_TypeApi.typeEq(a.t,b.t)
            else:
                return False
        if ((c1.args is not None) and (not haxe_rtti_TypeApi.leq(_hx_local_0,c1.args,c2.args))):
            return False
        return True
haxe_rtti_TypeApi._hx_class = haxe_rtti_TypeApi
globalClasses._hx_classes["haxe.rtti.TypeApi"] = haxe_rtti_TypeApi


class haxe_rtti_TypeTree(Enum):
    __slots__ = ()
    _hx_class_name = "haxe.rtti.TypeTree"
    _hx_constructs = ["TPackage", "TClassdecl", "TEnumdecl", "TTypedecl", "TAbstractdecl"]

    @staticmethod
    def TPackage(name,full,subs):
        return haxe_rtti_TypeTree("TPackage", 0, (name,full,subs))

    @staticmethod
    def TClassdecl(c):
        return haxe_rtti_TypeTree("TClassdecl", 1, (c,))

    @staticmethod
    def TEnumdecl(e):
        return haxe_rtti_TypeTree("TEnumdecl", 2, (e,))

    @staticmethod
    def TTypedecl(t):
        return haxe_rtti_TypeTree("TTypedecl", 3, (t,))

    @staticmethod
    def TAbstractdecl(a):
        return haxe_rtti_TypeTree("TAbstractdecl", 4, (a,))
haxe_rtti_TypeTree._hx_class = haxe_rtti_TypeTree
globalClasses._hx_classes["haxe.rtti.TypeTree"] = haxe_rtti_TypeTree


class haxe_rtti_XmlParser:
    _hx_class_name = "haxe.rtti.XmlParser"
    _hx_fields = ["root", "curplatform"]
    _hx_methods = ["sort", "sortFields", "process", "mergeRights", "mergeDoc", "mergeFields", "newField", "mergeClasses", "mergeEnums", "mergeTypedefs", "mergeAbstracts", "merge", "mkPath", "mkTypeParams", "mkRights", "xerror", "xroot", "processElement", "xmeta", "xoverloads", "xpath", "xclass", "xclassfield", "xenum", "xenumfield", "xabstract", "xtypedef", "xtype", "xtypeparams", "defplat"]

    def __init__(self):
        self.curplatform = None
        self.root = list()

    def sort(self,l = None):
        if (l is None):
            l = self.root
        def _hx_local_0(e1,e2):
            n1 = None
            if (e1.index == 0):
                _g = e1.params[1]
                _g = e1.params[2]
                p = e1.params[0]
                n1 = (" " + ("null" if p is None else p))
            else:
                n1 = haxe_rtti_TypeApi.typeInfos(e1).path
            n2 = None
            if (e2.index == 0):
                _g = e2.params[1]
                _g = e2.params[2]
                p = e2.params[0]
                n2 = (" " + ("null" if p is None else p))
            else:
                n2 = haxe_rtti_TypeApi.typeInfos(e2).path
            if (n1 > n2):
                return 1
            return -1
        l.sort(key= python_lib_Functools.cmp_to_key(_hx_local_0))
        _g = 0
        while (_g < len(l)):
            x = (l[_g] if _g >= 0 and _g < len(l) else None)
            _g = (_g + 1)
            tmp = x.index
            if (tmp == 0):
                _g1 = x.params[0]
                _g2 = x.params[1]
                l1 = x.params[2]
                self.sort(l1)
            elif (tmp == 1):
                c = x.params[0]
                self.sortFields(c.fields)
                self.sortFields(c.statics)
            elif (tmp == 2):
                _g3 = x.params[0]
            elif (tmp == 3):
                _g4 = x.params[0]
            elif (tmp == 4):
                _g5 = x.params[0]
            else:
                pass

    def sortFields(self,a):
        def _hx_local_0(f1,f2):
            v1 = haxe_rtti_TypeApi.isVar(f1.type)
            v2 = haxe_rtti_TypeApi.isVar(f2.type)
            if (v1 and (not v2)):
                return -1
            if (v2 and (not v1)):
                return 1
            if (f1.name == "new"):
                return -1
            if (f2.name == "new"):
                return 1
            if (f1.name > f2.name):
                return 1
            return -1
        a.sort(key= python_lib_Functools.cmp_to_key(_hx_local_0))

    def process(self,x,platform):
        self.curplatform = platform
        if ((x.nodeType != Xml.Document) and ((x.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
        this1 = x
        self.xroot(this1)

    def mergeRights(self,f1,f2):
        if ((((f1.get == haxe_rtti_Rights.RInline) and ((f1.set == haxe_rtti_Rights.RNo))) and ((f2.get == haxe_rtti_Rights.RNormal))) and ((f2.set == haxe_rtti_Rights.RMethod))):
            f1.get = haxe_rtti_Rights.RNormal
            f1.set = haxe_rtti_Rights.RMethod
            return True
        if Type.enumEq(f1.get,f2.get):
            return Type.enumEq(f1.set,f2.set)
        else:
            return False

    def mergeDoc(self,f1,f2):
        if (f1.doc is None):
            f1.doc = f2.doc
        elif (f2.doc is None):
            f2.doc = f1.doc
        return True

    def mergeFields(self,f,f2):
        if (not haxe_rtti_TypeApi.fieldEq(f,f2)):
            if (((f.name == f2.name) and ((self.mergeRights(f,f2) or self.mergeRights(f2,f)))) and self.mergeDoc(f,f2)):
                return haxe_rtti_TypeApi.fieldEq(f,f2)
            else:
                return False
        else:
            return True

    def newField(self,c,f):
        pass

    def mergeClasses(self,c,c2):
        if (c.isInterface != c2.isInterface):
            return False
        if (self.curplatform is not None):
            _this = c.platforms
            x = self.curplatform
            _this.append(x)
        if (c.isExtern != c2.isExtern):
            c.isExtern = False
        _g = 0
        _g1 = c2.fields
        while (_g < len(_g1)):
            f2 = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            found = None
            _g2 = 0
            _g3 = c.fields
            while (_g2 < len(_g3)):
                f = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                _g2 = (_g2 + 1)
                if self.mergeFields(f,f2):
                    found = f
                    break
            if (found is None):
                self.newField(c,f2)
                _this = c.fields
                _this.append(f2)
            elif (self.curplatform is not None):
                _this1 = found.platforms
                x = self.curplatform
                _this1.append(x)
        _g = 0
        _g1 = c2.statics
        while (_g < len(_g1)):
            f2 = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            found = None
            _g2 = 0
            _g3 = c.statics
            while (_g2 < len(_g3)):
                f = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                _g2 = (_g2 + 1)
                if self.mergeFields(f,f2):
                    found = f
                    break
            if (found is None):
                self.newField(c,f2)
                _this = c.statics
                _this.append(f2)
            elif (self.curplatform is not None):
                _this1 = found.platforms
                x = self.curplatform
                _this1.append(x)
        return True

    def mergeEnums(self,e,e2):
        if (e.isExtern != e2.isExtern):
            return False
        if (self.curplatform is not None):
            _this = e.platforms
            x = self.curplatform
            _this.append(x)
        _g = 0
        _g1 = e2.constructors
        while (_g < len(_g1)):
            c2 = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            found = None
            _g2 = 0
            _g3 = e.constructors
            while (_g2 < len(_g3)):
                c = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                _g2 = (_g2 + 1)
                if haxe_rtti_TypeApi.constructorEq(c,c2):
                    found = c
                    break
            if (found is None):
                _this = e.constructors
                _this.append(c2)
            elif (self.curplatform is not None):
                _this1 = found.platforms
                x = self.curplatform
                _this1.append(x)
        return True

    def mergeTypedefs(self,t,t2):
        if (self.curplatform is None):
            return False
        _this = t.platforms
        x = self.curplatform
        _this.append(x)
        t.types.h[self.curplatform] = t2.type
        return True

    def mergeAbstracts(self,a,a2):
        if (self.curplatform is None):
            return False
        if ((len(a.to) != len(a2.to)) or ((len(a._hx_from) != len(a2._hx_from)))):
            return False
        _g = 0
        _g1 = len(a.to)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (not haxe_rtti_TypeApi.typeEq((a.to[i] if i >= 0 and i < len(a.to) else None).t,(a2.to[i] if i >= 0 and i < len(a2.to) else None).t)):
                return False
        _g = 0
        _g1 = len(a._hx_from)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if (not haxe_rtti_TypeApi.typeEq((a._hx_from[i] if i >= 0 and i < len(a._hx_from) else None).t,(a2._hx_from[i] if i >= 0 and i < len(a2._hx_from) else None).t)):
                return False
        if (a2.impl is not None):
            self.mergeClasses(a.impl,a2.impl)
        _this = a.platforms
        x = self.curplatform
        _this.append(x)
        return True

    def merge(self,t):
        from python import python_Boot
        inf = haxe_rtti_TypeApi.typeInfos(t)
        _this = inf.path
        pack = _this.split(".")
        cur = self.root
        curpack = list()
        if (len(pack) != 0):
            pack.pop()
        _g = 0
        while (_g < len(pack)):
            p = (pack[_g] if _g >= 0 and _g < len(pack) else None)
            _g = (_g + 1)
            found = False
            _g1 = 0
            while (_g1 < len(cur)):
                pk = (cur[_g1] if _g1 >= 0 and _g1 < len(cur) else None)
                _g1 = (_g1 + 1)
                if (pk.index == 0):
                    _g2 = pk.params[1]
                    pname = pk.params[0]
                    subs = pk.params[2]
                    if (pname == p):
                        found = True
                        cur = subs
                        break
            curpack.append(p)
            if (not found):
                pk1 = list()
                x = haxe_rtti_TypeTree.TPackage(p,".".join([python_Boot.toString1(x1,'') for x1 in curpack]),pk1)
                cur.append(x)
                cur = pk1
        _g = 0
        while (_g < len(cur)):
            ct = (cur[_g] if _g >= 0 and _g < len(cur) else None)
            _g = (_g + 1)
            tmp = None
            if (ct.index == 0):
                _g1 = ct.params[0]
                _g2 = ct.params[1]
                _g3 = ct.params[2]
                tmp = True
            else:
                tmp = False
            if tmp:
                continue
            tinf = haxe_rtti_TypeApi.typeInfos(ct)
            if (tinf.path == inf.path):
                sameType = True
                if ((tinf.doc is None) != ((inf.doc is None))):
                    if (inf.doc is None):
                        inf.doc = tinf.doc
                    else:
                        tinf.doc = inf.doc
                if (tinf.path == "haxe._Int64.NativeInt64"):
                    continue
                if (((tinf.module == inf.module) and ((tinf.doc == inf.doc))) and ((tinf.isPrivate == inf.isPrivate))):
                    tmp1 = ct.index
                    if (tmp1 == 0):
                        _g4 = ct.params[0]
                        _g5 = ct.params[1]
                        _g6 = ct.params[2]
                        sameType = False
                    elif (tmp1 == 1):
                        c = ct.params[0]
                        if (t.index == 1):
                            c2 = t.params[0]
                            if self.mergeClasses(c,c2):
                                return
                        else:
                            sameType = False
                    elif (tmp1 == 2):
                        e = ct.params[0]
                        if (t.index == 2):
                            e2 = t.params[0]
                            if self.mergeEnums(e,e2):
                                return
                        else:
                            sameType = False
                    elif (tmp1 == 3):
                        td = ct.params[0]
                        if (t.index == 3):
                            td2 = t.params[0]
                            if self.mergeTypedefs(td,td2):
                                return
                    elif (tmp1 == 4):
                        a = ct.params[0]
                        if (t.index == 4):
                            a2 = t.params[0]
                            if self.mergeAbstracts(a,a2):
                                return
                        else:
                            sameType = False
                    else:
                        pass
                msg = (((("module " + HxOverrides.stringOrNull(inf.module)) + " should be ") + HxOverrides.stringOrNull(tinf.module)) if ((tinf.module != inf.module)) else ("documentation is different" if ((tinf.doc != inf.doc)) else ("private flag is different" if ((tinf.isPrivate != inf.isPrivate)) else ("type kind is different" if ((not sameType)) else "could not merge definition"))))
                _this = tinf.platforms
                raise haxe_Exception.thrown((((((((("Incompatibilities between " + HxOverrides.stringOrNull(tinf.path)) + " in ") + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in _this]))) + " and ") + HxOverrides.stringOrNull(self.curplatform)) + " (") + ("null" if msg is None else msg)) + ")"))
        cur.append(t)

    def mkPath(self,p):
        return p

    def mkTypeParams(self,p):
        pl = p.split(":")
        if ((pl[0] if 0 < len(pl) else None) == ""):
            return list()
        return pl

    def mkRights(self,r):
        r1 = r
        _hx_local_0 = len(r1)
        if (_hx_local_0 == 4):
            if (r1 == "null"):
                return haxe_rtti_Rights.RNo
            else:
                return haxe_rtti_Rights.RCall(r)
        elif (_hx_local_0 == 7):
            if (r1 == "dynamic"):
                return haxe_rtti_Rights.RDynamic
            else:
                return haxe_rtti_Rights.RCall(r)
        elif (_hx_local_0 == 6):
            if (r1 == "inline"):
                return haxe_rtti_Rights.RInline
            elif (r1 == "method"):
                return haxe_rtti_Rights.RMethod
            else:
                return haxe_rtti_Rights.RCall(r)
        else:
            return haxe_rtti_Rights.RCall(r)

    def xerror(self,c):
        tmp = None
        if (c.nodeType == Xml.Document):
            tmp = "Document"
        else:
            if (c.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c.nodeType is None)) else _Xml_XmlType_Impl_.toString(c.nodeType))))))
            tmp = c.nodeName
        raise haxe_Exception.thrown(("Invalid " + ("null" if tmp is None else tmp)))

    def xroot(self,x):
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            self.merge(self.processElement(c1))

    def processElement(self,x):
        if ((x.nodeType != Xml.Document) and ((x.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
        this1 = x
        c = this1
        _g = None
        if (c.nodeType == Xml.Document):
            _g = "Document"
        else:
            if (c.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c.nodeType is None)) else _Xml_XmlType_Impl_.toString(c.nodeType))))))
            _g = c.nodeName
        _g1 = _g
        _hx_local_0 = len(_g1)
        if (_hx_local_0 == 5):
            if (_g1 == "class"):
                return haxe_rtti_TypeTree.TClassdecl(self.xclass(c))
            else:
                return self.xerror(c)
        elif (_hx_local_0 == 4):
            if (_g1 == "enum"):
                return haxe_rtti_TypeTree.TEnumdecl(self.xenum(c))
            else:
                return self.xerror(c)
        elif (_hx_local_0 == 7):
            if (_g1 == "typedef"):
                return haxe_rtti_TypeTree.TTypedecl(self.xtypedef(c))
            else:
                return self.xerror(c)
        elif (_hx_local_0 == 8):
            if (_g1 == "abstract"):
                return haxe_rtti_TypeTree.TAbstractdecl(self.xabstract(c))
            else:
                return self.xerror(c)
        else:
            return self.xerror(c)

    def xmeta(self,x):
        ml = []
        _g = 0
        _g1 = haxe_xml__Access_NodeListAccess_Impl_.resolve(x,"m")
        while (_g < len(_g1)):
            m = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            pl = []
            _g2 = 0
            _g3 = haxe_xml__Access_NodeListAccess_Impl_.resolve(m,"e")
            while (_g2 < len(_g3)):
                p = (_g3[_g2] if _g2 >= 0 and _g2 < len(_g3) else None)
                _g2 = (_g2 + 1)
                x = haxe_xml__Access_Access_Impl_.get_innerHTML(p)
                pl.append(x)
            x1 = _hx_AnonObject({'name': haxe_xml__Access_AttribAccess_Impl_.resolve(m,"n"), 'params': pl})
            ml.append(x1)
        return ml

    def xoverloads(self,x):
        l = list()
        m = x.elements()
        while m.hasNext():
            m1 = m.next()
            x = self.xclassfield(m1)
            l.append(x)
        return l

    def xpath(self,x):
        path = self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path"))
        params = list()
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            x = self.xtype(c1)
            params.append(x)
        return _hx_AnonObject({'path': path, 'params': params})

    def xclass(self,x):
        csuper = None
        doc = None
        tdynamic = None
        interfaces = list()
        fields = list()
        statics = list()
        meta = []
        isInterface = x.exists("interface")
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            _g = None
            if (c1.nodeType == Xml.Document):
                _g = "Document"
            else:
                if (c1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                _g = c1.nodeName
            _g1 = _g
            _hx_local_0 = len(_g1)
            if (_hx_local_0 == 10):
                if (_g1 == "implements"):
                    x3 = self.xpath(c1)
                    interfaces.append(x3)
                elif c1.exists("static"):
                    x4 = self.xclassfield(c1)
                    statics.append(x4)
                else:
                    x5 = self.xclassfield(c1)
                    fields.append(x5)
            elif (_hx_local_0 == 12):
                if (_g1 == "haxe_dynamic"):
                    x2 = c1.firstElement()
                    if ((x2.nodeType != Xml.Document) and ((x2.nodeType != Xml.Element))):
                        raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x2.nodeType is None)) else _Xml_XmlType_Impl_.toString(x2.nodeType))))))
                    this1 = x2
                    tdynamic = self.xtype(this1)
                elif c1.exists("static"):
                    x4 = self.xclassfield(c1)
                    statics.append(x4)
                else:
                    x5 = self.xclassfield(c1)
                    fields.append(x5)
            elif (_hx_local_0 == 4):
                if (_g1 == "meta"):
                    meta = self.xmeta(c1)
                elif c1.exists("static"):
                    x4 = self.xclassfield(c1)
                    statics.append(x4)
                else:
                    x5 = self.xclassfield(c1)
                    fields.append(x5)
            elif (_hx_local_0 == 7):
                if (_g1 == "extends"):
                    if isInterface:
                        x1 = self.xpath(c1)
                        interfaces.append(x1)
                    else:
                        csuper = self.xpath(c1)
                elif c1.exists("static"):
                    x4 = self.xclassfield(c1)
                    statics.append(x4)
                else:
                    x5 = self.xclassfield(c1)
                    fields.append(x5)
            elif (_hx_local_0 == 8):
                if (_g1 == "haxe_doc"):
                    doc = haxe_xml__Access_Access_Impl_.get_innerData(c1)
                elif c1.exists("static"):
                    x4 = self.xclassfield(c1)
                    statics.append(x4)
                else:
                    x5 = self.xclassfield(c1)
                    fields.append(x5)
            elif c1.exists("static"):
                x4 = self.xclassfield(c1)
                statics.append(x4)
            else:
                x5 = self.xclassfield(c1)
                fields.append(x5)
        return _hx_AnonObject({'file': (haxe_xml__Access_AttribAccess_Impl_.resolve(x,"file") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"file")) else None), 'path': self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")), 'module': (self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"module")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"module")) else None), 'doc': doc, 'isPrivate': x.exists("private"), 'isExtern': x.exists("extern"), 'isFinal': x.exists("final"), 'isInterface': isInterface, 'params': self.mkTypeParams(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"params")), 'superClass': csuper, 'interfaces': interfaces, 'fields': fields, 'statics': statics, 'tdynamic': tdynamic, 'platforms': self.defplat(), 'meta': meta})

    def xclassfield(self,x,defPublic = None):
        if (defPublic is None):
            defPublic = False
        e = x.elements()
        t = self.xtype(e.next())
        doc = None
        meta = []
        overloads = None
        c = e
        while c.hasNext():
            c1 = c.next()
            _g = None
            if (c1.nodeType == Xml.Document):
                _g = "Document"
            else:
                if (c1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                _g = c1.nodeName
            _g1 = _g
            _hx_local_0 = len(_g1)
            if (_hx_local_0 == 9):
                if (_g1 == "overloads"):
                    overloads = self.xoverloads(c1)
                else:
                    self.xerror(c1)
            elif (_hx_local_0 == 4):
                if (_g1 == "meta"):
                    meta = self.xmeta(c1)
                else:
                    self.xerror(c1)
            elif (_hx_local_0 == 8):
                if (_g1 == "haxe_doc"):
                    doc = haxe_xml__Access_Access_Impl_.get_innerData(c1)
                else:
                    self.xerror(c1)
            else:
                self.xerror(c1)
        tmp = None
        if (x.nodeType == Xml.Document):
            tmp = "Document"
        else:
            if (x.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
            tmp = x.nodeName
        return _hx_AnonObject({'name': tmp, 'type': t, 'isPublic': (x.exists("public") or defPublic), 'isFinal': x.exists("final"), 'isOverride': x.exists("override"), 'line': (Std.parseInt(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"line")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"line")) else None), 'doc': doc, 'get': (self.mkRights(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"get")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"get")) else haxe_rtti_Rights.RNormal), 'set': (self.mkRights(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"set")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"set")) else haxe_rtti_Rights.RNormal), 'params': (self.mkTypeParams(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"params")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"params")) else []), 'platforms': self.defplat(), 'meta': meta, 'overloads': overloads, 'expr': (haxe_xml__Access_AttribAccess_Impl_.resolve(x,"expr") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"expr")) else None)})

    def xenum(self,x):
        cl = list()
        doc = None
        meta = []
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            tmp = None
            if (c1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (c1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                tmp = c1.nodeName
            if (tmp == "haxe_doc"):
                doc = haxe_xml__Access_Access_Impl_.get_innerData(c1)
            else:
                tmp1 = None
                if (c1.nodeType == Xml.Document):
                    tmp1 = "Document"
                else:
                    if (c1.nodeType != Xml.Element):
                        raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                    tmp1 = c1.nodeName
                if (tmp1 == "meta"):
                    meta = self.xmeta(c1)
                else:
                    x1 = self.xenumfield(c1)
                    cl.append(x1)
        return _hx_AnonObject({'file': (haxe_xml__Access_AttribAccess_Impl_.resolve(x,"file") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"file")) else None), 'path': self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")), 'module': (self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"module")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"module")) else None), 'doc': doc, 'isPrivate': x.exists("private"), 'isExtern': x.exists("extern"), 'params': self.mkTypeParams(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"params")), 'constructors': cl, 'platforms': self.defplat(), 'meta': meta})

    def xenumfield(self,x):
        args = None
        docElements = x.elementsNamed("haxe_doc")
        xdoc = (docElements.next() if (docElements.hasNext()) else None)
        meta = (self.xmeta(haxe_xml__Access_NodeAccess_Impl_.resolve(x,"meta")) if (haxe_xml__Access_HasNodeAccess_Impl_.resolve(x,"meta")) else [])
        if haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"a"):
            _this = haxe_xml__Access_AttribAccess_Impl_.resolve(x,"a")
            names = _this.split(":")
            elts = x.elements()
            args = list()
            _g = 0
            while (_g < len(names)):
                c = (names[_g] if _g >= 0 and _g < len(names) else None)
                _g = (_g + 1)
                opt = False
                if ((("" if ((0 >= len(c))) else c[0])) == "?"):
                    opt = True
                    c = HxString.substr(c,1,None)
                x1 = _hx_AnonObject({'name': c, 'opt': opt, 't': self.xtype(elts.next())})
                args.append(x1)
        tmp = None
        if (x.nodeType == Xml.Document):
            tmp = "Document"
        else:
            if (x.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
            tmp = x.nodeName
        tmp1 = None
        if (xdoc is None):
            tmp1 = None
        else:
            if ((xdoc.nodeType != Xml.Document) and ((xdoc.nodeType != Xml.Element))):
                raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((xdoc.nodeType is None)) else _Xml_XmlType_Impl_.toString(xdoc.nodeType))))))
            this1 = xdoc
            tmp1 = haxe_xml__Access_Access_Impl_.get_innerData(this1)
        return _hx_AnonObject({'name': tmp, 'args': args, 'doc': tmp1, 'meta': meta, 'platforms': self.defplat()})

    def xabstract(self,x):
        doc = None
        impl = None
        athis = None
        meta = []
        to = []
        _hx_from = []
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            _g = None
            if (c1.nodeType == Xml.Document):
                _g = "Document"
            else:
                if (c1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                _g = c1.nodeName
            _g1 = _g
            _hx_local_0 = len(_g1)
            if (_hx_local_0 == 4):
                if (_g1 == "from"):
                    t = c1.elements()
                    while t.hasNext():
                        t1 = t.next()
                        x1 = t1.firstElement()
                        if ((x1.nodeType != Xml.Document) and ((x1.nodeType != Xml.Element))):
                            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x1.nodeType is None)) else _Xml_XmlType_Impl_.toString(x1.nodeType))))))
                        this1 = x1
                        x2 = self.xtype(this1)
                        x3 = (haxe_xml__Access_AttribAccess_Impl_.resolve(t1,"field") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(t1,"field")) else None)
                        _hx_from.append(_hx_AnonObject({'t': x2, 'field': x3}))
                elif (_g1 == "impl"):
                    impl = self.xclass(haxe_xml__Access_NodeAccess_Impl_.resolve(c1,"class"))
                elif (_g1 == "meta"):
                    meta = self.xmeta(c1)
                elif (_g1 == "this"):
                    x4 = c1.firstElement()
                    if ((x4.nodeType != Xml.Document) and ((x4.nodeType != Xml.Element))):
                        raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x4.nodeType is None)) else _Xml_XmlType_Impl_.toString(x4.nodeType))))))
                    this2 = x4
                    athis = self.xtype(this2)
                else:
                    self.xerror(c1)
            elif (_hx_local_0 == 8):
                if (_g1 == "haxe_doc"):
                    doc = haxe_xml__Access_Access_Impl_.get_innerData(c1)
                else:
                    self.xerror(c1)
            elif (_hx_local_0 == 2):
                if (_g1 == "to"):
                    t2 = c1.elements()
                    while t2.hasNext():
                        t3 = t2.next()
                        x5 = t3.firstElement()
                        if ((x5.nodeType != Xml.Document) and ((x5.nodeType != Xml.Element))):
                            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x5.nodeType is None)) else _Xml_XmlType_Impl_.toString(x5.nodeType))))))
                        this3 = x5
                        x6 = self.xtype(this3)
                        x7 = (haxe_xml__Access_AttribAccess_Impl_.resolve(t3,"field") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(t3,"field")) else None)
                        to.append(_hx_AnonObject({'t': x6, 'field': x7}))
                else:
                    self.xerror(c1)
            else:
                self.xerror(c1)
        return _hx_AnonObject({'file': (haxe_xml__Access_AttribAccess_Impl_.resolve(x,"file") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"file")) else None), 'path': self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")), 'module': (self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"module")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"module")) else None), 'doc': doc, 'isPrivate': x.exists("private"), 'params': self.mkTypeParams(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"params")), 'platforms': self.defplat(), 'meta': meta, 'athis': athis, 'to': to, '_hx_from': _hx_from, 'impl': impl})

    def xtypedef(self,x):
        doc = None
        t = None
        meta = []
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            tmp = None
            if (c1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (c1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                tmp = c1.nodeName
            if (tmp == "haxe_doc"):
                doc = haxe_xml__Access_Access_Impl_.get_innerData(c1)
            else:
                tmp1 = None
                if (c1.nodeType == Xml.Document):
                    tmp1 = "Document"
                else:
                    if (c1.nodeType != Xml.Element):
                        raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((c1.nodeType is None)) else _Xml_XmlType_Impl_.toString(c1.nodeType))))))
                    tmp1 = c1.nodeName
                if (tmp1 == "meta"):
                    meta = self.xmeta(c1)
                else:
                    t = self.xtype(c1)
        types = haxe_ds_StringMap()
        if (self.curplatform is not None):
            types.h[self.curplatform] = t
        return _hx_AnonObject({'file': (haxe_xml__Access_AttribAccess_Impl_.resolve(x,"file") if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"file")) else None), 'path': self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")), 'module': (self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"module")) if (haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"module")) else None), 'doc': doc, 'isPrivate': x.exists("private"), 'params': self.mkTypeParams(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"params")), 'type': t, 'types': types, 'platforms': self.defplat(), 'meta': meta})

    def xtype(self,x):
        from python import python_internal_ArrayImpl
        
        _g = None
        if (x.nodeType == Xml.Document):
            _g = "Document"
        else:
            if (x.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
            _g = x.nodeName
        _g1 = _g
        _hx_local_0 = len(_g1)
        if (_hx_local_0 == 1):
            if (_g1 == "a"):
                fields = list()
                f = x.elements()
                while f.hasNext():
                    f1 = f.next()
                    f2 = self.xclassfield(f1,True)
                    f2.platforms = list()
                    fields.append(f2)
                return haxe_rtti_CType.CAnonymous(fields)
            elif (_g1 == "c"):
                return haxe_rtti_CType.CClass(self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")),self.xtypeparams(x))
            elif (_g1 == "d"):
                t = None
                tx = x.firstElement()
                if (tx is not None):
                    if ((tx.nodeType != Xml.Document) and ((tx.nodeType != Xml.Element))):
                        raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((tx.nodeType is None)) else _Xml_XmlType_Impl_.toString(tx.nodeType))))))
                    this1 = tx
                    t = self.xtype(this1)
                return haxe_rtti_CType.CDynamic(t)
            elif (_g1 == "e"):
                return haxe_rtti_CType.CEnum(self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")),self.xtypeparams(x))
            elif (_g1 == "f"):
                args = list()
                _this = haxe_xml__Access_AttribAccess_Impl_.resolve(x,"a")
                aname = _this.split(":")
                eargs_current = 0
                eargs_array = aname
                evalues = None
                if haxe_xml__Access_HasAttribAccess_Impl_.resolve(x,"v"):
                    _this = haxe_xml__Access_AttribAccess_Impl_.resolve(x,"v")
                    evalues = haxe_iterators_ArrayIterator(_this.split(":"))
                else:
                    evalues = None
                e = x.elements()
                while e.hasNext():
                    e1 = e.next()
                    opt = False
                    a = None
                    if (eargs_current < len(eargs_array)):
                        a1 = eargs_current
                        eargs_current = (eargs_current + 1)
                        a = (eargs_array[a1] if a1 >= 0 and a1 < len(eargs_array) else None)
                    else:
                        a = None
                    if (a is None):
                        a = ""
                    if ((("" if ((0 >= len(a))) else a[0])) == "?"):
                        opt = True
                        a = HxString.substr(a,1,None)
                    v = None
                    if ((evalues is None) or ((evalues.current >= len(evalues.array)))):
                        v = None
                    else:
                        def _hx_local_2():
                            _hx_local_1 = evalues.current
                            evalues.current = (evalues.current + 1)
                            return _hx_local_1
                        v = python_internal_ArrayImpl._get(evalues.array, _hx_local_2())
                    x1 = self.xtype(e1)
                    args.append(_hx_AnonObject({'name': a, 'opt': opt, 't': x1, 'value': (None if ((v == "")) else v)}))
                ret = python_internal_ArrayImpl._get(args, (len(args) - 1))
                python_internal_ArrayImpl.remove(args,ret)
                return haxe_rtti_CType.CFunction(args,ret.t)
            elif (_g1 == "t"):
                return haxe_rtti_CType.CTypedef(self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")),self.xtypeparams(x))
            elif (_g1 == "x"):
                return haxe_rtti_CType.CAbstract(self.mkPath(haxe_xml__Access_AttribAccess_Impl_.resolve(x,"path")),self.xtypeparams(x))
            else:
                return self.xerror(x)
        elif (_hx_local_0 == 7):
            if (_g1 == "unknown"):
                return haxe_rtti_CType.CUnknown
            else:
                return self.xerror(x)
        else:
            return self.xerror(x)

    def xtypeparams(self,x):
        p = list()
        c = x.elements()
        while c.hasNext():
            c1 = c.next()
            x = self.xtype(c1)
            p.append(x)
        return p

    def defplat(self):
        l = list()
        if (self.curplatform is not None):
            x = self.curplatform
            l.append(x)
        return l

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.root = None
        _hx_o.curplatform = None
haxe_rtti_XmlParser._hx_class = haxe_rtti_XmlParser
globalClasses._hx_classes["haxe.rtti.XmlParser"] = haxe_rtti_XmlParser


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
globalClasses._hx_classes["haxe.unit.TestCase"] = haxe_unit_TestCase


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
globalClasses._hx_classes["haxe.unit.TestResult"] = haxe_unit_TestResult


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
        from python import python_Boot
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
        from python import python_Lib 
        python_Lib.printString(Std.string(v))

    @staticmethod
    def customTrace(v,p = None):
        haxe_unit_TestRunner.print((((((HxOverrides.stringOrNull(p.fileName) + ":") + Std.string(p.lineNumber)) + ": ") + Std.string(v)) + "\n"))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.result = None
        _hx_o.cases = None
haxe_unit_TestRunner._hx_class = haxe_unit_TestRunner
globalClasses._hx_classes["haxe.unit.TestRunner"] = haxe_unit_TestRunner


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
globalClasses._hx_classes["haxe.unit.TestStatus"] = haxe_unit_TestStatus


class haxe_xml_Parser:
    _hx_class_name = "haxe.xml.Parser"
    __slots__ = ()
    _hx_statics = ["escapes", "parse", "doParse", "isValidChar"]

    @staticmethod
    def parse(_hx_str,strict = None):
        if (strict is None):
            strict = False
        doc = Xml.createDocument()
        haxe_xml_Parser.doParse(_hx_str,strict,0,doc)
        return doc

    @staticmethod
    def doParse(_hx_str,strict,p = None,parent = None):
        if (p is None):
            p = 0
        xml = None
        state = 1
        next = 1
        aname = None
        start = 0
        nsubs = 0
        nbrackets = 0
        buf = StringBuf()
        escapeNext = 1
        attrValQuote = -1
        while (p < len(_hx_str)):
            c = ord(_hx_str[p])
            state1 = state
            if (state1 == 0):
                c1 = c
                if ((((c1 == 32) or ((c1 == 13))) or ((c1 == 10))) or ((c1 == 9))):
                    pass
                else:
                    state = next
                    continue
            elif (state1 == 1):
                if (c == 60):
                    state = 0
                    next = 2
                else:
                    start = p
                    state = 13
                    continue
            elif (state1 == 2):
                c2 = c
                if (c2 == 33):
                    index = (p + 1)
                    if (((-1 if ((index >= len(_hx_str))) else ord(_hx_str[index]))) == 91):
                        p = (p + 2)
                        if (HxString.substr(_hx_str,p,6).upper() != "CDATA["):
                            raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected <![CDATA[",_hx_str,p))
                        p = (p + 5)
                        state = 17
                        start = (p + 1)
                    else:
                        tmp = None
                        index1 = (p + 1)
                        if (((-1 if ((index1 >= len(_hx_str))) else ord(_hx_str[index1]))) != 68):
                            index2 = (p + 1)
                            tmp = (((-1 if ((index2 >= len(_hx_str))) else ord(_hx_str[index2]))) == 100)
                        else:
                            tmp = True
                        if tmp:
                            if (HxString.substr(_hx_str,(p + 2),6).upper() != "OCTYPE"):
                                raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected <!DOCTYPE",_hx_str,p))
                            p = (p + 8)
                            state = 16
                            start = (p + 1)
                        else:
                            tmp1 = None
                            index3 = (p + 1)
                            if (((-1 if ((index3 >= len(_hx_str))) else ord(_hx_str[index3]))) == 45):
                                index4 = (p + 2)
                                tmp1 = (((-1 if ((index4 >= len(_hx_str))) else ord(_hx_str[index4]))) != 45)
                            else:
                                tmp1 = True
                            if tmp1:
                                raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected <!--",_hx_str,p))
                            else:
                                p = (p + 2)
                                state = 15
                                start = (p + 1)
                elif (c2 == 47):
                    if (parent is None):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected node name",_hx_str,p))
                    start = (p + 1)
                    state = 0
                    next = 10
                elif (c2 == 63):
                    state = 14
                    start = p
                else:
                    state = 3
                    start = p
                    continue
            elif (state1 == 3):
                if (not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))):
                    if (p == start):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected node name",_hx_str,p))
                    xml = Xml.createElement(HxString.substr(_hx_str,start,(p - start)))
                    parent.addChild(xml)
                    nsubs = (nsubs + 1)
                    state = 0
                    next = 4
                    continue
            elif (state1 == 4):
                c3 = c
                if (c3 == 47):
                    state = 11
                elif (c3 == 62):
                    state = 9
                else:
                    state = 5
                    start = p
                    continue
            elif (state1 == 5):
                if (not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))):
                    if (start == p):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected attribute name",_hx_str,p))
                    tmp2 = HxString.substr(_hx_str,start,(p - start))
                    aname = tmp2
                    if xml.exists(aname):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Duplicate attribute [" + ("null" if aname is None else aname)) + "]"),_hx_str,p))
                    state = 0
                    next = 6
                    continue
            elif (state1 == 6):
                if (c == 61):
                    state = 0
                    next = 7
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected =",_hx_str,p))
            elif (state1 == 7):
                c4 = c
                if ((c4 == 39) or ((c4 == 34))):
                    buf = StringBuf()
                    state = 8
                    start = (p + 1)
                    attrValQuote = c
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected \"",_hx_str,p))
            elif (state1 == 8):
                c5 = c
                if (c5 == 38):
                    _hx_len = (p - start)
                    s = (HxString.substr(_hx_str,start,None) if ((_hx_len is None)) else HxString.substr(_hx_str,start,_hx_len))
                    buf.b.write(s)
                    state = 18
                    escapeNext = 8
                    start = (p + 1)
                elif ((c5 == 62) or ((c5 == 60))):
                    if strict:
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Invalid unescaped " + HxOverrides.stringOrNull("".join(map(chr,[c])))) + " in attribute value"),_hx_str,p))
                    elif (c == attrValQuote):
                        len1 = (p - start)
                        s1 = (HxString.substr(_hx_str,start,None) if ((len1 is None)) else HxString.substr(_hx_str,start,len1))
                        buf.b.write(s1)
                        val = buf.b.getvalue()
                        buf = StringBuf()
                        xml.set(aname,val)
                        state = 0
                        next = 4
                elif (c == attrValQuote):
                    len2 = (p - start)
                    s2 = (HxString.substr(_hx_str,start,None) if ((len2 is None)) else HxString.substr(_hx_str,start,len2))
                    buf.b.write(s2)
                    val1 = buf.b.getvalue()
                    buf = StringBuf()
                    xml.set(aname,val1)
                    state = 0
                    next = 4
            elif (state1 == 9):
                p = haxe_xml_Parser.doParse(_hx_str,strict,p,xml)
                start = p
                state = 1
            elif (state1 == 10):
                if (not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))):
                    if (start == p):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected node name",_hx_str,p))
                    v = HxString.substr(_hx_str,start,(p - start))
                    if ((parent is None) or ((parent.nodeType != 0))):
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Unexpected </" + ("null" if v is None else v)) + ">, tag is not open"),_hx_str,p))
                    if (parent.nodeType != Xml.Element):
                        raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((parent.nodeType is None)) else _Xml_XmlType_Impl_.toString(parent.nodeType))))))
                    if (v != parent.nodeName):
                        if (parent.nodeType != Xml.Element):
                            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((parent.nodeType is None)) else _Xml_XmlType_Impl_.toString(parent.nodeType))))))
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Expected </" + HxOverrides.stringOrNull(parent.nodeName)) + ">"),_hx_str,p))
                    state = 0
                    next = 12
                    continue
            elif (state1 == 11):
                if (c == 62):
                    state = 1
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected >",_hx_str,p))
            elif (state1 == 12):
                if (c == 62):
                    if (nsubs == 0):
                        parent.addChild(Xml.createPCData(""))
                    return p
                else:
                    raise haxe_Exception.thrown(haxe_xml_XmlParserException("Expected >",_hx_str,p))
            elif (state1 == 13):
                if (c == 60):
                    len3 = (p - start)
                    s3 = (HxString.substr(_hx_str,start,None) if ((len3 is None)) else HxString.substr(_hx_str,start,len3))
                    buf.b.write(s3)
                    child = Xml.createPCData(buf.b.getvalue())
                    buf = StringBuf()
                    parent.addChild(child)
                    nsubs = (nsubs + 1)
                    state = 0
                    next = 2
                elif (c == 38):
                    len4 = (p - start)
                    s4 = (HxString.substr(_hx_str,start,None) if ((len4 is None)) else HxString.substr(_hx_str,start,len4))
                    buf.b.write(s4)
                    state = 18
                    escapeNext = 13
                    start = (p + 1)
            elif (state1 == 14):
                tmp3 = None
                if (c == 63):
                    index5 = (p + 1)
                    tmp3 = (((-1 if ((index5 >= len(_hx_str))) else ord(_hx_str[index5]))) == 62)
                else:
                    tmp3 = False
                if tmp3:
                    p = (p + 1)
                    str1 = HxString.substr(_hx_str,(start + 1),((p - start) - 2))
                    parent.addChild(Xml.createProcessingInstruction(str1))
                    nsubs = (nsubs + 1)
                    state = 1
            elif (state1 == 15):
                tmp4 = None
                tmp5 = None
                if (c == 45):
                    index6 = (p + 1)
                    tmp5 = (((-1 if ((index6 >= len(_hx_str))) else ord(_hx_str[index6]))) == 45)
                else:
                    tmp5 = False
                if tmp5:
                    index7 = (p + 2)
                    tmp4 = (((-1 if ((index7 >= len(_hx_str))) else ord(_hx_str[index7]))) == 62)
                else:
                    tmp4 = False
                if tmp4:
                    parent.addChild(Xml.createComment(HxString.substr(_hx_str,start,(p - start))))
                    nsubs = (nsubs + 1)
                    p = (p + 2)
                    state = 1
            elif (state1 == 16):
                if (c == 91):
                    nbrackets = (nbrackets + 1)
                elif (c == 93):
                    nbrackets = (nbrackets - 1)
                elif ((c == 62) and ((nbrackets == 0))):
                    parent.addChild(Xml.createDocType(HxString.substr(_hx_str,start,(p - start))))
                    nsubs = (nsubs + 1)
                    state = 1
            elif (state1 == 17):
                tmp6 = None
                tmp7 = None
                if (c == 93):
                    index8 = (p + 1)
                    tmp7 = (((-1 if ((index8 >= len(_hx_str))) else ord(_hx_str[index8]))) == 93)
                else:
                    tmp7 = False
                if tmp7:
                    index9 = (p + 2)
                    tmp6 = (((-1 if ((index9 >= len(_hx_str))) else ord(_hx_str[index9]))) == 62)
                else:
                    tmp6 = False
                if tmp6:
                    child1 = Xml.createCData(HxString.substr(_hx_str,start,(p - start)))
                    parent.addChild(child1)
                    nsubs = (nsubs + 1)
                    p = (p + 2)
                    state = 1
            elif (state1 == 18):
                if (c == 59):
                    s5 = HxString.substr(_hx_str,start,(p - start))
                    if (((-1 if ((0 >= len(s5))) else ord(s5[0]))) == 35):
                        c6 = (Std.parseInt(("0" + HxOverrides.stringOrNull(HxString.substr(s5,1,(len(s5) - 1))))) if ((((-1 if ((1 >= len(s5))) else ord(s5[1]))) == 120)) else Std.parseInt(HxString.substr(s5,1,(len(s5) - 1))))
                        s6 = "".join(map(chr,[c6]))
                        buf.b.write(s6)
                    elif (not (s5 in haxe_xml_Parser.escapes.h)):
                        if strict:
                            raise haxe_Exception.thrown(haxe_xml_XmlParserException(("Undefined entity: " + ("null" if s5 is None else s5)),_hx_str,p))
                        s7 = Std.string((("&" + ("null" if s5 is None else s5)) + ";"))
                        buf.b.write(s7)
                    else:
                        s8 = Std.string(haxe_xml_Parser.escapes.h.get(s5,None))
                        buf.b.write(s8)
                    start = (p + 1)
                    state = escapeNext
                elif ((not (((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))) or ((c == 45))))) and ((c != 35))):
                    if strict:
                        raise haxe_Exception.thrown(haxe_xml_XmlParserException(("Invalid character in entity: " + HxOverrides.stringOrNull("".join(map(chr,[c])))),_hx_str,p))
                    s9 = "".join(map(chr,[38]))
                    buf.b.write(s9)
                    len5 = (p - start)
                    s10 = (HxString.substr(_hx_str,start,None) if ((len5 is None)) else HxString.substr(_hx_str,start,len5))
                    buf.b.write(s10)
                    p = (p - 1)
                    start = (p + 1)
                    state = escapeNext
            else:
                pass
            p = (p + 1)
        if (state == 1):
            start = p
            state = 13
        if (state == 13):
            if (parent.nodeType == 0):
                if (parent.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((parent.nodeType is None)) else _Xml_XmlType_Impl_.toString(parent.nodeType))))))
                raise haxe_Exception.thrown(haxe_xml_XmlParserException((("Unclosed node <" + HxOverrides.stringOrNull(parent.nodeName)) + ">"),_hx_str,p))
            if ((p != start) or ((nsubs == 0))):
                _hx_len = (p - start)
                s = (HxString.substr(_hx_str,start,None) if ((_hx_len is None)) else HxString.substr(_hx_str,start,_hx_len))
                buf.b.write(s)
                parent.addChild(Xml.createPCData(buf.b.getvalue()))
                nsubs = (nsubs + 1)
            return p
        if (((not strict) and ((state == 18))) and ((escapeNext == 13))):
            s = "".join(map(chr,[38]))
            buf.b.write(s)
            _hx_len = (p - start)
            s = (HxString.substr(_hx_str,start,None) if ((_hx_len is None)) else HxString.substr(_hx_str,start,_hx_len))
            buf.b.write(s)
            parent.addChild(Xml.createPCData(buf.b.getvalue()))
            nsubs = (nsubs + 1)
            return p
        raise haxe_Exception.thrown(haxe_xml_XmlParserException("Unexpected end",_hx_str,p))

    @staticmethod
    def isValidChar(c):
        if (not ((((((((c >= 97) and ((c <= 122))) or (((c >= 65) and ((c <= 90))))) or (((c >= 48) and ((c <= 57))))) or ((c == 58))) or ((c == 46))) or ((c == 95))))):
            return (c == 45)
        else:
            return True
haxe_xml_Parser._hx_class = haxe_xml_Parser
globalClasses._hx_classes["haxe.xml.Parser"] = haxe_xml_Parser


class haxe_xml_Printer:
    _hx_class_name = "haxe.xml.Printer"
    __slots__ = ("output", "pretty")
    _hx_fields = ["output", "pretty"]
    _hx_methods = ["writeNode", "write", "newline", "hasChildren"]
    _hx_statics = ["print"]

    def __init__(self,pretty):
        self.output = StringBuf()
        self.pretty = pretty

    def writeNode(self,value,tabs):
        _g = value.nodeType
        if (_g == 0):
            _this = self.output
            s = Std.string((("null" if tabs is None else tabs) + "<"))
            _this.b.write(s)
            if (value.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string(value.nodeName)
            _this.b.write(s)
            attribute = value.attributes()
            while attribute.hasNext():
                attribute1 = attribute.next()
                _this = self.output
                s = Std.string(((" " + ("null" if attribute1 is None else attribute1)) + "=\""))
                _this.b.write(s)
                input = StringTools.htmlEscape(value.get(attribute1),True)
                _this1 = self.output
                s1 = Std.string(input)
                _this1.b.write(s1)
                self.output.b.write("\"")
            if self.hasChildren(value):
                self.output.b.write(">")
                if self.pretty:
                    self.output.b.write("\n")
                if ((value.nodeType != Xml.Document) and ((value.nodeType != Xml.Element))):
                    raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
                _g_current = 0
                _g_array = value.children
                while (_g_current < len(_g_array)):
                    child = _g_current
                    _g_current = (_g_current + 1)
                    child1 = (_g_array[child] if child >= 0 and child < len(_g_array) else None)
                    self.writeNode(child1,((("null" if tabs is None else tabs) + "\t") if (self.pretty) else tabs))
                _this = self.output
                s = Std.string((("null" if tabs is None else tabs) + "</"))
                _this.b.write(s)
                if (value.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
                _this = self.output
                s = Std.string(value.nodeName)
                _this.b.write(s)
                self.output.b.write(">")
                if self.pretty:
                    self.output.b.write("\n")
            else:
                self.output.b.write("/>")
                if self.pretty:
                    self.output.b.write("\n")
        elif (_g == 1):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            nodeValue = value.nodeValue
            if (len(nodeValue) != 0):
                input = (("null" if tabs is None else tabs) + HxOverrides.stringOrNull(StringTools.htmlEscape(nodeValue)))
                _this = self.output
                s = Std.string(input)
                _this.b.write(s)
                if self.pretty:
                    self.output.b.write("\n")
        elif (_g == 2):
            _this = self.output
            s = Std.string((("null" if tabs is None else tabs) + "<![CDATA["))
            _this.b.write(s)
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string(value.nodeValue)
            _this.b.write(s)
            self.output.b.write("]]>")
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 3):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            commentContent = value.nodeValue
            commentContent = EReg("[\n\r\t]+","g").replace(commentContent,"")
            commentContent = (("<!--" + ("null" if commentContent is None else commentContent)) + "-->")
            _this = self.output
            s = Std.string(tabs)
            _this.b.write(s)
            input = StringTools.trim(commentContent)
            _this = self.output
            s = Std.string(input)
            _this.b.write(s)
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 4):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string((("<!DOCTYPE " + HxOverrides.stringOrNull(value.nodeValue)) + ">"))
            _this.b.write(s)
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 5):
            if ((value.nodeType == Xml.Document) or ((value.nodeType == Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _this = self.output
            s = Std.string((("<?" + HxOverrides.stringOrNull(value.nodeValue)) + "?>"))
            _this.b.write(s)
            if self.pretty:
                self.output.b.write("\n")
        elif (_g == 6):
            if ((value.nodeType != Xml.Document) and ((value.nodeType != Xml.Element))):
                raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
            _g_current = 0
            _g_array = value.children
            while (_g_current < len(_g_array)):
                child = _g_current
                _g_current = (_g_current + 1)
                child1 = (_g_array[child] if child >= 0 and child < len(_g_array) else None)
                self.writeNode(child1,tabs)
        else:
            pass

    def write(self,input):
        _this = self.output
        s = Std.string(input)
        _this.b.write(s)

    def newline(self):
        if self.pretty:
            self.output.b.write("\n")

    def hasChildren(self,value):
        if ((value.nodeType != Xml.Document) and ((value.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((value.nodeType is None)) else _Xml_XmlType_Impl_.toString(value.nodeType))))))
        _g_current = 0
        _g_array = value.children
        while (_g_current < len(_g_array)):
            child = _g_current
            _g_current = (_g_current + 1)
            child1 = (_g_array[child] if child >= 0 and child < len(_g_array) else None)
            _g = child1.nodeType
            if ((_g == 1) or ((_g == 0))):
                return True
            elif ((_g == 3) or ((_g == 2))):
                if ((child1.nodeType == Xml.Document) or ((child1.nodeType == Xml.Element))):
                    raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((child1.nodeType is None)) else _Xml_XmlType_Impl_.toString(child1.nodeType))))))
                if (len(StringTools.ltrim(child1.nodeValue)) != 0):
                    return True
            else:
                pass
        return False

    @staticmethod
    def print(xml,pretty = None):
        if (pretty is None):
            pretty = False
        printer = haxe_xml_Printer(pretty)
        printer.writeNode(xml,"")
        return printer.output.b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.output = None
        _hx_o.pretty = None
haxe_xml_Printer._hx_class = haxe_xml_Printer
globalClasses._hx_classes["haxe.xml.Printer"] = haxe_xml_Printer

class haxe_xml_XmlParserException:
    _hx_class_name = "haxe.xml.XmlParserException"
    __slots__ = ("message", "lineNumber", "positionAtLine", "position", "xml")
    _hx_fields = ["message", "lineNumber", "positionAtLine", "position", "xml"]
    _hx_methods = ["toString"]

    def __init__(self,message,xml,position):
        self.xml = xml
        self.message = message
        self.position = position
        self.lineNumber = 1
        self.positionAtLine = 0
        _g = 0
        _g1 = position
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = (-1 if ((i >= len(xml))) else ord(xml[i]))
            if (c == 10):
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.lineNumber
                _hx_local_0.lineNumber = (_hx_local_1 + 1)
                _hx_local_1
                self.positionAtLine = 0
            elif (c != 13):
                _hx_local_2 = self
                _hx_local_3 = _hx_local_2.positionAtLine
                _hx_local_2.positionAtLine = (_hx_local_3 + 1)
                _hx_local_3

    def toString(self):
        return ((((((HxOverrides.stringOrNull(Type.getClassName(Type.getClass(self))) + ": ") + HxOverrides.stringOrNull(self.message)) + " at line ") + Std.string(self.lineNumber)) + " char ") + Std.string(self.positionAtLine))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.message = None
        _hx_o.lineNumber = None
        _hx_o.positionAtLine = None
        _hx_o.position = None
        _hx_o.xml = None
haxe_xml_XmlParserException._hx_class = haxe_xml_XmlParserException
globalClasses._hx_classes["haxe.xml.XmlParserException"] = haxe_xml_XmlParserException


class haxe_xml__Access_Access_Impl_:
    _hx_class_name = "haxe.xml._Access.Access_Impl_"
    __slots__ = ()
    _hx_statics = ["get_x", "get_name", "get_node", "get_nodes", "get_att", "get_has", "get_hasNode", "get_elements", "_new", "get_innerData", "get_innerHTML"]
    x = None
    name = None
    innerData = None
    innerHTML = None
    node = None
    nodes = None
    att = None
    has = None
    hasNode = None
    elements = None

    @staticmethod
    def get_x(this1):
        return this1

    @staticmethod
    def get_name(this1):
        if (this1.nodeType == Xml.Document):
            return "Document"
        else:
            if (this1.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
            return this1.nodeName

    @staticmethod
    def get_node(this1):
        return this1

    @staticmethod
    def get_nodes(this1):
        return this1

    @staticmethod
    def get_att(this1):
        return this1

    @staticmethod
    def get_has(this1):
        return this1

    @staticmethod
    def get_hasNode(this1):
        return this1

    @staticmethod
    def get_elements(this1):
        return this1.elements()

    @staticmethod
    def _new(x):
        if ((x.nodeType != Xml.Document) and ((x.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
        this1 = x
        return this1

    @staticmethod
    def get_innerData(this1):
        if ((this1.nodeType != Xml.Document) and ((this1.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
        it_current = 0
        it_array = this1.children
        if (it_current >= len(it_array)):
            tmp = None
            if (this1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (this1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
                tmp = this1.nodeName
            raise haxe_Exception.thrown((("null" if tmp is None else tmp) + " does not have data"))
        v = it_current
        it_current = (it_current + 1)
        v1 = (it_array[v] if v >= 0 and v < len(it_array) else None)
        if (it_current < len(it_array)):
            n = it_current
            it_current = (it_current + 1)
            n1 = (it_array[n] if n >= 0 and n < len(it_array) else None)
            tmp = None
            if ((v1.nodeType == Xml.PCData) and ((n1.nodeType == Xml.CData))):
                if ((v1.nodeType == Xml.Document) or ((v1.nodeType == Xml.Element))):
                    raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((v1.nodeType is None)) else _Xml_XmlType_Impl_.toString(v1.nodeType))))))
                tmp = (StringTools.trim(v1.nodeValue) == "")
            else:
                tmp = False
            if tmp:
                if (it_current >= len(it_array)):
                    if ((n1.nodeType == Xml.Document) or ((n1.nodeType == Xml.Element))):
                        raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((n1.nodeType is None)) else _Xml_XmlType_Impl_.toString(n1.nodeType))))))
                    return n1.nodeValue
                n2 = it_current
                it_current = (it_current + 1)
                n21 = (it_array[n2] if n2 >= 0 and n2 < len(it_array) else None)
                tmp = None
                if (n21.nodeType == Xml.PCData):
                    if ((n21.nodeType == Xml.Document) or ((n21.nodeType == Xml.Element))):
                        raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((n21.nodeType is None)) else _Xml_XmlType_Impl_.toString(n21.nodeType))))))
                    tmp = (StringTools.trim(n21.nodeValue) == "")
                else:
                    tmp = False
                if (tmp and ((it_current >= len(it_array)))):
                    if ((n1.nodeType == Xml.Document) or ((n1.nodeType == Xml.Element))):
                        raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((n1.nodeType is None)) else _Xml_XmlType_Impl_.toString(n1.nodeType))))))
                    return n1.nodeValue
            tmp = None
            if (this1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (this1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
                tmp = this1.nodeName
            raise haxe_Exception.thrown((("null" if tmp is None else tmp) + " does not only have data"))
        if ((v1.nodeType != Xml.PCData) and ((v1.nodeType != Xml.CData))):
            tmp = None
            if (this1.nodeType == Xml.Document):
                tmp = "Document"
            else:
                if (this1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
                tmp = this1.nodeName
            raise haxe_Exception.thrown((("null" if tmp is None else tmp) + " does not have data"))
        if ((v1.nodeType == Xml.Document) or ((v1.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((v1.nodeType is None)) else _Xml_XmlType_Impl_.toString(v1.nodeType))))))
        return v1.nodeValue

    @staticmethod
    def get_innerHTML(this1):
        s_b = python_lib_io_StringIO()
        if ((this1.nodeType != Xml.Document) and ((this1.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
        _g_current = 0
        _g_array = this1.children
        while (_g_current < len(_g_array)):
            x = _g_current
            _g_current = (_g_current + 1)
            x1 = (_g_array[x] if x >= 0 and x < len(_g_array) else None)
            s_b.write(Std.string(haxe_xml_Printer.print(x1)))
        return s_b.getvalue()
haxe_xml__Access_Access_Impl_._hx_class = haxe_xml__Access_Access_Impl_
globalClasses._hx_classes["haxe.xml._Access.Access_Impl_"] = haxe_xml__Access_Access_Impl_


class haxe_xml__Access_AttribAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.AttribAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve", "_hx_set"]

    @staticmethod
    def resolve(this1,name):
        if (this1.nodeType == Xml.Document):
            raise haxe_Exception.thrown(("Cannot access document attribute " + ("null" if name is None else name)))
        v = this1.get(name)
        if (v is None):
            if (this1.nodeType != Xml.Element):
                raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
            raise haxe_Exception.thrown(((HxOverrides.stringOrNull(this1.nodeName) + " is missing attribute ") + ("null" if name is None else name)))
        return v

    @staticmethod
    def _hx_set(this1,name,value):
        if (this1.nodeType == Xml.Document):
            raise haxe_Exception.thrown(("Cannot access document attribute " + ("null" if name is None else name)))
        this1.set(name,value)
        return value
haxe_xml__Access_AttribAccess_Impl_._hx_class = haxe_xml__Access_AttribAccess_Impl_
globalClasses._hx_classes["haxe.xml._Access.AttribAccess_Impl_"] = haxe_xml__Access_AttribAccess_Impl_


class haxe_xml__Access_HasAttribAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.HasAttribAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve"]

    @staticmethod
    def resolve(this1,name):
        if (this1.nodeType == Xml.Document):
            raise haxe_Exception.thrown(("Cannot access document attribute " + ("null" if name is None else name)))
        return this1.exists(name)
haxe_xml__Access_HasAttribAccess_Impl_._hx_class = haxe_xml__Access_HasAttribAccess_Impl_
globalClasses._hx_classes["haxe.xml._Access.HasAttribAccess_Impl_"] = haxe_xml__Access_HasAttribAccess_Impl_


class haxe_xml__Access_HasNodeAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.HasNodeAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve"]

    @staticmethod
    def resolve(this1,name):
        return this1.elementsNamed(name).hasNext()
haxe_xml__Access_HasNodeAccess_Impl_._hx_class = haxe_xml__Access_HasNodeAccess_Impl_
globalClasses._hx_classes["haxe.xml._Access.HasNodeAccess_Impl_"] = haxe_xml__Access_HasNodeAccess_Impl_


class haxe_xml__Access_NodeAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.NodeAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve"]

    @staticmethod
    def resolve(this1,name):
        x = this1.elementsNamed(name).next()
        if (x is None):
            xname = None
            if (this1.nodeType == Xml.Document):
                xname = "Document"
            else:
                if (this1.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((this1.nodeType is None)) else _Xml_XmlType_Impl_.toString(this1.nodeType))))))
                xname = this1.nodeName
            raise haxe_Exception.thrown(((("null" if xname is None else xname) + " is missing element ") + ("null" if name is None else name)))
        if ((x.nodeType != Xml.Document) and ((x.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x.nodeType is None)) else _Xml_XmlType_Impl_.toString(x.nodeType))))))
        this1 = x
        return this1
haxe_xml__Access_NodeAccess_Impl_._hx_class = haxe_xml__Access_NodeAccess_Impl_
globalClasses._hx_classes["haxe.xml._Access.NodeAccess_Impl_"] = haxe_xml__Access_NodeAccess_Impl_


class haxe_xml__Access_NodeListAccess_Impl_:
    _hx_class_name = "haxe.xml._Access.NodeListAccess_Impl_"
    __slots__ = ()
    _hx_statics = ["resolve"]

    @staticmethod
    def resolve(this1,name):
        l = []
        x = this1.elementsNamed(name)
        while x.hasNext():
            x1 = x.next()
            if ((x1.nodeType != Xml.Document) and ((x1.nodeType != Xml.Element))):
                raise haxe_Exception.thrown(("Invalid nodeType " + HxOverrides.stringOrNull((("null" if ((x1.nodeType is None)) else _Xml_XmlType_Impl_.toString(x1.nodeType))))))
            this1 = x1
            l.append(this1)
        return l
haxe_xml__Access_NodeListAccess_Impl_._hx_class = haxe_xml__Access_NodeListAccess_Impl_
globalClasses._hx_classes["haxe.xml._Access.NodeListAccess_Impl_"] = haxe_xml__Access_NodeListAccess_Impl_


anon.classesinmodule(sys.modules[__name__])
