
from _hx_AnonObject import _hx_AnonObject
import globalClasses

from classes_hscript import Date, Sys 

import math as Math
from os import path as python_lib_os_Path
import os as python_lib_Os
from haxe import haxe_io_Input, haxe_io_Output

class sys_FileSystem:
    _hx_class_name = "sys.FileSystem"
    __slots__ = ()
    _hx_statics = ["exists", "stat", "rename", "fullPath", "absolutePath", "isDirectory", "createDirectory", "deleteFile", "deleteDirectory", "readDirectory"]

    @staticmethod
    def exists(path):
        return python_lib_os_Path.exists(path)

    @staticmethod
    def stat(path):
        s = python_lib_Os.stat(path)
        return _hx_AnonObject({'gid': s.st_gid, 'uid': s.st_uid, 'atime': Date.fromTime((1000 * s.st_atime)), 'mtime': Date.fromTime((1000 * s.st_mtime)), 'ctime': Date.fromTime((1000 * s.st_ctime)), 'size': s.st_size, 'dev': s.st_dev, 'ino': s.st_ino, 'nlink': s.st_nlink, 'rdev': getattr(s,"st_rdev",0), 'mode': s.st_mode})

    @staticmethod
    def rename(path,newPath):
        python_lib_Os.rename(path,newPath)

    @staticmethod
    def fullPath(relPath):
        return python_lib_os_Path.realpath(relPath)

    @staticmethod
    def absolutePath(relPath):
        from haxe import haxe_io_Path
        if haxe_io_Path.isAbsolute(relPath):
            return relPath
        return haxe_io_Path.join([Sys.getCwd(), relPath])

    @staticmethod
    def isDirectory(path):
        return python_lib_os_Path.isdir(path)

    @staticmethod
    def createDirectory(path):
        python_lib_Os.makedirs(path,511,True)

    @staticmethod
    def deleteFile(path):
        python_lib_Os.remove(path)

    @staticmethod
    def deleteDirectory(path):
        python_lib_Os.rmdir(path)

    @staticmethod
    def readDirectory(path):
        return python_lib_Os.listdir(path)
sys_FileSystem._hx_class = sys_FileSystem
globalClasses._hx_classes["sys.FileSystem"] = sys_FileSystem


class sys_io_FileInput(haxe_io_Input):
    _hx_class_name = "sys.io.FileInput"
    __slots__ = ("impl",)
    _hx_fields = ["impl"]
    _hx_methods = ["set_bigEndian", "seek", "tell", "eof", "readByte", "readBytes", "close", "readAll", "readFullBytes", "read", "readUntil", "readLine", "readFloat", "readDouble", "readInt8", "readInt16", "readUInt16", "readInt24", "readUInt24", "readInt32", "readString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Input


    def __init__(self,impl):
        self.impl = impl

    def set_bigEndian(self,b):
        return self.impl.set_bigEndian(b)

    def seek(self,p,pos):
        self.impl.seek(p,pos)

    def tell(self):
        return self.impl.tell()

    def eof(self):
        return self.impl.eof()

    def readByte(self):
        return self.impl.readByte()

    def readBytes(self,s,pos,_hx_len):
        return self.impl.readBytes(s,pos,_hx_len)

    def close(self):
        self.impl.close()

    def readAll(self,bufsize = None):
        return self.impl.readAll(bufsize)

    def readFullBytes(self,s,pos,_hx_len):
        self.impl.readFullBytes(s,pos,_hx_len)

    def read(self,nbytes):
        return self.impl.read(nbytes)

    def readUntil(self,end):
        return self.impl.readUntil(end)

    def readLine(self):
        return self.impl.readLine()

    def readFloat(self):
        return self.impl.readFloat()

    def readDouble(self):
        return self.impl.readDouble()

    def readInt8(self):
        return self.impl.readInt8()

    def readInt16(self):
        return self.impl.readInt16()

    def readUInt16(self):
        return self.impl.readUInt16()

    def readInt24(self):
        return self.impl.readInt24()

    def readUInt24(self):
        return self.impl.readUInt24()

    def readInt32(self):
        return self.impl.readInt32()

    def readString(self,_hx_len,encoding = None):
        return self.impl.readString(_hx_len)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.impl = None
sys_io_FileInput._hx_class = sys_io_FileInput
globalClasses._hx_classes["sys.io.FileInput"] = sys_io_FileInput


class sys_io_FileOutput(haxe_io_Output):
    _hx_class_name = "sys.io.FileOutput"
    __slots__ = ("impl",)
    _hx_fields = ["impl"]
    _hx_methods = ["seek", "tell", "set_bigEndian", "writeByte", "writeBytes", "flush", "close", "write", "writeFullBytes", "writeFloat", "writeDouble", "writeInt8", "writeInt16", "writeUInt16", "writeInt24", "writeUInt24", "writeInt32", "prepare", "writeInput", "writeString"]
    _hx_statics = []
    _hx_interfaces = []
    _hx_super = haxe_io_Output


    def __init__(self,impl):
        self.impl = impl

    def seek(self,p,pos):
        self.impl.seek(p,pos)

    def tell(self):
        return self.impl.tell()

    def set_bigEndian(self,b):
        return self.impl.set_bigEndian(b)

    def writeByte(self,c):
        self.impl.writeByte(c)

    def writeBytes(self,s,pos,_hx_len):
        return self.impl.writeBytes(s,pos,_hx_len)

    def flush(self):
        self.impl.flush()

    def close(self):
        self.impl.close()

    def write(self,s):
        self.impl.write(s)

    def writeFullBytes(self,s,pos,_hx_len):
        self.impl.writeFullBytes(s,pos,_hx_len)

    def writeFloat(self,x):
        self.impl.writeFloat(x)

    def writeDouble(self,x):
        self.impl.writeDouble(x)

    def writeInt8(self,x):
        self.impl.writeInt8(x)

    def writeInt16(self,x):
        self.impl.writeInt16(x)

    def writeUInt16(self,x):
        self.impl.writeUInt16(x)

    def writeInt24(self,x):
        self.impl.writeInt24(x)

    def writeUInt24(self,x):
        self.impl.writeUInt24(x)

    def writeInt32(self,x):
        self.impl.writeInt32(x)

    def prepare(self,nbytes):
        self.impl.prepare(nbytes)

    def writeInput(self,i,bufsize = None):
        self.impl.writeInput(i,bufsize)

    def writeString(self,s,encoding = None):
        self.impl.writeString(s)

    @staticmethod
    def _hx_empty_init(_hx_o):
        _hx_o.impl = None
sys_io_FileOutput._hx_class = sys_io_FileOutput
globalClasses._hx_classes["sys.io.FileOutput"] = sys_io_FileOutput

