import sublime
import sublime_plugin


class LaravelGotoViewController(sublime_plugin.TextCommand):
    def run(self, edit):
        # only trigger the command if the cursor is in these scopes
        supported_scopes = [
            "string.quoted.single.php",
            "string.quoted.double.php"
        ]

        self.cursorPos = self.getCursorPos()

        # all scopes at the cursor position
        scopes = self.getScopes()

        for supported_scope in supported_scopes:
            if supported_scope in scopes:

                text = self.getText()

                window = self.view.window()
                window.run_command("show_overlay", {
                    "overlay": "goto",
                    "text": "resources/views/" + text + ".blade.php"}
                )

    def getCursorPos(self):
        return self._getFirstSelection().begin()

    def getScopes(self):
        return self.view.scope_name(self.cursorPos).split(' ')

    def getText(self):
        # expand to single or double quotes
        self._expandSelectionToQuotes()

        region = self._getFirstSelection()

        # extract the word from the region
        text = self.view.substr(region)

        self._clearSelection()
        return self._normalizeSelected(text)

    def _getFirstSelection(self):
        return self.view.sel()[0]

    def _expandSelectionToQuotes(self):
        window = self.view.window()
        window.run_command("expand_selection", {"to": "scope"})

    def _normalizeSelected(self, text):
        text = text.replace('.', '/')
        text = text.replace('\'', '').replace('"', '')
        text = text.replace(')', '').replace('(', '')
        return text

    def _clearSelection(self):
        self.view.sel().clear()
        self.view.sel().add(self.cursorPos)
