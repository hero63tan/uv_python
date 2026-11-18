# Python 函式呼叫與引數傳遞完全指南

在 Python 中，定義函式與呼叫函式是寫程式的核心能力。而「**如何將資料正確傳遞給函式**」往往是初學者最容易混淆的部分。

本講義將帶你循序漸進掌握引數（Arguments）的傳遞方式，以及 Python 3 中常見的特殊符號：`/`、`*`、`*args` 與 `**kwargs`。

---

## 目錄
1. [觀念釐清：參數（Parameter） vs. 引數（Argument）](#1-觀念釐清參數-parameter-vs-引數-argument)
2. [基本呼叫方式：位置引數與關鍵字引數](#2-基本呼叫方式位置引數與關鍵字引數)
3. [預設值引數（Default Arguments）](#3-預設值引數default-arguments)
4. [限定引數符號：`/` 與 `*`](#4-限定引數符號--與-)
5. [可變長度引數：`*args` 與 `**kwargs`](#5-可變長度引數-args-與-kwargs)
6. [呼叫時的星號解包（Argument Unpacking）](#6-呼叫時的星號解包argument-unpacking)
7. [語法全貌速查地圖](#7-語法全貌速查地圖)
8. [新手常見錯誤排行榜（常見報錯與解法）](#8-新手常見錯誤排行榜常見報錯與解法)
9. [隨堂動手實作練習](#9-隨堂動手實作練習)

---

## 1. 觀念釐清：參數（Parameter） vs. 引數（Argument）

很多時候這兩個名詞會被混用，但在觀念上它們是有區別的：

- **參數（Parameter）**：定義函式時，放在括號內用來接收資料的變數名稱（佔位符）。
- **引數（Argument）**：呼叫函式時，實際傳進去的值或物件。

```python
# 這裡的 name 和 age 是「參數 (Parameters)」
def introduce(name, age):
    print(f"大家好，我是 {name}，今年 {age} 歲。")

# 這裡的 "小明" 和 18 是「引數 (Arguments)」
introduce("小明", 18)
```

---

## 2. 基本呼叫方式：位置引數與關鍵字引數

傳入引數給函式時，主要有兩種方式：

### 2.1 位置引數（Positional Arguments）
依照**定義時的先後順序**，一對一將引數填入參數。

```python
def make_coffee(size, flavor):
    print(f"製作一杯 {size} 的 {flavor} 咖啡")

# 呼叫方式：依位置對應
make_coffee("大杯", "拿鐵")   # size="大杯", flavor="拿鐵"
make_coffee("拿鐵", "大杯")   # 順序顛倒會導致語意錯誤！
```

### 2.2 關鍵字引數（Keyword Arguments）
呼叫時明確指出**參數名稱與值（`參數名=值`）**，此時順序可以調換。

```python
# 呼叫方式：指定名稱，順序不同也沒關係
make_coffee(flavor="拿鐵", size="大杯")
make_coffee(size="中杯", flavor="美式")
```

### 2.3 混合使用時的黃金鐵則
> [!IMPORTANT]
> **位置引數永遠必須在關鍵字引數之前！**

```python
# 正確：先位置，後關鍵字
make_coffee("大杯", flavor="卡布奇諾")

# 錯誤：關鍵字後面不能再放位置引數！
# make_coffee(size="大杯", "卡布奇諾") 
# -> SyntaxError: positional argument follows keyword argument
```

---

## 3. 預設值引數（Default Arguments）

可以在定義函式時賦予參數「預設值」。呼叫時若未提供，則使用預設值。

```python
def greet(name, msg="早安"):
    print(f"{name}，{msg}！")

greet("小華")             # 使用預設值 -> 小華，早安！
greet("小華", "晚安")      # 覆蓋預設值 -> 小華，晚安！
greet("小華", msg="你好")  # 用關鍵字覆蓋 -> 小華，你好！
```

> [!WARNING]
> 定義函式時，**沒有預設值的參數**必須排在**有預設值的參數**前面：
> ```python
> # 錯誤寫法：
> def bad_func(msg="早安", name): ... # SyntaxError
> ```

---

## 4. 限定引數符號：`/` 與 `*`

Python 提供兩個特別的符號，用來強制規範呼叫者「只能用某種方式」傳遞引數。

### 4.1 `/` 符號：僅限位置引數（Positional-Only）
- **規則**：出現在 `/` **左側**的所有參數，呼叫時**只能用位置引數**傳入，不能使用 `參數名=值` 的關鍵字傳入。
- **適用場景**：參數名稱無特別語意、內建函式常用（如 `abs()`、`len()`）。

```python
def calculate_area(width, height, /):
    return width * height

# 正確呼叫：
print(calculate_area(10, 5))

# 錯誤呼叫：使用了關鍵字名稱
# calculate_area(width=10, height=5)
# -> TypeError: calculate_area() got some positional-only arguments passed as keyword arguments: 'width, height'
```

---

### 4.2 `*` 符號：僅限關鍵字引數（Keyword-Only）
- **規則**：出現在獨立的 `*` **右側**的所有參數，呼叫時**必須使用關鍵字引數**傳入，不接受單純依位置傳入。
- **適用場景**：避免呼叫時一堆布林值或數值讓人看不懂（例如 `open_window(True, False, 10)` 可讀性差，改用關鍵字限定更清晰）。

```python
def create_user(username, *, is_admin=False, send_email=True):
    print(f"建立用戶: {username}, 管理員: {is_admin}, 發信: {send_email}")

# 正確呼叫：* 右側必須帶參數名稱
create_user("alice", is_admin=True)
create_user("bob", send_email=False)

# 錯誤呼叫：不能依位置傳遞
# create_user("charlie", True, False)
# -> TypeError: create_user() takes 1 positional argument but 3 were given
```

---

### 4.3 組合使用：`/` 與 `*` 同時出現

```python
def configure(mode, /, timeout, *, verbose=False):
    print(f"模式: {mode}, 超時: {timeout}, 詳細日誌: {verbose}")

# 呼叫分析：
# 1. mode    : 只能用位置引數
# 2. timeout : 自由（位置引數或關鍵字引數皆可）
# 3. verbose : 只能用關鍵字引數

configure("fast", 30, verbose=True)           # 正確
configure("fast", timeout=30, verbose=False)  # 正確
```

---

## 5. 可變長度引數：`*args` 與 `**kwargs`

當你無法預先知道使用者會傳入多少個引數時，可使用星號收集參數。

### 5.1 `*args`：收集多餘的位置引數（打包成 Tuple）
- 參數名稱前的單星號 `*` 會把傳入的多餘位置引數打包成一個 **Tuple**（常命名為 `args`）。

```python
def sum_all(*numbers):
    print(f"接收到的型態: {type(numbers)}, 內容: {numbers}")
    return sum(numbers)

print(sum_all(1, 2, 3))        # 輸出: 6 (numbers 為 (1, 2, 3))
print(sum_all(10, 20, 30, 40)) # 輸出: 100
print(sum_all())               # 輸出: 0 (沒傳入時為空 tuple ())
```

---

### 5.2 `**kwargs`：收集多餘的關鍵字引數（打包成 Dictionary）
- 參數名稱前的雙星號 `**` 會把傳入的多餘關鍵字引數打包成一個 **Dictionary**（常命名為 `kwargs`，意即 Keyword Arguments）。

```python
def print_student_info(name, **details):
    print(f"學生: {name}")
    print(f"詳細資料型態: {type(details)}, 內容: {details}")
    for key, value in details.items():
        print(f" - {key}: {value}")

print_student_info("小明", age=16, city="台北", hobby="吉他")
```

---

## 6. 呼叫時的星號解包（Argument Unpacking）

星號除了用在「函式定義」中收集資料，也常用在「**呼叫函式時**」將容器（串列、字典）解包（拆開）成一個個獨立的引數。

### 6.1 `*` 解包串列 / 元組為位置引數
```python
def add(a, b, c):
    return a + b + c

my_numbers = [10, 20, 30]

# 一般呼叫：需要手動寫索引 add(my_numbers[0], my_numbers[1], my_numbers[2])
# 使用 * 解包：
result = add(*my_numbers)  # 等同於 add(10, 20, 30)
print(result)              # 60
```

### 6.2 `**` 解包字典為關鍵字引數
```python
def make_profile(name, job, country):
    return f"{name} 是住在 {country} 的 {job}"

user_data = {
    "name": "Alex",
    "job": "工程師",
    "country": "台灣"
}

# 使用 ** 解包：
intro = make_profile(**user_data) # 等同於 make_profile(name="Alex", job="工程師", country="台灣")
print(intro)
```

---

## 7. 語法全貌速查地圖

Python 函式定義中，參數擺放的順序非常嚴謹，完整順序如下：

$$\text{def func(} \underbrace{\text{pos\_only}}_{/ \text{ 左側}}, \mathbf{/}, \underbrace{\text{standard}}_{\text{普通參數}}, \underbrace{\text{*args}}_{\text{多餘位置}}, \underbrace{\text{kw\_only}}_{* \text{ 右側}}, \underbrace{\text{**kwargs}}_{\text{多餘關鍵字}} \text{):}$$

### 視覺化速查表

| 符號 / 語法 | 作用 | 呼叫時限制 | 範例 |
| :--- | :--- | :--- | :--- |
| **`param`** | 一般參數 | 可使用位置引數，也可使用關鍵字引數 | `f(10)` 或 `f(x=10)` |
| **`/`** | 僅限位置引數分隔符 | 其**左邊**的參數只能依位置傳入 | `def f(a, /):` $\rightarrow$ `f(1)` |
| **`*`** | 僅限關鍵字引數分隔符 | 其**右邊**的參數必須以關鍵字傳入 | `def f(*, b):` $\rightarrow$ `f(b=2)` |
| **`*args`** | 收集可變數量位置引數 | 將多傳的位置引數裝入 Tuple | `f(1, 2, 3)` |
| **`**kwargs`** | 收集可變數量關鍵字引數 | 將多傳的鍵值對裝入 Dict | `f(a=1, b=2)` |
| 呼叫端 **`*list`** | 解包序列 | 將 Iterable 拆散成個別位置引數傳入 | `f(*[1, 2])` |
| 呼叫端 **`**dict`** | 解包字典 | 將 Dict 拆散成關鍵字引數傳入 | `f(**{'a':1})` |

---

## 8. 新手常見錯誤排行榜（常見報錯與解法）

### 錯誤 1：位置引數放在關鍵字引數後面
```python
# 報錯：SyntaxError: positional argument follows keyword argument
def greet(greeting, name):
    print(greeting, name)

# 錯誤示範：
greet(greeting="嗨", "小明")  # ❌

# 正確寫法：
greet("嗨", name="小明")      # ✔️
greet("嗨", "小明")          # ✔️
```

### 錯誤 2：同一個參數重複給值
```python
# 報錯：TypeError: ... got multiple values for argument 'x'
def demo(x, y):
    return x + y

# 錯誤示範：第一個引數 10 已經給了 x，後面又寫 x=20
demo(10, 5, x=20)           # ❌
```

### 錯誤 3：對 `/` 前面的參數使用關鍵字
```python
# 報錯：TypeError: ... got some positional-only arguments passed as keyword arguments
def div(a, b, /):
    return a / b

div(a=10, b=2)              # ❌ 只能寫 div(10, 2)
```

### 錯誤 4：漏掉 `*` 後面必須指定的關鍵字
```python
# 報錯：TypeError: ... takes 0 positional arguments but 1 was given
def alert(*, msg):
    print(msg)

alert("火災注意！")          # ❌
alert(msg="火災注意！")       # ✔️
```

---

## 9. 隨堂動手實作練習

請在同目錄下的 [`practice.py`](./practice.py) 中開啟程式，嘗試回答並實作以下題目：

### 【練習 1：觀念判斷】
觀察以下函式定義：
```python
def send_email(to, /, subject, *, urgent=False):
    pass
```
請問下列哪幾種呼叫方式是**合法**的？哪幾種會**報錯**？
1. `send_email("boss@test.com", "開會通知", urgent=True)`
2. `send_email(to="boss@test.com", subject="開會通知")`
3. `send_email("boss@test.com", subject="開會通知", urgent=False)`
4. `send_email("boss@test.com", "開會通知", True)`

*(解答附於 `practice.py` 註解中)*

---

### 【練習 2：動手設計函式】
請定義一個名為 `order_drink` 的函式：
- 參數 1（`item`）：飲品名稱，**僅限位置引數**傳入（使用 `/`）。
- 參數 2（`size`）：容量（預設 `"中杯"`），可位置也可關鍵字。
- 參數 3（`sugar`）：甜度，**僅限關鍵字引數**傳入（使用 `*`）。
- 參數 4（`ice`）：冰塊，**僅限關鍵字引數**傳入（使用 `*`）。
- 其他附加備註（`extra`）：支援接收任意額外的關鍵字引數（使用 `**kwargs`）。

呼叫範例：
```python
order_drink("珍珠奶茶", "大杯", sugar="微糖", ice="少冰", note="環保杯", bag=True)
```
期望輸出：
```text
訂單：大杯 珍珠奶茶
甜度：微糖, 冰塊：少冰
其他要求：{'note': '環保杯', 'bag': True}
```
