#!/usr/bin/env python3
#Use: find kmer repeats and index
def most_frequent_kmer(sequence,k):
    length=len(sequence)
    if k>length:
        return "k is bigger than the length of the sequence"
    else:
        if k==length:
            return sequence
        else:
            dic_count={}
            for i in range(length-k+1):
                kmer=sequence[i:i+k]
                if kmer not in dic_count:
                    dic_count[kmer]=1
                else:
                    dic_count[kmer]+=1
            value_key_list=[(value, key) for key, value in dic_count.items()]
            return value_key_list
some=most_frequent_kmer("ACTGATCGATCACTGGCAGCGCTACTGACGTACTG",4)
print(some)