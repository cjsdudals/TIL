<h1>Register (레지스터)</h1>
<h3>레지스터란?</h3>
CPU가 요청을 처리하는데 필요한 데이터를 일시적으로 저장하는 다목적 공간이다.<br>
프로세서 내부에 있는 작은 공간이며 연산제어, 디버깅등을 목적으로 사용한다.<br>
RAM과 다르고 RAM에 있는 데이터에 접근하기 위해서는 물리적으로 먼 길을 돌아가야 하는데 레지스터를 이용하여 고속으로 데이터를 처리할 수 있다.<br>
프로그램을 직접적으로 실행하는 CPU에서 사용되는 저장공간이다.<br>
<br>
연산 속도<br>
HDD < Memory < Register
<br>

---
<h3>레지스터의 단위</h3>
<h5>Bit</h5>
데이터를 표현할 수 있는 가장 작은 단위이고 0과 1로 구분된다.
<h5>Byte</h5>
8개의 Bit가 모이면 byte라고 하며 0xFF(255)까지 표현가능하다.<br>
레지스터로는 AL, AH, BL, BH, CL, CH, DL, DH 가 있다.
<h5>Word</h5>
2개의 byte가 모이면 word라 하며 0xFFFF(65535)까지 표현가능하다.<br>
레지스터로는 AX, BX, CX, DX, SI, DI, BP, SP, IP 가 있다.
<h5>Double word</h5>
word 2개가 모이면 dword라 하며 0xFFFFFF(4294967295)까지 표현가능하다.<br>
레지스터로는 EAX, EBX, ECX, EDX, ESI, EDI, EBP, ESP, EIP 가 있다.
<h5>Kilobyte</h5>
32bit의 제곱으로 값을 표현한다.

---
<h3>범용 레지스터 (General Purpose Register)</h3>
레지스터들 중에서도 각각 특별한 용도가 정해져 있는 레지스터
<img src = './image/general purpose register.png'>

||특징|
|:---|:---:|
|EAX|곱셈과 나눗셈 명령어에서 자동적으로 사용된다.|
|ECX|CPU에 의해 자동적으로 루프카운터로 사용된다.|
|EBP|고급언어에서 스택에 있는 함수 매개 변수와 지역 변수를 참조하기 위해서 사용된다. <br>고급수준의 프로그래밍이 아니라면 일반적인 계산과 데이터 전송에는 사용하지 말아야한다.|
|ESP|스택에 있는 데이터의 주소를 지정한다.<br>ESP는 보통의 계산과 데이터 전송에는 거의 사용되지 않는다.|
|ESI, EDI|고속 메모리 전송 명령어에서 사용한다.|
|||
|EIP|명령어 포인터 레지스터는 실행 할 다음 명령어의 주소를 포함한다.<br>어떤 기계어 명령어는 EIP를 조작하여 프로그램 새 위치로 분기하게 한다.|
|EFLAGS|CPU연산의 결과를 반영하는 개별적인 2진수 비트들로 구성된다.|
<br>
<img src = './image/general purpose register_1.png'>

||산술 연산 레지스터|
|:---|:---:|
|AX|산술 논리 연산에 사용되며, 함수의 리턴값이 여기에 저장된다.|
|BX|간접 번지 지정시에 사용되며, 배열의 인덱스 값을 저장한다.|
|CX|반복문의 반복 횟수(counter) 지정 시에 사용되며, 문자열 처리에도 사용된다.|
|DX|AX의 보조적인 역할을 하며, AX와 합쳐져서 확장된 메모리로 사용된다.<br> 또한 I/O 주소를 지정할 때 사용된다.|
||인덱스 레지스터|
|SI(Stack Index)|복사나 비교를 할 때 사용되는 소스문자이다.|
|DI(Base Index)|복사나 비교를 할 때 사용되는 목적지 문자이고 stos, movs를 사용할 때 마다 1씩 증가한다|
||포인터 레지스터|
|SP(Stack Pointer)|스택의 가장 윗부분을 가르키고 스택에 값이 쌓이면 ESP도 증가한다.|
|BP(Base Pointer)|스택의 제일 바닥 부분을 주소가 가르키고 EBP밑에는 Return값이 있다.|

<img src = './image/general purpose register_2.png'>

---
<h3>세그먼트 레지스터 (Segment Register)</h3>
현재 메모리 주소를 표현하기 위한 세그먼트 디스크립터 테이블(GOT, Global Descriptor Table)의 위치를 나타내며 각 영역의 기본 위치를 가르킨다.<br>
<img src='./image/segment register.png'>

||특징|
|:---|:---:|
|CS(Code Segment)|코드 영역을 가르키는 레지스터로 데이터 이동 명령으로 값을 변경할 수 없다.(jmp or 인터럽트 관련 명령으로 변경 가능)|
|SS(Stack Segment)|스택 영역을 가르키는 레지스터로 데이터 이동 명령으로 값을 변경할 수 있다.<br> SP, BP등의 레지스터를 통해 스택에 접근할 때 암시적으로 사용된다.|
|DS(Data Segment)|데이터 영역을 가르키는 레지스터로 데이터 이동 명령으로 값을 변경할 수 있다.|
|ES(Extra Segment)|데이터 관련 확장 레지스터로 문자열과 관련된 작업을 처리할 때 암시적으로 사용된다.|
|FS, GS|데이터 관련 확장 레지스터로 ES와 함께 확장 레지스터로 사용된다.|
|Index|SDT(Segment Discriptor Table)에 대한 인덱스로 13bit이다. (2^13-1)개 만큼 가질 수 있으므로 13bit만 있으면 된다.|
|TI|Table Indicator의 약자로 디스크립터 테이블이 global(=0)인지 local(=1)인지 설정한다.|
|RPL|요구 특권 레벨 값이다. (00:커널, 11:유저)|

<br>

---
<h3>컨트롤 레지스터(Control Register)</h3>
운영체제의 운영 모드를 변경하고 현재 운영중인 모드의 기능을 제어하는 레지스터이다. 총 5개의 컨트롤 레지스터가 존재한다.

||특징|
|:---|:---:|
|CR0|운영 모드를 제어하는 레지스터로 실제 모드에서 보호 모드로 전환하는 역할을 하고 캐시기능, 페이징기능등을 활성화한다.|
|CR1|프로세서에 의해 예약된 레지스터|
|CR2|Page fault 발생 시 발생한 선형 주소가 저장되는 레지스터로 페이징 기능을 활성화한 후에는 Page fault 발생했을때만 유효하다.|
|CR3|페이지 디렉토리의 물리주소와 페이지 캐시에 관련된 기능을 설정하는 레지스터이다.|
|CR4|프로세서에서 지원하는 각종 확장 기능을 제어하는 레지스터로 페이지 크기 확장 또는 메모리 확장기능을 활성화시킨다.|
|CR8|IA-32e 모드에서 추가된 레지스터로 테스크 우선순위 레지스터의 값을 제어하는 레지스터이다.프로세스 외부에서 발생하는 인터럽트를 필터해주는 역할이다.|

<img src='./image/control register.png'>

---
<h3>E-flag 레지스터(E-flag Register)</h3>

비트별 플래그

---
0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ID | VIF | AC | VM | RF | 0 | NT | IOPL | IOPL | OF | DF | IF | TF | SF | ZF | 0 | AF | 0 | PF | 1 | CF
---
---

<br>

||플래그|설명|
|:---|:---:|:---:|
|연산결과|CF(Carry Flag)|덧셈과 뺄셈에서 빌림수 발생시 1로 설정|
||PF(Parrity Flag)|연산 결과가 짝수이면 1, 홀수이면 0으로 설정|
||AF(Auxiliary carry Flag)|16비트 연산시 빌림수 발생시 1로 설정|
||ZF(Zero Flag)|연산 결과가 0이면 1로 설정|
||SF(Sign Flag)|연산 결과 최상위 비트가 1인 경우 1로 설정|
||OF(Overflow Flag)|연산 결과가 용량을 초과하였을경우 1로 설정|
|시스템 제어|TF(Trap Flag)|프로그램 추적시 1로 설정, 명령을 한줄씩 실행한다.|
||IF(Interrupt enable Flag)|외부 인터럽트 요구를 받아들일때 1로 설정|
||AC(Alignment Check)|CR0 레지스터의 AM bit와 함께 1로 설정하면 메모리 참조시 정렬 체크를 활성화 한다.|
||IOPL(I/O Privilege Level)|현재 특권 수준이 IOPL보다 높은 경우에 I/O 주소 접근한다. 11이 가장 낮다.|
||NT(Nested Task)|연결 작업 제어, 1로 설정시 현재 작업이 기존 실행 작업과 연결됨을 의미한다.|
||RF(Resume Flag)|디버깅시 프로세서에 일시 중지 예외 발생 제어|
||VM(Virtual-8086 mode)|Virtual-8086-mode 활성화시 1로 설정|
||VIF(Virtual Interrupt Pending)|가상 이미지의 인터럽트 요구를 받아들일때 1로 설정된다.VIP와 같이 사용된다.|
||VIP(Virtual Interrupt Pending)|가상 모드 인터럽트가 지연시 1로 설정|
||ID(ID Flag)|CPUID 명령어 지원 여부로 1로 설정시 지원|
|문자열 제어|DF(Direction Flag)|문자열 복사 명령과 관련된 제어 플래그<br>1로 설정되어 있으면 문자열 복사시 주소값이 감소한다.|

---
<h3>IP(Instruction Pointer)</h3>
CPU가 처리해야하는 명령어의 주소를 나타내는 레지스터<br>
EIP에 저장된 주소의 명령어를 처리하고 크기만큼 다음으로 이동하여 또 명령어를 실행시킨다.<br><br>

출처 : https://hongci.tistory.com/21?category=219348