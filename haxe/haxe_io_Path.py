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
_hx_classes["haxe.io.Path"] = haxe_io_Path


