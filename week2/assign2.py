def func1(name):
    # your code here
    def distance(p1,p2): #計算距離
        (x1,y1,z1) = p1 
        (x2,y2,z2) = p2
        distance = abs(x1-x2)+abs(y1-y2) #abs 絕對值
        if z1!=z2:
            distance+=2 #如果不在線的同一測 就+2
        return distance

    悟空 = (0,0,0) #(X,Y,Z)
    特南克斯 = (1,-2,0)
    辛巴 = (-3,3,0)
    貝吉塔 = (-4,-1,0)
    丁滿 = (-1,4,1) 
    弗利沙 = (4,-1,1)

    points = {
        "悟空" : 悟空,
        "特南克斯" : 特南克斯,
        "辛巴" : 辛巴,
        "貝吉塔" : 貝吉塔,
        "丁滿" : 丁滿,
        "弗利沙" : 弗利沙,
    }
    
    target = points[name] #找到目標的name 存進targer中
    results = [] 
    for other_name, other_pt in points.items():
        if other_name == name: #如果name相同就直接跳過
            continue
        d = distance(target, other_pt) #比較 target 和 其他point的距離 存進d
        results.append((other_name, d)) #把 其他的name和 剛剛的d append進results
    
    results.sort(key=lambda x: x[1]) #由小排至大
    min_distance = results[0][1] #最小值存入 min_distance
    max_distance = results[-1][1] #最大值存入 max_distance

    nearest = [] #計算同樣近的
    for n , d in results:
        if d == min_distance:
            nearest.append(n)
    farthest = [] #計算同樣遠的
    for n , d in results:
        if d == max_distance:
            farthest.append(n)
    print("最遠的是：", "、".join(farthest), "；最近的是：", "、".join(nearest))

print("=== Task 1 ===")
func1("辛巴")  # print 最遠弗利沙；最近丁滿、貝吉塔
func1("悟空")  # print 最遠丁滿、弗利沙；最近特南克斯
func1("弗利沙")  # print 最遠辛巴；最近特南克斯
func1("特南克斯")  # print 最遠丁滿；最近悟空

# your code here, maybe
def func2(ss, start, end, criteria):
# your code here
    if not hasattr(func2, "bookings"): 
        func2.bookings = {s["name"]: [] for s in ss} # 幫每個服務建立一個空的list，用來記錄未來的預約時段

    field = op = raw_value = " " #預設 field , op , raw_value都沒有值
    if ">=" in criteria: #撿查 criteria中 有沒有>=
        field, raw_value = criteria.split(">=") #如果有的話，就切開左邊給field 右邊給raw_value
        # c>=800 會把 c 給 field ， 800給raw_value
        op = ">=" #把>=存入op
    elif "<=" in criteria:
        field, raw_value = criteria.split("<=")
        op = "<="
    elif "=" in criteria:
        field, raw_value = criteria.split("=")
        op = "="
    else:
        print("Sorry"); return #如果都沒有就回傳Sorry

    def is_available(ss_name):
        #從booking的list中看時段是否可預約
        for a, b in func2.bookings.get(ss_name, []): 
            #己預約的開始時間是 a 結束時間是 b
            if not (end <= a or start >= b): 
                #如果新的結束end在 舊的 a (開始時間) 之前 或 新的start在 舊的 b (結束時間) 之後
                #就會衝突，回傳False (不可預約)
                return False
        return True #如果end在a之後 或 start在b之前 就回傳True

    candidates = []

    if field == "name":  #如果field存入的是name的情況
        for s in ss:
            if s["name"] == raw_value and is_available(s["name"]): #如果輸入的name是可預約的 就append進去
                candidates.append(s)
    else: #如果今天不是 name 的情況
        val = float(raw_value) #把 raw_value 字串 轉成 浮點數

        for s in ss:
            fv = float(s[field]) #把field 轉成 浮點數
            ok = (op == ">=" and fv >= val) or (op == "<=" and fv <= val) 
            #看使用者輸入的是 >=，如果是>= 就比較 服務者是否有>= 
            #或使用者輸入的是 <= 就比較 服務者是否有<=
            if ok and is_available(s["name"]): #如果有符合 且 在is_available中可以被預約 就append進去
                candidates.append(s)

    if op == ">=": #如果 op是 >= 的情況 
        candidates.sort(key=lambda s: ((s[field]), s["name"])) 
        #把 candidates 排序 field,name 按field最小到最大， 如果相同的話用name去排
    else: #如果 op是 <= 的情況 就相反過來看
        candidates.sort(key=lambda s: (-(s[field]), s["name"]))

    if candidates: #如果在candidates中有符合條件的話就
        chosen = candidates[0] #找出最符合條件的服務者
        func2.bookings[chosen["name"]].append((start, end)) #把這一次chosen到的服務者的start 和 end 紀錄到booking中
        print(chosen["name"])
    else:
        print("Sorry")


services=[
{"name":"S1", "r":4.5, "c":1000},
{"name":"S2", "r":3, "c":1200},
{"name":"S3", "r":3.8, "c":800}
]
print("=== Task 2 ===")
func2(services, 15, 17, "c>=800") # S3
func2(services, 11, 13, "r<=4") # S3
func2(services, 10, 12, "name=S3") # Sorry
func2(services, 15, 18, "r>=4.5") # S1
func2(services, 16, 18, "r>=4") # Sorry
func2(services, 13, 17, "name=S1") # Sorry
func2(services, 8, 9, "c<=1500") # S2

def func3(index):
    # your code here
    num = (23) #初始值
    sequence = (-2,-3,1,2) #數列的變化
    for i in range(index-1): # 第一次是初始值 不用計算變化 所以只跑 index-1 次
        result = sequence [(i+1) % len(sequence)]# 從序列中取下一個變化值 用取餘數的方法 循環回開頭 
        num = num + result
    print(num)

print("=== Task 3 ===")
func3(1)   # print 23
func3(5)   # print 21
func3(10)  # print 16
func3(30)  # print 6


def func4(sp, stat, n):
    # your code here
    #1.先從stat中 找出可以使用的車廂
    #2.使用for迴圈 比對在 "sp"中 >= n 的數字 然後取最小 print出來
    #3.如果沒有 就找比n小的數字中最大的 然後print出來
    usable = [i for i in range(len(sp)) if stat[i] == '0']
    enough = [i for i in usable if sp[i] >= n]

    if enough: 
        min_i = min(enough, key=lambda i: sp[i])
        print(min_i)
    else:
        less = [i for i in usable if sp[i] < n]
        max_i = max(less, key=lambda i: sp[i])
        print(max_i)

print("=== Task 4 ===")
func4([3, 1, 5, 4, 3, 2], "101000", 2)  # print 5
func4([1, 0, 5, 1, 3],     "10100",  4)  # print 4
func4([4, 6, 5, 8],        "1000",   4)  # print 2