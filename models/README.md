### Files description 
- **cof_model.pkl** – A trained model that incorporates both physicochemical descriptors of DNA sequences and cofactor-related features as input variables.
- **cofactor_model.ipynb** – The notebook containing the training pipeline and evaluation procedures for the cofactor-based classification model.
- **model_config.py** – A configuration file defining the hyperparameters used for training and evaluating the classification models.
- **seq_model.pkl** – A model trained using only the physicochemical descriptors derived from the DNA sequence itself, without cofactor information.
- **sequence_model.ipynb** – The notebook containing the model training code, focused solely on sequence-based features.

### Model selection and feature processing
During the model selection phase, two algorithms were explored: **LightGBM** and **Random Forest Classifier**. The Random Forest model was ultimately selected as the final classifier due to its superior performance across evaluation metrics, particularly its lower false positive rate compared to LGBM. The **Matthews Correlation Coefficient** (MCC) was employed as the primary evaluation metric for both training and testing, due to its robustness in handling imbalanced classification tasks.

To enhance model interpretability and eliminate redundant or irrelevant features, **Recursive Feature Elimination** (RFE) was applied as the feature selection strategy. The process identified 38 optimal features that contributed most significantly to predictive performance.
