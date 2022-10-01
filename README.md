# sqrt
Square root any precision

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
