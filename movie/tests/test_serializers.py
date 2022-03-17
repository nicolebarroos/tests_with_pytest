from movie.serializers import MovieSerializer


def test_valid_movie_serializer():
    valid_serializer_data = {
        "title": "Homem-Aranha: Sem Volta para Casa",
        "genre": "Ação/Aventura",
        "year": "2021"
    }

    serializer = MovieSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_movie_serializer():
    invalid_serializer_data = {
        "title": "Homem-Aranha: Sem Volta para Casa",
        "genre": "Ação/Aventura",
    }

    serializer = MovieSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"year": ["This field is required."]}
