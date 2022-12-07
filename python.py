import sys
import _hx_AnonObject as anon
from _hx_AnonObject import _hx_AnonObject

import globalClasses
from classes_hscript import Enum, HxOverrides, HxString, Std 
import math as Math
import inspect as python_lib_Inspect
import sys as python_lib_Sys

import math as Math
import functools as python_lib_Functools

from haxe import haxe_io_Input, haxe_io_Output


class python_Boot:
    _hx_class_name = "python.Boot"
    __slots__ = ()
    _hx_statics = ["keywords", "arrayJoin", "safeJoin", "isPyBool", "isPyInt", "isPyFloat", "isClass", "isAnonObject", "_add_dynamic", "toString", "toString1", "isMetaType", "fields", "isString", "isArray", "simpleField", "createClosure", "hasField", "field", "getInstanceFields", "getSuperClass", "getClassFields", "unsafeFastCodeAt", "handleKeywords", "prefixLength", "unhandleKeywords", "implementsInterface"]
    
    @staticmethod
    def arrayJoin(x,sep):
        return sep.join([python_Boot.toString1(x1,'') for x1 in x])

    @staticmethod
    def safeJoin(x,sep):
        return sep.join([x1 for x1 in x])

    @staticmethod
    def isPyBool(o):
        return isinstance(o,bool)

    @staticmethod
    def isPyInt(o):
        if isinstance(o,int):
            return (not isinstance(o,bool))
        else:
            return False

    @staticmethod
    def isPyFloat(o):
        return isinstance(o,float)

    @staticmethod
    def isClass(o):
        if (o is not None):
            if not HxOverrides.eq(o,str):
                return python_lib_Inspect.isclass(o)
            else:
                return True
        else:
            return False

    @staticmethod
    def isAnonObject(o):
        return isinstance(o,_hx_AnonObject)

    @staticmethod
    def _add_dynamic(a,b):
        if (isinstance(a,str) and isinstance(b,str)):
            return (a + b)
        if (isinstance(a,str) or isinstance(b,str)):
            return (python_Boot.toString1(a,"") + python_Boot.toString1(b,""))
        return (a + b)

    @staticmethod
    def toString(o):
        return python_Boot.toString1(o,"")

    @staticmethod
    def toString1(o,s):
        if (o is None):
            return "null"
        if isinstance(o,str):
            return o
        if (s is None):
            s = ""
        if (len(s) >= 5):
            return "<...>"
        if isinstance(o,bool):
            if o:
                return "true"
            else:
                return "false"
        if (isinstance(o,int) and (not isinstance(o,bool))):
            return str(o)
        if isinstance(o,float):
            try:
                if (o == int(o)):
                    return str(Math.floor((o + 0.5)))
                else:
                    return str(o)
            except BaseException as _g:
                None
                return str(o)
        if isinstance(o,list):
            o1 = o
            l = len(o1)
            st = "["
            s = (("null" if s is None else s) + "\t")
            _g = 0
            _g1 = l
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                prefix = ""
                if (i > 0):
                    prefix = ","
                st = (("null" if st is None else st) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1((o1[i] if i >= 0 and i < len(o1) else None),s))))))
            st = (("null" if st is None else st) + "]")
            return st
        try:
            if hasattr(o,"toString"):
                return o.toString()
        except BaseException as _g:
            None
        if hasattr(o,"__class__"):
            if isinstance(o,_hx_AnonObject):
                toStr = None
                try:
                    fields = python_Boot.fields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (("{ " + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " }")
                except BaseException as _g:
                    None
                    return "{ ... }"
                if (toStr is None):
                    return "{ ... }"
                else:
                    return toStr
            if isinstance(o,Enum):
                o1 = o
                l = len(o1.params)
                hasParams = (l > 0)
                if hasParams:
                    paramsStr = ""
                    _g = 0
                    _g1 = l
                    while (_g < _g1):
                        i = _g
                        _g = (_g + 1)
                        prefix = ""
                        if (i > 0):
                            prefix = ","
                        paramsStr = (("null" if paramsStr is None else paramsStr) + HxOverrides.stringOrNull(((("null" if prefix is None else prefix) + HxOverrides.stringOrNull(python_Boot.toString1(o1.params[i],s))))))
                    return (((HxOverrides.stringOrNull(o1.tag) + "(") + ("null" if paramsStr is None else paramsStr)) + ")")
                else:
                    return o1.tag
            if hasattr(o,"_hx_class_name"):
                if (o.__class__.__name__ != "type"):
                    fields = python_Boot.getInstanceFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((HxOverrides.stringOrNull(o._hx_class_name) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
                else:
                    fields = python_Boot.getClassFields(o)
                    _g = []
                    _g1 = 0
                    while (_g1 < len(fields)):
                        f = (fields[_g1] if _g1 >= 0 and _g1 < len(fields) else None)
                        _g1 = (_g1 + 1)
                        x = ((("" + ("null" if f is None else f)) + " : ") + HxOverrides.stringOrNull(python_Boot.toString1(python_Boot.simpleField(o,f),(("null" if s is None else s) + "\t"))))
                        _g.append(x)
                    fieldsStr = _g
                    toStr = (((("#" + HxOverrides.stringOrNull(o._hx_class_name)) + "( ") + HxOverrides.stringOrNull(", ".join([x1 for x1 in fieldsStr]))) + " )")
                    return toStr
            if ((type(o) == type) and (o == str)):
                return "#String"
            if ((type(o) == type) and (o == list)):
                return "#Array"
            if callable(o):
                return "function"
            try:
                if hasattr(o,"__repr__"):
                    return o.__repr__()
            except BaseException as _g:
                None
            if hasattr(o,"__str__"):
                return o.__str__([])
            if hasattr(o,"__name__"):
                return o.__name__
            return "???"
        else:
            return str(o)

    @staticmethod
    def isMetaType(v,t):
        return ((type(v) == type) and (v == t))

    @staticmethod
    def fields(o):
        a = []
        if (o is not None):
            if hasattr(o,"_hx_fields"):
                fields = o._hx_fields
                if (fields is not None):
                    return list(fields)
            if isinstance(o,_hx_AnonObject):
                d = o.__dict__
                keys = d.keys()
                handler = python_Boot.unhandleKeywords
                for k in keys:
                    if (k != '_hx_disable_getattr'):
                        a.append(handler(k))
            elif hasattr(o,"__dict__"):
                d = o.__dict__
                keys1 = d.keys()
                for k in keys1:
                    a.append(k)
        return a

    @staticmethod
    def isString(o):
        return isinstance(o,str)

    @staticmethod
    def isArray(o):
        return isinstance(o,list)

    @staticmethod
    def simpleField(o,field):
        if (field is None):
            return None
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        if hasattr(o,field1):
            return getattr(o,field1)
        else:
            return None

    @staticmethod
    def createClosure(obj,func):
        return python_internal_MethodClosure(obj,func)

    @staticmethod
    def hasField(o,field):
        if isinstance(o,_hx_AnonObject):
            return o._hx_hasattr(field)
        return hasattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)))

    @staticmethod
    def field(o,field):
        if (field is None):
            return None
        if isinstance(o,str):
            field1 = field
            _hx_local_0 = len(field1)
            if (_hx_local_0 == 10):
                if (field1 == "charCodeAt"):
                    return python_internal_MethodClosure(o,HxString.charCodeAt)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 11):
                if (field1 == "lastIndexOf"):
                    return python_internal_MethodClosure(o,HxString.lastIndexOf)
                elif (field1 == "toLowerCase"):
                    return python_internal_MethodClosure(o,HxString.toLowerCase)
                elif (field1 == "toUpperCase"):
                    return python_internal_MethodClosure(o,HxString.toUpperCase)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 9):
                if (field1 == "substring"):
                    return python_internal_MethodClosure(o,HxString.substring)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 5):
                if (field1 == "split"):
                    return python_internal_MethodClosure(o,HxString.split)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 7):
                if (field1 == "indexOf"):
                    return python_internal_MethodClosure(o,HxString.indexOf)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 8):
                if (field1 == "toString"):
                    return python_internal_MethodClosure(o,HxString.toString)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_0 == 6):
                if (field1 == "charAt"):
                    return python_internal_MethodClosure(o,HxString.charAt)
                elif (field1 == "length"):
                    return len(o)
                elif (field1 == "substr"):
                    return python_internal_MethodClosure(o,HxString.substr)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            else:
                field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                if hasattr(o,field1):
                    return getattr(o,field1)
                else:
                    return None
        elif isinstance(o,list):
            field1 = field
            _hx_local_1 = len(field1)
            if (_hx_local_1 == 11):
                if (field1 == "lastIndexOf"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.lastIndexOf)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 4):
                if (field1 == "copy"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.copy)
                elif (field1 == "join"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.join)
                elif (field1 == "push"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.push)
                elif (field1 == "sort"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.sort)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 5):
                if (field1 == "shift"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.shift)
                elif (field1 == "slice"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.slice)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 7):
                if (field1 == "indexOf"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.indexOf)
                elif (field1 == "reverse"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.reverse)
                elif (field1 == "unshift"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.unshift)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 3):
                if (field1 == "map"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.map)
                elif (field1 == "pop"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.pop)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 8):
                if (field1 == "contains"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.contains)
                elif (field1 == "iterator"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.iterator)
                elif (field1 == "toString"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.toString)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 16):
                if (field1 == "keyValueIterator"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.keyValueIterator)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            elif (_hx_local_1 == 6):
                if (field1 == "concat"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.concat)
                elif (field1 == "filter"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.filter)
                elif (field1 == "insert"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.insert)
                elif (field1 == "length"):
                    return len(o)
                elif (field1 == "remove"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.remove)
                elif (field1 == "splice"):
                    return python_internal_MethodClosure(o,python_internal_ArrayImpl.splice)
                else:
                    field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                    if hasattr(o,field1):
                        return getattr(o,field1)
                    else:
                        return None
            else:
                field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
                if hasattr(o,field1):
                    return getattr(o,field1)
                else:
                    return None
        else:
            field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
            if hasattr(o,field1):
                return getattr(o,field1)
            else:
                return None

    @staticmethod
    def getInstanceFields(c):
        f = (list(c._hx_fields) if (hasattr(c,"_hx_fields")) else [])
        if hasattr(c,"_hx_methods"):
            f = (f + c._hx_methods)
        sc = python_Boot.getSuperClass(c)
        if (sc is None):
            return f
        else:
            scArr = python_Boot.getInstanceFields(sc)
            scMap = set(scArr)
            _g = 0
            while (_g < len(f)):
                f1 = (f[_g] if _g >= 0 and _g < len(f) else None)
                _g = (_g + 1)
                if (not (f1 in scMap)):
                    scArr.append(f1)
            return scArr

    @staticmethod
    def getSuperClass(c):
        if (c is None):
            return None
        try:
            if hasattr(c,"_hx_super"):
                return c._hx_super
            return None
        except BaseException as _g:
            None
        return None

    @staticmethod
    def getClassFields(c):
        if hasattr(c,"_hx_statics"):
            x = c._hx_statics
            return list(x)
        else:
            return []

    @staticmethod
    def unsafeFastCodeAt(s,index):
        return ord(s[index])

    @staticmethod
    def handleKeywords(name):
        if (name in python_Boot.keywords):
            return ("_hx_" + name)
        elif ((((len(name) > 2) and ((ord(name[0]) == 95))) and ((ord(name[1]) == 95))) and ((ord(name[(len(name) - 1)]) != 95))):
            return ("_hx_" + name)
        else:
            return name

    @staticmethod
    def unhandleKeywords(name):
        if (HxString.substr(name,0,python_Boot.prefixLength) == "_hx_"):
            real = HxString.substr(name,python_Boot.prefixLength,None)
            if (real in python_Boot.keywords):
                return real
        return name

    @staticmethod
    def implementsInterface(value,cls):
        loop = None
        def _hx_local_1(intf):
            f = (intf._hx_interfaces if (hasattr(intf,"_hx_interfaces")) else [])
            if (f is not None):
                _g = 0
                while (_g < len(f)):
                    i = (f[_g] if _g >= 0 and _g < len(f) else None)
                    _g = (_g + 1)
                    if (i == cls):
                        return True
                    else:
                        l = loop(i)
                        if l:
                            return True
                return False
            else:
                return False
        loop = _hx_local_1
        currentClass = value.__class__
        result = False
        while (currentClass is not None):
            if loop(currentClass):
                result = True
                break
            currentClass = python_Boot.getSuperClass(currentClass)
        return result
python_Boot._hx_class = python_Boot
globalClasses._hx_classes["python.Boot"] = python_Boot


class python_HaxeIterable:
    _hx_class_name = "python.HaxeIterable"
    __slots__ = ("x",)
    _hx_fields = ["x"]
    _hx_methods = ["iterator"]

    def __init__(self,x):
        self.x = x

    def iterator(self):
        return python_HaxeIterator(self.x.__iter__())

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.x = None
python_HaxeIterable._hx_class = python_HaxeIterable
globalClasses._hx_classes["python.HaxeIterable"] = python_HaxeIterable


class python_HaxeIterator:
    _hx_class_name = "python.HaxeIterator"
    __slots__ = ("it", "x", "has", "checked")
    _hx_fields = ["it", "x", "has", "checked"]
    _hx_methods = ["next", "hasNext"]

    def __init__(self,it):
        self.checked = False
        self.has = False
        self.x = None
        self.it = it

    def next(self):
        if (not self.checked):
            self.hasNext()
        self.checked = False
        return self.x

    def hasNext(self):
        from haxe import haxe_Exception
        if (not self.checked):
            try:
                self.x = self.it.__next__()
                self.has = True
            except BaseException as _g:
                None
                if Std.isOfType(haxe_Exception.caught(_g).unwrap(),StopIteration):
                    self.has = False
                    self.x = None
                else:
                    raise _g
            self.checked = True
        return self.has

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.it = None
        _hx_o.x = None
        _hx_o.has = None
        _hx_o.checked = None
python_HaxeIterator._hx_class = python_HaxeIterator
globalClasses._hx_classes["python.HaxeIterator"] = python_HaxeIterator


class python_Lib:
    _hx_class_name = "python.Lib"
    __slots__ = ()
    _hx_statics = ["lineEnd", "get___name__", "print", "printString", "println", "dictToAnon", "anonToDict", "anonAsDict", "dictAsAnon", "toPythonIterable", "toHaxeIterable", "toHaxeIterator"]
    __name__ = None

    @staticmethod
    def get___name__():
        return __name__

    @staticmethod
    def print(v):
        python_Lib.printString(Std.string(v))

    @staticmethod
    def printString(_hx_str):
        encoding = "utf-8"
        if (encoding is None):
            encoding = "utf-8"
        python_lib_Sys.stdout.buffer.write(_hx_str.encode(encoding, "strict"))
        python_lib_Sys.stdout.flush()

    @staticmethod
    def println(v):
        _hx_str = Std.string(v)
        python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))

    @staticmethod
    def dictToAnon(v):
        return _hx_AnonObject(v.copy())

    @staticmethod
    def anonToDict(o):
        if isinstance(o,_hx_AnonObject):
            return o.__dict__.copy()
        else:
            return None

    @staticmethod
    def anonAsDict(o):
        if isinstance(o,_hx_AnonObject):
            return o.__dict__
        else:
            return None

    @staticmethod
    def dictAsAnon(d):
        return _hx_AnonObject(d)

    @staticmethod
    def toPythonIterable(it):
        def _hx_local_3():
            def _hx_local_2():
                from haxe import haxe_Exception
                it1 = HxOverrides.iterator(it)
                _hx_self = None
                def _hx_local_0():
                    if it1.hasNext():
                        return it1.next()
                    else:
                        raise haxe_Exception.thrown(StopIteration())
                def _hx_local_1():
                    return _hx_self
                this1 = _hx_AnonObject({'__next__': _hx_local_0, '__iter__': _hx_local_1})
                _hx_self = this1
                return _hx_self
            return _hx_AnonObject({'__iter__': _hx_local_2})
        return _hx_local_3()

    @staticmethod
    def toHaxeIterable(it):
        return python_HaxeIterable(it)

    @staticmethod
    def toHaxeIterator(it):
        return python_HaxeIterator(it)
python_Lib._hx_class = python_Lib
globalClasses._hx_classes["python.Lib"] = python_Lib


class python_NativeStringTools:
    _hx_class_name = "python.NativeStringTools"
    __slots__ = ()
    _hx_statics = ["format", "encode", "contains", "strip", "rpartition", "startswith", "endswith"]

    @staticmethod
    def format(s,args):
        return s.format(*args)

    @staticmethod
    def encode(s,encoding = None,errors = None):
        if (encoding is None):
            encoding = "utf-8"
        if (errors is None):
            errors = "strict"
        return s.encode(encoding, errors)

    @staticmethod
    def contains(s,e):
        return (e in s)

    @staticmethod
    def strip(s,chars = None):
        return s.strip(chars)

    @staticmethod
    def rpartition(s,sep):
        return s.rpartition(sep)

    @staticmethod
    def startswith(s,prefix):
        return s.startswith(prefix)

    @staticmethod
    def endswith(s,suffix):
        return s.endswith(suffix)
python_NativeStringTools._hx_class = python_NativeStringTools
globalClasses._hx_classes["python.NativeStringTools"] = python_NativeStringTools


class python__KwArgs_KwArgs_Impl_:
    _hx_class_name = "python._KwArgs.KwArgs_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "toDict", "toDictHelper", "fromDict", "fromT", "typed", "get"]

    @staticmethod
    def _new(d):
        this1 = d
        return this1

    @staticmethod
    def toDict(this1):
        return python__KwArgs_KwArgs_Impl_.toDictHelper(this1,None)

    @staticmethod
    def toDictHelper(this1,x):
        return this1

    @staticmethod
    def fromDict(d):
        this1 = d
        return this1

    @staticmethod
    def fromT(d):
        this1 = python_Lib.anonAsDict(d)
        return this1

    @staticmethod
    def typed(this1):
        return _hx_AnonObject(python__KwArgs_KwArgs_Impl_.toDictHelper(this1,None))

    @staticmethod
    def get(this1,key,_hx_def):
        return this1.get(key,_hx_def)
python__KwArgs_KwArgs_Impl_._hx_class = python__KwArgs_KwArgs_Impl_
globalClasses._hx_classes["python._KwArgs.KwArgs_Impl_"] = python__KwArgs_KwArgs_Impl_


class python__NativeIterable_NativeIterable_Impl_:
    _hx_class_name = "python._NativeIterable.NativeIterable_Impl_"
    __slots__ = ()
    _hx_statics = ["toHaxeIterable", "iterator"]

    @staticmethod
    def toHaxeIterable(this1):
        return python_HaxeIterable(this1)

    @staticmethod
    def iterator(this1):
        return python_HaxeIterator(this1.__iter__())
python__NativeIterable_NativeIterable_Impl_._hx_class = python__NativeIterable_NativeIterable_Impl_
globalClasses._hx_classes["python._NativeIterable.NativeIterable_Impl_"] = python__NativeIterable_NativeIterable_Impl_


class python__NativeIterator_NativeIterator_Impl_:
    _hx_class_name = "python._NativeIterator.NativeIterator_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "toHaxeIterator"]

    @staticmethod
    def _new(p):
        this1 = p
        return this1

    @staticmethod
    def toHaxeIterator(this1):
        return python_HaxeIterator(this1)
python__NativeIterator_NativeIterator_Impl_._hx_class = python__NativeIterator_NativeIterator_Impl_
globalClasses._hx_classes["python._NativeIterator.NativeIterator_Impl_"] = python__NativeIterator_NativeIterator_Impl_


class python__VarArgs_VarArgs_Impl_:
    _hx_class_name = "python._VarArgs.VarArgs_Impl_"
    __slots__ = ()
    _hx_statics = ["_new", "raw", "toArray", "fromArray"]

    @staticmethod
    def _new(d):
        this1 = d
        return this1

    @staticmethod
    def raw(this1):
        return this1

    @staticmethod
    def toArray(this1):
        if (not Std.isOfType(this1,list)):
            return list(this1)
        else:
            return this1

    @staticmethod
    def fromArray(d):
        this1 = d
        return this1
python__VarArgs_VarArgs_Impl_._hx_class = python__VarArgs_VarArgs_Impl_
globalClasses._hx_classes["python._VarArgs.VarArgs_Impl_"] = python__VarArgs_VarArgs_Impl_


class python_internal_ArrayImpl:
    _hx_class_name = "python.internal.ArrayImpl"
    __slots__ = ()
    _hx_statics = ["get_length", "concat", "copy", "iterator", "keyValueIterator", "indexOf", "lastIndexOf", "join", "toString", "pop", "push", "unshift", "remove", "contains", "shift", "slice", "sort", "splice", "map", "filter", "insert", "reverse", "_get", "_set", "unsafeGet", "unsafeSet", "resize"]

    @staticmethod
    def get_length(x):
        return len(x)

    @staticmethod
    def concat(a1,a2):
        return (a1 + a2)

    @staticmethod
    def copy(x):
        return list(x)

    @staticmethod
    def iterator(x):
        return python_HaxeIterator(x.__iter__())

    @staticmethod
    def keyValueIterator(x):
        from haxe import haxe_iterators_ArrayKeyValueIterator
        return haxe_iterators_ArrayKeyValueIterator(x)

    @staticmethod
    def indexOf(a,x,fromIndex = None):
        _hx_len = len(a)
        l = (0 if ((fromIndex is None)) else ((_hx_len + fromIndex) if ((fromIndex < 0)) else fromIndex))
        if (l < 0):
            l = 0
        _g = l
        _g1 = _hx_len
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            if HxOverrides.eq(a[i],x):
                return i
        return -1

    @staticmethod
    def lastIndexOf(a,x,fromIndex = None):
        _hx_len = len(a)
        l = (_hx_len if ((fromIndex is None)) else (((_hx_len + fromIndex) + 1) if ((fromIndex < 0)) else (fromIndex + 1)))
        if (l > _hx_len):
            l = _hx_len
        while True:
            l = (l - 1)
            tmp = l
            if (not ((tmp > -1))):
                break
            if HxOverrides.eq(a[l],x):
                return l
        return -1

    @staticmethod
    def join(x,sep):
        return sep.join([python_Boot.toString1(x1,'') for x1 in x])

    @staticmethod
    def toString(x):
        return (("[" + HxOverrides.stringOrNull(",".join([python_Boot.toString1(x1,'') for x1 in x]))) + "]")

    @staticmethod
    def pop(x):
        if (len(x) == 0):
            return None
        else:
            return x.pop()

    @staticmethod
    def push(x,e):
        x.append(e)
        return len(x)

    @staticmethod
    def unshift(x,e):
        x.insert(0, e)

    @staticmethod
    def remove(x,e):
        try:
            x.remove(e)
            return True
        except BaseException as _g:
            None
            return False

    @staticmethod
    def contains(x,e):
        return (e in x)

    @staticmethod
    def shift(x):
        if (len(x) == 0):
            return None
        return x.pop(0)

    @staticmethod
    def slice(x,pos,end = None):
        return x[pos:end]

    @staticmethod
    def sort(x,f):
        x.sort(key= python_lib_Functools.cmp_to_key(f))

    @staticmethod
    def splice(x,pos,_hx_len):
        if (pos < 0):
            pos = (len(x) + pos)
        if (pos < 0):
            pos = 0
        res = x[pos:(pos + _hx_len)]
        del x[pos:(pos + _hx_len)]
        return res

    @staticmethod
    def map(x,f):
        return list(map(f,x))

    @staticmethod
    def filter(x,f):
        return list(filter(f,x))

    @staticmethod
    def insert(a,pos,x):
        a.insert(pos, x)

    @staticmethod
    def reverse(a):
        a.reverse()

    @staticmethod
    def _get(x,idx):
        if ((idx > -1) and ((idx < len(x)))):
            return x[idx]
        else:
            return None

    @staticmethod
    def _set(x,idx,v):
        l = len(x)
        while (l < idx):
            x.append(None)
            l = (l + 1)
        if (l == idx):
            x.append(v)
        else:
            x[idx] = v
        return v

    @staticmethod
    def unsafeGet(x,idx):
        return x[idx]

    @staticmethod
    def unsafeSet(x,idx,val):
        x[idx] = val
        return val

    @staticmethod
    def resize(x,_hx_len):
        l = len(x)
        if (l < _hx_len):
            idx = (_hx_len - 1)
            v = None
            l1 = len(x)
            while (l1 < idx):
                x.append(None)
                l1 = (l1 + 1)
            if (l1 == idx):
                x.append(v)
            else:
                x[idx] = v
        elif (l > _hx_len):
            pos = _hx_len
            len1 = (l - _hx_len)
            if (pos < 0):
                pos = (len(x) + pos)
            if (pos < 0):
                pos = 0
            res = x[pos:(pos + len1)]
            del x[pos:(pos + len1)]
python_internal_ArrayImpl._hx_class = python_internal_ArrayImpl
globalClasses._hx_classes["python.internal.ArrayImpl"] = python_internal_ArrayImpl


class python_internal_Internal:
    _hx_class_name = "python.internal.Internal"
    __slots__ = ()
python_internal_Internal._hx_class = python_internal_Internal
globalClasses._hx_classes["python.internal.Internal"] = python_internal_Internal


class python_internal_MethodClosure:
    _hx_class_name = "python.internal.MethodClosure"
    __slots__ = ("obj", "func")
    _hx_fields = ["obj", "func"]
    _hx_methods = ["__call__"]

    def __init__(self,obj,func):
        self.obj = obj
        self.func = func

    def __call__(self,*args):
        return self.func(self.obj,*args)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.obj = None
        _hx_o.func = None
python_internal_MethodClosure._hx_class = python_internal_MethodClosure
globalClasses._hx_classes["python.internal.MethodClosure"] = python_internal_MethodClosure





class python_io_IInput:
    _hx_class_name = "python.io.IInput"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["set_bigEndian", "readByte", "readBytes", "close", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString"]
python_io_IInput._hx_class = python_io_IInput
globalClasses._hx_classes["python.io.IInput"] = python_io_IInput


class python_io_IOutput:
    _hx_class_name = "python.io.IOutput"
    __slots__ = ("bigEndian",)
    _hx_fields = ["bigEndian"]
    _hx_methods = ["set_bigEndian", "writeByte", "writeBytes", "flush", "close", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]
python_io_IOutput._hx_class = python_io_IOutput
globalClasses._hx_classes["python.io.IOutput"] = python_io_IOutput

class python_io_IFileInput:
    _hx_class_name = "python.io.IFileInput"
    __slots__ = ()
    _hx_methods = ["seek", "tell", "eof"]
    _hx_interfaces = [python_io_IInput]
python_io_IFileInput._hx_class = python_io_IFileInput
globalClasses._hx_classes["python.io.IFileInput"] = python_io_IFileInput

class python_io_IFileOutput:
    _hx_class_name = "python.io.IFileOutput"
    __slots__ = ()
    _hx_methods = ["seek", "tell"]
    _hx_interfaces = [python_io_IOutput]
python_io_IFileOutput._hx_class = python_io_IFileOutput
globalClasses._hx_classes["python.io.IFileOutput"] = python_io_IFileOutput


class python_io_IoTools:
    _hx_class_name = "python.io.IoTools"
    __slots__ = ()
    _hx_statics = ["createFileInputFromText", "createFileInputFromBytes", "createFileOutputFromText", "createFileOutputFromBytes", "seekInTextMode", "seekInBinaryMode"]

    @staticmethod
    def createFileInputFromText(t):
        from sys_hscript import sys_io_FileInput
        return sys_io_FileInput(python_io_FileTextInput(t))

    @staticmethod
    def createFileInputFromBytes(t):
        from sys_hscript import sys_io_FileInput
        return sys_io_FileInput(python_io_FileBytesInput(t))

    @staticmethod
    def createFileOutputFromText(t):
        from sys_hscript import sys_io_FileOutput
        return sys_io_FileOutput(python_io_FileTextOutput(t))

    @staticmethod
    def createFileOutputFromBytes(t):
        from sys_hscript import sys_io_FileOutput
        return sys_io_FileOutput(python_io_FileBytesOutput(t))

    @staticmethod
    def seekInTextMode(stream,tell,p,pos):
        pos1 = None
        pos2 = pos.index
        if (pos2 == 0):
            pos1 = 0
        elif (pos2 == 1):
            p = (tell() + p)
            pos1 = 0
        elif (pos2 == 2):
            stream.seek(0,2)
            p = (tell() + p)
            pos1 = 0
        else:
            pass
        stream.seek(p,pos1)

    @staticmethod
    def seekInBinaryMode(stream,p,pos):
        pos1 = None
        pos2 = pos.index
        if (pos2 == 0):
            pos1 = 0
        elif (pos2 == 1):
            pos1 = 1
        elif (pos2 == 2):
            pos1 = 2
        else:
            pass
        stream.seek(p,pos1)
python_io_IoTools._hx_class = python_io_IoTools
globalClasses._hx_classes["python.io.IoTools"] = python_io_IoTools

class python_io_NativeInput(haxe_io_Input):
    _hx_class_name = "python.io.NativeInput"
    __slots__ = ("stream", "wasEof")
    _hx_fields = ["stream", "wasEof"]
    _hx_methods = ["get_canSeek", "close", "tell", "throwEof", "eof", "readinto", "seek", "readBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,s):
        from haxe import haxe_Exception
        self.wasEof = None
        self.stream = s
        self.set_bigEndian(False)
        self.wasEof = False
        if (not self.stream.readable()):
            raise haxe_Exception.thrown("Write-only stream")

    def get_canSeek(self):
        return self.stream.seekable()

    def close(self):
        self.stream.close()

    def tell(self):
        return self.stream.tell()

    def throwEof(self):
        from haxe import haxe_Exception, haxe_io_Eof
        self.wasEof = True
        raise haxe_Exception.thrown(haxe_io_Eof())

    def eof(self):
        return self.wasEof

    def readinto(self,b):
        from haxe import haxe_Exception
        raise haxe_Exception.thrown("abstract method, should be overridden")

    def seek(self,p,mode):
        from haxe import haxe_Exception
        raise haxe_Exception.thrown("abstract method, should be overridden")

    def readBytes(self,s,pos,_hx_len):
        from haxe import haxe_Exception, haxe_io_Error
        if (((pos < 0) or ((_hx_len < 0))) or (((pos + _hx_len) > s.length))):
            raise haxe_Exception.thrown(haxe_io_Error.OutsideBounds)
        ba = bytearray(_hx_len)
        ret = self.readinto(ba)
        if (ret == 0):
            self.throwEof()
        s.blit(pos,haxe_io_Bytes.ofData(ba),0,_hx_len)
        return ret

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.stream = None
        _hx_o.wasEof = None
python_io_NativeInput._hx_class = python_io_NativeInput
globalClasses._hx_classes["python.io.NativeInput"] = python_io_NativeInput


class python_io_NativeBytesInput(python_io_NativeInput):
    _hx_class_name = "python.io.NativeBytesInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["readByte", "seek", "readinto"]
    _hx_statics = []
    _hx_interfaces = [python_io_IInput]
    _hx_super = python_io_NativeInput


    def __init__(self,stream):
        super().__init__(stream)

    def readByte(self):
        ret = self.stream.read(1)
        if (len(ret) == 0):
            self.throwEof()
        return ret[0]

    def seek(self,p,pos):
        self.wasEof = False
        python_io_IoTools.seekInBinaryMode(self.stream,p,pos)

    def readinto(self,b):
        return self.stream.readinto(b)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeBytesInput._hx_class = python_io_NativeBytesInput
globalClasses._hx_classes["python.io.NativeBytesInput"] = python_io_NativeBytesInput

class python_io_FileBytesInput(python_io_NativeBytesInput):
    _hx_class_name = "python.io.FileBytesInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileInput]
    _hx_super = python_io_NativeBytesInput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileBytesInput._hx_class = python_io_FileBytesInput
globalClasses._hx_classes["python.io.FileBytesInput"] = python_io_FileBytesInput


class python_io_NativeOutput(haxe_io_Output):
    _hx_class_name = "python.io.NativeOutput"
    __slots__ = ("stream",)
    _hx_fields = ["stream"]
    _hx_methods = ["get_canSeek", "close", "prepare", "flush", "tell"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,stream):
        from haxe import haxe_Exception
        self.stream = None
        self.set_bigEndian(False)
        self.stream = stream
        if (not stream.writable()):
            raise haxe_Exception.thrown("Read only stream")

    def get_canSeek(self):
        return self.stream.seekable()

    def close(self):
        self.stream.close()

    def prepare(self,nbytes):
        self.stream.truncate(nbytes)

    def flush(self):
        self.stream.flush()

    def tell(self):
        return self.stream.tell()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.stream = None
python_io_NativeOutput._hx_class = python_io_NativeOutput
globalClasses._hx_classes["python.io.NativeOutput"] = python_io_NativeOutput

class python_io_NativeTextOutput(python_io_NativeOutput):
    _hx_class_name = "python.io.NativeTextOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["seek", "writeBytes", "writeByte"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = python_io_NativeOutput


    def __init__(self,stream):
        from haxe import haxe_Exception
        super().__init__(stream)
        if (not stream.writable()):
            raise haxe_Exception.thrown("Read only stream")

    def seek(self,p,pos):
        python_io_IoTools.seekInTextMode(self.stream,self.tell,p,pos)

    def writeBytes(self,s,pos,_hx_len):
        return self.stream.buffer.write(s.b[pos:(pos + _hx_len)])

    def writeByte(self,c):
        self.stream.write("".join(map(chr,[c])))

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeTextOutput._hx_class = python_io_NativeTextOutput
globalClasses._hx_classes["python.io.NativeTextOutput"] = python_io_NativeTextOutput

class python_io_NativeBytesOutput(python_io_NativeOutput):
    _hx_class_name = "python.io.NativeBytesOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["seek", "prepare", "writeByte", "writeBytes"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = python_io_NativeOutput


    def __init__(self,stream):
        super().__init__(stream)

    def seek(self,p,pos):
        python_io_IoTools.seekInBinaryMode(self.stream,p,pos)

    def prepare(self,nbytes):
        self.stream.truncate(nbytes)

    def writeByte(self,c):
        self.stream.write(bytearray([c]))

    def writeBytes(self,s,pos,_hx_len):
        return self.stream.write(s.b[pos:(pos + _hx_len)])

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeBytesOutput._hx_class = python_io_NativeBytesOutput
globalClasses._hx_classes["python.io.NativeBytesOutput"] = python_io_NativeBytesOutput







class python_io_NativeTextInput(python_io_NativeInput):
    _hx_class_name = "python.io.NativeTextInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = ["readByte", "seek", "readinto"]
    _hx_statics = []
    _hx_interfaces = [python_io_IInput]
    _hx_super = python_io_NativeInput


    def __init__(self,stream):
        super().__init__(stream)

    def readByte(self):
        ret = self.stream.buffer.read(1)
        if (len(ret) == 0):
            self.throwEof()
        return ret[0]

    def seek(self,p,pos):
        self.wasEof = False
        python_io_IoTools.seekInTextMode(self.stream,self.tell,p,pos)

    def readinto(self,b):
        return self.stream.buffer.readinto(b)

    @staticmethod
    def _hx_empty_init(_hx_o):        pass
python_io_NativeTextInput._hx_class = python_io_NativeTextInput
globalClasses._hx_classes["python.io.NativeTextInput"] = python_io_NativeTextInput

class python_io_FileBytesOutput(python_io_NativeBytesOutput):
    _hx_class_name = "python.io.FileBytesOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileOutput]
    _hx_super = python_io_NativeBytesOutput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileBytesOutput._hx_class = python_io_FileBytesOutput
globalClasses._hx_classes["python.io.FileBytesOutput"] = python_io_FileBytesOutput


class python_io_FileTextInput(python_io_NativeTextInput):
    _hx_class_name = "python.io.FileTextInput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileInput]
    _hx_super = python_io_NativeTextInput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileTextInput._hx_class = python_io_FileTextInput
globalClasses._hx_classes["python.io.FileTextInput"] = python_io_FileTextInput


class python_io_FileTextOutput(python_io_NativeTextOutput):
    _hx_class_name = "python.io.FileTextOutput"
    __slots__ = ()
    _hx_fields = []
    _hx_methods = []
    _hx_statics = []
    _hx_interfaces = [python_io_IFileOutput]
    _hx_super = python_io_NativeTextOutput


    def __init__(self,stream):
        super().__init__(stream)
python_io_FileTextOutput._hx_class = python_io_FileTextOutput
globalClasses._hx_classes["python.io.FileTextOutput"] = python_io_FileTextOutput











class python_lib__Re_Choice_Impl_:
    _hx_class_name = "python.lib._Re.Choice_Impl_"
    __slots__ = ()
    _hx_statics = ["fromA", "fromB"]

    @staticmethod
    def fromA(x):
        return x

    @staticmethod
    def fromB(x):
        return x
python_lib__Re_Choice_Impl_._hx_class = python_lib__Re_Choice_Impl_
globalClasses._hx_classes["python.lib._Re.Choice_Impl_"] = python_lib__Re_Choice_Impl_


class python_lib__Re_RegexHelper:
    _hx_class_name = "python.lib._Re.RegexHelper"
    __slots__ = ()
    _hx_statics = ["findallDynamic"]

    @staticmethod
    def findallDynamic(r,string,pos = None,endpos = None):
        if (endpos is None):
            if (pos is None):
                return r.findall(string)
            else:
                return r.findall(string,pos)
        else:
            return r.findall(string,pos,endpos)
python_lib__Re_RegexHelper._hx_class = python_lib__Re_RegexHelper
globalClasses._hx_classes["python.lib._Re.RegexHelper"] = python_lib__Re_RegexHelper


anon.classesinmodule(sys.modules[__name__])
