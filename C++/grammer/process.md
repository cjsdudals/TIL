<h3>메모리 처리</h3>
new 연산자 delete 연산자는 각각 메모리를 할당하고 해제하는 연산자이다.

<h3>타입 처리</h3>

|연산|표현식|
|:---|:---:|
|런타임 타입 식별|typeid(x)|
|타입 식별|typeid(t)|
|오브젝트의 크기|sizeof(x) 또는 sizeof x|
|타입의 크기|sizeof(t)|
|인수의 개수|sizeof...(p)|
|타입 인수의 개수|sizeof...(p)|
|맞춤(Alignment)|alignof(x)|
|타입의 맞춤|alignof(y)|

<h3>오류 처리</h3>
throw 연산자는 실행 시 예외를 나타내는데 사용

<h3>오버 로딩 (overloading)</h3>
새로운 타입에 대한 연산자들을 정의할 수 있다.

내장 타입들의 연산자는 변경할 수 없다.

대부분의 연산자는 오버로딩할 수 있다.

<h5>오버로딩할 수 없는 연산자</h5>
<ul>:: 스코프 지정</ul>
<ul>. 멤버 선택</ul>
<ul>.* 포인터를 통한 멤버 선택</ul>
<ul>? 조건부</ul>
<ul>sizeof 타입이나 오브젝트의 크기</ul>
<ul>sizeof... 인수의 개수</ul>
<ul>alignof 타입이나 오브젝트의 메모리 맞춤</ul>
<ul>typeid 타입 식별자</ul>