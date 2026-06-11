def printt(n):
    """
    Print integers from n up to (but not including) 6, using recursion.

    The function calls itself with n + 1: each call prints one number, then
    hands the next number to a fresh call of itself.

    Base case (the stop condition): when n reaches 6, the `return` runs
    *before* print() and *before* the recursive call, so that deepest call
    prints nothing and simply ends. This is what breaks the chain -- without
    it the function would recurse forever and raise RecursionError. The
    return does NOT call printt(n + 1); it ends that one call right away.

    Execution trace for printt(1)
    ------------------------------
    Read top to bottom. Indenting RIGHT = going deeper (a call). Indenting
    LEFT = a return landing back in the call one level above it.

        printt(1)              -> print 1, then call deeper
            printt(2)          -> print 2, then call deeper
                printt(3)      -> print 3, then call deeper
                    printt(4)  -> print 4, then call deeper
                        printt(5)      -> print 5, then call deeper
                            printt(6)  -> n == 6: RETURN  (no print)
                        back in printt(5): nothing left after the call -> return
                    back in printt(4): nothing left -> return
                back in printt(3): nothing left -> return
            back in printt(2): nothing left -> return
        back in printt(1): nothing left -> return  (done, back to call site)

    So when the return fires inside printt(6), control lands back inside
    printt(5) -- at the point right after its `printt(6)` call. Because that
    recursive call is the LAST statement, there's nothing left to do, so
    printt(5) returns too, landing in printt(4), and so on, one level at a
    time, all the way back to the original printt(1) call.

    Nothing prints on the way back up; all the printing happened going down.

    Printed output:  1  2  3  4  5
    (6 is never printed -- the base case returns before printing it.)

    Tip: if you moved print(n) to *after* printt(n + 1), the numbers would
    print on the way back up instead, in reverse: 5 4 3 2 1.
    """
    if n == 6:
        return
    print(n)
    printt(n + 1)