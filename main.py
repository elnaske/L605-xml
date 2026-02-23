from src.ttxml import *

def main():
    doc = parse_tt_xml("data.xml")

    to_treetagger_xml(doc, "res1.xml")

    doc2 = parse_tt_xml("res1.xml")

    to_treetagger_xml(doc2, "res2.xml")
    
    doc3 = parse_tt_xml("res2.xml")

    print(document_to_text(doc2) == document_to_text(doc3))

if __name__=="__main__":
    main()