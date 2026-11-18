# Python 例外處理（Exception Handling）完全教學指南

在寫程式的過程中，即使語法完全正確，程式在執行時還是可能遇到無法預期的狀況（例如：使用者亂輸入文字、要開啟的檔案不存在、除以零等）。

如果沒有預先防範，程式就會立刻噴出一長串紅字並**直接閃退崩潰**。本篇教材將由淺入深，帶你學會如何使用 Python 的「例外處理」機制，讓你的程式變得穩固又優雅！

---

## 目錄
- [前言：語法錯誤 vs. 執行階段例外](#前言語法錯誤-vs-執行階段例外)
- [第 1 步：常見的例外地雷有哪些？](#第-1-步常見的例外地雷有哪些)
- [第 2 步：最基礎的防護罩 —— `try...except`](#第-2-步最基礎的防護罩--tryexcept)
- [第 3 步：精準捕捉 —— 分別捕捉不同例外與 `as e`](#第-3-步精準捕捉--分別捕捉不同例外與-as-e)
- [第 4 步：完整四部曲 —— `try...except...else...finally`](#第-4-步完整四部曲--tryexceptelsefinally)
- [第 5 步：主動引爆地雷 —— 使用 `raise`](#第-5-步主動引爆地雷--使用-raise)
- [第 6 步：進階實戰 —— 自訂例外類別（Custom Exceptions）](#第-6-步進階實戰--自訂例外類別custom-exceptions)
- [第 7 步：新手常見避坑指南（Best Practices）](#第-7-步新手常見避坑指南best-practices)
- [第 8 步：課堂動手實作練習](#第-8-步課堂動手實作練習)

---

## 前言：語法錯誤 vs. 執行階段例外

在 Python 中，錯誤大致分為兩大類：

1. **語法錯誤（SyntaxError）**：
   - 程式碼根本不符合 Python 語法規範（例如：括號沒關、漏打冒號 `:`、縮排錯誤）。
   - **程式連跑都不會跑**，直譯器在編譯階段就直接擋下。
2. **例外（Exception / 執行階段錯誤）**：
   - 語法完全合法，但程式在「**執行時（Runtime）**」遇到了意外狀況。
   - 例如：請使用者輸入年齡，對方卻輸入了文字 `"abc"`，導致 `int("abc")` 當場爆炸。

> [!NOTE]
> **「例外處理（Exception Handling）」** 的目的，就是為了在程式踩到地雷時，能夠有**應變計畫**，而不是直接崩潰閃退。

---

## 第 1 步：常見的例外地雷有哪些？

在學會如何抓地雷前，我們先來認識 Python 最常見的幾種例外型態：

| 例外型態 (Exception) | 觸發原因 | 程式碼死因範例 |
| :--- | :--- | :--- |
| **`ZeroDivisionError`** | 數字被 `0` 除 | `10 / 0` |
| **`ValueError`** | 傳入的值型態對，但內容無效 | `int("hello")` |
| **`TypeError`** | 對不相容的資料型態進行操作 | `"10" + 5` |
| **`IndexError`** | 存取了串列（List）不存在的索引 | `lst = [1, 2]; print(lst[5])` |
| **`KeyError`** | 查詢字典（Dict）中不存在的鍵 | `d = {"a": 1}; print(d["b"])` |
| **`FileNotFoundError`** | 試圖開啟一個不存在的檔案 | `open("ghost.txt", "r")` |

---

## 第 2 步：最基礎的防護罩 —— `try...except`

最基本也是最核心的結構是 `try` 和 `except`：

```text
try:
    # 可能會出事的程式碼
except:
    # 萬一真的出事時，要執行的應變措施
```

### 範例：計算除法
假設我們讓使用者輸入兩個數字相除：

#### ❌ 沒做防護的版本（容易閃退）：
```python
num1 = int(input("請輸入被除數: "))
num2 = int(input("請輸入除數: "))
result = num1 / num2
print(f"結果是：{result}")
```
> 若使用者輸入除數為 `0`，終端機立刻噴出 `ZeroDivisionError: division by zero` 並中斷程式！

#### ✔️ 使用 `try...except` 的保護版本：
```python
try:
    num1 = int(input("請輸入被除數: "))
    num2 = int(input("請輸入除數: "))
    result = num1 / num2
    print(f"結果是：{result}")
except ZeroDivisionError:
    print("⚠️ 錯誤：除數不能為 0，請重新輸入！")
except ValueError:
    print("⚠️ 錯誤：只能輸入阿拉伯數字！")

print("程式繼續平穩運行中...")
```

- 當 `try` 區塊中的任何一行拋出例外，Python 會**立即跳出 `try`**，前往對應的 `except` 執行處理。
- 處理完畢後，**程式不會閃退**，會繼續執行後續程式碼。

---

## 第 3 步：精準捕捉 —— 分別捕捉不同例外與 `as e`

### 3.1 分門別類捕捉（推薦寫法）
不同的錯誤往往需要不同的應對方式（例如輸入文字請對方重填，檔案找不到請確認路徑）。

```python
try:
    scores = [95, 88, 100]
    idx = int(input("請輸入想查詢第幾位學生成績 (0~2): "))
    print(f"成績是: {scores[idx]}")
except ValueError:
    print("請輸入整數數字！")
except IndexError:
    print("超出學生名單範圍！")
```

### 3.2 合併捕捉多個例外
若多種例外的處理邏輯相同，可用圓括號打包成元組（Tuple）：

```python
try:
    val = 10 / int(input("請輸入一個數字: "))
except (ValueError, ZeroDivisionError):
    print("輸入無效或輸入了 0！")
```

### 3.3 取得 Python 官方錯誤訊息 —— `as e`
如果你想把 Python 內建的詳細錯誤原因印出來或記錄到日誌（Log），可以使用 `as 變數名稱`（慣用 `as e`）：

```python
try:
    num = int("abc")
except ValueError as e:
    print(f"抓到錯誤了！詳細原因：{e}")
    # 輸出：抓到錯誤了！詳細原因：invalid literal for int() with base 10: 'abc'
```

---

## 第 4 步：完整四部曲 —— `try...except...else...finally`

Python 的例外處理其實最多有四個關鍵字可以搭配：

```text
try:
    # 1. 嘗試執行（可能會發生錯誤的程式）
except:
    # 2. 發生例外時才執行（應變與補救）
else:
    # 3. 完全沒有發生任何錯誤時才執行
finally:
    # 4. 無論有沒有發生錯誤，最後「一定」會執行
```

### 生活比喻：出門旅行
- `try`：嘗試搭飛機出國。
- `except`：萬一飛機取消（發生例外），改住機場飯店。
- `else`：順利抵達目的地（沒出事），開心吃大餐！
- `finally`：不管順利還是取消，最後「一定都要回家」。

### 實戰程式碼範例：檔案安全讀取
```python
file = None
try:
    print("【1. 準備開啟檔案】")
    file = open("data.txt", "r", encoding="utf-8")
    content = file.read()
except FileNotFoundError:
    print("【2. 錯誤】找不到指定的檔案！")
else:
    print("【3. 成功】讀取完成，內容字數為：", len(content))
finally:
    print("【4. 收尾】執行清理作業...")
    if file:
        file.close()
        print("檔案已安全關閉。")
```

> [!TIP]
> **`finally` 的核心用途**：通常用來釋放系統資源，例如關閉檔案、斷開資料庫連線、關閉網路 Socket 等。就算在 `try` 裡面寫了 `return`，`finally` 也保證一定會先被執行！

---

## 第 5 步：主動引爆地雷 —— 使用 `raise`

有時候，Python 本身不覺得有錯，但**不符合我們的業務邏輯**。這時我們可以用 `raise` **主動拋出例外**。

### 範例：年齡防呆機制
Python 不知道年齡不能是負數或 300 歲，但我們的函式可以主動擋下：

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("年齡必須是整數！")
    if age < 0 or age > 130:
        raise ValueError(f"無效的年齡：{age}，年齡必須介於 0 到 130 歲之間！")
    print(f"年齡設定成功：{age} 歲")

# 測試呼叫：
try:
    set_age(25)    # 正常
    set_age(-5)    # 主動觸發 ValueError
except ValueError as e:
    print("警告：", e)
```

---

## 第 6 步：進階實戰 —— 自訂例外類別（Custom Exceptions）

在大型專案或團隊開發中，Python 內建的例外（如 `ValueError`）可能不夠具體。我們可以建立專屬的「自訂例外類別」。

### 建立方式：繼承 `Exception`

```python
# 1. 定義自訂例外類別（繼承內建的 Exception）
class InsufficientFundsError(Exception):
    """存款餘額不足例外"""
    def __init__(self, balance, amount):
        super().__init__(f"提款失敗！目前餘額為 {balance} 元，但您想提領 {amount} 元。")
        self.balance = balance
        self.amount = amount

# 2. 模擬銀行提款函式
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

# 3. 呼叫與捕捉
try:
    my_balance = 1000
    print("目前餘額：", my_balance)
    my_balance = withdraw(my_balance, 1500)
except InsufficientFundsError as err:
    print(f"[交易警示] {err}")
```

**輸出結果**：
```text
目前餘額： 1000
[交易警示] 提款失敗！目前餘額為 1000 元，但您想提領 1500 元。
```

---

## 第 7 步：新手常見避坑指南（Best Practices）

### ❌ 坑 1：不要裸寫 `except:`（消音地雷）
```python
# 絕對不要這樣寫！
try:
    do_something()
except:
    pass
```
> **為什麼？**
> 這會把使用者按 `Ctrl + C`（`KeyboardInterrupt`）或是打錯變數名稱的 `NameError` 通通吃掉，導致程式卡死或除錯時完全找不到原因。
> **解法**：至少寫 `except Exception as e:` 並印出錯誤訊息。

### ❌ 坑 2：不要濫用例外處理來當作一般邏輯分支
```python
# 不良示範：
try:
    val = my_dict["key"]
except KeyError:
    val = "default"

# 更好更直覺的寫法：
val = my_dict.get("key", "default")
```

---

## 第 8 步：課堂動手實作練習

### 【實作題 1：防呆整數輸入器】
請寫一個函式 `safe_input_integer(prompt)`：
- 提示使用者輸入一個整數。
- 如果使用者輸入的不是整數（觸發 `ValueError`），請印出「格式錯誤，請再試一次！」，並**重複提示直到使用者輸入正確的整數為止**。
- 最後回傳該整數值。

<details>
<summary>點擊查看【實作題 1】參考解答</summary>

```python
def safe_input_integer(prompt):
    while True:
        try:
            val = int(input(prompt))
            return val
        except ValueError:
            print("格式錯誤，這不是整數，請再試一次！")

# 測試
age = safe_input_integer("請輸入你的年齡: ")
print(f"你的年齡是：{age}")
```
</details>

---

### 【實作題 2：安全除法計算機】
請設計一個 `safe_divide()` 函式：
- 接收兩個參數 `a` 與 `b`。
- 計算 $a \div b$。
- 使用 `try...except...else...finally`：
  - 若除數為 0，捕捉並印出 `"除數不可為 0"`。
  - 若型態不支援（例如傳入字串），捕捉並印出 `"輸入資料型態不正確"`。
  - 若計算成功，在 `else` 區塊印出 `"計算成功，結果為: ..."`。
  - 在 `finally` 區塊固定印出 `"--- 計算任務結束 ---"`。

<details>
<summary>點擊查看【實作題 2】參考解答</summary>

```python
def safe_divide(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        print("【錯誤】除數不可為 0！")
    except TypeError:
        print("【錯誤】輸入資料型態不正確，必須是數值！")
    else:
        print(f"【成功】計算結果為: {res}")
    finally:
        print("--- 計算任務結束 ---\n")

# 測試
safe_divide(10, 2)
safe_divide(10, 0)
safe_divide("10", 2)
```
</details>
