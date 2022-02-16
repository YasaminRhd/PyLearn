from Media import Media

class Movie(Media):
  
  def __init__(self, category, name, director, imdbscore, url, duration, casts, genre):
    super().__init__(category, name, director, imdbscore, url, duration, casts)
    self.genre = genre

  
  def show_info(self):
    super().show_info()
    print(f"genre: {self.genre}")


  def edit_media(self):
    super().edit_media()
    self.genre = input('new genre: ')