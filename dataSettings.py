import os
import json
import sys
import random
from tkinter import *
from tkinter import messagebox 
from termcolor import cprint
from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll, Center
from textual.widgets import Button, ContentSwitcher, DataTable, Markdown, Static, LoadingIndicator, Pretty

messagebox.showwarning("WARNING!", "If this program is run in a 'dumb terminal', it will most likely not work\nPlease make sure this program is run in the windows 'terminal' app and not command prompt")

configJson = json.load(open("./config.json"))
dataJsonFile = json.load(open("./data.json"))
print(dataJsonFile)
markdownWelcomeMessage = """# Welcome!
At the top you will notice a bunch of buttons to edit the config, data, and more!

## This program uses textual for selecting data. if you are unable to see the buttons, you may be using a 'dumb terminal' and this program may not work
"""

class ContentSwitcherApp(App[None]):
    CSS_PATH = "dataSettings.tcss"

    def compose(self) -> ComposeResult:
        with Horizontal(id="buttons"):
            yield Button("Welcome!", id="markdown")  
            yield Button("Data", id="data-table")
            yield Button("Reload Data", id="loadDataJsons")

        with ContentSwitcher(initial="markdown"):  
            yield Pretty(object=dataJsonFile, id="data-table")
            with VerticalScroll(id="markdown"):
                yield Markdown(markdownWelcomeMessage)
            with LoadingIndicator(id="loadDataJsons"):
                configJson = json.load(open("config.json"))
                dataJsonFile = json.load(open("data.json"))
                yield Markdown("# Loaded Files!")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one(ContentSwitcher).current = event.button.id  


if __name__ == "__main__":
    ContentSwitcherApp().run()