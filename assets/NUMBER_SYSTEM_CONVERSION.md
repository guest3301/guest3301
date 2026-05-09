
### 1. Decimal to Binary (Repeated division by 2, read remainders bottom to top)

#### (1) 289
| Division | Quotient | Remainder |
|----------|----------|-----------|
| 289 ÷ 2  | 144      | 1         |
| 144 ÷ 2  | 72       | 0         |
| 72 ÷ 2   | 36       | 0         |
| 36 ÷ 2   | 18       | 0         |
| 18 ÷ 2   | 9        | 0         |
| 9 ÷ 2    | 4        | 1         |
| 4 ÷ 2    | 2        | 0         |
| 2 ÷ 2    | 1        | 0         |
| 1 ÷ 2    | 0        | 1         |

Read remainders from last to first: **100100001₂**

#### (2) 675
| Division | Quotient | Remainder |
|----------|----------|-----------|
| 675 ÷ 2  | 337      | 1         |
| 337 ÷ 2  | 168      | 1         |
| 168 ÷ 2  | 84       | 0         |
| 84 ÷ 2   | 42       | 0         |
| 42 ÷ 2   | 21       | 0         |
| 21 ÷ 2   | 10       | 1         |
| 10 ÷ 2   | 5        | 0         |
| 5 ÷ 2    | 2        | 1         |
| 2 ÷ 2    | 1        | 0         |
| 1 ÷ 2    | 0        | 1         |

Read upward: **1010100011₂**

#### (3) 467
| Division | Quotient | Remainder |
|----------|----------|-----------|
| 467 ÷ 2  | 233      | 1         |
| 233 ÷ 2  | 116      | 1         |
| 116 ÷ 2  | 58       | 0         |
| 58 ÷ 2   | 29       | 0         |
| 29 ÷ 2   | 14       | 1         |
| 14 ÷ 2   | 7        | 0         |
| 7 ÷ 2    | 3        | 1         |
| 3 ÷ 2    | 1        | 1         |
| 1 ÷ 2    | 0        | 1         |

Read upward: **111010011₂**

---

### 2. Binary to Decimal (Multiply each 1 by its power of 2, sum)

Given: **1110000₂** 

Write positions from right (0-index):
1 1 1 0 0 0 0  (bits)
6 5 4 3 2 1 0  (positions)

Contribution = 1×2⁶ + 1×2⁵ + 1×2⁴ + 0×... = 64 + 32 + 16 = **112₁₀**

---

### 3. Octal to Binary (Each octal digit → 3 bits, pad each to 3 bits)

**Mapping method:** Convert each digit individually to binary using division.

#### (1) 246₈
- Digit 2 → 2 decimal → binary: 10₂ → pad to 3 bits → **010**
- Digit 4 → 4 decimal → binary: 100₂ → already 3 bits → **100**
- Digit 6 → 6 decimal → binary: 110₂ → **110**
Combine: **010100110₂** → remove leading zero → **10100110₂**

#### (2) 345₈
- 3 → binary 11₂ → pad to 011
- 4 → 100
- 5 → 101
Combine: **011100101₂** → **11100101₂**

---

### 4. Binary to Octal (Group bits in 3 from right, each group to octal)

**Mapping:**  
0→000, 1→001, 2→010, 3→011, 4→100, 5→101, 6→110, 7→111

#### (1) 1100110₂
Group from right: 1 100 110 → pad left group to 3 bits: 001 100 110
Convert each:
- 001₂ = 1₈
- 100₂ = 4₈
- 110₂ = 6₈
Result: **146₈**

#### (2) 1100010₂
Group: 1 100 010 → pad to 001 100 010
- 001 → 1
- 100 → 4
- 010 → 2
Result: **142₈**

---

### 5. Hexadecimal to Binary (Each hex digit → 4 bits, pad each to 4 bits)

- Mapping:  
0→0000, 1→0001, …, 9→1001, A→1010, B→1011, C→1100, D→1101, E→1110, F→1111

#### (1) 9A₁₆
- 9 → binary 1001 (4 bits exactly)
- A = 10 decimal → binary: 1010 (4 bits)
Combine: **10011010₂**

#### (2) 8BF₁₆
- 8 → 1000
- B = 11 → binary: 1011
- F = 15 → binary: 1111
Combine: **100010111111₂**

---

### 6. Binary to Hexadecimal (Group bits in 4 from right, each group to hex)

#### (1) 11000101010₂
Group from right: 110 0010 1010 → pad left to 4 bits: 0110 0010 1010
- 0110₂ = 6₁₆
- 0010₂ = 2₁₆
- 1010₂ = A₁₆
Result: **62A₁₆**

#### (2) 11100010110₂
Group: 111 0001 0110 → pad to 0111 0001 0110
- 0111 → 7
- 0001 → 1
- 0110 → 6
Result: **716₁₆**

