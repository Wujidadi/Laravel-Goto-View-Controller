class Path:
    def __init__(self, view):
        self.root = view.window().extract_variables()

    def for_controllers(self):
        return self.root['folder'] + '/app/Http/Controllers/'

    def for_views(self):
            return self.root['folder'] + '/resources/views/'
