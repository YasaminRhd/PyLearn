import pytube, Actor

class Media:

  mediaList = []

  def __init__(self, category, name, director, imdbscore, url, duration, casts):
    self.category = category
    self.name = name
    self.director = director
    self.imdbscore = imdbscore
    self.url = url
    self.duration = duration
    self.casts = []
    for person in casts.split('.'):
      self.casts.append(Actor.Actor(person))
  

  def show_info(self):
    print('------------------------------')
    print(f"Category of the media: {self.category}\nName of the media: {self.name}\nDirector: {self.director}\nIMDB score: {self.imdbscore}\nDuration: {self.duration}\nCasts: {Media.show_casts(self.casts)}")


  def download(self):
    link = self.url
    first_stream = pytube.YouTube(link).streams.first()
    first_stream.download(output_path='./', filename='media.mp4')

    
  def show_casts(casts):
    actors = []
    for person in casts:
      actors.append(person.name)
    return actors


  def edit_media(self):
    self.category = input('Enter new category: ')
    self.name = input('Enter new name: ')
    self.director = input('Enter new director: ')
    self.imdbscore = input('Enter new imdbscore: ')
    self.url = input('Enter new url: ')
    self.duration = input('Enter new duration: ')
    casts = input('Enter new casts(seperated by comma): ')
    self.casts = []
    for person in casts.split(','):
      self.casts.append(Actor.Actor(person))    
