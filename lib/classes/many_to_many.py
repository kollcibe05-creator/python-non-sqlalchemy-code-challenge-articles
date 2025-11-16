class Article:
    all = []
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self.title = title
        Article.all.append(self)  #adds all of the attributes in a list if they meet requirements and make them globally scoped for access
    @property
    def title(self):
        return self._title   
    @title.setter
    def title(self, title):
        if type(title) == str and 5<len(title)<=50 :
            self._title = title  
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError('Author must be instance of Author') 
        self._author = author       
    @property
    def magazine(self):
        return self._magazine  
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError('Magazine must be instance of Magazine')   
        self._magazine = magazine                    
        
class Author:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if(hasattr(self, "_name")):
            return    
        elif(type(name) == str and len(name)>0):
            self._name = name   
    def articles(self):
        return [article for article in Article.all if article.author is self]
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))
    def add_article(self, magazine, title):
        return Article(self, magazine, title) #Error
    def topic_areas(self):
        magazines = self.magazines()
        if not magazines:
            return None  
        return list(set(magazine.category for magazine in magazines))          

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if type(name) == str and 2<=len(name)<=16:
            self._name = name 
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if type(category) == str and len(category)>0:
            self._category = category
    def articles(self):
        return [article for article in Article.all if article.magazine is self]
    def contributors(self):
        return list(set(article.author for article in self.articles()))
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        contributors = [author for author, count in author_counts.items() if count>2]
        return contributors if contributors else None
# mark = Author("Mark")
# # print(hasattr(mark, "name"))      
# print(mark.name)
# # print(setattr(mark, "name", "Luke"))

# magazine = Magazine("Vogue","Fashion")

# # print(magazine.category)
# # print(type(Magazine))