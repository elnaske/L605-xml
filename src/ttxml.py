# Download:
# https://raw.githubusercontent.com/amir-zeldes/gum/refs/heads/master/xml/GUM_interview_chomsky.xml

class Token:
    def __init__(self, word, penn_pos, lemma, claws_pos, upos, deprel, morph):
        self.word = word
        self.penn_pos = penn_pos
        self.lemma = lemma
        self.claws_pos = claws_pos
        self.upos = upos
        self.deprel = deprel
        self.morph = morph

    def __repr__(self):
        return f"Token({self.word!r}, {self.upos!r})"


class Sentence:
    def __init__(self, sent_type=None, transition=None):
        self.type = sent_type
        self.transition = transition
        self.tokens = []
        self.speaker = None

    def __repr__(self):
        words = ' '.join(t.word for t in self.tokens[:5])
        if len(self.tokens) > 5:
            words += ' ...'
        return f"Sentence(type={self.type!r}, {len(self.tokens)} tokens, {words!r})"


class Paragraph:
    def __init__(self):
        self.sentences = []

    def __repr__(self):
        return f"Paragraph({len(self.sentences)} sentences)"


class Document:
    def __init__(self, doc_id=None):
        self.id = doc_id
        self.paragraphs = []

    def __repr__(self):
        n_sents = sum(len(p.sentences) for p in self.paragraphs)
        return f"Document({self.id!r}, {n_sents} sentences)"


def is_xml_close_tag(line):
    return line.starts_with("</") and line.endswith(">")


def parse_xml_close_tag(line):
    if is_xml_close_tag(line):
        return line.strip("<>/")


def is_xml_open_tag(line):
    return line.starts_with("<") and not line.starts_with("</") and line.endswith(">")


def parse_xml_open_tag(line):
    if is_xml_open_tag(line):
        return line.split()[0].strip('<>')


def is_token_line(line):
    pass


def parse_token_line(line):
    pass


def sentence_to_text(sentence):
    pass


def document_to_text(doc):
    pass


def parse_tt_xml(tt_xml_filepath):
    with open(tt_xml_filepath, "r") as f:
        lines = f.readlines()



def to_treetagger_xml(doc):
    pass
