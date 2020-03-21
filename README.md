# awb

Auto White Balance

ダウンロードURL

https://github.com/tomoemagica/awb

ダウンロードした、awb.pyをDFL\worksapaceの下に置きます


使用方法

py awb.py

機能

DFL\worksapace\data_srcの下の、動画のコマ画像を、自動ホワイトバランスします

自動ホワイトバランス後の動画のコマ画像は、DFL\worksapace\data_src\awbフォルダに書き込まれます

元画像のDFL\worksapace\data_srcの下の画像はそのままです

srcの顔色がバラバラな時に、顔色の補正に役立つかも知れません


# clahe.py

カラー画像を Equalize(ヒストグラム平坦化)します(より高度な平坦化(CLAHE))

ダウンロードURL

https://github.com/tomoemagica/awb

ダウンロードした、clahe.pyをDFL\worksapaceの下に置きます


使用方法

py clahe.py

機能

DFL\worksapace\data_srcの下の、動画のコマ画像を、輝度だけヒストグラム平坦化します

輝度だけヒストグラム平坦化後の動画のコマ画像は、DFL\worksapace\data_src\claheフォルダに書き込まれます

元画像のDFL\worksapace\data_srcの下の画像はそのままです

srcの顔色がバラバラな時に、顔色の補正に役立つかも知れません


# const.py

カラー画像を Contrast stretching(コントラストストレッチ)します

ダウンロードURL

https://github.com/tomoemagica/awb

ダウンロードした、const.pyをDFL\worksapaceの下に置きます


使用方法

py const.py

機能

DFL\worksapace\data_srcの下の、動画のコマ画像を、コントラストストレッチします

コントラストストレッチ後の動画のコマ画像は、DFL\worksapace\data_src\constフォルダに書き込まれます

元画像のDFL\worksapace\data_srcの下の画像はそのままです

srcの顔色がバラバラな時に、顔色の補正に役立つかも知れません


#別の使用方法

awb.py, clahe.py, const.pyなどは、色味が変な動画を、コマにしておいて

コマ画像を変換

ffmpegで元の動画の映像トラックに

Mkvtoolnix-guiで元の動画の音声トラックを抜き取る

Mkvtoolnix-guiで変換された映像トラックと音声トラックをMerge

で動画の自動ホワイトバランスや輝度ヒストグラム平坦化、コントラストストレッチできます
