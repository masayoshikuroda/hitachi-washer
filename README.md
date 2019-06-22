# hitachi_washer

## Pitch detection from WAV file

一秒に約８回音程（周波数）を出力する。

```
$ aubio pitch -r 8000 -B 2048 -H 1024 -m fcomb -s -90 test.wav | awk '{print $2}'
```

リサンプリングして、一秒に約８回音程（周波数）を出力する。

```
$ aubio pitch -r 44100 -B 8192 -H 5512 -m fcomb -s -90 sine.wav 
```

