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

## 検出したい音程ファイルを、WAVファイルから生成

```
$ aubio pitch -r 8000 -B 2048 -H 1024 -m fcomb -s -90 wcorrel.wav | awk '{print $2}' > wcorrel.pitch
```

## WAVファイルから音程を検出

```
$ aubio pitch -r 8000 -B 2048 -H 1024 -m fcomb -s -90 target.wav | awk '{print $2}' | python acorrel.py | python wtrigger.py
```

## マイクから音程を検出したらRESTサーバにPOSTする

```
$ python wpitch.py | python acorrel.py | python wtrigger.py | python  wpost $url
```



