class Book:
    def __init__(self, title, page, year, writer):
        self.title = title
        self.page = page
        self.year = year
        self.writer = writer
    def tell(self):
        print('Title:"{}", Page:"{}", Year:"{}", Writer:"{}"'.format(self.title, self.page, self.year, self.writer), end=" ")
