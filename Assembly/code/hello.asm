section .data
    msg db "Hello World", 0x0A  ;msg == 변수이름, db == 데이터 타입(btye), 0x0A == 개행문자
                            ;db == byte(1byte), dw == word(4byte), dd == double(8byte)

section .text
    global _start

_start:
    mov eax, 4  ;4번 == sys_write
    mov ebx, 1  ;1번 == 정상동작햄
    mov ecx, msg
    mov edx, 12 ;msg의 길이
    int 0x80    ;실행을 하기위한 인터럽트 호출

    mov eax, 1  ;1번 == sys_exit
    mov ebx, 0
    int 0x80