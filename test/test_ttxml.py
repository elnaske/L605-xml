import pytest
from src.ttxml import *

@pytest.fixture
def open_tag_line():
    return '<s type="frag" transition="establishment">'

@pytest.fixture
def close_tag_line():
    return '</s>'

@pytest.fixture
def token_line():
    return 'Interview	NN	interview	NN1	NOUN	root	Inter-view'

def test_is_xml_close_tag(open_tag_line, close_tag_line, token_line):
    assert is_xml_close_tag(close_tag_line)
    assert not is_xml_close_tag(open_tag_line)
    assert not is_xml_close_tag(token_line)


def test_parse_xml_close_tag(open_tag_line, close_tag_line, token_line):
    assert parse_xml_close_tag(close_tag_line) == "s"

    with pytest.raises(ValueError):
        parse_xml_close_tag(open_tag_line)
    with pytest.raises(ValueError):
        parse_xml_close_tag(token_line)

def test_is_xml_open_tag(open_tag_line, close_tag_line, token_line):
    assert is_xml_open_tag(open_tag_line)
    assert not is_xml_open_tag(close_tag_line)
    assert not is_xml_open_tag(token_line)

def test_parse_xml_open_tag(open_tag_line, close_tag_line, token_line):
    assert parse_xml_open_tag(open_tag_line) == "s"

    with pytest.raises(ValueError):
        parse_xml_open_tag(close_tag_line)
    with pytest.raises(ValueError):
        parse_xml_open_tag(token_line)

def test_is_token_line(open_tag_line, close_tag_line, token_line):
    assert is_token_line(token_line)
    assert not is_token_line(open_tag_line)
    assert not is_token_line(close_tag_line)

def test_parse_token_line(open_tag_line, close_tag_line, token_line):
    assert parse_token_line(token_line) == Token("Interview", "NN", "interview", "NN1", "NOUN", "root", "Inter-view")

    with pytest.raises(ValueError):
        parse_token_line(close_tag_line)
    with pytest.raises(ValueError):
        parse_token_line(open_tag_line)


# def test_parse_token_line(line):
#     pass

# def test_sentence_to_text(sentence):
#     pass


# def test_document_to_text(doc):
#     pass


# def test_parse_tt_xml(tt_xml_filepath):
#     pass

# def test_to_treetagger_xml(doc):
#     pass
