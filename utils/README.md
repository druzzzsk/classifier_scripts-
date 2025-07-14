### Files description 
- **autoencoder/** – This directory contains the convolutional autoencoder (CAE) model, trained to extract latent physicochemical representations from DNA sequences. The CAE captures abstract, high-dimensional features encoding structural and biochemical properties of nucleotide sequences, which are subsequently used as input descriptors for machine learning models.

- **constants.py** – A configuration file that defines essential static components for feature construction and model training. This includes:

  - kmer_2_dict – a dictionary mapping k-mers to numerical representations;
  - sel_features – the list of selected features retained after feature selection;
  - cofactor_mapping – a dictionary for encoding cofactor categories.
  
- **feature_engineering_tools.py** – This module defines core utility functions for feature engineering. It includes procedures for extracting encoded representations from the convolutional autoencoder and constructing the final input feature table used for model training and evaluation.

To obtain a range of physicochemical descriptors for DNA sequences, use the function **get_full_descriptors_for_classifier** from the **feature_engineering_tools.py** module. This function takes as input a **dataset** and the **name of the column containing the DNA sequences**.

The function outputs a comprehensive set of descriptors, including those generated via an **autoencoder**, as well as **k-mer frequency** representations computed directly from the input sequences.
