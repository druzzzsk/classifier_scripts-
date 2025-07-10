import re
import pandas as pd
import numpy as np

from PyBioMed import Pydna

from utils.autoencoder import (
    encoding,
    generate_latent_representations,
    filter_sequences,
    generate_rdkit_descriptors,
)
from utils.constants import kmer_2_dict



def calculate_kmer(seq, k):
    dnaclass = Pydna.PyDNA(seq)
    kmer = list(dnaclass.GetKmer(k=k).values())
    return kmer

def calculate_autoencoder(df_ml, seq_column_name):
    filtered_sequences = filter_sequences(
        sequences=df_ml,
        max_length=96,
        sequences_column_name=seq_column_name,
        shuffle_seqs=False,
    )
    descriptors_set = generate_rdkit_descriptors()
    encoded_sequences = encoding(
        sequences_list=filtered_sequences[seq_column_name],
        polymer_type="DNA",
        descriptors=descriptors_set,
        num=96,
    )
    x_autoencoder = generate_latent_representations(
        encoded_sequences=encoded_sequences,
        path_to_model_folder=r"utils/autoencoder/nucleic_acids",
    )
    return x_autoencoder

def get_full_descriptors_for_classifier(df, seq_column_name):
    kmer_2_features = list(kmer_2_dict.keys())
    autoencoder_features = list(generate_rdkit_descriptors().columns)
    features_names = [*kmer_2_features, *autoencoder_features]

    df_sequence = pd.DataFrame(
        np.concatenate(
            (
                np.array([calculate_kmer(seq, 2) for seq in df[seq_column_name]]),
                calculate_autoencoder(df_ml=df, seq_column_name=seq_column_name),
            ),
            axis=1,
        )
    )
    
    df_sequence.columns = [*features_names]
    return df_sequence



