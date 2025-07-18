while True:
    try:
        if int(input()) > 0:
            rsp = "vai ter duas!"
        else:
            rsp = "vai ter copa!"
        print(rsp)
    except EOFError:
        break