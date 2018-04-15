import sublime
import sublime_plugin


class LaravelGotoViewController(sublime_plugin.TextCommand):
    def run(self, edit):
        global callbacks_on_load
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
                root = window.extract_variables()

                controllers_path = root['folder'] + '/app/Http/Controllers/'
                views_path = root['folder'] + '/resources/views/'

                if '@' in text:
                    controller, method = text.split('@')

                    filename = controller + '.php'
                    found_view = window.open_file(controllers_path + filename)

                    if not found_view.is_loading():
                        self.show_at_center(found_view, method)
                    else:
                        sublime.set_timeout(lambda: self.show_at_center(found_view, method), 100)

                elif 'controller' in text.lower():
                    filename = text + '.php'
                    window.open_file(controllers_path + filename)

                else:
                    filename = text + '.blade.php'
                    window.open_file(views_path + filename)

    def show_at_center(self, view, method):
        symbols = view.symbols()

        for region, symbol_method in symbols:
            if symbol_method == method:
                view.show_at_center(region.end())
                view.sel().clear()
                view.sel().add(region.end())

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

