# -*- coding: utf-8 -*-
import pytest
from src.job.word import count_words


class TestWord():
    def test_word_counts(self):
        count_words('test')

    def test_pass_invalidate(self):
        with pytest.raises(TypeError):
            count_words(1)
