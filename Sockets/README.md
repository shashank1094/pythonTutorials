# Socket Programming

https://realpython.com/python-sockets/

# Server :
```commandline
Connected by ('127.0.0.1', 61998)
Data is : b'POST / HTTP/1.1\r\nUser-Agent: PostmanRuntime/7.35.0\r\nAccept: */*\r\nPostman-Token: 234892d3-5672-401d-89e7-7df48975d2a7\r\nHost: 127.0.0.1:65432\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nContent-Length: 0\r\n\r\n'
Data is : b''


Connected by ('127.0.0.1', 62000)
Data is : b'Hello, world'
Data is : b''


Connected by ('127.0.0.1', 62003)
Data is : b'GET / HTTP/1.1\r\nHost: 127.0.0.1:65432\r\nConnection: keep-alive\r\nsec-ch-ua: "Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "macOS"\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br, zstd\r\nAccept-Language: en-GB,en-US;q=0.9,en;q=0.8\r\n\r\n'
Data is : b''
```

## netstat
```commandline
(.venv) pythonTutorials % netstat -an | grep -i 65432             
Active Internet connections (including servers)
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)    
tcp4       0      0  127.0.0.1.65432        *.*                    LISTEN     


(.venv) pythonTutorials % netstat -an | grep -i 65432
tcp4       0      0  127.0.0.1.65432        127.0.0.1.62009        ESTABLISHED
tcp4       0      0  127.0.0.1.62009        127.0.0.1.65432        ESTABLISHED
tcp4       0      0  127.0.0.1.65432        *.*                    LISTEN     
(.venv) pythonTutorials % netstat -an | grep -i 65432
tcp4       0      0  127.0.0.1.65432        127.0.0.1.62009        FIN_WAIT_2 
tcp4       0      0  127.0.0.1.62009        127.0.0.1.65432        CLOSE_WAIT 
```

## lsof

```commandline
(.venv) pythonTutorials % lsof -i -n | grep -i 65432 
COMMAND     PID       USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
Python    68694 sishashank    3u  IPv4 0xc1915071b49e81ae      0t0  TCP 127.0.0.1:65432 (LISTEN)
(.venv) pythonTutorials % lsof -i -n | head -n +1   

(.venv) pythonTutorials % lsof -i -n | head -n +2
COMMAND     PID       USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
rapportd   1151 sishashank    9u  IPv4 0xb40f0c9e0697fc28      0t0  TCP *:58988 (LISTEN)

```

## ps -aef

```commandline
(.venv) pythonTutorials % ps -aef | head -n +1   
  UID   PID  PPID   C STIME   TTY           TIME CMD
  503 68694 93847   0  2:45AM ??         0:00.04 /Users/sishashank/Desktop/pythonTutorials/.venv/bin/python /Users/sishashank/Desktop/pythonTutorials/Sockets/echo-server.py

```