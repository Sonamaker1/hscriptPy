class hscript_ModuleDecl(Enum):
    __slots__ = ()
    _hx_class_name = "hscript.ModuleDecl"
    _hx_constructs = ["DPackage", "DImport", "DClass", "DTypedef"]

    @staticmethod
    def DPackage(path):
        return hscript_ModuleDecl("DPackage", 0, (path,))

    @staticmethod
    def DImport(path,everything = None):
        return hscript_ModuleDecl("DImport", 1, (path,everything))

    @staticmethod
    def DClass(c):
        return hscript_ModuleDecl("DClass", 2, (c,))

    @staticmethod
    def DTypedef(c):
        return hscript_ModuleDecl("DTypedef", 3, (c,))
hscript_ModuleDecl._hx_class = hscript_ModuleDecl
_hx_classes["hscript.ModuleDecl"] = hscript_ModuleDecl

