GPIO 함수

```cpp
DigitalOut 변수이름(핀번호); // 핀 번호를 출력 모드로 설정해 변수로 사용한다.
변수이름.write(1); // 핀으로 HIGH값 출력(함수)
변수이름 = 0; // 핀으로 LOW값 출력(연산자)
변수이름.is_connected(void) // GPIO 핀에 연결되어있는지 사용
변수이름.mode(PinMode pull) // PullUp, PullDown, PullNone, OpenDrain, PullDefault 중 선택
변수이름.read() // 현재 핀의 상태
```

PC와 UART 통신

```cpp
Serial pc(SERIAL_TX, SERIAL_RX); // UART 통신을 위한 설정
pc.printf(""); // pc에 출력
pc.putc(); // pc로 데이터 보내기
pc.getc(); // pc로 데이터 받아오기
```

주기적인 데이터 처리
```cpp
wait(기다릴 시간) // 함수 사용 시점부터 해당 시간만큼 기다림
wait_ms()
wait_us()

Timer t1; // 타이머처럼 시작하면 멈출때까지 계속 시간이 흘러감
t1.start();
t1.reset();
t1.stop();
t1.read();

Ticker t1; // 콜백 함수를 사용하여 초 만큼 함수를 계속 실행함
t1.attach(함수, 초);

Timeout flipper; // 콜백 함수를 사용하여 함수를 초 뒤에 한번만 실행함
flipper.attach(함수, 초);
```