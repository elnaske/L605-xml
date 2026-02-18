from src.ttxml import *

def main():
    line = "Interview	NN	interview	NN1	NOUN	root	Inter-view"
    print(parse_token_line(line))

if __name__=="__main__":
    main()