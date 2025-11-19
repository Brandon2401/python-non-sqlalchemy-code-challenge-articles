from .article import Article

class Magazine:

    def __init__(self, name, category):
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles=[article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors=[
            author for author in self.contributors()
            if len([a for a in self.articles() if a.author is author]) > 2
        ]
        return authors if authors else None 
