from .article import Article

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        self._name = name

    @property
    def name(self):
        return self._name   

 
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list({mag.category for mag in mags})
