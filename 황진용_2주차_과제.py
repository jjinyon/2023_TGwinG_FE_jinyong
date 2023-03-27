#1
def sum(a,b):
    return a+b
#ex) print(sum(a,b)

#2
def sub(a,b):
    return a-b
#ex) print(sub(a,b))

#3
def mul(a,b):
    return a*b
#ex) print(a,b)

#4
def div(a,b):
    return a/b
#ex) print(div(a,b))

#5
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)
#ex) print(distance(1,1,4,5))

#6
def title():
    lylics = "Switch sides and I'm beside you."
    return lylics[21:31]
#ex) print(title())

#7
def reverseStr(string):
    return string[::-1]
#ex) print(reverseStr("hello"))

#8
def introduce():
    return "제 이름은 {이름} 입니다. 취미는 {취미} 입니다. 저는 {재학중인학교}를 다니고 있습니다. 제 생일은 {yyddmm} 입니다.".format(이름 = input("이름을 입력하세요 : "),취미 = input("취미를 입력하세요 : "),재학중인학교 = input("재학 중인 학교를 입력하세요 : "),yyddmm = input("생일을 입력하세요 화: "))
print(introduce())

#9
def calc():
    a ,b=int(input("첫 번째 수를 입력하세요 : ")), int(input("두 번째 수를 입력하세요 : "))
    print(f"두 수의 합 : {a+b}\n두 수의 차 : {a-b}\n두 수의 곱 : {a*b}\n두 수의 몫 : {a//b}")
    return
