#IMPORT LIBRARIES: PANDAS, NUMPY,MATPLOTLIB, OPENPYXL#

import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

#IMPORTING DATASET INTO A DATAFRAME
Liver_Profile = pd.read_excel('C:\\Users\\GUDULU\\PycharmProjects\\Pandas Data Analysis\\Liver_Disease_Analysis-master'
                              '\\Indian Liver Patient Dataset.xlsx')



#Declaring Age Groups
Age_Group = []
for i in Liver_Profile['Age']:
    if i < 18:
        Age_Group.append('Children')
    elif 18 < i < 40:
        Age_Group.append('Young')
    elif i > 60:
        Age_Group.append('Senior')
    else:
        Age_Group.append('Middle Age')

#Adding AgeGroups to the Datarame
Liver_Profile.insert(1, 'Age Group', Age_Group)

#Creating New Dataframes on the basis of Age Groups
Children= Liver_Profile[Liver_Profile['Age Group']=='Children']
Young= Liver_Profile[Liver_Profile['Age Group']=='Young']
Middle_Age= Liver_Profile[Liver_Profile['Age Group']=='Middle Age']
Senior= Liver_Profile[Liver_Profile['Age Group']=='Senior']

Count=[(Children['Age Group'].count()), (Young['Age Group'].count()), (Middle_Age['Age Group'].count()),
       (Senior['Age Group'].count())]

#BAR GRAPH USING MATPLOTLIB TO NUMBER OF INDIVIDUAL

#def addlabel(x,y):
    #  for i in range(len(x)):
    #     plt.text(i, y[i], y[i], ha='center')
#plt.bar(['Children', 'Young', 'Middle', 'Senior'], Count, width=0.8)
#addlabel(['Children', 'Young', 'Middle', 'Senior'], Count)
#plt.xlabel('Age Groups')
#plt.ylabel('No. of Individuals')
#plt.title('Distribution of Individuals in Various age Groups')
#plt.show()

#plt.savefig('Distribution of Individuals in Various age Groups.png')


#RESETTING INDEX AND PRINITING NUMBER OF ROWS IN EACH DATASET
Children.reset_index(drop=True, inplace=True)
Young.reset_index(drop=True, inplace=True)
Middle_Age.reset_index(drop=True, inplace=True)
Senior.reset_index(drop=True, inplace=True)

#print("The Number of Children in the Dataset: ", Children['Age'].count(),
     # "\nThe Number Of Young Individuals in the dataset: ", Young['Age'].count(),
      #"\nThe Number of Middle aged Citizens in the Dataset: ", Middle_Age['Age'].count(),
      #"\nThe Number of Senior Citizens in the Dataset: ", Senior['Age'].count())#

#FUNCTION TO PRINT THE SAME STATEMENT
def protprint (x, y, z):
   print ('Number of ', x,
          'having Protein level', y,
          'are: ',z,'\n')


#print("Welcome\nEnter the option you want to check")
#Normal_ranges = int(input("1. To find the Normal Ranges\n2. To Analyse Total_Bilirubin Data\n3. To Analyse Total "
                       #  "Protein Content\n"))


 #       print("Ideal range for Bilirubin is 0.30-0.20mg/dl\nIdeal Range for Total Protein is 6.00-8.30mg/dl")


  #  Choose=int(input("This dataset contains Analysis of Liver profile of 583 individuals between the age of 5 and 70\n"
                   #  "Choose the number for the corresponding data:\n1. Analysis of Total_Bilirubin contents in Children"
                    # "\n2. Analysis of Total_Bilirubin contents in Age group of 18 and 40"
                     #"\n3. Analysis of Total_Bilirubin contents in Age of 40 and 60"
                     #"\n4. Analysis of Total_Bilirubin contents in individuals above 60\n"))

#ANALYSIS FOR TOTAL_BILIRUBIN CONTENT FOR CHILDREN

Children_TBilirubin= Children[['Age', 'Gender', 'Total_Bilirubin']]
Result = []
for j in Children_TBilirubin['Total_Bilirubin']:
      if j<0.30:
            Result.append('Below Normal')
      elif j>1.20:
            Result.append('Above Normal')
      else:
            Result.append('Normal')

Children_TBilirubin.insert(3, 'Result', Result)
Children_TBilirubin_Mean = Children_TBilirubin['Total_Bilirubin'].mean()

MChild_AboveNormal= Children_TBilirubin[(Children_TBilirubin.Result== 'Above Normal')
                                                & (Children_TBilirubin.Gender =='Male')]


FChild_AboveNormal= Children_TBilirubin[(Children_TBilirubin.Result== 'Above Normal')
                                                & (Children_TBilirubin.Gender =='Female')]

MChild_Normal= Children_TBilirubin[(Children_TBilirubin['Result']=='Normal') & (Children_TBilirubin.Gender=='Male')]
FChild_Normal= Children_TBilirubin[(Children_TBilirubin['Result']=='Normal') & (Children_TBilirubin.Gender=='Female')]

#GRAPHICAL ANALYSIS

#FUNCTION TO ADD TEXT ON BAR GRAPH
def addlabel(x,y):
            for i in range(len(x)):
                plt.text(i, y[i], y[i], ha='center')

#FUNCTION TO GET COUNT FOR RESULTS
def Counts(s):
            k=0
            g=0
            h=0
            for i in s:
                if i=='Normal':
                    k=k+1
                elif i=='Above Normal':
                    g=g+1
                else:
                    h=h+1

            if h==0:
                return [k,g]
            else:
                return [k,g,h]

#BAR GRAPH FOR DISTRIBUTION OF CHILDREN IN GIVEN RANGE

#plt.bar(Children_TBilirubin['Result'].drop_duplicates(), Counts(Children_TBilirubin['Result']), width=0.2, color='red')
#addlabel(Children_TBilirubin['Result'].drop_duplicates(), Counts(Children_TBilirubin['Result']))
#plt.title("Distribution of Children")
#plt.xlabel("Interpretation")
#plt.ylabel("Number of Children")
#plt.ylim(0, 30)
#plt.show()
#plt.savefig("Distribution of Children.png")

#PIE CHART

#fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(10,8))

        #M_Count = [(MChild_Normal.Result.count()), (MChild_AboveNormal.Result.count())]
        #ax1.pie(M_Count, labels=['Normal', 'Above Normal'], autopct='%0.2f%%')
        #ax1.set_title("Distribution of Male\nChildren")


        #F_Count = [(FChild_Normal.Result.count()), (FChild_AboveNormal.Result.count())]
        #ax2.pie(F_Count, labels=['Normal', 'Above Normal'], autopct='%0.2f%%')
        #ax2.set_title('Distribution of Female\nChildren')
        #plt.show()

        #plt.bar(Children_TBilirubin['Age'], Children_TBilirubin['Total_Bilirubin'])

        #plt.xlim(0,20)
        #plt.xlabel("Age")
        #plt.ylabel("Total Bilirubin")
        #plt.title("Total Bilirubin content below 18")
        #plt.show()

#print("Average Bilirubin Concentration found in Body of children below 18 Years of age is: ", round(Children_TBilirubin_Mean,2),
         #"\nNumber of Male Children having Total Bilirubin Above Normal are: ", MChild_AboveNormal.Result.count(),
          #    "\nNumber of Female Children having Total Bilirubin Above Normal are: ",FChild_AboveNormal.Result.count(),
           #   "\nNumber of Female Children having Total Bilirubin in Normal Range: ",FChild_Normal.Result.count(),
            #  "\nNumber of Male Children having Total Bilirubin in Normal range: ",MChild_Normal.Result.count())


##############################################################################################################################
#ANALYSIS FOR TOTAL_BILIRUBIN CONTENT FOR YOUNG AGE
Young_TBilirubin= Young[['Age', 'Gender', 'Total_Bilirubin']]
Result = []
for j in Young_TBilirubin['Total_Bilirubin']:
            if j<0.30:
                Result.append('Below Normal')
            elif j>1.20:
                Result.append('Above Normal')
            else:
                Result.append('Normal')
Young_TBilirubin['Result']= Result


Young_TBilirubin_Mean= round(Young_TBilirubin['Total_Bilirubin'].mean(), 2)

MYoung_AboveNormal= Young_TBilirubin[(Young_TBilirubin.Result == 'Above Normal')
                                                & (Young_TBilirubin.Gender == 'Male')]

FYoung_AboveNormal= Young_TBilirubin[(Young_TBilirubin.Result== 'Above Normal')
                                                & (Young_TBilirubin.Gender =='Female')]

MYoung_Normal= Young_TBilirubin[(Young_TBilirubin['Result']=='Normal') & (Young_TBilirubin.Gender=='Male')]
FYoung_Normal= Young_TBilirubin[(Young_TBilirubin['Result']=='Normal') & (Young_TBilirubin.Gender=='Female')]



#        print("Number of Young Male having Total Bilirubin Above Normal are: ", MYoung_AboveNormal.Result.count(),
 #             "\nNumber of Young Female having Total Bilirubin Above Normal are: ",FYoung_AboveNormal.Result.count(),
  #            "\nNumber of Young Female having Total Bilirubin in Normal Range: ",FYoung_Normal.Result.count(),
   #           "\nNumber of Young Male having Total Bilirubin in Normal range: ",MYoung_Normal.Result.count())


    #ANALYSIS FOR TOTAL_BILIRUBIN CONTENT FOR MIDDLE AGE GROUP
Middle_TBilirubin= Middle_Age[['Age', 'Gender', 'Total_Bilirubin']]
Result = []
for j in Middle_TBilirubin['Total_Bilirubin']:
            if j<0.30:
                Result.append('Below Normal')
            elif j>1.20:
                Result.append('Above Normal')
            else:
                Result.append('Normal')
Middle_TBilirubin['Result']= Result

M_Middle_AboveNormal= Middle_TBilirubin[(Middle_TBilirubin.Result== 'Above Normal')
                                                & (Middle_TBilirubin.Gender =='Male')]

F_Middle_AboveNormal= Middle_TBilirubin[(Middle_TBilirubin.Result== 'Above Normal')
                                                & (Middle_TBilirubin.Gender =='Female')]

M_Middle_Normal= Middle_TBilirubin[(Middle_TBilirubin['Result']=='Normal') & (Middle_TBilirubin.Gender=='Male')]
F_Middle_Normal= Middle_TBilirubin[(Middle_TBilirubin['Result']=='Normal') & (Middle_TBilirubin.Gender=='Female')]


#        print("Number of Male in Middle age group having Total Bilirubin Above Normal are: ", M_Middle_AboveNormal.Result.count(),
 #             "\nNumber of Female Middle having Total Bilirubin Above Normal are: ",F_Middle_AboveNormal.Result.count(),
  #            "\nNumber of  Female Middle having Total Bilirubin in Normal Range: ",F_Middle_Normal.Result.count(),
   #           "\nNumber of Male Middle  having Total Bilirubin in Normal range: ",M_Middle_Normal.Result.count())



#ANALYSIS FOR TOTAL_BILIRUBIN CONTENT FOR SENIOR CITIZEN
Senior_TBilirubin= Senior[['Age', 'Gender', 'Total_Bilirubin']]
Result = []
for j in Senior_TBilirubin['Total_Bilirubin']:
            if j<0.30:
                Result.append('Below Normal')
            elif j>1.20:
                Result.append('Above Normal')
            else:
                Result.append('Normal')
Senior_TBilirubin['Result']= Result

M_Senior_AboveNormal= Senior_TBilirubin[(Senior_TBilirubin.Result== 'Above Normal')
                                                & (Senior_TBilirubin.Gender =='Male')]


F_Senior_AboveNormal= Senior_TBilirubin[(Senior_TBilirubin.Result== 'Above Normal')
                                                & (Senior_TBilirubin.Gender =='Female')]

M_Senior_Normal= Senior_TBilirubin[(Senior_TBilirubin['Result']=='Normal') & (Senior_TBilirubin.Gender=='Male')]
F_Senior_Normal=Senior_TBilirubin[(Senior_TBilirubin['Result']=='Normal') & (Senior_TBilirubin.Gender=='Female')]


#        print("Number of Male Senior Citizens having Total Bilirubin Above Normal are: ", M_Senior_AboveNormal.Result.count(),
 #             "\nNumber of Female Senior Citizens having Total Bilirubin Above Normal are: ",F_Senior_AboveNormal.Result.count(),
  #         "\nNumber of  Female Senior Citizens having Total Bilirubin in Normal Range: ",F_Senior_Normal.Result.count(),
   #           "\nNumber of Male Senior Citizens  having Total Bilirubin in Normal range: ",M_Senior_Normal.Result.count())


   # Choose_Protein = int(input("This dataset contains Analysis of Liver profile of 583 individuals between the age of 5 and 70\n"
    #          "Choose the number for the corresponding data:\n1. Analysis of Total_Protein contents in Children"
     #         "\n2. Analysis of Total_Protein contents in Age group of 18 and 40"
      #       "\n3. Analysis of Total_Protein contents in Age of 40 and 60"
       #       "\n4. Analysis of Total_Protein contents in individuals above 60\n"))



############Analysis OF PROTEIN CONCENTRATION IN CHILDREN#####################################



Total_Protein = Liver_Profile[['Age Group', 'Gender', 'Total_Proteins']]

Protein=[]
for p in Total_Protein['Total_Proteins']:
    if p < 6.30:
        Protein.append('Below Normal')
    elif p > 7.90:
        Protein.append('Above Normal')
    else:
        Protein.append('Normal')

Total_Protein['Results'] = Protein

#################_______ANALYSIS OF PROTEINS IN CHILDREN ##############################

F_Child_Above= Total_Protein[(Total_Protein['Results']=='Above Normal') & (Total_Protein['Gender']=='Female')
                                         & (Total_Protein['Age Group']=='Children')].Results.count()

F_Child_Below = Total_Protein[(Total_Protein['Results']=='Below Normal') & (Total_Protein['Gender']=='Female')
                                         & (Total_Protein['Age Group']=='Children')].Results.count()

F_Child_Normal = Total_Protein[(Total_Protein['Results']=='Normal') & (Total_Protein['Gender']=='Female')
                                         & (Total_Protein['Age Group']=='Children')].Results.count()


M_Child_Below = Total_Protein[(Total_Protein['Gender']== 'Male') & (Total_Protein['Age Group']=='Children')
                                          & (Total_Protein['Results']=='Below Normal')].Results.count()

M_Child_Above = Total_Protein[(Total_Protein['Gender']== 'Male') & (Total_Protein['Age Group']=='Children')
                                          & (Total_Protein['Results']=='Above Normal')].Results.count()

M_Child_Normal = Total_Protein[(Total_Protein['Gender']== 'Male') & (Total_Protein['Age Group']=='Children')
                                          & (Total_Protein['Results']=='Normal')].Results.count()

#            protprint('Female Children', 'Below Normal range', F_Child_Below)
 #           protprint('Female Children', 'Normal', F_Child_Normal)
  #          protprint('Female Children', 'Above Normal range', F_Child_Above)
   #         protprint('Male Children', 'Below Normal range', M_Child_Below)
    #        protprint('Male Children', 'Normal', M_Child_Normal)
     #       protprint('Male Children', 'Above Normal range', M_Child_Above)

##########################____ANALYSIS OF PROTEIN CONCENTRATION IN YOUNG____#####################

M_Young_Below = Total_Protein[(Total_Protein['Gender']== 'Male') & (Total_Protein['Age Group']=='Young')
                                          & (Total_Protein['Results']=='Below Normal')].Results.count()

M_Young_Normal = Total_Protein[(Total_Protein['Gender']== 'Male') & (Total_Protein['Age Group']=='Young')
                                          & (Total_Protein['Results']=='Normal')].Results.count()

M_Young_Above = Total_Protein[(Total_Protein['Gender']== 'Male') & (Total_Protein['Age Group']=='Young')
                                          & (Total_Protein['Results']=='Above Normal')].Results.count()

F_Young_Below = Total_Protein[(Total_Protein['Gender']== 'Female') & (Total_Protein['Age Group']=='Young')
                                          & (Total_Protein['Results']=='Below Normal')].Results.count()

F_Young_Normal = Total_Protein[(Total_Protein['Gender']== 'Female') & (Total_Protein['Age Group']=='Young')
                                          & (Total_Protein['Results']=='Normal')].Results.count()

F_Young_Above = Total_Protein[(Total_Protein['Gender']== 'Female') & (Total_Protein['Age Group']=='Young')
                                          & (Total_Protein['Results']=='Above Normal')].Results.count()

#            protprint('Young Female', 'Below Normal range', F_Young_Below)
 #           protprint('Young Female', 'Normal', F_Young_Normal)
  #          protprint('Young Female', 'Above Normal range', F_Young_Above)
   #         protprint('Young Male', 'Below Normal range', M_Young_Below)
    #        protprint('Young Male', 'Normal', M_Young_Normal)
     #       protprint('Young Male', 'Above Normal range', M_Young_Above)



##########################____ANALYSIS OF PROTEIN CONCENTRATION IN MIDDLE____#####################

M_Middle_Below = Total_Protein[(Total_Protein['Gender']== 'Male') & (Total_Protein['Age Group']=='Middle Age')
                                      & (Total_Protein['Results']=='Below Normal')].Results.count()

M_Middle_Normal = Total_Protein[(Total_Protein['Gender']== 'Male') & (Total_Protein['Age Group']=='Middle Age')
                                      & (Total_Protein['Results']=='Normal')].Results.count()

M_Middle_Above = Total_Protein[(Total_Protein['Gender']== 'Male') & (Total_Protein['Age Group']=='Middle Age')
                                      & (Total_Protein['Results']=='Above Normal')].Results.count()

F_Middle_Below = Total_Protein[(Total_Protein['Gender']== 'Female') & (Total_Protein['Age Group']=='Middle Age')
                                      & (Total_Protein['Results']=='Below Normal')].Results.count()

F_Middle_Normal = Total_Protein[(Total_Protein['Gender']== 'Female') & (Total_Protein['Age Group']=='Middle Age')
                                      & (Total_Protein['Results']=='Normal')].Results.count()

F_Middle_Above = Total_Protein[(Total_Protein['Gender']== 'Female') & (Total_Protein['Age Group']=='Middle Age')
                                      & (Total_Protein['Results']=='Above Normal')].Results.count()


#        protprint('Middle Aged Female', 'Below Normal range', F_Middle_Below)
 #       protprint('Middle Aged Female', 'Normal', F_Middle_Normal)
  #      protprint('Middle aged Female', 'Above Normal range', F_Middle_Above)
   #     protprint('Middle aged Male', 'Below Normal range', M_Middle_Below)
    #    protprint('Middle aged Male', 'Normal', M_Middle_Normal)
     #   protprint('Middle aged Male', 'Above Normal range', M_Middle_Above)

##########################____ANALYSIS OF PROTEIN CONCENTRATION IN SENIOR____#####################

M_Senior_Below = Total_Protein[(Total_Protein['Gender']== 'Male') & (Total_Protein['Age Group']=='Senior')
                                          & (Total_Protein['Results']=='Below Normal')].Results.count()

M_Senior_Normal = Total_Protein[(Total_Protein['Gender']== 'Male') & (Total_Protein['Age Group']=='Senior')
                                          & (Total_Protein['Results']=='Normal')].Results.count()

M_Senior_Above = Total_Protein[(Total_Protein['Gender']== 'Male') & (Total_Protein['Age Group']=='Senior')
                                          & (Total_Protein['Results']=='Above Normal')].Results.count()

F_Senior_Below = Total_Protein[(Total_Protein['Gender']== 'Female') & (Total_Protein['Age Group']=='Senior')
                                          & (Total_Protein['Results']=='Below Normal')].Results.count()

F_Senior_Normal = Total_Protein[(Total_Protein['Gender']== 'Female') & (Total_Protein['Age Group']=='Senior')
                                          & (Total_Protein['Results']=='Normal')].Results.count()

F_Senior_Above = Total_Protein[(Total_Protein['Gender']== 'Female') & (Total_Protein['Age Group']=='Senior')
                                          & (Total_Protein['Results']=='Above Normal')].Results.count()


#            protprint('Senior Aged Female', 'Below Normal range', F_Senior_Below)
 #           protprint('Senior Aged Female', 'Normal', F_Senior_Normal)
  #          protprint('Senior aged Female', 'Above Normal range', F_Senior_Above)
   #         protprint('Senior aged Male', 'Below Normal range', M_Senior_Below)
    #        protprint('Senior aged Male', 'Normal', M_Senior_Normal)
     #       protprint('Senior aged Male', 'Above Normal range', M_Senior_Above)


Bilirubin=[]
for p in Liver_Profile['Total_Bilirubin']:
    if p < 0.30:
      Bilirubin.append('Below Normal')
    elif p > 1.20:
        Bilirubin.append('Above Normal')
    else:
        Bilirubin.append('Normal')

Liver_Profile['B_Results']= Bilirubin
Liver_Profile['Prot_Results']= Protein

Liver_Profile.to_excel('LiverProfile1.xlsx')

High_Compare = Liver_Profile[(Liver_Profile['B_Results']=='Above Normal') & (Liver_Profile['Prot_Results']=='Above Normal')]
print("Number of pateints having High Protein and Bili are: ", High_Compare.B_Results.count())

Below_Compare = Liver_Profile[(Liver_Profile['B_Results']=='Below Normal') & (Liver_Profile['Prot_Results']=='Below Normal')]
print("Number of pateints having High Protein and Bili are: ", Below_Compare.B_Results.count())




