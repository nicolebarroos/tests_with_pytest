import pytest
from django.core.files.uploadedfile import SimpleUploadedFile #new
from movie.models import Movie, Actors
from datetime import datetime

#new
@pytest.fixture
def multiples_actors(db) -> Actors:
    create_file = SimpleUploadedFile('roteiro.pdf', b'these are the contents of the pdf file')
    return Actors.objects.bulk_create(
        [
            Actors(name="Tom Holland", role="Peter I", script=create_file),
            Actors(name="Tobey Maguire", role="Peter II", script=create_file),
            Actors(name="Andrew Garfield", role="Peter III", script=create_file),
        ]
    )


@pytest.mark.freeze_time('2022-02-14')
@pytest.mark.django_db
def test_movie_model(multiples_actors): #new
    movie = Movie(title="Homem-Aranha: Sem Volta para Casa", genre="Ação/Aventura", year="2021")
    movie.save()
    movie.actors.add(multiples_actors[0], multiples_actors[1], multiples_actors[2]) #new
    movie.save()
    assert movie.title == "Homem-Aranha: Sem Volta para Casa"
    assert movie.genre == "Ação/Aventura"
    assert movie.year == "2021"
    assert movie.actors.values().exists() #new
    assert movie.creation_date.strftime('%d/%m/%Y %H:%M:%S %f') == datetime.now().strftime('%d/%m/%Y %H:%M:%S %f')

    assert str(movie) == movie.title
