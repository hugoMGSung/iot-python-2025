# py02_gemini_app.py
# TKinter를 클래스화 
from tkinter import *
from tkinter.messagebox import * 
from tkinter.scrolledtext import *
from tkinter.font import *
import google.generativeai as genai

genai.configure(api_key='AIzaSyCYYMrvioYlwcLqlsE-sFQb2uaW33ZptB8')
model = genai.GenerativeModel('gemini-1.5-flash')

class window(Tk):
    def __init__(self):
        super().__init__() # 부모객체도 같이 초기화
        self.title('제미나이 챗봇 v2.0')
        self.geometry('730x450')
        self.iconbitmap('./image/chatbot.ico')
        # 클래스 작업할땐 self... 유심히. 
        self.protocol('WM_DELETE_WINDOW', self.onClosing)

        self.initWindow() # 윈도우 화면 초기화 멤버함수(메서드)

    def initWindow(self):
        self.myFont = Font(family='NanumGothic', size=10)
        self.boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)

        self.inputFrame = Frame(self, width=730, height=30, bg='#EFEFEF')
        self.inputFrame.pack(side=BOTTOM, fill=BOTH)

        self.textMessage = Text(self.inputFrame, width=75, height=1, wrap=WORD, 
                                font=self.myFont)
        # self.textMessage.bind('<Key>', self.keypress)  
        self.textMessage.pack(side=LEFT, padx=15)

        self.buttonSend = Button(self.inputFrame, text='전송', bg='green', fg='white',
                    font=self.myFont,
                    command=self.responseMessage)
        self.buttonSend.pack(side=RIGHT, padx=20, pady=5)

        # 나머지 부분 복사
        self.textResult = ScrolledText(self, wrap=WORD, bg='#000000', fg='white', font=self.myFont) # bg='black'
        self.textResult.pack(fill=BOTH, expand=True)

        # 10. 스크롤텍스트에 나올 메시지 디자인
        self.textResult.tag_configure('user', font=self.boldFont, foreground='yellow')
        self.textResult.tag_configure('ai', font=self.myFont, foreground='limegreen')  #89F336
        self.textResult.tag_configure('error', font=self.boldFont, foreground='red')

        # 9. 실행 후 바로 입력창에 포커스가 가도록
        self.textMessage.focus_set()

    def responseMessage(self):  # 내용 수정
        showinfo('동작', 
                 f'이제 API를 호출하면 됩니다!\n{self.textMessage.get("1.0", END)}')

    def onClosing(self):
        if askyesno('종료확인', '종료하시겠습니까?'):
            self.destroy() # 완전 종료

if __name__ == '__main__':
    print('Tkinter 클래스 시작!')
    app = window() # Tkinter 클래스 객체 생성
    app.mainloop()
