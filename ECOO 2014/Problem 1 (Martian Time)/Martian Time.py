for i in range(10):
    d, h, m = map(int, raw_input().split())
    d -= 1
    etm = d*24*60*60 + h*60*60 + m*60
    mtm = etm / (88642.663/86400)
    #print mtm, etm
    md = (mtm - (mtm%(24*60*60)))/(24*60*60) + 1

    mh = mtm - md*24*60*60
    mh = (mh - mh%(60**2))/(60**2)
    mh = int(mh%24)

    mm = mtm - md*24*60*60 - (mh)*60*60
    mm = (mm - mm%(60))/(60)
    mm = int(mm%60)


    mh = "0"*(2-len(str(mh))) + str(mh)
    mm = "0"*(2-len(str(mm))) + str(mm)

    print "Day {}, {}:{}".format(int(md), str(mh), str(mm))
