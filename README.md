# ros_google_speech_win

[ros_google_speech](https://github.com/naka-lab/ros_google_speech)をWindowsで動かす方法．

## インストール
- このリポジトリをcloneして，その中に[ros_google_speech](https://github.com/naka-lab/ros_google_speech)と[roslib](https://github.com/naka-tomo/roslib)をcloneする

```
git clone https://github.com/naka-lab/ros_google_speech_win.git

cd ros_google_speech_win
git clone https://github.com/naka-lab/ros_google_speech.git
git clone https://github.com/naka-tomo/roslib.git
pip install rospkg
pip install catkin_pkg
```

## 実行方法
- roscoreをUbuntuで動かす
- [run.bat](run.bat)をメモ帳で開き，上部の`ROS_MASTER_URI`と`ROS_HOSTNAME`を環境に合わせて修正
- `cd`でros_google_speech_winフォルダに移動し，`run.bat`をコマンドプロンプトから実行
  ```
  cd ros_google_speech_win
  run.bat
  ```
- 起動後の使い方は[ros_google_speech](https://github.com/naka-lab/ros_google_speech)と同じ

## Windowsから音声認識・合成を使う場合
- [example_grammar.py](example/example_grammar.py)のように，スクリプトの上部で`ROS_MASTER_URI`と`ROS_HOSTNAME`を環境に合わせて設定し，`roslib`へのパスを通す
- pythonで実行する
  ```
  cd example
  python example_grammar.py
  ```
- 使い方は
[ros_google_speech](https://github.com/naka-lab/ros_google_speech)と同じ
