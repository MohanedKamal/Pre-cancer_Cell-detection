#!/usr/bin/env python
#coding: utf-8

# # import Data

# In[396]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')


# In[441]:





# In[444]:

def cancer(path):
    global decision_tree
    global Dataframe
    data=pd.read_csv(path)
    #data.head()


    # In[398]:


    data.shape


    # # drop columns

    # In[399]:


    data=data.drop(['SNP_ID','Smoking','Aflatoxin','Radiations','Drinking','Asbestos','Hepatitis_B','Papilloma','Exposure','Unidentified_Mutations','Comment outliers'],axis=1)
    data=data.drop(['Comment_7_Sequence', 'Comment_8_publication', 'Comment_9_SNP','Comments', 'Pathogenicity'],axis=1)
    data=data.drop(['HG19_Start','HG19_End','HG18_Start','HG18_End','HG38_Start','HG38_End','HG19_Variant','HG18_Variant','HG38_Variant','Structure' ,'Domain','PTM','Mutant_Allele','Type','Variant Comment','Mutation_origin','Sample_origin','Name','Hereditary_syndrome','Genetic_Background'],axis=1)
    data=data.drop(['Comment prediction','Comment frequency','Comment activity','Comment splicing','Sift Prediction','Provean_prediction','Mutassessor_prediction:','Condel','Prediction_Label','Confident__Hypotheses','WT_AA_1','WT_AA_3'],axis=1)
    data=data.drop(['WAF1_', 'MDM2_', 'BAX_', '__14_3_3_s', 'AIP_', 'GADD45_', 'NOXA_','p53R2_','Act_outliers','Ins_Size','Del_Size','NG_017013.2_Variant','NG_017013.2','Exon:intron_start','Exon:intron_End','Variant_Classification','Internal','Solid','Transcript t1','Transcript t2','Transcript t3','Transcript t4','Transcript t5','Transcript t6','Transcript t7','Transcript t8','Protein p1 _TP53','Protein p3 _TP53_beta','Protein p4 _TP53_gamma','Protein p5 _Delta_133_TP53_alpha','Protein p6 _Delta_133_TP53_beta','Protein p7 _Delta_133_TP53_gamma','Protein p8 _Delta_40_TP53','Protein p9 _Delta_40_TP53_beta','Protein p10 _Delta_40_TP53_gamma','Protein p11 _Delta_160_TP53_alpha','Protein p12 _Delta_160_TP53_beta','Protein p13 _Delta_160_TP53_gamma','Tandem_Class'],axis=1)
    data.shape


    # In[445]:


    #data.head()


    # # pre_processing

    # In[446]:


    data.replace('?', np.NaN,inplace=True)
    #data.head()


    # In[442]:


    data.isnull().sum().sort_values(ascending=False)


    # In[403]:


    data = data.dropna(how='any',axis=0) 


    # In[443]:


    data.isnull().sum().sort_values(ascending=False)


    # # filter data with codon (248,249)

    # In[405]:


    codon = ['248', '249']
    data=data[data['Codon'].isin(codon)]


    # In[447]:


    #data.head()


    # # balance the dataset

    # In[407]:


    df1=data.loc[data['Sample_pathology'] == 'Premalignant disease']


    # In[408]:


    df=data.loc[data['Sample_pathology'] == 'Cancer']


    # In[409]:


    df2=df.sample(n=2000,random_state=42)


    # In[410]:


    values=['Cancer']
    data2=data[data['Sample_pathology'].isin(values) == False]


    # In[411]:


    dataframe=pd.concat([df2,data2])


    # In[412]:


    dataframe["Sample_pathology"].replace({"No disease": "No Disease"}, inplace=True)
    dataframe["Sample_pathology"].replace({"Non malignant disease": "No Disease"}, inplace=True)


    # In[413]:


    dataframe.drop(dataframe[dataframe['Sample_pathology'] == 'Immortalized cell line (in vitro)'].index, inplace = True)
    dataframe.drop(dataframe[dataframe['Sample_pathology'] == 'Healthy mutation carrier'].index, inplace = True)


    # In[414]:


    dataframe.drop(dataframe[dataframe['Sample_pathology'] == 'No Disease'].index, inplace = True)


    # In[415]:


    shuffled = dataframe.sample(frac=1,random_state=42).reset_index()
    shuffled=shuffled.drop(['index'],axis=1)


    # In[416]:


    Dataframe=pd.DataFrame(shuffled)


    # In[448]:


    #Dataframe.head()


    # In[418]:


    Dataframe.to_csv("pre_cancer_data.csv")


    # In[449]:


    Dataframe['Sample_pathology'].value_counts()


    # In[420]:


    D=[]
    D=['Start_cDNA',
    'End_cDNA','Codon','Base_Change_Size','Records_Number','Tumor_Repetition','Publication_Repetition','PCA_Score']
    for i in D:
        Dataframe[i]=Dataframe[i].astype(str).astype(float)


    # In[452]:


    Dataframe.corr()


    # In[422]:

    # # applay LabelEncoder

    # In[423]:


    from sklearn.preprocessing import LabelEncoder


    # In[424]:


    label_encoder=LabelEncoder()


    # In[425]:


    col_list = Dataframe.select_dtypes(include=['object']).columns.to_list()
    for i in col_list:
        Dataframe[i]=label_encoder.fit_transform(Dataframe[i])


    # In[455]:


    Dataframe.Sample_pathology.value_counts()


    # In[454]:


    precancer=Dataframe.loc[Dataframe['Sample_pathology'] == 1]
    precancer=precancer.sample(n=3,random_state=42)


    # In[453]:


    cancer=Dataframe.loc[Dataframe['Sample_pathology'] == 0]
    cancer=Dataframe.sample(n=6,random_state=42)


    # In[450]:


    testdata=pd.concat([precancer,cancer])


    # In[432]:


    test = testdata.sample(frac=1,random_state=42).reset_index()
    test=test.drop(['index'],axis=1)


    # In[434]:


    test=test.drop(['Database_ID','Sample_pathology'],axis=1)


    # In[481]:


    test.shape


    # In[482]:


    test.to_csv("testing.csv")


    
    # In[286]:


    x=Dataframe.drop(['Database_ID','Sample_pathology'],axis=1)
    y=Dataframe['Sample_pathology']


    # In[287]:


    from sklearn.model_selection import train_test_split
    from sklearn.neural_network import MLPClassifier
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import mean_squared_error 


    # # split data into train 80% test 20%

    # In[288]:


    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=22, shuffle =True,stratify=y)


    # In[289]:


    X_train.shape


    # In[290]:


    X_test.shape


   
   
    # In[296]:


    from sklearn.metrics import confusion_matrix

    # # cross_val_score for ANN

    # In[299]:


    from sklearn.model_selection import StratifiedKFold
    from sklearn.model_selection import cross_val_score
    #knnclassifier = KNeighborsClassifier(n_neighbors=4)
    #print(cross_val_score(MLPClassifierModel, x, y, cv=3, scoring ='accuracy').mean())


    # # DecisionTreeClassifier

    # In[300]:


    from sklearn.tree import DecisionTreeClassifier
    decision_tree = DecisionTreeClassifier(random_state=0, max_depth=7,class_weight='balanced')
    decision_tree = decision_tree.fit(X_train, y_train)


    # In[301]:

    train_score=decision_tree.score(X_train, y_train)*100
    
    

    # In[302]:
    test_score=decision_tree.score(X_test, y_test)*100

   


    # # cross_val_score for DecisionTreeClassifier

    # In[303]:

    accuracy=cross_val_score(decision_tree, x, y, cv=3, scoring ='accuracy').mean()
    #print(accuracy)


    # In[304]:


    y_pred = decision_tree.predict(X_test)


    # In[305]:


    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)
    cm_df = pd.DataFrame(cm,index = ['cancer','pre_cancer'], columns = ['cancer','pre_cancer'])
    plt.figure(figsize=(5,4))
    sns.heatmap(cm_df, annot=True)
    plt.title('Confusion Matrix')
    plt.xlabel('Actal Values')
    plt.ylabel('Predicted Values')
    #plt.show()
    cm

    #print(train_score)
    return train_score,test_score,accuracy

    # # Apply SVM

    # In[306]:



    # In[309]:


    from sklearn.metrics import confusion_matrix


    # In[311]:

def test(path):
    train,test,error=cancer('D:/gp/UMD_mutations_US (Autosaved)2.csv')
    global x
    #from sklearn.tree import DecisionTreeClassifier
    Dataframe.shape


    # # Testing

    # In[494]:


    testing=pd.read_csv(path)


    # In[495]:


    testing.shape


    # In[496]:


    submission = pd.DataFrame(decision_tree.predict(testing))
    submission.columns = ['Segmentation']
    submission['Segmentation'] = submission['Segmentation']
    sumb=submission['Segmentation'].tolist()
    
    #print(sumb)
    if sumb[0]==0:
        x='Cancer'
    else:
        x='pre_cancer'

    return x
    


