import pytest
from rest_framework.exceptions import ErrorDetail

from movie.serializers import MovieSerializer
from datetime import datetime
from rest_framework.utils import json
from rest_framework.utils.encoders import JSONEncoder


def test_valid_movie_serializer():
    valid_serializer_data = {
        "title": "Homem-Aranha: Sem Volta para Casa",
        "genre": "Ação/Aventura",
        "year": "2021",
        "creation_date": '2022-02-14T00:00:00-03:00'
    }

    serializer = MovieSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert json.loads(json.dumps(serializer.validated_data, cls=JSONEncoder)) == valid_serializer_data
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
    assert serializer.errors == {"year": [ErrorDetail(string='Este campo é obrigatório.', code='required')]}
