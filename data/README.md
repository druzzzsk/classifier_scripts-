### Files description

- **db_dnazymes_v2.csv** — the origin dataset containing sequences of active and non-active DNAzymes annotated with their respective cofactors. Active sequences from these dataset represent the target class for machine learning applications.

- **get_training_data.py** — a script designed to generate a training dataset. It creates randomly synthesized sequences representing the negative class. The generated sequence lengths follow the same distribution as those of the positive class. Additionally, the script assigns cofactors to the generated sequences by sampling from the cofactor distribution observed in the original dataset.

- **mapping.csv** — a mapping table containing label-encoded representation of the cofactors.

- **test_100_sample.csv** — a sample of 100 sequences intended for model testing purposes.

- **training_data.csv** — the final output dataset containing both positive and artificially created negative examples, as well as all the descriptors needed for training.

The training data consist of 154 target class samples and 1,000 synthetically generated negative class sequences. Feature representation is based on physicochemical properties of nucleotides, encoded via a convolutional autoencoder (CAE) trained to learn abstract sequence-level descriptors 
