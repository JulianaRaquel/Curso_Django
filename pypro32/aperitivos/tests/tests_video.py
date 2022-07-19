from django.urls import reverse
import pytest
from model_mommy import mommy
from pypro32.aperitivos.models import Video
from pypro32.django_assertions import assert_contains


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}"')

