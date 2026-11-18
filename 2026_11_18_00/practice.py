"""
Python 函式引數傳遞範例程式與練習題 (2026-11-18)
搭配講義：function_arguments.md
"""

print("=== 1. 位置引數 vs 關鍵字引數 ===")


def make_coffee(size, flavor):
    print(f"製作一杯 {size} 的 {flavor} 咖啡")


# 位置引數：依順序
make_coffee("大杯", "拿鐵")

# 關鍵字引數：指定名稱（順序可調換）
make_coffee(flavor="美式", size="中杯")

# 混合：位置在前，關鍵字在後
make_coffee("特大杯", flavor="摩卡")


print("\n=== 2. 符號 /（僅限位置引數 Positional-Only）===")


def calculate_area(width, height, /):
    return width * height


# 只能依位置傳入：
print(f"長方形面積 (10, 5): {calculate_area(10, 5)}")
# calculate_area(width=10, height=5)  # 這樣會拋出 TypeError！


print("\n=== 3. 符號 *（僅限關鍵字引數 Keyword-Only）===")


def create_user(username, *, is_admin=False, send_email=True):
    print(f"用戶: {username} | 管理員: {is_admin} | 發信: {send_email}")


create_user("alice", is_admin=True)
create_user("bob", send_email=False)
# create_user("charlie", True)  # 這樣會拋出 TypeError！


print("\n=== 4. 可變引數 *args 與 **kwargs ===")


def demo_args_kwargs(title, *args, **kwargs):
    print(f"標題: {title}")
    print(f"*args (Tuple): {args}")
    print(f"**kwargs (Dict): {kwargs}")


demo_args_kwargs("範例一", 1, 2, 3, mode="auto", debug=True)


print("\n=== 5. 解包技巧 (Unpacking) ===")


def add_three(a, b, c):
    return a + b + c


nums = [10, 20, 30]
print(f"串列解包加總: {add_three(*nums)}")

info = {"size": "中杯", "flavor": "燕麥拿鐵"}
make_coffee(**info)


print("\n" + "=" * 40)
print("【課堂練習區】")
print("=" * 40)

# ----------------------------------------------------
# 練習 1 解答驗證：
# 函式定義：def send_email(to, /, subject, *, urgent=False):
# 1. send_email("boss@test.com", "開會通知", urgent=True)    -> 合法 (to是位置, subject是位置, urgent是關鍵字)
# 2. send_email(to="boss@test.com", subject="開會通知")      -> 非法 (to在/左側，不能用關鍵字)
# 3. send_email("boss@test.com", subject="開會通知")         -> 合法 (subject可用關鍵字)
# 4. send_email("boss@test.com", "開會通知", True)           -> 非法 (urgent在*右側，必須用關鍵字)
# ----------------------------------------------------


# ----------------------------------------------------
# 練習 2：請實作 order_drink 函式
# 規格：
#   - item: 飲品名稱，僅限位置引數 (/)
#   - size: 容量，預設 "中杯"，可位置也可關鍵字
#   - sugar: 甜度，僅限關鍵字引數 (*)
#   - ice: 冰塊，僅限關鍵字引數 (*)
#   - **extra: 接收其他任意備註
# ----------------------------------------------------


def order_drink(item, /, size="中杯", *, sugar, ice, **extra):
    print(f"訂單：{size} {item}")
    print(f"甜度：{sugar}, 冰塊：{ice}")
    if extra:
        print(f"其他要求：{extra}")


print("\n[測試練習 2 成果]")
order_drink("珍珠奶茶", "大杯", sugar="微糖", ice="少冰", note="環保杯", bag=True)
order_drink("四季春", sugar="無糖", ice="去冰")

print("\n全數範例與實作已順利執行完成！")
