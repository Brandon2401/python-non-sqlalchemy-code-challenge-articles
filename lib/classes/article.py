class Article:
    all = []

    def __init__(self, author, magazine, title):
        
        if not hasattr(author, "name"):
            raise TypeError("Author must be an instance of Author.")
        
        if not hasattr(magazine, "category"):
            raise TypeError("Magazine must be an instance of Magazine.")
       
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")

        self._title = title
        self.author = author
        self.magazine = magazine

        Article.all.append(self)

   
    @property
    def title(self):
        return self._title

    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not hasattr(value, "name"):
            raise TypeError("Author must be an Author instance.")
        self._author = value

    
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not hasattr(value, "category"):
            raise TypeError("Magazine must be a Magazine instance.")
        self._magazine = value
