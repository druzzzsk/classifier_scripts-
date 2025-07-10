kmer_2_dict = {
    'AA': 0, 'AC': 0, 'AG': 0, 'AT': 1,
    'CA': 0, 'CC': 0, 'CG': 0, 'CT': 0,
    'GA': 0, 'GC': 1, 'GG': 0, 'GT': 0,
    'TA': 0, 'TC': 0, 'TG': 1, 'TT': 0
}

sel_features = ['AA', 'AC', 'AG', 'AT', 'CC', 'CT', 'GA', 
                'GC', 'GG', 'GT', 'TC', 'TG', 'TT', 'lipinskiHBD', 
                'NumRotatableBonds', 'NumHeavyAtoms', 'NumAtoms', 
                'NumHeteroatoms', 'NumAmideBonds', 'FractionCSP3', 
                'NumAliphaticRings', 'NumSaturatedRings', 'NumAliphaticHeterocycles', 
                'NumSpiroAtoms', 'NumUnspecifiedAtomStereoCenters', 'labuteASA', 
                'CrippenClogP', 'CrippenMR', 'chi0v', 'chi2v', 'chi3v', 'chi4v', 
                'chi0n', 'chi1n', 'chi2n', 'chi3n', 'chi4n', 'kappa3'
]

cofactor_mapping = {
    0: ['Ag+'], 1: ['Ca2+'], 2: ['Cd2+'], 3: ['Ce3+', 'Cr3+'], 4: ['Ce3+'],
    5: ['Co2+'], 6: ['Cu2+'], 7: ['Gd3+'], 8: ['Mg2+'], 9: ['Mn2+', 'Co2+'],
    10: ['Mn2+', 'Mg2+', 'Zn2+'], 11: ['Mn2+', 'Mg2+'], 12: ['Mn2+', 'Ni2+', 'Co2+', 'Cd2+'],
    13: ['Mn2+'], 14: ['Na+'], 15: ['Nd3+'], 16: ['Ni2+', 'Co2+'], 17: ['Ni2+'],
    18: ['No cofactor'], 19: ['Pb2+'], 20: ['Sm3+'], 21: ['Tm3+', 'Er3+'], 22: ['Zn2+']
}

