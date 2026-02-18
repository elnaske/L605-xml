# Download:
# https://raw.githubusercontent.com/amir-zeldes/gum/refs/heads/master/xml/GUM_interview_chomsky.xml

import re

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
    return line.startswith("</") and line.endswith(">")


def parse_xml_close_tag(line):
    if not is_xml_close_tag(line):
        raise ValueError("Line does not contain an XML close tag.")
    return line.strip("<>/")


def is_xml_open_tag(line):
    return line.startswith("<") and not line.startswith("</") and line.endswith(">")


def parse_xml_open_tag(line):
    if not is_xml_open_tag(line):
        raise ValueError("Line does not contain an XML open tag.")
    tag_name = line.split()[0].strip('<>')
    attributes_dict = {}

    pattern = r'\b(\w+)="(\w+)"'

    for arg in re.findall(pattern, line):
        k, v = arg
        attributes_dict[k] = v

    return tag_name, attributes_dict


def is_token_line(line):
    return '\t' in line and not line.startswith('<')


def parse_token_line(line):
    if not is_token_line(line):
        raise ValueError("Line does not contain any tokens.")
    
    fields = line.split('\t')
    return Token(*fields)


def sentence_to_text(sentence):
    pass


def document_to_text(doc):
    pass


def parse_tt_xml(tt_xml_filepath):
    with open(tt_xml_filepath, "r") as f:
        lines = f.readlines()

    doc = None
    current_sentence = None
    current_paragraph = None
    current_speaker = None

    for line in lines:
        line = line.strip()
        if is_xml_open_tag(line):
            tag, args = parse_xml_open_tag(line)
            if tag == "text":
                # args = line.split()
                # id = args[1].split('=')[1].strip('"')
                doc = Document(args["id"])
            if tag == "s":
                # args = line.split()
                # sent_args = [args[i].split('=')[1].strip('"') for i in range(1,len(args))]
                current_sentence = Sentence(args["type"], args["transition"])
            if tag in ["head", "p", "sp", "caption"]:
                current_paragraph = Paragraph()
            if tag == "sp":
                current_speaker = args["who"]

        elif is_xml_close_tag(line):
            tag = parse_xml_close_tag(line)
            if tag == "s":
                current_paragraph.sentences += [current_sentence]
                current_sentence = None
            if tag in ["head", "p", "sp", "caption"]:
                doc.paragraphs += [current_paragraph]
                current_paragraph = None
            if tag == "sp":
                current_speaker = None
        elif is_token_line(line):
            current_sentence.tokens += [parse_token_line(line)]
            current_sentence.speaker = current_speaker
    
    return doc



def to_treetagger_xml(doc):
    pass
