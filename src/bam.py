
class BAM():
    def __init__(self, filename, title=''):
        self.filename = filename
        self.title = title if title else self.filename.split('/')[-1]
        self.title2 = self.title.replace(' ', '_').replace('(', '_').replace(')', '_')
        self.ref = None

    def __str__(self):
        return self.title

    def getSamfileFlags(self):
        if self.filename.endswith('.bam'):
            return 'rb'
        elif self.filename.endswith('.cram'):
            return 'rc'
        else:
            return 'r'
    
    def setReference(self, ref):
        self.ref = ref

    def getReference(self):
        return self.ref