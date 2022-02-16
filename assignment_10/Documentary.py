from Media import Media

class Documentary(Media):
  
  def __init__(self, category, name, director, imdbscore, url, duration, casts, narrator):
    super().__init__(category, name, director, imdbscore, url, duration, casts)
    self.narrator = narrator

  
  def show_info(self):
    super().show_info()
    print(f"narrator: {self.narrator}")


  def edit_media(self):
    super().edit_media()
    self.narrator = input('new narrator: ')