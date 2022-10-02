def sqr(n, d = 3):
    '''
        sqr(n, d = 3) function runs on python3 trying to be more human style
        and so overcoming sqrt() integer arithmetic limits. (math library function)
        The return root type may be int or string related to input one.
        
        It accepts 2 args (only the first mandatory). The first one is
        the number what it's root run on. The second arg specifies the
        exact digit number without rounding, required after the floating point
        and it's applied only if the first arg is string typed:
            sqr('2.0', d = 32)     root='1.41421356237309504880168872420969'   
                                        (1.4142135623730951 sqrt math module) 
                                        (1.4142135623730950488016887242097 win10 calc)
        
        1st arg integer numeric strings are allowed of any length (32,64,128,512,1024,2048 digits
        can be considered) and MUST BE SUFFIXED WITH .0 TO BE VALID:
            sqr('12345678901234567890123456789012.0', d = 32)     root='3513641828820144.25311122238169983374820460606471'
                                                                       (3513641828820144.0 sqrt math module) 
                                                                       (3513641828820144.2531112223816998 win10 calc)
        
        If your input is int:
            sqr(12345678901234567890123456789012, d = 32)
        you'll get only int result without decimals (d arg is disabled with int values also if it is specified):
            root=3513641828820144
        
        Trying input:
            sqr(12345678901234567890123456789012.0, d = 32)
        
        you'll get this error:
            ValueError: 'float', type not valid: 1.2345678901234567e+31    
            
        Success with:
            sqr('2.0001', 5)   root='1.41424' (string)
            sqr('0.0', 32)     root='0.0'     (string)
            sqr(0, 32)         root=0         (int)
            sqr('0.01')        root='0.100'   (perfect square string)
            sqr('625.0')       root='25.000'  (perfect square string)
            sqr(625, 32)       root=25        (int perfect square)
            sqr(+9, 32)        root=3         (int perfect square)
        
        Failure:
            sqr('1.357e-05', 5) ValueError: Floating number format not valid: 1.357e-05 (Scientific Notation)
            sqr(-4, 32)         ValueError: Negative number: -4
            sqr(0.0, 32)        ValueError: 'float', type not valid: 0.0
            sqr('+625.0', 32)   ValueError: Floating number format not valid: +625.0
    '''                                       
    d = abs(int(d))
    if type(n) == int: #only integer square root (not floating point)        
        if int(n) < 0:
            raise ValueError(F"Negative number: {n}")
    
        if n < 100: #square root between 0 and 9
            root = [0,1,1,1,2,2,2,2,2,3,
                    3,3,3,3,3,3,4,4,4,4,
                    4,4,4,4,4,5,5,5,5,5,
                    5,5,5,5,5,5,6,6,6,6,
                    6,6,6,6,6,6,6,6,6,7,
                    7,7,7,7,7,7,7,7,7,7,
                    7,7,7,7,8,8,8,8,8,8,
                    8,8,8,8,8,8,8,8,8,8,
                    8,9,9,9,9,9,9,9,9,9,
                    9,9,9,9,9,9,9,9,9,9]
            return root[n]
        
        ns = str(n)
        Lns = len(ns)
        Lroot = Lns+1 >> 1 #X2division
        L = 10**(Lroot-1) 
        H = 10**Lroot
        while L <= H:
            I = (L + H) // 2
            I2 = I*I
            if I2 == n or I2<n<(I+1)*(I+1): 
                return I        
            if I2 > n:
                H = I - 1
            else:
                L = I + 1

    if type(n) == str:
        #VALIDATION n
        nv = n.split('.')
        if len(nv) != 2 or not (nv[0].isnumeric() and nv[1].isnumeric()):
            raise ValueError(F"Floating number format not valid: {n}")    
               
        n0 = nv[0]; L_n0 = len(n0)         
        n1 = nv[1]; L_n1 = len(n1)         
        
        if L_n0 > 1:
            n0 = n0.lstrip('0')
            if not len(n0): #if zero
                n0 = '0'
        if L_n1 > 1:
            n1 = n1.rstrip('0')
            if not len(n1): #if zero
                n1 = '0'
        
        # 0.0
        if n0 + '.' + n1 == '0.0':
            return '0.0'

        L_rx = len(str(n0))+1 >> 1 #X2Division - root digit length                       
        L_n1 = len(n1) #floating digit number 
        
        if n0 == '0': # 0 < n < 1
            shift = L_n1+1 >> 1 #X2Division - decimal point position
            ds = d - shift
            if L_n1 % 2: #odd (dispari):
                op = n1 + '0' + ds*'00'
            else:        #even (pari)
                op = n1       + ds*'00'
            r1 = str(sqr(int(op), 0))
            r1_len = len(r1)
            if ds > 0:
                return '0.' + (shift-r1_len+ds)*'0' + r1
            return '0.' + ((shift-r1_len)*'0' + r1)[0:d]
        elif n1 == '0':
            root = str(sqr(int(n0 + d* '00'), 0))
            return root[0:L_rx] + '.' + root[L_rx:]
        else:
            if L_n1 % 2: #odd (dispari)
                temp = str(sqr(int(n0 + n1 + '0' + (d-1)*'00'), 0))
                return temp[0:L_rx] + '.' + temp[L_rx:L_rx+d]
            else:        #even (pari)
                temp = str(sqr(int(n0 + n1 + (d-1)*'00'), 0))
                return temp[0:L_rx] + '.' + temp[L_rx:L_rx+d]
        
    if type(n) == float:
        raise ValueError(F"'float', type not valid: {n}")
    else:
        raise ValueError(F"Type not valid: {n}")
