# ros_google_speech_win

[ros_google_speech](https://github.com/naka-lab/ros_google_speech)をWindowsで動かす方法．

## インストール
- Windowsでこのリポジトリをcloneして，その中に[ros_google_speech](https://github.com/naka-lab/ros_google_speech)と[ros_portable](https://github.com/naka-tomo/ros_portable)をcloneする

```
git clone https://github.com/naka-lab/ros_google_speech_win.git

cd ros_google_speech_win
git clone https://github.com/naka-lab/ros_google_speech.git
git clone https://github.com/naka-tomo/ros_portable.git
pip install rospkg
pip install catkin_pkg
pip install websocket-server
```

## 実行方法
- roscore動かす（[ros_portable](https://github.com/naka-tomo/ros_portable)を使えばwindowsでも実行可能）
- Windowsで，[run.bat](run.bat)をメモ帳等で開き，上部の`ROS_MASTER_URI`と`ROS_HOSTNAME`を環境に合わせて修正
- `cd`でros_google_speech_winフォルダに移動し，`run.bat`をコマンドプロンプトから実行
  ```
  cd ros_google_speech_win
  run.bat
  ```
- 起動後の使い方は[ros_google_speech](https://github.com/naka-lab/ros_google_speech)と同じ

## Windowsから音声認識・合成を使う場合
- [example_grammar.py](example/example_grammar.py)のように，スクリプトの上部で`ROS_MASTER_URI`と`ROS_HOSTNAME`を環境に合わせて設定し，`ros_portable/python_pakage`へのパスを通す
- pythonで実行する
  ```
  cd example
  python example_grammar.py
  ```
- 使い方は
[ros_google_speech](https://github.com/naka-lab/ros_google_speech)と同じ
