from argparse import ArgumentParser
import numpy as np

def load_embed(filename, max_vocab=-1):
    words, embeds = [], []
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            word, vector = line.rstrip().split(' ', 1)
            vector = np.fromstring(vector, sep=' ')
            words.append(word)
            embeds.append(vector)
            if len(embeds) == max_vocab:
                break
    return words, np.array(embeds)


def main():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    parser.add_argument('--normalize', default='renorm,center,renorm,center,renorm,center,renorm,center,renorm,center,renorm', type=str)
    parser.add_argument('--max_vocab', default=-1, type=int)
    args = parser.parse_args()

    words, embeds = load_embed(args.input_file, max_vocab=args.max_vocab)

    for t in args.normalize.split(','):
        if t == 'center':
            embeds -= embeds.mean(axis=0)[np.newaxis, :]
        elif t == 'renorm':
            embeds /= np.linalg.norm(embeds, axis=1)[:, np.newaxis] + 1e-8
        elif t != '':
            raise Exception('Unknown normalization type: "%s"' % t)

    with open(args.output_file, 'w') as f:
        print >> f, embeds.shape[0], embeds.shape[1]
        for word, embed in zip(words, embeds):
            vector_str = ' '.join(`x` for x in embed)
            print >> f, word, vector_str


if __name__ == '__main__':
    main()
