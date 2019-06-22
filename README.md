# hitachi_washer

## Pitch detection from WAV file using aubio

一秒に約８回音程（周波数）を出力する。

```
$ aubio pitch -r 8000 -B 2048 -H 1024 -m fcomb -s -90 wcorrel.wav | awk '{print $2}'
```

リサンプリングして、一秒に約８回音程（周波数）を出力する。

```
$ aubio pitch -r 44100 -B 8192 -H 5512 -m fcomb -s -90 wcorrel.wav
```

## Get correlation pitch from wave file

```
$ aubio pitch -r 8000 -B 2048 -H 1024 -m fcomb -s -90 wcorrel.wav | awk '{print $2}' > wcorrel.pitch
```

## Detect correlated pitch from wave file

```
$ aubio pitch -r 8000 -B 2048 -H 1024 -m fcomb -s -90 wcorrel.wav | awk '{print $2}' | python acorrel.py | python wtrigger.py
```

## POST REST server when detect correlated pitche from mic

```
$ python wpitch.py | python acorrel.py | python wtrigger.py | python  wpost $url
```



