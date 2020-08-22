
class BAM():
    def __init__(self, filename, title=''):
        self.filename = filename
        if title != '':
            self.title = title
        else:
            self.title = self.filename.split('/')[-1]

    def __str__(self):
        return self.title
