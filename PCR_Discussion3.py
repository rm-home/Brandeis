#!/usr/bin/env python3
#Use: Sample simulation of PCR

#My inputs; all primers given must be 5' to 3'. Remember the reverse primer is on the complimentry strand(bottom) and you have to flip it as its 3' to 5'
Forward_Primer="ACTGATCGATCGGATCGGATT"
Reverse_Primer="GTACTGACGTAGCTTAATGCAG"  # If you loaded this into a viewer this is complementry to the 5' sequence of "CTGCATTAAGCTACGTCAGTAC"  would look like "GACGTAATTCGATGCAGTCATG" 3'-5'
Sequence="ATGCTACTGATCGATCGGATCGGATTTACCGTCTAGCTACGTACGTACGTCATATTCTTTCGCGTACGGCTATCGACTGACTGACTGACTGCATTAAGCTACGTCAGTACGATCGACTGACTGACT"


#post modifications:
Reverse_Primer=Reverse_Primer[::-1] # this gets back to the 3' side, from whatever the user input is


#the previous reverse complement function in the notes flipped the sequence, by reading nucleotides from the left to right
#I didn't like it, as my goal remember was to use the *find method to locate indexes and slice the 5' sequence
def complement(dna_sequence):
	#dictionary for complement of nucleotide in DNA
	dic1={'A':'T','G':'C','C':'G','T':'A'}
	list_rc=[]
	for nucleotide in dna_sequence:
		new_nucleo=dic1[nucleotide]
		list_rc.append(new_nucleo)
		comp_sequence="".join(list_rc)
	return comp_sequence

Sequence_complement=complement("ATGCTACTGATCGATCGGATCGGATTTACCGTCTAGCTACGTACGTACGTCATATTCTTTCGCGTACGGCTATCGACTGACTGACTGACTGCATTAAGCTACGTCAGTACGATCGACTGACTGACT")


#now lets anchor by finding the indecies finding and where the reverse ends:
Reverse_index=Sequence_complement.find(Reverse_Primer)+len(Reverse_Primer)
forward_index=Sequence.find(Forward_Primer)


#Output:
print(Sequence[forward_index:Reverse_index]) #this is our actual result in silico result




