#!/usr/bin/env python
import argparse
from Bio import SeqIO
import pandas as pd

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--k', type=int, default=21)
    args = parser.parse_args()

    rows = []
    for rec in SeqIO.parse(args.input, 'fasta'):
        seq = str(rec.seq).upper().replace('T','U')
        for i in range(len(seq)-args.k+1):
            subseq = seq[i:i+args.k]
            rows.append({'seq': subseq, 'label': 0.5})
    pd.DataFrame(rows).to_csv(args.out, index=False)
    print('Wrote', len(rows), 'rows to', args.out)
