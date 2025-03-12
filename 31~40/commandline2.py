import argparse

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('language',choices=['English','Japanese'])
    args=parser.parse_args()
    print(args.language)