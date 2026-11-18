# Python 函式引數傳遞程式碼說明書 (function.ipynb)
### Multilingual Code Manual: Traditional Chinese | English | 日本語

本說明書針對 [`2026_11_18/function.ipynb`](./function.ipynb) 筆記本中的所有程式碼單元（Cells）進行逐段深度解說。每個單元均提供**繁體中文詳細說明**，並隨附 **English** 與 **日本語** 的摺疊展開對照區塊，方便對照學習國際化技術術語。

---

## 目錄 (Table of Contents / 目次)
- [單元 1：函式基本定義與呼叫 (Basic Function Definition & Call)](#單元-1函式基本定義與呼叫-basic-function-definition--call)
- [單元 2：引數位置（Positional Arguments / 位置引数）](#單元-2引數位置positional-arguments--位置引数)
- [單元 3：引數名稱（Keyword Arguments / キーワード引数）](#單元-3引數名稱keyword-arguments--キーワード引数)
- [單元 4：混用規則——位置引數必須在關鍵字引數之前](#單元-4混用規則位置引數必須在關鍵字引數之前)
- [單元 5：指配預設值（Default Arguments / デフォルト引数）](#單元-5指配預設值default-arguments--デフォルト引数)
- [單元 6：特殊符號 `/` —— 僅限位置引數（Positional-Only / 位置専用引数）](#單元-6特殊符號---僅限位置引數positional-only--位置専用引数)
- [單元 7：特殊符號 `*` —— 僅限關鍵字引數（Keyword-Only / キーワード専用引数）](#單元-7特殊符號---僅限關鍵字引數keyword-only--キーワード専用引数)
- [單元 8：綜合切分架構——同時使用 `/` 與 `*`](#單元-8綜合切分架構同時使用--與-)
- [單元 9：`*args` —— 打包多餘的位置引數為 Tuple](#單元-9args--打包多餘的位置引數為-tuple)
- [單元 10：`**kwargs` —— 打包多餘的關鍵字引數為 Dict](#單元-10kwargs--打包多餘的關鍵字引數為-dict)
- [單元 11：內建函式實戰 1 —— `print()`](#單元-11內建函式實戰-1--print)
- [單元 12：內建函式實戰 2 —— `sorted()`](#單元-12內建函式實戰-2--sorted)
- [附錄：多語術語對照與常見錯誤速查表](#附錄多語術語對照與常見錯誤速查表)

---

## 單元 1：函式基本定義與呼叫 (Basic Function Definition & Call)

### 程式碼 (Cell 1)
```python
def greet(name):
    print(f"Hello,{name}")

greet("小明")
greet("Hero")
```

### 輸出結果 (Output)
```text
Hello,小明
Hello,Hero
```

### 繁體中文解析
1. **參數（Parameter）**：定義函式時 `greet(name)` 括號內的 `name` 是參數（佔位變數）。
2. **引數（Argument）**：呼叫函式時傳入的 `"小明"` 與 `"Hero"` 是引數（實體資料）。
3. 呼叫時，引數會逐一傳遞給參數並執行函式主體。

<details>
<summary><b>🌐 English Explanation</b></summary>

- **Parameters vs. Arguments**: 
  - A **parameter** (`name`) is the variable defined in the function declaration.
  - An **argument** (`"小明"`, `"Hero"`) is the actual value passed into the function when calling it.
- **Execution**: When `greet("小明")` is invoked, the argument `"小明"` is bound to the parameter `name`, printing `"Hello,小明"`.
</details>

<details>
<summary><b>🗾 日本語解説 (Japanese Explanation)</b></summary>

- **仮引数（Parameter）と実引数（Argument）**:
  - **仮引数（Parameter）**：関数定義 `def greet(name):` の括弧内にある変数名 `name` のこと。
  - **実引数（Argument）**：関数呼び出し `greet("小明")` 時に実際に渡される値（データ）のこと。
- **実行の流れ**：呼び出し時に実引数が仮引数に代入され、関数内のブロックが順次実行されます。
</details>

---

## 單元 2：引數位置（Positional Arguments / 位置引数）

### 程式碼 (Cell 2)
```python
def describe_pet(animal, name):
    print(f"我養了一隻 {animal}，它的名字是 {name}。")

describe_pet("狗", "小白")  
describe_pet("小白", "狗")
#describe_pet("狗")
#describe_pet("狗", "小白", 1)
```

### 輸出結果 (Output)
```text
我養了一隻 狗，它的名字是 小白。
我養了一隻 小白，它的名字是 狗。
```

### 繁體中文解析
- **位置對應**：Python 依排列順序從左到右，第 1 個值傳給第 1 個參數、第 2 個值傳給第 2 個參數。
- **順序錯誤的影響**：第二行 `describe_pet("小白", "狗")` 順序顛倒，造成邏輯荒謬（「我養了一隻小白，它的名字是狗」）。

> [!WARNING]
> **引數數量不符報錯解析：**
> 1. 少傳引數：`describe_pet("狗")` $\rightarrow$ `TypeError: describe_pet() missing 1 required positional argument: 'name'`
> 2. 多傳引數：`describe_pet("狗", "小白", 1)` $\rightarrow$ `TypeError: describe_pet() takes 2 positional arguments but 3 were given`

<details>
<summary><b>🌐 English Explanation</b></summary>

- **Positional Arguments**: Arguments mapped to parameters purely based on their order (from left to right).
- **Order Matters**: Swapping the order produces unintended logic (e.g., calling `"小白"` before `"狗"` switches animal and name).
- **Arity Mismatch**:
  - Passing too few arguments raises `TypeError: missing 1 required positional argument`.
  - Passing too many arguments raises `TypeError: takes 2 positional arguments but 3 were given`.
</details>

<details>
<summary><b>🗾 日本語解説 (Japanese Explanation)</b></summary>

- **位置引数（Positional Arguments）**: 渡された順番に従って左から順に対応する仮引数へと代入される最も基本的な渡し方です。
- **順序の重要性**: 引数の順序を間違えると、意味が意図しないものになってしまいます（「小白という動物で、名前が狗」になってしまうなど）。
- **個数不一致のエラー**:
  - 不足時：`TypeError: missing 1 required positional argument`
  - 超過時：`TypeError: takes 2 positional arguments but 3 were given`
</details>

---

## 單元 3：引數名稱（Keyword Arguments / キーワード引数）

### 程式碼 (Cell 3)
```python
def describe_pet(animal, name):
    print(f"我養了一隻 {animal}，它的名字是 {name}。")

describe_pet(animal="狗", name="小白")
describe_pet(name="小白", animal="狗")
```

### 輸出結果 (Output)
```text
我養了一隻 狗，它的名字是 小白。
我養了一隻 狗，它的名字是 小白。
```

### 繁體中文解析
- 呼叫時明確指定 **`參數名稱=值`**。
- **優點 1：順序無關**。即使顛倒寫，Python 也能精確配對。
- **優點 2：可讀性高**。呼叫端一眼就能看出每個引數的用途。

<details>
<summary><b>🌐 English Explanation</b></summary>

- **Keyword Arguments**: Arguments passed in the format `name=value`.
- **Order Independence**: Because arguments are explicitly matched by their parameter names, order does not matter.
- **High Readability**: Makes calling code self-documenting and less error-prone.
</details>

<details>
<summary><b>🗾 日本語解説 (Japanese Explanation)</b></summary>

- **キーワード引数（Keyword Arguments）**: 呼び出し時に `仮引数名=値` の形式で指定して渡す方法です。
- **順序に依存しない**: 名前で直接指定するため、順番を入れ替えても正確にパラメータへ届きます。
- **可読性の向上**: どの値がどのパラメータに対応しているかがコード上で明確になります。
</details>

---

## 單元 4：混用規則——位置引數必須在關鍵字引數之前

### 程式碼 (Cell 4)
```python
describe_pet(animal="狗", name="小白")
```

### 繁體中文解析
- **黃金鐵則**：混用位置引數與關鍵字引數時，**位置引數永遠必須在前面**。
- ❌ **錯誤示範 1（順序顛倒）**：
  ```python
  describe_pet(animal="狗", "小白")
  # SyntaxError: positional argument follows keyword argument
  ```
- ❌ **錯誤示範 2（重複賦值）**：
  ```python
  describe_pet("狗", animal="貓")
  # TypeError: describe_pet() got multiple values for argument 'animal'
  ```

<details>
<summary><b>🌐 English Explanation</b></summary>

- **Syntax Rule**: **Positional arguments must ALWAYS appear before keyword arguments**.
- `describe_pet(animal="狗", "小白")` causes `SyntaxError: positional argument follows keyword argument`.
- Duplicate assignments like `describe_pet("狗", animal="貓")` cause `TypeError: got multiple values for argument`.
</details>

<details>
<summary><b>🗾 日本語解説 (Japanese Explanation)</b></summary>

- **併用時の鉄則**: **位置引数は必ずキーワード引数よりも前に記述しなければなりません**。
- `describe_pet(animal="狗", "小白")` のようにキーワード引数の後ろに位置引数を置くと `SyntaxError` になります。
- `describe_pet("狗", animal="貓")` のように同じ引数に重複して値を渡すと `TypeError: got multiple values for argument` が発生します。
</details>

---

## 單元 5：指配預設值（Default Arguments / デフォルト引数）

### 程式碼 (Cell 5)
```python
def order_drink(drink, ice="正常冰", sugar="半糖"):
    print(f"你點了一杯 {drink}，冰塊量為 {ice}，甜度為 {sugar}。")

order_drink("咖啡")
order_drink("咖啡", "少冰")
order_drink("咖啡", sugar="無糖")
order_drink("咖啡", sugar="無糖", ice="少冰")
```

### 輸出結果 (Output)
```text
你點了一杯 咖啡，冰塊量為 正常冰，甜度為 半糖。
你點了一杯 咖啡，冰塊量為 少冰，甜度為 半糖。
你點了一杯 咖啡，冰塊量為 正常冰，甜度為 無糖。
你點了一杯 咖啡，冰塊量為 少冰，甜度為 無糖。
```

### 繁體中文解析
1. **設定預設值**：在 `def` 宣告時給予預設值（`ice="正常冰"`, `sugar="半糖"`）。
2. **靈活呼叫**：未傳入時採用預設值；可依位置覆蓋，也可使用關鍵字引數**跳過中間參數**（如直接指定 `sugar="無糖"`）。

<details>
<summary><b>🌐 English Explanation</b></summary>

- **Default Parameter Values**: Parameters initialized with defaults when defining the function.
- **Skipping & Overriding**:
  - If omitted, the default value is used.
  - Can be overridden positionally or by specifying keyword arguments (allowing you to skip earlier defaults).
</details>

<details>
<summary><b>🗾 日本語解説 (Japanese Explanation)</b></summary>

- **デフォルト引数（Default Arguments）**: 関数定義時にあらかじめ初期値を設定しておける仕組みです。
- **省略と上書き**:
  - 引数を渡さなければ自動的にデフォルト値が使われます。
  - 位置で手前から上書きすることも、キーワード指定で特定の項目だけをピンポイントで上書きすることも可能です。
</details>

---

## 單元 6：特殊符號 `/` —— 僅限位置引數（Positional-Only / 位置専用引数）

### 程式碼 (Cell 6)
```python
def cale_bmi(w, h , /):
    bmi = w / (h ** 2)
    print(f"你的BMI為 {bmi:.2f}")   

cale_bmi(70, 1.75)
```

### 輸出結果 (Output)
```text
你的BMI為 22.86
```

### 繁體中文解析
- 符號 `/` 是分隔標記。
- **規則**：寫在 `/` **左側**的所有參數（`w`, `h`），呼叫時**只能用位置引數**傳入，不能寫出名稱。
- ❌ **錯誤範例**：
  ```python
  cale_bmi(w=70, h=1.75)
  # TypeError: cale_bmi() got some positional-only arguments passed as keyword arguments: 'w, h'
  ```

<details>
<summary><b>🌐 English Explanation</b></summary>

- **Positional-Only Marker (`/`)**: Introduced in Python 3.8.
- **Rule**: All parameters to the **left** of `/` can ONLY be passed positionally. Passing them as keyword arguments raises `TypeError`.
- **Purpose**: Prevents callers from relying on parameter names that may be renamed in the future.
</details>

<details>
<summary><b>🗾 日本語解説 (Japanese Explanation)</b></summary>

- **位置専用引数の記号（`/`）**: Python 3.8 で追加された構文です。
- **ルール**: `/` より**左側**にあるすべてのパラメータは、呼び出し時に**位置引数としてしか渡せません**（キーワード指定は不可）。
- キーワード引数として渡すと `TypeError` となります。パラメータ名に依存させたくない標準ライブラリなどで重宝されます。
</details>

---

## 單元 7：特殊符號 `*` —— 僅限關鍵字引數（Keyword-Only / キーワード専用引数）

### 程式碼 (Cell 7)
```python
def send_email(to, *, subject, urgent=False):
    print(f"寄信給 {to}，主旨為 {subject}，是否緊急：{urgent}")

send_email("hero63@gmail.com", subject="會議通知", urgent=True)
send_email("hero63@gmail.com", urgent=True, subject="會議通知")
```

### 輸出結果 (Output)
```text
寄信給 hero63@gmail.com，主旨為 會議通知，是否緊急：True
寄信給 hero63@gmail.com，主旨為 會議通知，是否緊急：True
```

### 繁體中文解析
- 單獨出現的 `*` 是分隔標記。
- **規則**：寫在 `*` **右側**的所有參數（`subject`, `urgent`），呼叫時**必須使用關鍵字引數**，不接受依位置傳遞。
- ❌ **錯誤範例**：
  ```python
  send_email("hero63@gmail.com", "會議通知", True)
  # TypeError: send_email() takes 1 positional argument but 3 were given
  ```

<details>
<summary><b>🌐 English Explanation</b></summary>

- **Keyword-Only Marker (`*`)**:
- **Rule**: All parameters to the **right** of `*` MUST be passed as keyword arguments.
- **Purpose**: Enforces readability, especially for boolean flags (e.g. `urgent=True`) where raw positional literals would be cryptic.
</details>

<details>
<summary><b>🗾 日本語解説 (Japanese Explanation)</b></summary>

- **キーワード専用引数の記号（`*`）**:
- **ルール**: 単独の `*` より**右側**にあるパラメータは、呼び出し時に**必ずキーワード引数（名前指定）で渡さなければなりません**。
- `urgent=True` のような真偽値（フラグ）を位置だけで渡すと可読性が著しく低下するため、名前指定を強制してミスを防ぐ目的で使用されます。
</details>

---

## 單元 8：綜合切分架構——同時使用 `/` 與 `*`

### 程式碼 (Cell 8)
```python
def register(id_no, /, name, *, role="student"):
    print(f"編號：{id_no}｜姓名：{name}｜身分：{role}")

register("A01", "小明", role="leader")
```

### 輸出結果 (Output)
```text
編號：A01｜姓名：小明｜身分：leader
```

### 語法切分地圖 (Syntax Partition Map)
$$\text{def func(} \underbrace{\text{id\_no}}_{\text{只能位置}}, \mathbf{/}, \underbrace{\text{name}}_{\text{位置或名稱皆可}}, \mathbf{*}, \underbrace{\text{role}}_{\text{只能關鍵字}} \text{):}$$

<details>
<summary><b>🌐 English Explanation</b></summary>

- **Partition Breakdown**:
  1. `id_no` (Left of `/`): Positional-only.
  2. `name` (Between `/` and `*`): Standard parameter (can be positional or keyword).
  3. `role` (Right of `*`): Keyword-only.
</details>

<details>
<summary><b>🗾 日本語解説 (Japanese Explanation)</b></summary>

- **3つの領域の切り分け**:
  1. `id_no`（`/` の左側）：位置専用引数（キーワード指定不可）。
  2. `name`（`/` と `*` の間）：通常引数（位置でもキーワードでも自由）。
  3. `role`（`*` の右側）：キーワード専用引数（必ずキーワード指定）。
</details>

---

## 單元 9：`*args` —— 打包多餘的位置引數為 Tuple

### 程式碼 (Cell 9)
```python
def sum_scores(*scores):
    print("收到", scores, type(scores))
    return sum(scores)

print(sum_scores(90, 80, 70))
print(sum_scores(90, 80))
print(sum_scores())
```

### 輸出結果 (Output)
```text
收到 (90, 80, 70) <class 'tuple'>
240
收到 (90, 80) <class 'tuple'>
170
收到 () <class 'tuple'>
0
```

### 繁體中文解析
- 單星號 `*args` 用於函式定義時，可動態接收任意數量的位置引數，並打包為 **`tuple`（元組）**。
- 未傳入任何引數時為空元組 `()`。

<details>
<summary><b>🌐 English Explanation</b></summary>

- **Arbitrary Positional Arguments (`*args`)**:
- Packs any extra positional arguments into a `tuple`.
- Passing zero arguments results in an empty tuple `()`.
</details>

<details>
<summary><b>🗾 日本語解説 (Japanese Explanation)</b></summary>

- **可変長位置引数（`*args`）**:
- 任意の数の位置引数を受け取り、それらをひとつの **`tuple`（タプル）** にまとめてパックします。
- 引数を何も渡さなかった場合は空のタプル `()` となります。
</details>

---

## 單元 10：`**kwargs` —— 打包多餘的關鍵字引數為 Dict

### 程式碼 (Cell 10)
```python
def build_profile(name, age, **info):
    print(f"姓名：{name}｜年齡：{age}")
    print("其他資訊：", info, type(info))

build_profile("小明", 18, city="台北", hobby="打籃球", play="電腦遊戲")
```

### 輸出結果 (Output)
```text
姓名：小明｜年齡：18
其他資訊： {'city': '台北', 'hobby': '打籃球', 'play': '電腦遊戲'} <class 'dict'>
```

### 繁體中文解析
- 雙星號 `**kwargs` 用於函式定義時，可動態接收任意額外的關鍵字引數，並打包為 **`dict`（字典）**。

<details>
<summary><b>🌐 English Explanation</b></summary>

- **Arbitrary Keyword Arguments (`**kwargs`)**:
- Packs any excess keyword arguments (`key=value`) into a `dict`.
</details>

<details>
<summary><b>🗾 日本語解説 (Japanese Explanation)</b></summary>

- **可変長キーワード引数（`**kwargs`）**:
- 事前に定義されていない任意のキーワード引数を **`dict`（辞書）** にまとめてパックします。
</details>

---

## 單元 11：內建函式實戰 1 —— `print()`

### 程式碼 (Cell 11)
```python
# print(*objects, sep=' ', end='\n', file=None, flush=False)
print('a', 'b', 1, 23, 56)
print('a', 'b', 1, 23, 56, sep='-')
print('a', 'b', 1, 23, 56, end="good\n")
```

### 輸出結果 (Output)
```text
a b 1 23 56
a-b-1-23-56
a b 1 23 56good
```

### 繁體中文解析
- `*objects`：可傳入任意多個要印出的值。
- `sep` 與 `end` 位於 `*objects` 後方，自動成為**僅限關鍵字引數**，呼叫時必須指定名稱。

<details>
<summary><b>🌐 English Explanation</b></summary>

- `*objects` allows printing arbitrary numbers of items.
- Because `sep` and `end` follow `*objects`, they are keyword-only and require explicit names (`sep='-'`).
</details>

<details>
<summary><b>🗾 日本語解説 (Japanese Explanation)</b></summary>

- `*objects` により何個でも自由に出力する値を渡せます。
- `*objects` の後ろにある `sep` や `end` は自動的に**キーワード専用**となるため、変更時は必ず名前を指定します。
</details>

---

## 單元 12：內建函式實戰 2 —— `sorted()`

### 程式碼 (Cell 12)
```python
# sorted(iterable, /, *, key=None, reverse=False)
sorted([3, 1, 5, 2, 4])
sorted([8, 92, 63, 75], reverse=True)
```

### 輸出結果 (Output)
```text
[92, 75, 63, 8]
```

### 繁體中文解析
- `iterable` 位於 `/` 左側，只能用位置引數傳入。
- `key` 與 `reverse` 位於 `*` 右側，必須用關鍵字引數傳入（如 `reverse=True`）。

<details>
<summary><b>🌐 English Explanation</b></summary>

- `iterable` is to the left of `/` $\rightarrow$ positional-only.
- `reverse` is to the right of `*` $\rightarrow$ keyword-only (`reverse=True`).
</details>

<details>
<summary><b>🗾 日本語解説 (Japanese Explanation)</b></summary>

- `iterable` は `/` の左にあるため**位置専用**です。
- `reverse` は `*` の右にあるため**キーワード専用**（`reverse=True`）です。
</details>

---

## 附錄：多語術語對照與常見錯誤速查表

### 1. 專業術語對照表 (Terminology Translation)

| 繁體中文 | English | 日本語 | 說明 |
| :--- | :--- | :--- | :--- |
| **參數** | Parameter | 仮引数 (かりひきすう) | 定義函式時宣告的變數 |
| **引數** | Argument | 実引数 (じつひきすう) | 呼叫函式時實際傳入的值 |
| **位置引數** | Positional Argument | 位置引数 | 依照順序對應的引數 |
| **關鍵字引數** | Keyword Argument | キーワード引数 | 透過 `名稱=值` 指定的引數 |
| **預設值引數** | Default Argument | デフォルト引数 | 擁有預設初始值的參數 |
| **僅限位置引數 (`/`)** | Positional-Only | 位置専用引数 | 只能以位置傳遞，不可寫名稱 |
| **僅限關鍵字引數 (`*`)** | Keyword-Only | キーワード専用引数 | 必須寫出名稱傳遞 |
| **打包 / 解包** | Packing / Unpacking | パック / アンパック (展開) | 星號打包與拆散資料容器 |

---

### 2. 常見錯誤與除錯指南 (Common Errors & Debugging)

| 錯誤類型 (Error Type) | 原因說明 (Cause) | 修正方式 (Solution) |
| :--- | :--- | :--- |
| `SyntaxError: positional argument follows keyword argument` | 位置引數寫在關鍵字引數後面 | 將位置引數全部移到前面 |
| `TypeError: got some positional-only arguments passed as keyword arguments` | 對 `/` 左邊的參數指定了名稱 | 移除名稱，純粹依位置傳入 |
| `TypeError: takes X positional argument but Y were given` | 對 `*` 右邊的參數用位置傳入 | 補上參數名稱（`名稱=值`） |
| `TypeError: got multiple values for argument` | 同一參數同時被位置和名稱指定 | 移除重複指定的引數 |
