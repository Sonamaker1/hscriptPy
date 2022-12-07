
from _hx_AnonObject import _hx_AnonObject
import globalClasses
 

import math as Math
import re as python_lib_Re

import math as python_lib_Math
import math as Math
from os import path as python_lib_os_Path
import inspect as python_lib_Inspect
import sys as python_lib_Sys
try:
    import msvcrt as python_lib_Msvcrt
except:
    pass
import os as python_lib_Os
import random as python_lib_Random
import re as python_lib_Re
import subprocess as python_lib_Subprocess
try:
    import termios as python_lib_Termios
except:
    pass
import time as python_lib_Time
import timeit as python_lib_Timeit
try:
    import tty as python_lib_Tty
except:
    pass
from datetime import datetime as python_lib_datetime_Datetime
from datetime import timedelta as python_lib_datetime_Timedelta
from datetime import timezone as python_lib_datetime_Timezone
from io import StringIO as python_lib_io_StringIO
import urllib.parse as python_lib_urllib_Parse

Math.NEGATIVE_INFINITY = float("-inf")
Math.POSITIVE_INFINITY = float("inf")
Math.NaN = float("nan")
Math.PI = python_lib_Math.pi

class Bool: pass

class Date:
    _hx_class_name = "Date"
    __slots__ = ("date", "dateUTC")
    _hx_fields = ["date", "dateUTC"]
    _hx_methods = ["getTime", "getHours", "getMinutes", "getSeconds", "getFullYear", "getMonth", "getDate", "getDay", "getUTCHours", "getUTCMinutes", "getUTCSeconds", "getUTCFullYear", "getUTCMonth", "getUTCDate", "getUTCDay", "getTimezoneOffset", "toString"]
    _hx_statics = ["now", "fromTime", "makeLocal", "UTC", "fromString"]

    def __init__(self,year,month,day,hour,_hx_min,sec):
        self.dateUTC = None
        if (year < python_lib_datetime_Datetime.min.year):
            year = python_lib_datetime_Datetime.min.year
        if (day == 0):
            day = 1
        self.date = Date.makeLocal(python_lib_datetime_Datetime(year,(month + 1),day,hour,_hx_min,sec,0))
        self.dateUTC = self.date.astimezone(python_lib_datetime_Timezone.utc)

    def getTime(self):
        return (self.date.timestamp() * 1000)

    def getHours(self):
        return self.date.hour

    def getMinutes(self):
        return self.date.minute

    def getSeconds(self):
        return self.date.second

    def getFullYear(self):
        return self.date.year

    def getMonth(self):
        return (self.date.month - 1)

    def getDate(self):
        return self.date.day

    def getDay(self):
        return HxOverrides.mod(self.date.isoweekday(), 7)

    def getUTCHours(self):
        return self.dateUTC.hour

    def getUTCMinutes(self):
        return self.dateUTC.minute

    def getUTCSeconds(self):
        return self.dateUTC.second

    def getUTCFullYear(self):
        return self.dateUTC.year

    def getUTCMonth(self):
        return (self.dateUTC.month - 1)

    def getUTCDate(self):
        return self.dateUTC.day

    def getUTCDay(self):
        return HxOverrides.mod(self.dateUTC.isoweekday(), 7)

    def getTimezoneOffset(self):
        x = (self.date.utcoffset() / python_lib_datetime_Timedelta(0,60))
        tmp = None
        try:
            tmp = int(x)
        except BaseException as _g:
            None
            tmp = None
        return -tmp

    def toString(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def now():
        d = Date(2000,0,1,0,0,0)
        d.date = Date.makeLocal(python_lib_datetime_Datetime.now())
        d.dateUTC = d.date.astimezone(python_lib_datetime_Timezone.utc)
        return d

    @staticmethod
    def fromTime(t):
        d = Date(2000,0,1,0,0,0)
        d.date = Date.makeLocal(python_lib_datetime_Datetime.fromtimestamp((t / 1000.0)))
        d.dateUTC = d.date.astimezone(python_lib_datetime_Timezone.utc)
        return d

    @staticmethod
    def makeLocal(date):
        from python import python__KwArgs_KwArgs_Impl_
        try:
            return date.astimezone()
        except BaseException as _g:
            None
            tzinfo = python_lib_datetime_Datetime.now(python_lib_datetime_Timezone.utc).astimezone().tzinfo
            return date.replace(**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'tzinfo': tzinfo})))

    @staticmethod
    def UTC(year,month,day,hour,_hx_min,sec):
        return (python_lib_datetime_Datetime(year,(month + 1),day,hour,_hx_min,sec,0,python_lib_datetime_Timezone.utc).timestamp() * 1000)

    @staticmethod
    def fromString(s):
        from haxe import haxe_Exception 
        _g = len(s)
        if (_g == 8):
            k = s.split(":")
            return Date.fromTime((((Std.parseInt((k[0] if 0 < len(k) else None)) * 3600000.) + ((Std.parseInt((k[1] if 1 < len(k) else None)) * 60000.))) + ((Std.parseInt((k[2] if 2 < len(k) else None)) * 1000.))))
        elif (_g == 10):
            k = s.split("-")
            return Date(Std.parseInt((k[0] if 0 < len(k) else None)),(Std.parseInt((k[1] if 1 < len(k) else None)) - 1),Std.parseInt((k[2] if 2 < len(k) else None)),0,0,0)
        elif (_g == 19):
            k = s.split(" ")
            _this = (k[0] if 0 < len(k) else None)
            y = _this.split("-")
            _this = (k[1] if 1 < len(k) else None)
            t = _this.split(":")
            return Date(Std.parseInt((y[0] if 0 < len(y) else None)),(Std.parseInt((y[1] if 1 < len(y) else None)) - 1),Std.parseInt((y[2] if 2 < len(y) else None)),Std.parseInt((t[0] if 0 < len(t) else None)),Std.parseInt((t[1] if 1 < len(t) else None)),Std.parseInt((t[2] if 2 < len(t) else None)))
        else:
            raise haxe_Exception.thrown(("Invalid date format : " + ("null" if s is None else s)))

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.date = None
        _hx_o.dateUTC = None
Date._hx_class = Date
globalClasses._hx_classes["Date"] = Date


class Dynamic: pass


class EReg:
    _hx_class_name = "EReg"
    __slots__ = ("pattern", "matchObj", "_hx_global")
    _hx_fields = ["pattern", "matchObj", "global"]
    _hx_methods = ["match", "matched", "matchedLeft", "matchedRight", "matchedPos", "matchSub", "split", "replace", "map"]
    _hx_statics = ["escape"]

    def __init__(self,r,opt):
        self.matchObj = None
        self._hx_global = False
        options = 0
        _g = 0
        _g1 = len(opt)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = (-1 if ((i >= len(opt))) else ord(opt[i]))
            if (c == 109):
                options = (options | python_lib_Re.M)
            if (c == 105):
                options = (options | python_lib_Re.I)
            if (c == 115):
                options = (options | python_lib_Re.S)
            if (c == 117):
                options = (options | python_lib_Re.U)
            if (c == 103):
                self._hx_global = True
        self.pattern = python_lib_Re.compile(r,options)

    def match(self,s):
        self.matchObj = python_lib_Re.search(self.pattern,s)
        return (self.matchObj is not None)

    def matched(self,n):
        return self.matchObj.group(n)

    def matchedLeft(self):
        return HxString.substr(self.matchObj.string,0,self.matchObj.start())

    def matchedRight(self):
        return HxString.substr(self.matchObj.string,self.matchObj.end(),None)

    def matchedPos(self):
        return _hx_AnonObject({'pos': self.matchObj.start(), 'len': (self.matchObj.end() - self.matchObj.start())})

    def matchSub(self,s,pos,_hx_len = None):
        if (_hx_len is None):
            _hx_len = -1
        if (_hx_len != -1):
            self.matchObj = self.pattern.search(s,pos,(pos + _hx_len))
        else:
            self.matchObj = self.pattern.search(s,pos)
        return (self.matchObj is not None)

    def split(self,s):
        from python import python_HaxeIterator
        if self._hx_global:
            ret = []
            lastEnd = 0
            x = python_HaxeIterator(python_lib_Re.finditer(self.pattern,s))
            while x.hasNext():
                x1 = x.next()
                x2 = HxString.substring(s,lastEnd,x1.start())
                ret.append(x2)
                lastEnd = x1.end()
            x = HxString.substr(s,lastEnd,None)
            ret.append(x)
            return ret
        else:
            self.matchObj = python_lib_Re.search(self.pattern,s)
            if (self.matchObj is None):
                return [s]
            else:
                return [HxString.substring(s,0,self.matchObj.start()), HxString.substr(s,self.matchObj.end(),None)]

    def replace(self,s,by):
        from python import python_Boot
        _this = by.split("$$")
        by = "_hx_#repl#__".join([python_Boot.toString1(x1,'') for x1 in _this])
        def _hx_local_0(x):
            res = by
            g = x.groups()
            _g = 0
            _g1 = len(g)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                gs = g[i]
                if (gs is None):
                    continue
                delimiter = ("$" + HxOverrides.stringOrNull(str((i + 1))))
                _this = (list(res) if ((delimiter == "")) else res.split(delimiter))
                res = gs.join([python_Boot.toString1(x1,'') for x1 in _this])
            _this = res.split("_hx_#repl#__")
            res = "$".join([python_Boot.toString1(x1,'') for x1 in _this])
            return res
        replace = _hx_local_0
        return python_lib_Re.sub(self.pattern,replace,s,(0 if (self._hx_global) else 1))

    def map(self,s,f):
        buf_b = python_lib_io_StringIO()
        pos = 0
        right = s
        cur = self
        while (pos < len(s)):
            if (self.matchObj is None):
                self.matchObj = python_lib_Re.search(self.pattern,s)
            else:
                self.matchObj = self.matchObj.re.search(s,pos)
            if (self.matchObj is None):
                break
            pos1 = self.matchObj.end()
            curPos_pos = cur.matchObj.start()
            curPos_len = (cur.matchObj.end() - cur.matchObj.start())
            buf_b.write(Std.string(HxString.substr(HxString.substr(cur.matchObj.string,0,cur.matchObj.start()),pos,None)))
            buf_b.write(Std.string(f(cur)))
            right = HxString.substr(cur.matchObj.string,cur.matchObj.end(),None)
            if (not self._hx_global):
                buf_b.write(Std.string(right))
                return buf_b.getvalue()
            if (curPos_len == 0):
                buf_b.write(Std.string(("" if (((pos1 < 0) or ((pos1 >= len(s))))) else s[pos1])))
                right = HxString.substr(right,1,None)
                pos = (pos1 + 1)
            else:
                pos = pos1
        buf_b.write(Std.string(right))
        return buf_b.getvalue()

    @staticmethod
    def escape(s):
        return python_lib_Re.escape(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.pattern = None
        _hx_o.matchObj = None
        _hx_o._hx_global = None
EReg._hx_class = EReg
globalClasses._hx_classes["EReg"] = EReg

class Enum:
    _hx_class_name = "Enum"
    __slots__ = ("tag", "index", "params")
    _hx_fields = ["tag", "index", "params"]
    _hx_methods = ["__str__"]

    def __init__(self,tag,index,params):
        self.tag = tag
        self.index = index
        self.params = params

    def __str__(self):
        if (self.params is None):
            return self.tag
        else:
            return self.tag + '(' + (', '.join(str(v) for v in self.params)) + ')'

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.tag = None
        _hx_o.index = None
        _hx_o.params = None
Enum._hx_class = Enum
globalClasses._hx_classes["Enum"] = Enum


class Float: pass


class HxOverrides:
    _hx_class_name = "HxOverrides"
    __slots__ = ()
    _hx_statics = ["iterator", "keyValueIterator", "eq", "stringOrNull", "shift", "pop", "push", "join", "filter", "map", "toUpperCase", "toLowerCase", "split", "length", "rshift", "modf", "mod", "arrayGet", "arraySet", "mapKwArgs", "reverseMapKwArgs"]

    @staticmethod
    def iterator(x):
        from haxe import haxe_iterators_ArrayIterator
    
        if isinstance(x,list):
            return haxe_iterators_ArrayIterator(x)
        return x.iterator()

    @staticmethod
    def keyValueIterator(x):
        from haxe import haxe_iterators_ArrayKeyValueIterator
        if isinstance(x,list):
            return haxe_iterators_ArrayKeyValueIterator(x)
        return x.keyValueIterator()

    @staticmethod
    def eq(a,b):
        if (isinstance(a,list) or isinstance(b,list)):
            return a is b
        return (a == b)

    @staticmethod
    def stringOrNull(s):
        if (s is None):
            return "null"
        else:
            return s

    @staticmethod
    def shift(x):
        if isinstance(x,list):
            _this = x
            return (None if ((len(_this) == 0)) else _this.pop(0))
        return x.shift()

    @staticmethod
    def pop(x):
        if isinstance(x,list):
            _this = x
            return (None if ((len(_this) == 0)) else _this.pop())
        return x.pop()

    @staticmethod
    def push(x,e):
        if isinstance(x,list):
            _this = x
            _this.append(e)
            return len(_this)
        return x.push(e)

    @staticmethod
    def join(x,sep):
        from python import python_Boot
        if isinstance(x,list):
            return sep.join([python_Boot.toString1(x1,'') for x1 in x])
        return x.join(sep)

    @staticmethod
    def filter(x,f):
        if isinstance(x,list):
            return list(filter(f,x))
        return x.filter(f)

    @staticmethod
    def map(x,f):
        if isinstance(x,list):
            return list(map(f,x))
        return x.map(f)

    @staticmethod
    def toUpperCase(x):
        if isinstance(x,str):
            return x.upper()
        return x.toUpperCase()

    @staticmethod
    def toLowerCase(x):
        if isinstance(x,str):
            return x.lower()
        return x.toLowerCase()

    @staticmethod
    def split(x,delimiter):
        if isinstance(x,str):
            _this = x
            if (delimiter == ""):
                return list(_this)
            else:
                return _this.split(delimiter)
        return x.split(delimiter)

    @staticmethod
    def length(x):
        if isinstance(x,str):
            return len(x)
        elif isinstance(x,list):
            return len(x)
        return x.length

    @staticmethod
    def rshift(val,n):
        return ((val % 0x100000000) >> n)

    @staticmethod
    def modf(a,b):
        if (b == 0.0):
            return float('nan')
        elif (a < 0):
            if (b < 0):
                return -(-a % (-b))
            else:
                return -(-a % b)
        elif (b < 0):
            return a % (-b)
        else:
            return a % b

    @staticmethod
    def mod(a,b):
        if (a < 0):
            if (b < 0):
                return -(-a % (-b))
            else:
                return -(-a % b)
        elif (b < 0):
            return a % (-b)
        else:
            return a % b

    @staticmethod
    def arrayGet(a,i):
        if isinstance(a,list):
            x = a
            if ((i > -1) and ((i < len(x)))):
                return x[i]
            else:
                return None
        else:
            return a[i]

    @staticmethod
    def arraySet(a,i,v):
        if isinstance(a,list):
            x = a
            v1 = v
            l = len(x)
            while (l < i):
                x.append(None)
                l = (l + 1)
            if (l == i):
                x.append(v1)
            else:
                x[i] = v1
            return v1
        else:
            a[i] = v
            return v

    @staticmethod
    def mapKwArgs(a,v):
        from python import python_HaxeIterator, python_Lib
        a1 = _hx_AnonObject(python_Lib.anonToDict(a))
        k = python_HaxeIterator(iter(v.keys()))
        while k.hasNext():
            k1 = k.next()
            val = v.get(k1)
            if a1._hx_hasattr(k1):
                x = getattr(a1,k1)
                setattr(a1,val,x)
                delattr(a1,k1)
        return a1

    @staticmethod
    def reverseMapKwArgs(a,v):
        from python import python_HaxeIterator
        a1 = a.copy()
        k = python_HaxeIterator(iter(v.keys()))
        while k.hasNext():
            k1 = k.next()
            val = v.get(k1)
            if (val in a1):
                x = a1.get(val,None)
                a1[k1] = x
                del a1[val]
        return a1
HxOverrides._hx_class = HxOverrides
globalClasses._hx_classes["HxOverrides"] = HxOverrides


class HxString:
    _hx_class_name = "HxString"
    __slots__ = ()
    _hx_statics = ["split", "charCodeAt", "charAt", "lastIndexOf", "toUpperCase", "toLowerCase", "indexOf", "indexOfImpl", "toString", "get_length", "fromCharCode", "substring", "substr"]

    @staticmethod
    def split(s,d):
        if (d == ""):
            return list(s)
        else:
            return s.split(d)

    @staticmethod
    def charCodeAt(s,index):
        if ((((s is None) or ((len(s) == 0))) or ((index < 0))) or ((index >= len(s)))):
            return None
        else:
            return ord(s[index])

    @staticmethod
    def charAt(s,index):
        if ((index < 0) or ((index >= len(s)))):
            return ""
        else:
            return s[index]

    @staticmethod
    def lastIndexOf(s,_hx_str,startIndex = None):
        if (startIndex is None):
            return s.rfind(_hx_str, 0, len(s))
        elif (_hx_str == ""):
            length = len(s)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            if (startIndex > length):
                return length
            else:
                return startIndex
        else:
            i = s.rfind(_hx_str, 0, (startIndex + 1))
            startLeft = (max(0,((startIndex + 1) - len(_hx_str))) if ((i == -1)) else (i + 1))
            check = s.find(_hx_str, startLeft, len(s))
            if ((check > i) and ((check <= startIndex))):
                return check
            else:
                return i

    @staticmethod
    def toUpperCase(s):
        return s.upper()

    @staticmethod
    def toLowerCase(s):
        return s.lower()

    @staticmethod
    def indexOf(s,_hx_str,startIndex = None):
        if (startIndex is None):
            return s.find(_hx_str)
        else:
            return HxString.indexOfImpl(s,_hx_str,startIndex)

    @staticmethod
    def indexOfImpl(s,_hx_str,startIndex):
        if (_hx_str == ""):
            length = len(s)
            if (startIndex < 0):
                startIndex = (length + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            if (startIndex > length):
                return length
            else:
                return startIndex
        return s.find(_hx_str, startIndex)

    @staticmethod
    def toString(s):
        return s

    @staticmethod
    def get_length(s):
        return len(s)

    @staticmethod
    def fromCharCode(code):
        return "".join(map(chr,[code]))

    @staticmethod
    def substring(s,startIndex,endIndex = None):
        if (startIndex < 0):
            startIndex = 0
        if (endIndex is None):
            return s[startIndex:]
        else:
            if (endIndex < 0):
                endIndex = 0
            if (endIndex < startIndex):
                return s[endIndex:startIndex]
            else:
                return s[startIndex:endIndex]

    @staticmethod
    def substr(s,startIndex,_hx_len = None):
        if (_hx_len is None):
            return s[startIndex:]
        else:
            if (_hx_len == 0):
                return ""
            if (startIndex < 0):
                startIndex = (len(s) + startIndex)
                if (startIndex < 0):
                    startIndex = 0
            return s[startIndex:(startIndex + _hx_len)]
HxString._hx_class = HxString
globalClasses._hx_classes["HxString"] = HxString


class IntIterator:
    _hx_class_name = "IntIterator"
    __slots__ = ("min", "max")
    _hx_fields = ["min", "max"]
    _hx_methods = ["hasNext", "next"]

    def __init__(self,_hx_min,_hx_max):
        self.min = _hx_min
        self.max = _hx_max

    def hasNext(self):
        return (self.min < self.max)

    def next(self):
        def _hx_local_3():
            def _hx_local_2():
                _hx_local_0 = self
                _hx_local_1 = _hx_local_0.min
                _hx_local_0.min = (_hx_local_1 + 1)
                return _hx_local_1
            return _hx_local_2()
        return _hx_local_3()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.min = None
        _hx_o.max = None
IntIterator._hx_class = IntIterator
globalClasses._hx_classes["IntIterator"] = IntIterator


class Int: pass


class Lambda:
    _hx_class_name = "Lambda"
    __slots__ = ()
    _hx_statics = ["array", "list", "map", "mapi", "flatten", "flatMap", "has", "exists", "foreach", "iter", "filter", "fold", "count", "empty", "indexOf", "find", "concat"]

    @staticmethod
    def array(it):
        a = list()
        i = HxOverrides.iterator(it)
        while i.hasNext():
            i1 = i.next()
            a.append(i1)
        return a

    @staticmethod
    def list(it):
        from haxe import haxe_ds_List
        l = haxe_ds_List()
        i = HxOverrides.iterator(it)
        while i.hasNext():
            i1 = i.next()
            l.add(i1)
        return l

    @staticmethod
    def map(it,f):
        from haxe import haxe_ds_List
        l = haxe_ds_List()
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            l.add(f(x1))
        return l

    @staticmethod
    def mapi(it,f):
        from haxe import haxe_ds_List
        l = haxe_ds_List()
        i = 0
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            tmp = i
            i = (i + 1)
            l.add(f(tmp,x1))
        return l

    @staticmethod
    def flatten(it):
        from haxe import haxe_ds_List
        l = haxe_ds_List()
        e = HxOverrides.iterator(it)
        while e.hasNext():
            e1 = e.next()
            x = HxOverrides.iterator(e1)
            while x.hasNext():
                x1 = x.next()
                l.add(x1)
        return l

    @staticmethod
    def flatMap(it,f):
        return Lambda.flatten(Lambda.map(it,f))

    @staticmethod
    def has(it,elt):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if HxOverrides.eq(x1,elt):
                return True
        return False

    @staticmethod
    def exists(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if f(x1):
                return True
        return False

    @staticmethod
    def foreach(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if (not f(x1)):
                return False
        return True

    @staticmethod
    def iter(it,f):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            f(x1)

    @staticmethod
    def filter(it,f):
        from haxe import haxe_ds_List
        l = haxe_ds_List()
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            if f(x1):
                l.add(x1)
        return l

    @staticmethod
    def fold(it,f,first):
        x = HxOverrides.iterator(it)
        while x.hasNext():
            x1 = x.next()
            first = f(x1,first)
        return first

    @staticmethod
    def count(it,pred = None):
        n = 0
        if (pred is None):
            _ = HxOverrides.iterator(it)
            while _.hasNext():
                _1 = _.next()
                n = (n + 1)
        else:
            x = HxOverrides.iterator(it)
            while x.hasNext():
                x1 = x.next()
                if pred(x1):
                    n = (n + 1)
        return n

    @staticmethod
    def empty(it):
        return (not HxOverrides.iterator(it).hasNext())

    @staticmethod
    def indexOf(it,v):
        i = 0
        v2 = HxOverrides.iterator(it)
        while v2.hasNext():
            v21 = v2.next()
            if HxOverrides.eq(v,v21):
                return i
            i = (i + 1)
        return -1

    @staticmethod
    def find(it,f):
        v = HxOverrides.iterator(it)
        while v.hasNext():
            v1 = v.next()
            if f(v1):
                return v1
        return None

    @staticmethod
    def concat(a,b):
        from haxe import haxe_ds_List
        l = haxe_ds_List()
        x = HxOverrides.iterator(a)
        while x.hasNext():
            x1 = x.next()
            l.add(x1)
        x = HxOverrides.iterator(b)
        while x.hasNext():
            x1 = x.next()
            l.add(x1)
        return l
Lambda._hx_class = Lambda
globalClasses._hx_classes["Lambda"] = Lambda


class Reflect:
    _hx_class_name = "Reflect"
    __slots__ = ()
    _hx_statics = ["hasField", "field", "setField", "getProperty", "setProperty", "callMethod", "fields", "isFunction", "compare", "isClosure", "compareMethods", "isObject", "isEnumValue", "deleteField", "copy", "makeVarArgs"]

    @staticmethod
    def hasField(o,field):
        from python import python_Boot
        return python_Boot.hasField(o,field)

    @staticmethod
    def field(o,field):
        from python import python_Boot
        return python_Boot.field(o,field)

    @staticmethod
    def setField(o,field,value):
        from python import python_Boot
        setattr(o,(("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field)),value)

    @staticmethod
    def getProperty(o,field):
        from python import python_Boot
        if (o is None):
            return None
        if (field in python_Boot.keywords):
            field = ("_hx_" + field)
        elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
            field = ("_hx_" + field)
        if isinstance(o,_hx_AnonObject):
            return Reflect.field(o,field)
        tmp = Reflect.field(o,("get_" + ("null" if field is None else field)))
        if ((tmp is not None) and callable(tmp)):
            return tmp()
        else:
            return Reflect.field(o,field)

    @staticmethod
    def setProperty(o,field,value):
        from python import python_Boot
        field1 = (("_hx_" + field) if ((field in python_Boot.keywords)) else (("_hx_" + field) if (((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95)))) else field))
        if isinstance(o,_hx_AnonObject):
            setattr(o,field1,value)
        elif hasattr(o,("set_" + ("null" if field1 is None else field1))):
            getattr(o,("set_" + ("null" if field1 is None else field1)))(value)
        else:
            setattr(o,field1,value)

    @staticmethod
    def callMethod(o,func,args):
        if callable(func):
            return func(*args)
        else:
            return None

    @staticmethod
    def fields(o):
        from python import python_Boot
        return python_Boot.fields(o)

    @staticmethod
    def isFunction(f):
        if (not ((python_lib_Inspect.isfunction(f) or python_lib_Inspect.ismethod(f)))):
            from python import python_Boot
            return python_Boot.hasField(f,"func_code")
        else:
            return True

    @staticmethod
    def compare(a,b):
        if ((a is None) and ((b is None))):
            return 0
        if (a is None):
            return 1
        elif (b is None):
            return -1
        elif HxOverrides.eq(a,b):
            return 0
        elif (a > b):
            return 1
        else:
            return -1

    @staticmethod
    def isClosure(v):
        from python import python_internal_MethodClosure
        return isinstance(v,python_internal_MethodClosure)

    @staticmethod
    def compareMethods(f1,f2):
        from python import python_internal_MethodClosure
        if HxOverrides.eq(f1,f2):
            return True
        if (isinstance(f1,python_internal_MethodClosure) and isinstance(f2,python_internal_MethodClosure)):
            m1 = f1
            m2 = f2
            if HxOverrides.eq(m1.obj,m2.obj):
                return (m1.func == m2.func)
            else:
                return False
        if ((not Reflect.isFunction(f1)) or (not Reflect.isFunction(f2))):
            return False
        return False

    @staticmethod
    def isObject(v):
        _g = Type.typeof(v)
        tmp = _g.index
        if (tmp == 4):
            return True
        elif (tmp == 6):
            _g1 = _g.params[0]
            return True
        else:
            return False

    @staticmethod
    def isEnumValue(v):
        if not HxOverrides.eq(v,Enum):
            return isinstance(v,Enum)
        else:
            return False

    @staticmethod
    def deleteField(o,field):
        from python import python_Boot
        if (field in python_Boot.keywords):
            field = ("_hx_" + field)
        elif ((((len(field) > 2) and ((ord(field[0]) == 95))) and ((ord(field[1]) == 95))) and ((ord(field[(len(field) - 1)]) != 95))):
            field = ("_hx_" + field)
        if (not python_Boot.hasField(o,field)):
            return False
        o.__delattr__(field)
        return True

    @staticmethod
    def copy(o):
        from python import python_Boot
        if (o is None):
            return None
        o2 = _hx_AnonObject({})
        _g = 0
        _g1 = python_Boot.fields(o)
        while (_g < len(_g1)):
            f = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            value = Reflect.field(o,f)
            setattr(o2,(("_hx_" + f) if ((f in python_Boot.keywords)) else (("_hx_" + f) if (((((len(f) > 2) and ((ord(f[0]) == 95))) and ((ord(f[1]) == 95))) and ((ord(f[(len(f) - 1)]) != 95)))) else f)),value)
        return o2

    @staticmethod
    def makeVarArgs(f):
        def _hx_local_0(*v):
            this1 = v
            return f((list(this1) if ((not Std.isOfType(this1,list))) else this1))
        return _hx_local_0
Reflect._hx_class = Reflect
globalClasses._hx_classes["Reflect"] = Reflect


class Std:
    _hx_class_name = "Std"
    __slots__ = ()
    _hx_statics = ["downcast", "instance", "isMetaType", "is", "isOfType", "string", "int", "parseInt", "shortenPossibleNumber", "parseFloat", "random"]

    @staticmethod
    def downcast(value,c):
        from python import python_Boot
        try:
            tmp = None
            if (not isinstance(value,c)):
                if c._hx_is_interface:
                    cls = c
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
                    tmp = result
                else:
                    tmp = False
            else:
                tmp = True
            if tmp:
                return value
            else:
                return None
        except BaseException as _g:
            None
            return None

    @staticmethod
    def instance(value,c):
        return Std.downcast(value,c)

    @staticmethod
    def isMetaType(v,t):
        return ((type(v) == type) and (v == t))

    @staticmethod
    def _hx_is(v,t):
        return Std.isOfType(v,t)

    @staticmethod
    def isOfType(v,t):
        if ((v is None) and ((t is None))):
            return False
        if (t is None):
            return False
        if ((type(t) == type) and (t == Dynamic)):
            return (v is not None)
        isBool = isinstance(v,bool)
        if (((type(t) == type) and (t == Bool)) and isBool):
            return True
        if ((((not isBool) and (not ((type(t) == type) and (t == Bool)))) and ((type(t) == type) and (t == Int))) and isinstance(v,int)):
            return True
        vIsFloat = isinstance(v,float)
        tmp = None
        tmp1 = None
        if (((not isBool) and vIsFloat) and ((type(t) == type) and (t == Int))):
            f = v
            tmp1 = (((f != Math.POSITIVE_INFINITY) and ((f != Math.NEGATIVE_INFINITY))) and (not python_lib_Math.isnan(f)))
        else:
            tmp1 = False
        if tmp1:
            tmp1 = None
            try:
                tmp1 = int(v)
            except BaseException as _g:
                None
                tmp1 = None
            tmp = (v == tmp1)
        else:
            tmp = False
        if ((tmp and ((v <= 2147483647))) and ((v >= -2147483648))):
            return True
        if (((not isBool) and ((type(t) == type) and (t == Float))) and isinstance(v,(float, int))):
            return True
        if ((type(t) == type) and (t == str)):
            return isinstance(v,str)
        isEnumType = ((type(t) == type) and (t == Enum))
        if ((isEnumType and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_constructs")):
            return True
        if isEnumType:
            return False
        isClassType = ((type(t) == type) and (t == Class))
        if ((((isClassType and (not isinstance(v,Enum))) and python_lib_Inspect.isclass(v)) and hasattr(v,"_hx_class_name")) and (not hasattr(v,"_hx_constructs"))):
            return True
        if isClassType:
            return False
        tmp = None
        try:
            tmp = isinstance(v,t)
        except BaseException as _g:
            None
            tmp = False
        if tmp:
            return True
        if python_lib_Inspect.isclass(t):
            from python import python_Boot
            cls = t
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
            currentClass = v.__class__
            result = False
            while (currentClass is not None):
                if loop(currentClass):
                    result = True
                    break
                currentClass = python_Boot.getSuperClass(currentClass)
            return result
        else:
            return False

    @staticmethod
    def string(s):
        from python import python_Boot
        return python_Boot.toString1(s,"")

    @staticmethod
    def int(x):
        try:
            return int(x)
        except BaseException as _g:
            None
            return None

    @staticmethod
    def parseInt(x):
        if (x is None):
            return None
        try:
            return int(x)
        except BaseException as _g:
            None
            base = 10
            _hx_len = len(x)
            foundCount = 0
            sign = 0
            firstDigitIndex = 0
            lastDigitIndex = -1
            previous = 0
            _g = 0
            _g1 = _hx_len
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = (-1 if ((i >= len(x))) else ord(x[i]))
                if (((c > 8) and ((c < 14))) or ((c == 32))):
                    if (foundCount > 0):
                        return None
                    continue
                else:
                    c1 = c
                    if (c1 == 43):
                        if (foundCount == 0):
                            sign = 1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 45):
                        if (foundCount == 0):
                            sign = -1
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (c1 == 48):
                        if (not (((foundCount == 0) or (((foundCount == 1) and ((sign != 0))))))):
                            if (not (((48 <= c) and ((c <= 57))))):
                                if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                    break
                    elif ((c1 == 120) or ((c1 == 88))):
                        if ((previous == 48) and ((((foundCount == 1) and ((sign == 0))) or (((foundCount == 2) and ((sign != 0))))))):
                            base = 16
                        elif (not (((48 <= c) and ((c <= 57))))):
                            if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                                break
                    elif (not (((48 <= c) and ((c <= 57))))):
                        if (not (((base == 16) and ((((97 <= c) and ((c <= 122))) or (((65 <= c) and ((c <= 90))))))))):
                            break
                if (((foundCount == 0) and ((sign == 0))) or (((foundCount == 1) and ((sign != 0))))):
                    firstDigitIndex = i
                foundCount = (foundCount + 1)
                lastDigitIndex = i
                previous = c
            if (firstDigitIndex <= lastDigitIndex):
                digits = HxString.substring(x,firstDigitIndex,(lastDigitIndex + 1))
                try:
                    return (((-1 if ((sign == -1)) else 1)) * int(digits,base))
                except BaseException as _g:
                    return None
            return None

    @staticmethod
    def shortenPossibleNumber(x):
        r = ""
        _g = 0
        _g1 = len(x)
        while (_g < _g1):
            i = _g
            _g = (_g + 1)
            c = ("" if (((i < 0) or ((i >= len(x))))) else x[i])
            _g2 = HxString.charCodeAt(c,0)
            if (_g2 is None):
                break
            else:
                _g3 = _g2
                if (((((((((((_g3 == 57) or ((_g3 == 56))) or ((_g3 == 55))) or ((_g3 == 54))) or ((_g3 == 53))) or ((_g3 == 52))) or ((_g3 == 51))) or ((_g3 == 50))) or ((_g3 == 49))) or ((_g3 == 48))) or ((_g3 == 46))):
                    r = (("null" if r is None else r) + ("null" if c is None else c))
                else:
                    break
        return r

    @staticmethod
    def parseFloat(x):
        try:
            return float(x)
        except BaseException as _g:
            None
            if (x is not None):
                r1 = Std.shortenPossibleNumber(x)
                if (r1 != x):
                    return Std.parseFloat(r1)
            return Math.NaN

    @staticmethod
    def random(x):
        if (x <= 0):
            return 0
        else:
            return int((python_lib_Random.random() * x))
Std._hx_class = Std
globalClasses._hx_classes["Std"] = Std


class StringBuf:
    _hx_class_name = "StringBuf"
    __slots__ = ("b",)
    _hx_fields = ["b"]
    _hx_methods = ["get_length", "add", "add1", "addChar", "addSub", "toString"]

    def __init__(self):
        self.b = python_lib_io_StringIO()

    def get_length(self):
        pos = self.b.tell()
        self.b.seek(0,2)
        _hx_len = self.b.tell()
        self.b.seek(pos,0)
        return _hx_len

    def add(self,x):
        s = Std.string(x)
        self.b.write(s)

    def add1(self,s):
        self.b.write(s)

    def addChar(self,c):
        s = "".join(map(chr,[c]))
        self.b.write(s)

    def addSub(self,s,pos,_hx_len = None):
        s1 = (HxString.substr(s,pos,None) if ((_hx_len is None)) else HxString.substr(s,pos,_hx_len))
        self.b.write(s1)

    def toString(self):
        return self.b.getvalue()

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.b = None
StringBuf._hx_class = StringBuf
globalClasses._hx_classes["StringBuf"] = StringBuf


class StringTools:
    _hx_class_name = "StringTools"
    __slots__ = ()
    _hx_statics = ["urlEncode", "urlDecode", "htmlEscape", "htmlUnescape", "contains", "startsWith", "endsWith", "isSpace", "ltrim", "rtrim", "trim", "lpad", "rpad", "replace", "hex", "fastCodeAt", "unsafeCodeAt", "iterator", "keyValueIterator", "isEof", "quoteUnixArg", "winMetaCharacters", "quoteWinArg"]

    @staticmethod
    def urlEncode(s):
        return python_lib_urllib_Parse.quote(s,"")

    @staticmethod
    def urlDecode(s):
        return python_lib_urllib_Parse.unquote(s)

    @staticmethod
    def htmlEscape(s,quotes = None):
        buf_b = python_lib_io_StringIO()
        _g_offset = 0
        _g_s = s
        while (_g_offset < len(_g_s)):
            index = _g_offset
            _g_offset = (_g_offset + 1)
            code = ord(_g_s[index])
            code1 = code
            if (code1 == 34):
                if quotes:
                    buf_b.write("&quot;")
                else:
                    buf_b.write("".join(map(chr,[code])))
            elif (code1 == 38):
                buf_b.write("&amp;")
            elif (code1 == 39):
                if quotes:
                    buf_b.write("&#039;")
                else:
                    buf_b.write("".join(map(chr,[code])))
            elif (code1 == 60):
                buf_b.write("&lt;")
            elif (code1 == 62):
                buf_b.write("&gt;")
            else:
                buf_b.write("".join(map(chr,[code])))
        return buf_b.getvalue()

    @staticmethod
    def htmlUnescape(s):
        from python import python_Boot
        _this = s.split("&gt;")
        _this1 = ">".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&lt;")
        _this1 = "<".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&quot;")
        _this1 = "\"".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&#039;")
        _this1 = "'".join([python_Boot.toString1(x1,'') for x1 in _this])
        _this = _this1.split("&amp;")
        return "&".join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def contains(s,value):
        startIndex = None
        return (((s.find(value) if ((startIndex is None)) else HxString.indexOfImpl(s,value,startIndex))) != -1)

    @staticmethod
    def startsWith(s,start):
        return s.startswith(start)

    @staticmethod
    def endsWith(s,end):
        return s.endswith(end)

    @staticmethod
    def isSpace(s,pos):
        if (((len(s) == 0) or ((pos < 0))) or ((pos >= len(s)))):
            return False
        c = HxString.charCodeAt(s,pos)
        if (not (((c > 8) and ((c < 14))))):
            return (c == 32)
        else:
            return True

    @staticmethod
    def ltrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,r)):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,r,(l - r))
        else:
            return s

    @staticmethod
    def rtrim(s):
        l = len(s)
        r = 0
        while ((r < l) and StringTools.isSpace(s,((l - r) - 1))):
            r = (r + 1)
        if (r > 0):
            return HxString.substr(s,0,(l - r))
        else:
            return s

    @staticmethod
    def trim(s):
        return StringTools.ltrim(StringTools.rtrim(s))

    @staticmethod
    def lpad(s,c,l):
        if (len(c) <= 0):
            return s
        buf = StringBuf()
        l = (l - len(s))
        while (buf.get_length() < l):
            s1 = Std.string(c)
            buf.b.write(s1)
        s1 = Std.string(s)
        buf.b.write(s1)
        return buf.b.getvalue()

    @staticmethod
    def rpad(s,c,l):
        if (len(c) <= 0):
            return s
        buf = StringBuf()
        s1 = Std.string(s)
        buf.b.write(s1)
        while (buf.get_length() < l):
            s = Std.string(c)
            buf.b.write(s)
        return buf.b.getvalue()

    @staticmethod
    def replace(s,sub,by):
        from python import python_Boot
        _this = (list(s) if ((sub == "")) else s.split(sub))
        return by.join([python_Boot.toString1(x1,'') for x1 in _this])

    @staticmethod
    def hex(n,digits = None):
        s = ""
        hexChars = "0123456789ABCDEF"
        while True:
            index = (n & 15)
            s = (HxOverrides.stringOrNull((("" if (((index < 0) or ((index >= len(hexChars))))) else hexChars[index]))) + ("null" if s is None else s))
            n = HxOverrides.rshift(n, 4)
            if (not ((n > 0))):
                break
        if ((digits is not None) and ((len(s) < digits))):
            diff = (digits - len(s))
            _g = 0
            _g1 = diff
            while (_g < _g1):
                _ = _g
                _g = (_g + 1)
                s = ("0" + ("null" if s is None else s))
        return s

    @staticmethod
    def fastCodeAt(s,index):
        if (index >= len(s)):
            return -1
        else:
            return ord(s[index])

    @staticmethod
    def unsafeCodeAt(s,index):
        return ord(s[index])

    @staticmethod
    def iterator(s):
        from haxe import haxe_iterators_StringIterator
        return haxe_iterators_StringIterator(s)

    @staticmethod
    def keyValueIterator(s):
        from haxe import haxe_iterators_StringKeyValueIterator
        return haxe_iterators_StringKeyValueIterator(s)

    @staticmethod
    def isEof(c):
        return (c == -1)

    @staticmethod
    def quoteUnixArg(argument):
        if (argument == ""):
            return "''"
        else:
            _this = EReg("[^a-zA-Z0-9_@%+=:,./-]","")
            _this.matchObj = python_lib_Re.search(_this.pattern,argument)
            if (_this.matchObj is None):
                return argument
            else:
                return (("'" + HxOverrides.stringOrNull(StringTools.replace(argument,"'","'\"'\"'"))) + "'")

    @staticmethod
    def quoteWinArg(argument,escapeMetaCharacters):
        from python import python_internal_ArrayImpl
        argument1 = argument
        _this = EReg("^[^ \t\\\\\"]+$","")
        _this.matchObj = python_lib_Re.search(_this.pattern,argument1)
        if (_this.matchObj is None):
            result_b = python_lib_io_StringIO()
            needquote = None
            startIndex = None
            if (((argument1.find(" ") if ((startIndex is None)) else HxString.indexOfImpl(argument1," ",startIndex))) == -1):
                startIndex = None
                needquote = (((argument1.find("\t") if ((startIndex is None)) else HxString.indexOfImpl(argument1,"\t",startIndex))) != -1)
            else:
                needquote = True
            needquote1 = (needquote or ((argument1 == "")))
            if needquote1:
                result_b.write("\"")
            bs_buf = StringBuf()
            _g = 0
            _g1 = len(argument1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                _g2 = HxString.charCodeAt(argument1,i)
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
            argument1 = result_b.getvalue()
        if escapeMetaCharacters:
            from haxe import haxe_SysTools
            result_b = python_lib_io_StringIO()
            _g = 0
            _g1 = len(argument1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                c = HxString.charCodeAt(argument1,i)
                if (python_internal_ArrayImpl.indexOf(haxe_SysTools.winMetaCharacters,c,None) >= 0):
                    result_b.write("".join(map(chr,[94])))
                result_b.write("".join(map(chr,[c])))
            return result_b.getvalue()
        else:
            return argument1
StringTools._hx_class = StringTools
globalClasses._hx_classes["StringTools"] = StringTools


class Sys:
    _hx_class_name = "Sys"
    __slots__ = ()
    _hx_statics = ["environ", "get_environ", "time", "exit", "print", "println", "args", "getEnv", "putEnv", "environment", "sleep", "setTimeLocale", "getCwd", "setCwd", "systemName", "command", "cpuTime", "executablePath", "_programPath", "programPath", "getChar", "stdin", "stdout", "stderr"]
    environ = None

    @staticmethod
    def get_environ():
        from python import python_HaxeIterator        
        _g = Sys.environ
        if (_g is None):
            from haxe import haxe_ds_StringMap
            
            environ = haxe_ds_StringMap()
            env = python_lib_Os.environ
            key = python_HaxeIterator(iter(env.keys()))
            while key.hasNext():
                key1 = key.next()
                value = env.get(key1,None)
                environ.h[key1] = value
            def _hx_local_1():
                def _hx_local_0():
                    Sys.environ = environ
                    return Sys.environ
                return _hx_local_0()
            return _hx_local_1()
        else:
            env = _g
            return env

    @staticmethod
    def time():
        return python_lib_Time.time()

    @staticmethod
    def exit(code):
        python_lib_Sys.exit(code)

    @staticmethod
    def print(v):
        from python import python_Lib
        python_Lib.printString(Std.string(v))

    @staticmethod
    def println(v):
        from python import python_Lib
        _hx_str = Std.string(v)
        python_Lib.printString((("" + ("null" if _hx_str is None else _hx_str)) + HxOverrides.stringOrNull(python_Lib.lineEnd)))

    @staticmethod
    def args():
        argv = python_lib_Sys.argv
        return argv[1:None]

    @staticmethod
    def getEnv(s):
        return Sys.get_environ().h.get(s,None)

    @staticmethod
    def putEnv(s,v):
        python_lib_Os.putenv(s,v)
        Sys.get_environ().h[s] = v

    @staticmethod
    def environment():
        return Sys.get_environ()

    @staticmethod
    def sleep(seconds):
        python_lib_Time.sleep(seconds)

    @staticmethod
    def setTimeLocale(loc):
        return False

    @staticmethod
    def getCwd():
        return python_lib_Os.getcwd()

    @staticmethod
    def setCwd(s):
        python_lib_Os.chdir(s)

    @staticmethod
    def systemName():
        from haxe import haxe_Exception
        _g = python_lib_Sys.platform
        x = _g
        if x.startswith("linux"):
            return "Linux"
        else:
            _g1 = _g
            _hx_local_0 = len(_g1)
            if (_hx_local_0 == 5):
                if (_g1 == "win32"):
                    return "Windows"
                else:
                    raise haxe_Exception.thrown("not supported platform")
            elif (_hx_local_0 == 6):
                if (_g1 == "cygwin"):
                    return "Windows"
                elif (_g1 == "darwin"):
                    return "Mac"
                else:
                    raise haxe_Exception.thrown("not supported platform")
            else:
                raise haxe_Exception.thrown("not supported platform")

    @staticmethod
    def command(cmd,args = None):
        from python import python__KwArgs_KwArgs_Impl_
        if (args is None):
            return python_lib_Subprocess.call(cmd,**python__KwArgs_KwArgs_Impl_.fromT(_hx_AnonObject({'shell': True})))
        else:
            return python_lib_Subprocess.call(([cmd] + args))

    @staticmethod
    def cpuTime():
        return python_lib_Timeit.default_timer()

    @staticmethod
    def executablePath():
        from python import python_internal_ArrayImpl
        return python_internal_ArrayImpl._get(python_lib_Sys.argv, 0)

    @staticmethod
    def programPath():
        return Sys._programPath

    @staticmethod
    def getChar(echo):
        from haxe import haxe_Exception
        ch = None
        _g = Sys.systemName()
        _g1 = _g
        _hx_local_0 = len(_g1)
        if (_hx_local_0 == 5):
            if (_g1 == "Linux"):
                fd = python_lib_Sys.stdin.fileno()
                old = python_lib_Termios.tcgetattr(fd)
                fileNo = fd
                when = python_lib_Termios.TCSADRAIN
                settings = old
                def _hx_local_1():
                    python_lib_Termios.tcsetattr(fileNo,when,settings)
                restore = _hx_local_1
                try:
                    python_lib_Tty.setraw(fd)
                    x = python_lib_Sys.stdin.read(1)
                    restore()
                    ch = HxString.charCodeAt(x,0)
                except BaseException as _g1:
                    None
                    e = haxe_Exception.caught(_g1).unwrap()
                    restore()
                    raise haxe_Exception.thrown(e)
            else:
                x = _g
                raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        elif (_hx_local_0 == 3):
            if (_g1 == "Mac"):
                fd = python_lib_Sys.stdin.fileno()
                old = python_lib_Termios.tcgetattr(fd)
                fileNo = fd
                when = python_lib_Termios.TCSADRAIN
                settings = old
                def _hx_local_2():
                    python_lib_Termios.tcsetattr(fileNo,when,settings)
                restore = _hx_local_2
                try:
                    python_lib_Tty.setraw(fd)
                    x = python_lib_Sys.stdin.read(1)
                    restore()
                    ch = HxString.charCodeAt(x,0)
                except BaseException as _g1:
                    None
                    e = haxe_Exception.caught(_g1).unwrap()
                    restore()
                    raise haxe_Exception.thrown(e)
            else:
                x = _g
                raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        elif (_hx_local_0 == 7):
            if (_g1 == "Windows"):
                ch = HxString.charCodeAt(python_lib_Msvcrt.getwch(),0)
            else:
                x = _g
                raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        else:
            x = _g
            raise haxe_Exception.thrown((("platform " + ("null" if x is None else x)) + " not supported"))
        if echo:
            from python import python_Lib
            python_Lib.printString(Std.string("".join(map(chr,[ch]))))
        return ch

    @staticmethod
    def stdin():
        from python import python_io_IoTools
        return python_io_IoTools.createFileInputFromText(python_lib_Sys.stdin)

    @staticmethod
    def stdout():
        from python import python_io_IoTools
        return python_io_IoTools.createFileOutputFromText(python_lib_Sys.stdout)

    @staticmethod
    def stderr():
        from python import python_io_IoTools
        return python_io_IoTools.createFileOutputFromText(python_lib_Sys.stderr)
Sys._hx_class = Sys
globalClasses._hx_classes["Sys"] = Sys




class Type:
    _hx_class_name = "Type"
    __slots__ = ()
    _hx_statics = ["getClass", "getEnum", "getSuperClass", "getClassName", "getEnumName", "resolveClass", "resolveEnum", "createInstance", "createEmptyInstance", "createEnum", "createEnumIndex", "getInstanceFields", "getClassFields", "getEnumConstructs", "typeof", "asEnumImpl", "enumEq", "enumConstructor", "enumParameters", "enumIndex", "allEnums"]

    @staticmethod
    def getClass(o):
        if (o is None):
            return None
        o1 = o
        if ((o1 is not None) and ((HxOverrides.eq(o1,str) or python_lib_Inspect.isclass(o1)))):
            return None
        if isinstance(o,_hx_AnonObject):
            return None
        if hasattr(o,"_hx_class"):
            return o._hx_class
        if hasattr(o,"__class__"):
            return o.__class__
        else:
            return None

    @staticmethod
    def getEnum(o):
        if (o is None):
            return None
        return o.__class__

    @staticmethod
    def getSuperClass(c):
        from python import python_Boot
        return python_Boot.getSuperClass(c)

    @staticmethod
    def getClassName(c):
        if hasattr(c,"_hx_class_name"):
            return c._hx_class_name
        else:
            if (c == list):
                return "Array"
            if (c == Math):
                return "Math"
            if (c == str):
                return "String"
            try:
                return c.__name__
            except BaseException as _g:
                None
                return None

    @staticmethod
    def getEnumName(e):
        return e._hx_class_name

    @staticmethod
    def resolveClass(name):
        if (name == "Array"):
            return list
        if (name == "Math"):
            return Math
        if (name == "String"):
            return str
        cl = globalClasses._hx_classes.get(name,None)
        tmp = None
        if (cl is not None):
            o = cl
            tmp = (not (((o is not None) and ((HxOverrides.eq(o,str) or python_lib_Inspect.isclass(o))))))
        else:
            tmp = True
        if tmp:
            return None
        return cl

    @staticmethod
    def resolveEnum(name):
        if (name == "Bool"):
            return Bool
        o = Type.resolveClass(name)
        if hasattr(o,"_hx_constructs"):
            return o
        else:
            return None

    @staticmethod
    def createInstance(cl,args):
        return cl(*args)

    @staticmethod
    def createEmptyInstance(cl):
        i = cl.__new__(cl)
        callInit = None
        def _hx_local_0(cl):
            sc = Type.getSuperClass(cl)
            if (sc is not None):
                callInit(sc)
            if hasattr(cl,"_hx_empty_init"):
                cl._hx_empty_init(i)
        callInit = _hx_local_0
        callInit(cl)
        return i

    @staticmethod
    def createEnum(e,constr,params = None):
        from haxe import haxe_Exception
        f = Reflect.field(e,constr)
        if (f is None):
            raise haxe_Exception.thrown(("No such constructor " + ("null" if constr is None else constr)))
        if Reflect.isFunction(f):
            if (params is None):
                raise haxe_Exception.thrown((("Constructor " + ("null" if constr is None else constr)) + " need parameters"))
            return Reflect.callMethod(e,f,params)
        if ((params is not None) and ((len(params) != 0))):
            raise haxe_Exception.thrown((("Constructor " + ("null" if constr is None else constr)) + " does not need parameters"))
        return f

    @staticmethod
    def createEnumIndex(e,index,params = None):
        from python import python_internal_ArrayImpl
        from haxe import haxe_Exception
        c = python_internal_ArrayImpl._get(e._hx_constructs, index)
        if (c is None):
            raise haxe_Exception.thrown((Std.string(index) + " is not a valid enum constructor index"))
        return Type.createEnum(e,c,params)

    @staticmethod
    def getInstanceFields(c):
        from python import python_Boot
        return python_Boot.getInstanceFields(c)

    @staticmethod
    def getClassFields(c):
        from python import python_Boot
        return python_Boot.getClassFields(c)

    @staticmethod
    def getEnumConstructs(e):
        if hasattr(e,"_hx_constructs"):
            x = e._hx_constructs
            return list(x)
        else:
            return []

    @staticmethod
    def typeof(v):
        if (v is None):
            return ValueType.TNull
        elif isinstance(v,bool):
            return ValueType.TBool
        elif isinstance(v,int):
            return ValueType.TInt
        elif isinstance(v,float):
            return ValueType.TFloat
        elif isinstance(v,str):
            return ValueType.TClass(str)
        elif isinstance(v,list):
            return ValueType.TClass(list)
        elif (isinstance(v,_hx_AnonObject) or python_lib_Inspect.isclass(v)):
            return ValueType.TObject
        elif isinstance(v,Enum):
            return ValueType.TEnum(v.__class__)
        elif (isinstance(v,type) or hasattr(v,"_hx_class")):
            return ValueType.TClass(v.__class__)
        elif callable(v):
            return ValueType.TFunction
        else:
            return ValueType.TUnknown

    @staticmethod
    def asEnumImpl(x):
        return x

    @staticmethod
    def enumEq(a,b):
        if HxOverrides.eq(a,b):
            return True
        try:
            if ((b is None) and (not HxOverrides.eq(a,b))):
                return False
            if (a.tag != b.tag):
                return False
            p1 = a.params
            p2 = b.params
            if (len(p1) != len(p2)):
                return False
            _g = 0
            _g1 = len(p1)
            while (_g < _g1):
                i = _g
                _g = (_g + 1)
                if (not Type.enumEq(p1[i],p2[i])):
                    return False
            if (a._hx_class != b._hx_class):
                return False
        except BaseException as _g:
            None
            return False
        return True

    @staticmethod
    def enumConstructor(e):
        return e.tag

    @staticmethod
    def enumParameters(e):
        return list(e.params)

    @staticmethod
    def enumIndex(e):
        return e.index

    @staticmethod
    def allEnums(e):
        ctors = Type.getEnumConstructs(e)
        ret = []
        _g = 0
        while (_g < len(ctors)):
            ctor = (ctors[_g] if _g >= 0 and _g < len(ctors) else None)
            _g = (_g + 1)
            v = Reflect.field(e,ctor)
            if Std.isOfType(v,e):
                ret.append(v)
        return ret
Type._hx_class = Type
globalClasses._hx_classes["Type"] = Type


class ValueType(Enum):
    __slots__ = ()
    _hx_class_name = "ValueType"
    _hx_constructs = ["TNull", "TInt", "TFloat", "TBool", "TObject", "TFunction", "TClass", "TEnum", "TUnknown"]

    @staticmethod
    def TClass(c):
        return ValueType("TClass", 6, (c,))

    @staticmethod
    def TEnum(e):
        return ValueType("TEnum", 7, (e,))
ValueType.TNull = ValueType("TNull", 0, ())
ValueType.TInt = ValueType("TInt", 1, ())
ValueType.TFloat = ValueType("TFloat", 2, ())
ValueType.TBool = ValueType("TBool", 3, ())
ValueType.TObject = ValueType("TObject", 4, ())
ValueType.TFunction = ValueType("TFunction", 5, ())
ValueType.TUnknown = ValueType("TUnknown", 8, ())
ValueType._hx_class = ValueType
globalClasses._hx_classes["ValueType"] = ValueType


class Xml:
    _hx_class_name = "Xml"
    __slots__ = ("nodeType", "nodeName", "nodeValue", "parent", "children", "attributeMap")
    _hx_fields = ["nodeType", "nodeName", "nodeValue", "parent", "children", "attributeMap"]
    _hx_methods = ["get_nodeName", "set_nodeName", "get_nodeValue", "set_nodeValue", "get", "set", "remove", "exists", "attributes", "iterator", "elements", "elementsNamed", "firstChild", "firstElement", "addChild", "removeChild", "insertChild", "toString", "ensureElementType"]
    _hx_statics = ["Element", "PCData", "CData", "Comment", "DocType", "ProcessingInstruction", "Document", "parse", "createElement", "createPCData", "createCData", "createComment", "createDocType", "createProcessingInstruction", "createDocument"]

    def __init__(self,nodeType):
        from haxe import haxe_ds_StringMap
        self.parent = None
        self.nodeValue = None
        self.nodeName = None
        self.nodeType = nodeType
        self.children = []
        self.attributeMap = haxe_ds_StringMap()

    def get_nodeName(self):
        from haxe import haxe_Exception
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.nodeName

    def set_nodeName(self,v):
        from haxe import haxe_Exception
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        def _hx_local_1():
            def _hx_local_0():
                self.nodeName = v
                return self.nodeName
            return _hx_local_0()
        return _hx_local_1()

    def get_nodeValue(self):
        from haxe import haxe_Exception
        if ((self.nodeType == Xml.Document) or ((self.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.nodeValue

    def set_nodeValue(self,v):
        from haxe import haxe_Exception
        if ((self.nodeType == Xml.Document) or ((self.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        def _hx_local_1():
            def _hx_local_0():
                self.nodeValue = v
                return self.nodeValue
            return _hx_local_0()
        return _hx_local_1()

    def get(self,att):
        from haxe import haxe_Exception
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.attributeMap.h.get(att,None)

    def set(self,att,value):
        from haxe import haxe_Exception
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        self.attributeMap.h[att] = value

    def remove(self,att):
        from haxe import haxe_Exception
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        self.attributeMap.remove(att)

    def exists(self,att):
        from haxe import haxe_Exception
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return (att in self.attributeMap.h)

    def attributes(self):
        from haxe import haxe_Exception
        if (self.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return self.attributeMap.keys()

    def iterator(self):
        from haxe import haxe_Exception
        from haxe import haxe_iterators_ArrayIterator
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return haxe_iterators_ArrayIterator(self.children)

    def elements(self):
        from haxe import haxe_Exception
        from haxe import haxe_iterators_ArrayIterator
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        _g = []
        _g1 = 0
        _g2 = self.children
        while (_g1 < len(_g2)):
            child = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
            _g1 = (_g1 + 1)
            if (child.nodeType == Xml.Element):
                _g.append(child)
        ret = _g
        return haxe_iterators_ArrayIterator(ret)

    def elementsNamed(self,name):
        from haxe import haxe_Exception
        from haxe import haxe_iterators_ArrayIterator
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        _g = []
        _g1 = 0
        _g2 = self.children
        while (_g1 < len(_g2)):
            child = (_g2[_g1] if _g1 >= 0 and _g1 < len(_g2) else None)
            _g1 = (_g1 + 1)
            tmp = None
            if (child.nodeType == Xml.Element):
                if (child.nodeType != Xml.Element):
                    raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((child.nodeType is None)) else _Xml_XmlType_Impl_.toString(child.nodeType))))))
                tmp = (child.nodeName == name)
            else:
                tmp = False
            if tmp:
                _g.append(child)
        ret = _g
        return haxe_iterators_ArrayIterator(ret)

    def firstChild(self):
        from haxe import haxe_Exception
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        return (self.children[0] if 0 < len(self.children) else None)

    def firstElement(self):
        from haxe import haxe_Exception
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        _g = 0
        _g1 = self.children
        while (_g < len(_g1)):
            child = (_g1[_g] if _g >= 0 and _g < len(_g1) else None)
            _g = (_g + 1)
            if (child.nodeType == Xml.Element):
                return child
        return None

    def addChild(self,x):
        from haxe import haxe_Exception
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        if (x.parent is not None):
            x.parent.removeChild(x)
        _this = self.children
        _this.append(x)
        x.parent = self

    def removeChild(self,x):
        from python import python_internal_ArrayImpl
        from haxe import haxe_Exception
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        if python_internal_ArrayImpl.remove(self.children,x):
            x.parent = None
            return True
        return False

    def insertChild(self,x,pos):
        from python import python_internal_ArrayImpl
        from haxe import haxe_Exception
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))
        if (x.parent is not None):
            python_internal_ArrayImpl.remove(x.parent.children,x)
        self.children.insert(pos, x)
        x.parent = self

    def toString(self):
        from haxe import haxe_xml_Printer
        return haxe_xml_Printer.print(self)

    def ensureElementType(self):
        from haxe import haxe_Exception
        if ((self.nodeType != Xml.Document) and ((self.nodeType != Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, expected Element or Document but found " + HxOverrides.stringOrNull((("null" if ((self.nodeType is None)) else _Xml_XmlType_Impl_.toString(self.nodeType))))))

    @staticmethod
    def parse(_hx_str):
        from haxe import haxe_xml_Parser
        return haxe_xml_Parser.parse(_hx_str)

    @staticmethod
    def createElement(name):
        from haxe import haxe_Exception
        xml = Xml(Xml.Element)
        if (xml.nodeType != Xml.Element):
            raise haxe_Exception.thrown(("Bad node type, expected Element but found " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeName = name
        return xml

    @staticmethod
    def createPCData(data):
        from haxe import haxe_Exception
        xml = Xml(Xml.PCData)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createCData(data):
        from haxe import haxe_Exception
        xml = Xml(Xml.CData)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createComment(data):
        from haxe import haxe_Exception
        xml = Xml(Xml.Comment)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createDocType(data):
        from haxe import haxe_Exception
        xml = Xml(Xml.DocType)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createProcessingInstruction(data):
        from haxe import haxe_Exception
        xml = Xml(Xml.ProcessingInstruction)
        if ((xml.nodeType == Xml.Document) or ((xml.nodeType == Xml.Element))):
            raise haxe_Exception.thrown(("Bad node type, unexpected " + HxOverrides.stringOrNull((("null" if ((xml.nodeType is None)) else _Xml_XmlType_Impl_.toString(xml.nodeType))))))
        xml.nodeValue = data
        return xml

    @staticmethod
    def createDocument():
        return Xml(Xml.Document)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.nodeType = None
        _hx_o.parent = None
        _hx_o.children = None
        _hx_o.attributeMap = None
Xml._hx_class = Xml
globalClasses._hx_classes["Xml"] = Xml

class _EnumValue_EnumValue_Impl_:
    _hx_class_name = "_EnumValue.EnumValue_Impl_"
    __slots__ = ()
    _hx_statics = ["match"]

    @staticmethod
    def match(this1,pattern):
        return False
_EnumValue_EnumValue_Impl_._hx_class = _EnumValue_EnumValue_Impl_
globalClasses._hx_classes["_EnumValue.EnumValue_Impl_"] = _EnumValue_EnumValue_Impl_


class _Xml_XmlType_Impl_:
    _hx_class_name = "_Xml.XmlType_Impl_"
    __slots__ = ()
    _hx_statics = ["Element", "PCData", "CData", "Comment", "DocType", "ProcessingInstruction", "Document", "toString"]

    @staticmethod
    def toString(this1):
        _g = this1
        if (_g == 0):
            return "Element"
        elif (_g == 1):
            return "PCData"
        elif (_g == 2):
            return "CData"
        elif (_g == 3):
            return "Comment"
        elif (_g == 4):
            return "DocType"
        elif (_g == 5):
            return "ProcessingInstruction"
        elif (_g == 6):
            return "Document"
        else:
            pass
_Xml_XmlType_Impl_._hx_class = _Xml_XmlType_Impl_
globalClasses._hx_classes["_Xml.XmlType_Impl_"] = _Xml_XmlType_Impl_


class _hx_AnonObject:
    _hx_disable_getattr = False
    def __init__(self, fields):
        self.__dict__ = fields
    def __repr__(self):
        return repr(self.__dict__)
    def __contains__(self, item):
        return item in self.__dict__
    def __getitem__(self, item):
        return self.__dict__[item]
    def __getattr__(self, name):
        if (self._hx_disable_getattr):
            raise AttributeError('field does not exist')
        else:
            return None
    def _hx_hasattr(self,field):
        self._hx_disable_getattr = True
        try:
            getattr(self, field)
            self._hx_disable_getattr = False
            return True
        except AttributeError:
            self._hx_disable_getattr = False
            return False


class Class: pass

import sys 
import _hx_AnonObject as anon
anon.classesinmodule(sys.modules[__name__])


