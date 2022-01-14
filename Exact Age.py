from datetime import date

today = date.today()

cyy, cmm, cdd = today.year, today.month, today.day

user_input = input("What is your birth date? (2020-12-31):")
dd = int(user_input[8:10])
mm = int(user_input[5:7])
yy = int(user_input[:4])
if cmm < mm:
    fyy = cyy - yy -1
    fmm = 12 - mm +1
else:
    fyy = cyy - yy
    fmm = 12 - mm
if cdd < dd:
    fdd = 30 - dd
else:
    fdd = cdd - dd
print("You are {} year(s), {} month(s) and {} day(s) old.".format(fyy, fmm, fdd))