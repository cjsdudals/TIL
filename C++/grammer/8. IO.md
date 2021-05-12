<h1>I/O</h1>
스트림은 프로그램이 문자를 삽입하거나 추출할 수 있는 개체이다.

표준 C++ 라이브러리에는 표준 입력및 출력 스트림 개체가 선언된 \<iostream> 헤더를 포함하고 있다.
<h3>표준 출력</h3>
cout은 << 로 표시하는 삽입 연산자와 함께 사용한다. 

endl은 개행 문자를 생성한다. ( \n )

```cpp
std::cout << "String" << std::endl;
```
모든 비교, 논리, 비트, 조건부 연산은 괄호로 둘러싸서 그룹으로 만들어야한다.

<h3>표준 입력</h3>
추출연산자 >> 를 cin 스트림에 적용해야한다.

```cpp
int age;
std::cin >> age;
std::cin >> width >> height; 
```
각 데이터는 공백, 탭 문자나 개행과 같이 공백 구분기호로 구분할 수 있다.

<h3>파일 입출력</h3>

|||
|:---|:---|
|ofstream|파일에 쓰기|
|ifstream|파일로부터 읽기|
|fstream|파일 읽기 및 쓰기 모두|

```cpp
#include <fstream>
int main(){
    std::ofstream file;
    file.open("file_name.txt");
    file << "text";
    file.close();
}
```
파일을 생성(덮어쓰기)하고 cout을 쓰는 것처럼 문장을 쓴다.

```cpp
#include <fstream>
int main(){
    std::ofstream file("file_name.txt");
}
```
로 파일 열기 가능하다.

<h3>서식 지정</h3>
헤더파일 \<iomanip> 에 있는 I/O 조작기로 서식을 지정할 수 있다.

```cpp
setprecision(16) // 정확한 숫자가 나온다.
setw(30) // 출력의 너비를 결정한다.
setfill('-') // 선택한 문자로 빈공간을 채운다.
left // 왼쪽 정렬
setf(ios_base::showpos) scientific // 정규화된 지수표현
oct // 8진수
hex // 16진수
dec // 10진수
boolapha // bool ( True or False )
unsetf() // 변경된 모든 서식 옵션을 재설정
```

<h3>I/O Error Process</h3>

파일은 존재하지 않아도 동작이 실패하지 않는다.

기본적으로 스트림은 예외를 발생시키지 않는다.

예외를 활성화 하려면 런타임 중에 각 스트림에 대해 예외를 활성화해야 한다.

