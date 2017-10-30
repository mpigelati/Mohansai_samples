def out_fun(msg):
    def inn_fun():
        print(msg)
    return inn_fun()

hi_fun =out_fun("hi")
by_fun=out_fun("bye")

hi_fun()
by_fun()

