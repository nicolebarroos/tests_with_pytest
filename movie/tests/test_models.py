import pytest

from movie.models import Movie
from datetime import datetime

@pytest.mark.freeze_time('2022-02-14')
@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title="Homem-Aranha: Sem Volta para Casa", genre="Ação/Aventura", year="2021")
    movie.save()
    assert movie.title == "Homem-Aranha: Sem Volta para Casa"
    assert movie.genre == "Ação/Aventura"
    assert movie.year == "2021"
    assert movie.creation_date.strftime('%d/%m/%Y %H:%M:%S %f') == datetime.now().strftime('%d/%m/%Y %H:%M:%S %f')

    assert str(movie) == movie.title
