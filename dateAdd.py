def date_prop(date):
    interval = 3
    yr = int(date[0])
    mo = int(date[1])
    da = int(date[2])
    ho = int(date[3])
    mi = int(date[4])
    se = int(date[5])

    new_yr = yr
    new_mo = mo
    new_da = da
    new_ho = ho
    new_mi = mi
    new_se = se + interval
    
    if new_se>59:
        new_se = new_se - 60
        new_mi = mi + 1
        if new_mi>59:
            new_mi = 0
            new_ho= ho + 1
            if new_ho>23:
                new_da = da + 1
                new_ho = 0
                if (mo==1 or mo==3 or mo==5 or mo==7 or mo==8 or mo==10 or mo==12) and (new_da>31):
                    new_da = 1
                    new_mo=mo+1
                    if new_mo>12:
                        new_mo=1
                        new_yr=yr+1
                    else:
                        pass
                elif (mo==1 or mo==4 or mo==6 or mo==9 or mo==11) and (new_da>30):
                    new_da = 1
                    new_mo=mo+1
                    if new_mo>12:
                        new_mo=1
                        new_yr=yr+1
                    else:
                        pass
                elif (mo==2) and new_da>28:
                    new_da = 1
                    new_mo=mo+1
                    if new_mo>12:
                        new_mo=1
                        new_yr=yr+1
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass

    return new_yr, new_mo, new_da, new_ho, new_mi, new_se
