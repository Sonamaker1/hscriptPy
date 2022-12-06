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
_hx_classes["haxe.Int64Helper"] = haxe_Int64Helper


