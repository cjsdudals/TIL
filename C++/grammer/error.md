<h1>Error (오류 처리)</h1>
<h3>단정 (Assertion)</h3>
프로그래밍 오류를 감지하기 위한 방법

cassert 헤더파일의 assert의 매크로는 포현식을 계산한 뒤 결과가 false 면 프로그램을 즉시 종료한다.

```cpp
#define NDEBUG
#include <cassert>
```
ㄴ> 모든 단정 비활성화

<h3>예외 (Exception)</h3>
프로그램의 적절한 지속을 방해하는 예외적인 상황을 위한 방법

<h5>동기 부여</h5>
잘못될 수 있는 모든 경우에 대해 검사를 수행하고 호출자에게 적절한 오류 코드를 알려준다.

호출자가 반환코드를 무시할 수 있다.

<h5>throw (던지기)</h5>

```cpp
throw error
```

예외가 발생할 경우 적절한 예외 처리로 전달한다.

<h5>try-catch (잡기)</h5>

```cpp
try {}
catch (exception) {}
```

문제가 생길것 같은 블록을 try 로 감싸고 닫는 중괄호 뒤에서 예외를 잡고 가능하다면 복구를 할 수 있다.

<h3>static_assert (정적 단정)</h3>
후에 설명