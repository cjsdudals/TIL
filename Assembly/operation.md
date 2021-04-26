INC (increase)
INC 피연산자
피연산자에 1을 더한다.
연산 결과에 따라 ZF 나 OF 가 SET 될 수 있다.
```
INC reg
INC mem
```

DEC (decrease)
DEC 피연산자
피연산자에 1을 뺀다.
연산 결과에 따라 ZF 나 OF 가 SET 될 수 있다.
```
DEC reg
DEC mem
```

ADD (add)
ADD Destination Source
Destination에 Source의 값을 더해서 Destination 에 저장하는 명령어
연산 결과에 따라 ZF, OF, CF 가 SET 될 수 있다.
```
ADD destination, source
ADD eax, 123
```

SUB (subtract)
SUB Destination Source
Destination에 Source의 값을 빼서 Destination 에 저장하는 명령어
연산 결과에 따라 ZF, OF, CF 가 SET 될 수 있다.
```
SUB destination, source
SUB eax, 123
```

MUL (unsigned Integer Multiply)
MUL 피연산자
부호 없는 al, ax, eax 의 값을 피연산자와 곱하는 명령어
피연산자가 8비트이면 al과 곱해서 ax에 저장되고, 16비트이면 ax와 곱하고 dx:ax에 저장된다.
```
MUL reg
MUL mem
```

IMUL (Integer Multiply)
IMUL 피연산자
IMUL Destination Value
IMUL Destination Value Value
부호 있는 al, ax, eax의 값을 피연산자와 곱한다.
결과에 따라 CF, OF 가 SET 될 수 있다.
```
IMUL mem // 단일 피연산자 이고 피연산자를 al, ax, eax 에 곱한다.
IMUL destination, value // value를 al, ax, eax 와 곱해서 destination 에 저장한다.
IMUL destination, value1, value2 // value 끼리 곱해서 destination 에 저장한다.
```

DIV (Unsigned Integer Divide)
DIV 피연산자
8, 16, 32비트 부호 없는 정수의 나눗셈을 수행한다.
```
DIV reg
DIV mem
```

MOV (move)
MOV Destination Source
Source 에서 Destination 으로 데이터를 복사한다.
```
MOV destination, source
MOV reg, reg
```

MOVS (move String)
MOVS Destination Source
Source 에서 Destination 으로 데이터를 복사한다.
```
MOVS destination, source
```

MOVSB, MOVSW, MOVSD (move String)
MOVSB
MOVSW
MOVSD
SI 또는 ESI 레지스터에 의해 지정된 메모리 주소의 내용들을 DI 또는 EDI 레지스터에 의해 지정되는 메모리 주소로 저장한다.
```
MOVSB
MOVSW
MOVSD
```

INT (interrupt)
INT value
소프트웨어 인터럽트를 발생시켜 운영체제의 서브루틴을 호출한다.
```
INT imm
INT 3
```

AND (Logical AND)
AND Destination Source
Destination 과 Source 피연산자의 각 비터가 1일때 AND 연산 된다.
AND 연산은 각 비터가 모두 1 일때만 결과 값이 1이 된다.
AND 연산을 통해 OF, CF가 0으로 SET 되고, 결과에 따라서 ZF 가 1로 SET 될 수 있다.
```
AND reg, reg
```

OR (Inclusive OR)
OR Destination Source
Destination 과 Source 피연산자의 각 비트가 OR 연산된다.
OR 연산은 각 비트가 모두 0이면 결과가 0이고 모두 0이 아니면 결과가 1이 된다.
OR 연산을 통해 OF, CF 가 0으로 SET 되고, 결과에 따라서 ZF 가 1로 SET 될 수 있다.
```
OR reg, reg
```

XOR (Exclusive OR)
XOR Destination Source
Destination 과 Source 피연산자의 각 비트가 XOR 연산된다.
XOR 연산은 각 비트가 서로 다른 값일때만 결과가 1이다. 같은 값이라면 결과는 0이 된다.
XOR 연산을 통해서 OF, CF 가 0으로 SET 되고, 결과에 따라서 ZF 가 1로 SET 될 수 있다.
레지스터를 0으로 초기화 시킬 때 XOR reg, reg 를 많이 사용한다.
```
XOR reg, reg
```

TEST (test)
TEST 피연산자, 피연산자
두 피연산자 사이에 논리적인 AND 연산을 수행하여 플래그 레지스터에 영향을 주지만 결과값은 저장하지 않는다.
OF, CF 는 항상 0으로 SET 되고 TEST 연산 결과 값이 0이면 ZF 가 1로, 0이 아니면 ZF 가 0으로 SET 된다.
```
TEST reg, reg
```

PUSH (push on stack)
PUSH value
스택에 값을 넣는다.
ESP 의 값이 4만큼 줄어들고 이 위치에 새로운 값이 채워진다.
```
PUSH reg16
```

PUSHAD (push ALL)
PUSHAD
EAX, EBX, ECX, EDX, ESI, EDI, ESP, EBP 레지스터의 값을 스택에 PUSH 한다.
레지스터의 값을 보관해야 할 필요가 있을 떄, 사용한다.
```
PUSHAD
```

PUSHFD (push Flags)
PUSHFD
플래그 레지스터를 스택에 PUSH 한다.
플레그 레지스터의 값을 보관할 필요가 있을 때, 사용한다.
```
PUSHFD
```

POP (pop from stack)
POP Destination
ESP 레지스터가 가르키고 있는 위치의 스택 공간에서 4byte 만큼을 Destination 피연산자에 복사한다.
그리고 ESP 레지스터의 값에 4를 더한다.
```
POP destination
```

POPAD (pop All Flags From Stack)
POPAD
스택에 존재하는 값을 EAX, EBX, ECX, EDX, ESI, EDI, ESP, EBP 레지스터로 POP 한다.
PUSHAD 명령어로 스택에 보관해놓은 레지스터 정보를 다시 이용하려고 할 때 사용한다.
```
POPAD
```

POPFD (pop Flags From Stack)
POPFD
스택에 존재하는 값을 플래그 레지스터로 POP 한다.
PUSHFD 명령어로 스택에 보관해 놓은 레지스터 정보를 다시 이용하려고 할 때 사용한다.
```
POPFD
```

XCHG(Exchange)
XCHG 피연산자1, 피연산자2
두 피연산자의 내용이 서로 교환된다.
XCHG 명령은 imm 값이 피연산자로 올 수 없다.
```
XCHG reg, reg
```

NEG (negate)
NEG 피연산자
피연산자의 2의 보수를 계산하여 결과를 피연산자에 저장한다.
```
NEG reg
NEG mem
```

PTR
피연산자의 크기를 재설정한다.
```
MOV eax, DWORD PTR value // value 의 크기를 DWORD 크기로 재설정하여 eax 레지스터에 복사한다.
```

OFFSET
세그먼트의 시작으로부터 변수가 위치한 거리까지의 상대적 거리를 리턴한다.
```
MOV esi, OFFSET value // value 가 존재하는 위치를 세그먼트 시작지점부터의 상대적 거리로 구해서 esi 레지스터에 복사한다.
```

LLEA (oad Effective Address)
LLEA Destination Source
Source 피연산자의 유효주소를 계산하여 Destination 피연산자에 복사한다.
주소를 알아내서 복사하는 명령어
```
LEA reg, mem
```

REP (repeat String)
ECX 레지스터를 카운터로 사용해서 문자열 관련 명령을 ECX > 0 인 동안 반복한다.
```
REP MOVS detination, source
```

JMP (jump Unconditionally to Lable)
JMP 피연산자
피연산자의 위치로 실행 흐름이 변경된다.
피연산자가 가리키는 코드로 점프 뛰어서 실행한다고 생각하면 된다.
```
JMP reg16
```

CALL (Call a Procedure)
함수 호출 시 사용된다.
JMP 명령어와 같이 프로그램의 실행 흐름이 변경되지만 JMP 명령어와 달리 돌아올 리턴 어드레스(CALL 다음 명령어)를 스택에 저장한다
되돌아올 주소를 저장하기 때문에 함수 호출 후 원래 위치로 실행 흐름을 되돌릴 수 있다.
```
CALL 함수 주소
CALL <JMP to APU> 특정 api 지목
CALL DWORD PTR[EAX+5]
```

CMP (Compare)
CMP 피연산자1 피연산자2
두 피연산자를 비교하는 작업을 한다.
Destination 피연산자에서 Source 피연산자를 목적으로 빼서 값을 비교한다.
두 피연산자의 값이 같다면 결과는 0이 되고 ZF 가 1로 SET 된다.
다르다면 ZF 는 0으로 SET 된다.
```
CMP reg, reg
```

NOP (no operation)
아무 일도 하지 않는 명령어이다.
리버싱 작업에서 목적에 따라 유용하게 사용 될 수 있다.
```
NOP
```