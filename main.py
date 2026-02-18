from src.ttxml import *

def main():
    doc = parse_tt_xml("data.xml")
    print(doc.paragraphs[0].sentences[0].tokens[0].word)
    print(len(doc.paragraphs[0].sentences))

if __name__=="__main__":
    main()