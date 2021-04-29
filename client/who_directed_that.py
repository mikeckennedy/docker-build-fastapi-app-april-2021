import requests

from movie_model import MovieModel


def main():
    title = get_title_from_user()
    movie: MovieModel = get_movie_from_svc(title)
    if not movie:
        print("Sorry, no movie found!")
        return

    print(f'{movie.title} was released in {movie.year} and directed by {movie.director}!')


def get_movie_from_svc(title):
    url = f'http://127.0.0.1:8000/api/movie/{title}'
    resp = requests.get(url)
    resp.raise_for_status()

    return MovieModel(**resp.json())


def get_title_from_user():
    return input("What title to search for? ")


if __name__ == '__main__':
    main()
