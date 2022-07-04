from django.urls import reverse
import pytest

from pypro32.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp):
    assert_contains(resp, '<h1>Vídeo Aperitivo: Motivação </h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/726398954?h=640cb055dc&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" ')

