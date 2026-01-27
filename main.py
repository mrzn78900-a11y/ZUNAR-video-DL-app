from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import threading
from downloader import download_video

class ZunarUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=20, spacing=10)

        self.url = TextInput(
            hint_text="Paste YouTube / Instagram link",
            size_hint=(1, 0.2)
        )

        self.status = Label(text="ZUNAR DL Ready")

        self.btn = Button(
            text="Download HD",
            size_hint=(1, 0.2)
        )
        self.btn.bind(on_press=self.start)

        self.add_widget(self.url)
        self.add_widget(self.btn)
        self.add_widget(self.status)

    def start(self, instance):
        self.status.text = "Downloading..."
        threading.Thread(target=self.download).start()

    def download(self):
        try:
            download_video(self.url.text)
            self.status.text = "Download Complete ✅"
        except:
            self.status.text = "Error ❌"

class ZunarDL(App):
    def build(self):
        self.title = "ZUNAR DL"
        return ZunarUI()

ZunarDL().run()
