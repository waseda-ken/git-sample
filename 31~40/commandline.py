import argparse

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('target1')
    parser.add_argument('target2')
    args=parser.parse_args()
    print(args.target1)
    print(args.target2)
