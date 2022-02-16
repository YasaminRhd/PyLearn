from Media import Media

class Series(Media):
  
  def __init__(self, category, name, director, imdbscore, url, duration, casts, genre, episodes, seasons):
    super().__init__(category, name, director, imdbscore, url, duration, casts)
    self.genre = genre
    self.episodes = episodes
    self.seasons = seasons

  
  def show_info(self):
    super().show_info()
    print('genre:', self.genre)
    print('episodes:', self.episodes)
    print('seasons:', self.seasons)
