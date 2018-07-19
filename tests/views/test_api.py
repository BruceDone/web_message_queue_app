# -*- coding: utf-8 -*-
import pytest
from src.app_factory import create_app


class TestApi():
    @pytest.fixture
    def client(self):
        app = create_app()

        return app.test_client()

    async def test_get_time(self, client):
        res = await client.get('/time')
        assert res
