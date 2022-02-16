from Media import Media

class Clip(Media):
  
  def __init__(self, category, name, director, imdbscore, url, duration, casts, creator):
    super().__init__(category, name, director, imdbscore, url, duration, casts)
    self.creator = creator

  
  def show_info(self):
    super().show_info()
    print(f"creator: {self.creator}")


  def edit_media(self):
    super().edit_media()
    self.creator = input('new creator: ')
