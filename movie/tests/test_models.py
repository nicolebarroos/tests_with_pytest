import pytest

from movie.models import Movie


@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title="Homem-Aranha: Sem Volta para Casa", genre="Ação/Aventura", year="2021")
    movie.save()
    assert movie.title == "Homem-Aranha: Sem Volta para Casa"
    assert movie.genre == "Ação/Aventura"
    assert movie.year == "2021"

    assert movie.created_date
    assert movie.update_date
    assert str(movie) == movie.title