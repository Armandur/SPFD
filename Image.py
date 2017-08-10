class Image:

    def __init__(self, start, index, end, content = None):
        self.start = str(start)
        self.index = int(index)
        self.end = str(end)

    def url(self):
        return str(self.start+str(self.index)+self.end)