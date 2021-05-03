<h1>Register (레지스터)</h1>
<h3>레지스터란?</h3>
CPU가 요청을 처리하는데 필요한 데이터를 일시적으로 저장하는 다목적 공간이다.<br>
프로세서 내부에 있는 작은 공간이며 연산제어, 디버깅등을 목적으로 사용한다.<br>
RAM과 다르고 RAM에 있는 데이터에 접근하기 위해서는 물리적으로 먼 길을 돌아가야 하는데 레지스터를 이용하여 고속으로 데이터를 처리할 수 있다.<br>
프로그램을 직접적으로 실행하는 CPU에서 사용되는 저장공간이다.<br>
<br>
연산 속도<br>
HDD < Memory \< Register
<br>
<h3>레지스터의 단위</h3>

---

---
-
---
-
---

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

<h3>범용 레지스터 (General Purpose Register)</h3>
