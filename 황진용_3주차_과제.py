# 1번
def grade(score):
    score="j"
    if a>=90:
        score="A"
    elif a>=80:
        score="B"
    elif a>=70:
        score="C"
    elif a>=60:
        score="D"
    else:
        score="F"
    return score


# 2번
def quadrant(x, y):
    if x>0:
        if y>0:
            b=1
        else:
            b=4
    else:
        if y>0:
            b=2
        else:
            b=3
    return f"제 {b}사분면"

# 3번
def leapYear(year):
    if year%4 == 0:
        if year%100 == 0 and year%400 != 0 :
            a="평년"
        else:
            a="윤년"
    else:
        a="평년"
    return a

# 4번
def dice(a, b, c):
    상금 = 0
    if a==b==c:
        상금 = 10000 + a*1000
    elif a==b:
        상금 = 1000 + a*100
    elif a==c:
        상금 = 1000 + a*100
    elif b==c:
        상금 = 1000 + b*100
    else:
        d = max(a,b,c)
        상금 = d*100 
    return 상금

# 5번
def alarm(time):
    b=str(time)
    if time>45:
        if int(b[len(b)-2:])>=45:
            c = time-45
        else:
            c = time-85
    else:
        c = 2315+time
    d = str(c)
    if c<10:
        d = "0 "+d
    elif c>=10 and c<100:
        d = "00" + d
    return f"{d[:len(d)-2]}시 {d[len(d)-2:]}분"