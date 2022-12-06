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
_hx_classes["haxe._Int64.Int64_Impl_"] = haxe__Int64_Int64_Impl_


