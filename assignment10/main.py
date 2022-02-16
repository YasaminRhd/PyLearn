import Media, Movie, Documentary, Series, Clip
from Media import Media

class Main:

  def __init__(self, address):
    database = open(address, 'r+')
    data = database.read()
    media = data.strip().split('\n')
    for line in media:
      info = line.split(',')
      if info[0] == 'movie':
        Media.mediaList.append(Movie.Movie(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7]))
      elif info[0] == 'documentary':
        Media.mediaList.append(Documentary.Documentary(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7]))
      elif info[0] == 'series':
        Media.mediaList.append(Series.Series(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9]))
      else:
        Media.mediaList.append(Clip.Clip(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7]))
    print('Loading the database... Done.')
    database.close()
    Main.menu()

    
  def menu():
    while True:
      choice = int(input('''
      1. add new media to the list
      2. edit media's info
      3. search by name
      4. remove media
      5. show media list
      6. advance search
      7. save and exit
      \t> '''))
      match choice:
        case 1:
          Main.add_media()
        case 2:
          Main.edit_media()
        case 3:
          name = input('name: ').title()
          media = Main.search(name)
          if media:
            media.show_info()
          else: print('404. Not Found.')
        case 4:
          Main.remove_media()
        case 5:
          Main.show_media_list()
        case 6:
          Main.advance_search()
        case 7:
          Main.save_and_exit()
          exit()


  def add_media():
    category = input('Choose between (Movie, Documentary, Series, Clip): ').lower()
    if category == 'movie':
      Media.mediaList.append(Movie.Movie(category, input('name: '), input('director: '), input('imdb score: '), input('url: '), input('duration in minutes: '), input('casts (seperated by comma): '), input('genre: ')))
    elif category == 'documentary':
      Media.mediaList.append(Documentary.Documentary(category, input('name: '), input('director: '), input('imdb score: '), input('url: '), input('duration in minutes: '), input('casts (seperated by comma): '), input('narrator: ')))
    elif category == 'series':
      Media.mediaList.append(Series.Series(category, input('name: '), input('director: '), input('imdb score: '), input('url: '), input('duration in minutes: '), input('casts (seperated by comma): '), input('genre: '), input('episodes: '), input('seasons: ')))
    elif category == 'clip':
      Media.mediaList.append(Clip.Clip(category, input('name: '), input('director: '), input('imdb score: '), input('url: '), input('duration in minutes: '), input('casts (seperated by comma): '), input('creator: ')))
    else: print("Category not supported!")
      
    
  def search(name):
    for media in Media.mediaList:
      if media.name == name:
        return media
    return False


  def edit_media():
      name = input('name: ').title()
      media = Main.search(name)
      if media:
        media.edit_media()
        print('edited successfully.')
      else: print('404. Not Found.')


  def remove_media():
    name = input('name: ').title()
    media = Main.search(name)
    if media:
      Media.mediaList.remove(media)
      print('Removed.')
    else: print('404. Not Found.')


  def show_media_list():
    for media in Media.mediaList:
      media.show_info()


  def advance_search():
    flag = False
    duration = list(map(int, input("Enter your preferred duration range: ").split()))
    for media in Media.mediaList:
      if media.category == 'movie' and duration[0] <= int(media.duration) <= duration[1]:
        media.show_info()
        flag = True
    if not flag:
      print("Sorry, couldn't find any movie in that range.")
  

  def save_and_exit():
    database = open(address, 'w')
    for media in Media.mediaList:
      actors = Media.show_casts(media.casts)
      casts = '.'.join(actors)
      if media.category == 'movie':
        string = f"{media.category},{media.name},{media.director},{media.imdbscore},{media.url},{media.duration},{casts},{media.genre}"
        database.write(string + '\n')
      elif media.category == 'documentary':
        string = f"{media.category},{media.name},{media.director},{media.imdbscore},{media.url},{media.duration},{casts},{media.narrator}"
        database.write(string + '\n')
      elif media.category == 'series':
        string = f"{media.category},{media.name},{media.director},{media.imdbscore},{media.url},{media.duration},{casts},{media.genre},{media.episodes},{media.seasons}"
        database.write(string + '\n')
      elif media.category == 'clip':
        string = f"{media.category},{media.name},{media.director},{media.imdbscore},{media.url},{media.duration},{casts},{media.creator}"
        database.write(string + '\n')
    database.close()


address = "Pylearn/Session 10/database.txt"
Main(address)
