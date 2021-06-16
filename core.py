import mainWin
import aboutWin
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import random

class core(QtWidgets.QMainWindow, mainWin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setConnect()

    def setupUi(self, parent):
        super().setupUi(parent)
        

    def setConnect(self):
        self.action_QT.triggered.connect(QtWidgets.QApplication.aboutQt)
        self.pushButton.clicked.connect(self.clicked)
        self.pushButton.setShortcut(" ")
        self.action_about.triggered.connect(self.about)

    def about(self):
        class AboutDialog(QtWidgets.QDialog, aboutWin.Ui_aboutWin):
            def __init__(self, parent):
                super().__init__(parent)
                self.setupUi(self)
        AboutDialog(self).show()

    def resizeEvent(self, Event):
        super().resizeEvent(Event)
        f = QtGui.QFont()
        re: QtGui.QResizeEvent = Event
        f.setFamily('MS Mincho')
        f.setPointSize(re.size().height()/2.5)
        self.label.setFont(f)

    def clicked(self):
        hiragana = ('あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に',
                    'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を')
        katakana = ('ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ',
                    'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ')
        usei = ('が', 'ぎ', 'ぐ', 'げ', 'ご', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'だ', 'ぢ', 'づ', 'で', 'ど', 'ば', 'び', 'ぶ', 'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ',
                'ぽ', 'ガ', 'ギ', 'グ', 'ゲ', 'ゴ', 'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ', 'ダ', 'ヂ', 'ヅ', 'デ', 'ド', 'バ', 'ビ', 'ブ', 'ベ', 'ボ', 'パ', 'ピ', 'プ', 'ペ', 'ポ')
        youon = ('きゃ', 'きゅ', 'きょ', 'しゃ', 'しゅ', 'しょ', 'ちゃ', 'ちゅ', 'ちょ', 'にゃ', 'にゅ', 'にょ', 'ひゃ', 'ひゅ', 'ひょ', 'みゃ', 'みゅ', 'みょ', 'りゃ', 'りゅ', 'りょ', 'ぎゃ', 'ぎゅ', 'ぎょ', 'じゃ', 'じゅ', 'じょ', 'びゃ', 'びゅ', 'びょ', 'ぴゃ', 'ぴゅ',
                 'ぴょ', 'キャ', 'キョ', 'キュ', 'シャ', 'シュ', 'ショ', 'チャ', 'チュ', 'チョ', 'ニャ', 'ニュ', 'ニョ', 'ヒャ', 'ヒュ', 'ヒョ', 'ミャ', 'ミュ', 'ミョ', 'リャ', 'リュ', 'リョ', 'ギャ', 'ギュ', 'ギョ', 'ジャ', 'ジュ', 'ジョ', 'ビャ', 'ビュ', 'ビョ', 'ピャ', 'ピュ', 'ピョ')
        sets = []
        if self.checkBox_2.isChecked():
            sets.extend(hiragana)
        if self.checkBox_3.isChecked():
            sets.extend(katakana)
        if self.checkBox_4.isChecked():
            sets.extend(usei)
        if self.checkBox.isChecked():
            sets.extend(youon)

        random.seed()
        for i in range(40):
            
            self.label.setText(sets[random.randint(0, len(sets)-1)])
            QtWidgets.QApplication.processEvents()
