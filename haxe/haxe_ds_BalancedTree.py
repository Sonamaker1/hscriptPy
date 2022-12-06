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
_hx_classes["haxe.ds.BalancedTree"] = haxe_ds_BalancedTree


