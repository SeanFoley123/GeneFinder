# -*- coding: utf-8 -*-
"""
YOUR HEADER COMMENT HERE

@author: SEAAAAAAAAAAAAAAAN FOOOOOOOOOOLEY

"""

import random
from amino_acids import aa, codons, aa_table   # you may find these useful
from load import load_seq


def shuffle_string(s):
    """Shuffles the characters in the input string
        NOTE: this is a helper function, you do not
        have to modify this in any way """
    return ''.join(random.sample(s, len(s)))

# YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    Added in the rest just to be safe.
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    """
    complement_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return complement_dict[nucleotide] #What kind of pants do biologists wear?


def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence

        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
        >>> get_reverse_complement("ATGCCCGCTTT")
        'AAAGCGGGCAT'
        >>> get_reverse_complement("CCGCGTTCA")
        'TGAACGCGG'
        I thought this was sufficient.
    """
    dna_out = []
    for i in range(1, len(dna)+1):
        dna_out.append(get_complement(dna[-i]))
    return ''.join(dna_out)


def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start
        codon and returns the sequence up to but not including the
        first in frame stop codon.  If there is no in frame stop codon,
        returns the whole string.

        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'

    I'll add in one just to check my TAA, cause why not it's easy
    >>> rest_of_ORF('ATGACGATAATTGCGTAA')
    'ATGACGATAATTGCG'
    """
    dna_out=[]
    dna_buffer = []
    for i in range(0, len(dna)):
        dna_buffer.append(dna[i])
        if (i+1)%3 == 0:
            a = ''.join(dna_buffer)
            if a == 'TAG' or a == 'TGA' or a == 'TAA':
                break
            else:
                dna_out.append(dna_buffer[0])
                dna_out.append(dna_buffer[1])
                dna_out.append(dna_buffer[2])
                dna_buffer = []
    if (i+1)%3 != 0:
        for k in dna_buffer:
            dna_out.append(k)
    return ''.join(dna_out)


def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA
        sequence and returns them as a list.  This function should
        only find ORFs that are in the default frame of the sequence
        (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
        I added in a test; it's interesting that if I have two end sequences
        in a row, I return a blank string ''. I don't think that's a big deal.
        The alternative is changing rest_of_ORF to only return if dna_out is
        longer than 0, then making sure the return is not None.
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']

    >>> find_all_ORFs_oneframe('ATGCGAAGATAGAGATAGTAGATGT')
    ['ATGCGAAGA', 'ATGT']
    """
    i = 0
    results = []
    while i<len(dna)-1:
        if dna[i:i+3] == 'ATG':
            temp = rest_of_ORF(dna[i:])
            results.append(temp)
            i = i+len(temp)+3
        else:
            i = i+3
    return results


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in
        all 3 possible frames and returns them as a list.  By non-nested we
        mean that if an ORF occurs entirely within another ORF and they are
        both in the same frame, it should not be included in the returned list
        of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    results = []
    for i in range(0,3):
        temp = find_all_ORFs_oneframe(dna[i:])
        results = results + temp
    return results


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
        These unit tests seem sufficient.
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    results = []
    results = results + find_all_ORFs(dna)
    results = results + find_all_ORFs(get_reverse_complement(dna))
    return results


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    pass


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence

        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    pass


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).

        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    pass


def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna

        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    # TODO: implement this
    pass

if __name__ == "__main__":
    import doctest
    doctest.run_docstring_examples(find_all_ORFs_both_strands, globals())