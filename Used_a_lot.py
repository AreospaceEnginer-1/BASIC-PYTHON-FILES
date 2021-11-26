def make_list(a_list, a_type = "str", num = False, stop = False, ask = "thing"):
    code = "a_list[var] = " + a_type + "(input(Give a \" + ask + \":\"))"
    var = 0
    if num:
        for_range(int(num), code = code)
    elif stop:
        ch = ""
        while ch != stop:
             eval(code)
             ch = input("Type " + str(stop) + " to continue:")
             a_list[var] =  + a_type + (input("Give a \" + ask + \":"))
    else:
       raise ValueError("Need to get num or stop")
    return a_list, var




             
             
