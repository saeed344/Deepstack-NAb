##DeepStack-DTIs

Deepstack-NAb: Using Lasso Feature Selection and Deep Stacked  Classifier.


###Deepstack-NAb uses the following dependencies:
* python 3.6 
* numpy
* pandas
* scikit-learn
* keras
* TesnorFlow

###Guiding principles:

**The dataset file contains the dataset in csv format.

**feature extraction:
1) graph based features : DCGR_main.ipynb implementation of CGR via remodeling
multiple information and FEGS.ipynb implementation of FEGS (Feature Extraction based on Graphical and
Statistical features), respectively.
2) Sequence-based features: PAAC.py, AAC.py, BLOSUM62.py and CTDC.py are the implementations of PseAAC, AAC, BLOSUM62 and CTDC.
3) NLP-based features: word2vec.ipynb and Fasttext_features_extraction.ipynb are the implementations of word2vector and Fast text features respectively.
   
** feature selection:
   Lasso.ipynb represents the lasso features selection.
  
   
** Classifier:
   DDeepStacking.ipynb is the implementation of deep stacked classifier. 
   DNN.ipynb is the implementation of deep neural network.
   ET..ipynb is the implementation of Extra tree. 
   GRU.ipynb is the implementation of gated recurrent unit. 
   MLP.ipynb is the implementation of Multi-layer perceptron. 
   SVM.ipynb is the implementation of support vector machine.
   XGBoost.ipynb is the implementation of eXtreme gradient boosting. 
