from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

# a codon - a tuple of three nuclotides
# a gene - a list of codons

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTTAGC"
# print(len(gene_str))

# define a utility function to convert str into a Gene
def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if(i+2) >= len(s): return gene
        # initilaize codon out of three nucloetides
        codon: Codon = (
            Nucleotide[s[i]],
            Nucleotide[s[i+1]],
            Nucleotide[s[i+2]]
        )
        gene.append(codon)
    return gene

my_gene: Gene = string_to_gene(gene_str)

def conversion(s: str) -> Gene:
    # create an empty list that will hold all our data
    geneList: Gene = []
    # loop through the entire string getting every three nucleotides (codon)
    for i in range(0, len(s), 3):
        if(i+2) >= len(s): return geneList 
        codon: Codon = (
            Nucleotide[s[i]],   # gets nucleotide 1 of the tuple
            Nucleotide[s[i+1]], # nucleotide 2
            Nucleotide[s[i+2]], # nucleotide 3
        ); geneList.append(codon)
    return geneList

# perform a linear search on the data
def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon: return True
    return False

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))


# using python's built in
ttt: Codon = (Nucleotide.T, Nucleotide.T, Nucleotide.T)
print(ttt in my_gene)


'''
Binary Search
'''
def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:                      # if we still have some search space
        mid: int = (low + high) // 2        # get the whole number section after division
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else: return True
    return False

my_sorted_gene: Gene = sorted(my_gene)
# print(my_sorted_gene)
print(binary_contains(my_sorted_gene, acg))
print(binary_contains(my_sorted_gene, gat))