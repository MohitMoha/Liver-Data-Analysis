create table Liver(
Age vachar(120), Age_Group varchar (120), Gender varchar(120), Total_Bilirubin float,Direct_Bilirubin float,
	Alkaline_Phosphotase float, Alamine_Aminotransferase float, Aspartate_Aminotransferase float, Total_Protein float, Albumin float,
	Albumin_Globulin_Ratio float,
	B_Results varchar(120), 
	Prot_Results varchar(120)
);
copy Liver from 'C:\Program Files\PostgreSQL\13\data\All files for Restoring Database\CSV files\LiverProfile1.csv' 
delimiters ',' csv header;

select * from liver order by age;

select count(Age) as "Number of Children" from Liver where age_group='Children';

select count(Age) as "Number of Young Individual" from Liver where age_group='Young';

select count(Age_Group) as "Number of Middle Aged Individual" from liver where age_group = 'Middle Age';

select count(Age) as "Number of Senior Individual" from Liver where age_group='Senior';

/*Analysis of Bilirubin*/

select Age, Total_Bilirubin from liver where age_group = 'Children' and B_results = 'Normal' and Gender= 'Male';

select Age, Total_Bilirubin from liver where age_group = 'Children' and B_results = 'Normal' and Gender= 'Female';

select Age, Total_Bilirubin from liver where age_group = 'Children' and B_results = ' Above Normal' and Gender= 'Female';

select Age, Total_Bilirubin from liver where age_group = 'Children' and B_results = 'Above Normal' and Gender= 'Male';

select Age, Total_Bilirubin from liver where age_group = 'Children' and B_results = 'Below Normal' and Gender= 'Female';

select Age, Total_Bilirubin  from liver where age_group = 'Children' and B_results = 'Below Normal' and Gender= 'Male';

select Age, Total_Bilirubin  from liver where age_group = 'Young' and B_results = 'Normal' and Gender= 'Female';

select Age, Total_Bilirubin  from liver where age_group = 'Young' and B_results = 'Normal' and Gender= 'Male';

select Age, Total_Bilirubin  from liver where age_group = 'Young' and B_results = 'Above Normal' and Gender= 'Female';

select Age, Total_Bilirubin  from liver where age_group = 'Young' and B_results = 'Above Normal' and Gender= 'Male';

select Age, Total_Bilirubin  from liver where age_group = 'Young' and B_results = 'Below Normal' and Gender= 'Female';

select Age, Total_Bilirubin  from liver where age_group = 'Young' and B_results = 'Below Normal' and Gender= 'Male';

select Age, Total_Bilirubin  from liver where age_group = 'Middle Age' and B_results = 'Normal' and Gender= 'Male';

select Age, Total_Bilirubin  from liver where age_group = 'Middle Age' and B_results = 'Normal' and Gender= 'Female';

select Age, Total_Bilirubin  from liver where age_group = 'Middle Age' and B_results = 'Above Normal' and Gender= 'Male';

select Age, Total_Bilirubin  from liver where age_group = 'Middle Age' and B_results = 'Above Normal' and Gender= 'Female';

select Age, Total_Bilirubin from liver where age_group = 'Middle Age' and B_results = 'Below Normal' and Gender= 'Male';

select Age, Total_Bilirubin  from liver where age_group = 'Middle Age' and B_results = 'Below Normal' and Gender= 'Female';

select Age, Total_Bilirubin  from liver where age_group = 'Middle Age' and B_results = 'Normal' and Gender= 'Male';

select Age, Total_Bilirubin  from liver where age_group = 'Senior' and B_results = 'Normal' and Gender= 'Female';

select Age, Total_Bilirubin  from liver where age_group = 'Senior' and B_results = 'Normal' and Gender= 'Male';

select Age, Total_Bilirubin  from liver where age_group = 'Senior' and B_results = 'Above Normal' and Gender= 'Female';

select Age, Total_Bilirubin  from liver where age_group = 'Senior' and B_results = 'Above Normal' and Gender= 'Male';

select Age, Total_Bilirubin  from liver where age_group = 'Senior' and B_results = 'Below Normal' and Gender= 'Male';

select Age, Total_Bilirubin  from liver where age_group = 'Senior' and B_results = 'Below Normal' and Gender= 'Female';


/*Analysis of Proteins*/

select Age, Total_Protein from liver where age_group = 'Children' and prot_results = 'Normal' and Gender= 'Male';

select Age, Total_Protein from liver where age_group = 'Children' and prot_results = 'Normal' and Gender= 'Female';

select Age, Total_Protein from liver where age_group = 'Children' and prot_results = ' Above Normal' and Gender= 'Female';

select Age, Total_Protein from liver where age_group = 'Children' and prot_results = 'Above Normal' and Gender= 'Male';

select Age, Total_Protein Proteinfrom liver where age_group = 'Children' and prot_results = 'Below Normal' and Gender= 'Female';

select Age, Total_Protein  from liver where age_group = 'Children' and prot_results = 'Below Normal' and Gender= 'Male';

select Age, Total_Protein  from liver where age_group = 'Young' and prot_results = 'Normal' and Gender= 'Female';

select Age, Total_Protein  from liver where age_group = 'Young' and prot_results = 'Normal' and Gender= 'Male';

select Age, Total_Protein  from liver where age_group = 'Young' and prot_results = 'Above Normal' and Gender= 'Female';

select Age, Total_Protein  from liver where age_group = 'Young' and prot_results = 'Above Normal' and Gender= 'Male';

select Age, Total_Protein  from liver where age_group = 'Young' and prot_results = 'Below Normal' and Gender= 'Female';

select Age, Total_Protein  from liver where age_group = 'Young' and prot_results = 'Below Normal' and Gender= 'Male';

select Age, Total_Protein  from liver where age_group = 'Middle Age' and prot_results = 'Normal' and Gender= 'Male';

select Age, Total_Protein  from liver where age_group = 'Middle Age' and prot_results = 'Normal' and Gender= 'Female';

select Age, Total_Protein  from liver where age_group = 'Middle Age' and prot_results = 'Above Normal' and Gender= 'Male';

select Age, Total_Protein  from liver where age_group = 'Middle Age' and prot_results = 'Above Normal' and Gender= 'Female';

select Age, Total_Protein from liver where age_group = 'Middle Age' and prot_results = 'Below Normal' and Gender= 'Male';

select Age, Total_Protein  from liver where age_group = 'Middle Age' and prot_results = 'Below Normal' and Gender= 'Female';

select Age, Total_Protein  from liver where age_group = 'Middle Age' and prot_results = 'Normal' and Gender= 'Male';

select Age, Total_Protein  from liver where age_group = 'Senior' and prot_results = 'Normal' and Gender= 'Female';

select Age, Total_Protein  from liver where age_group = 'Senior' and prot_results = 'Normal' and Gender= 'Male';

select Age, Total_Protein  from liver where age_group = 'Senior' and prot_results = 'Above Normal' and Gender= 'Female';

select Age, Total_Protein  from liver where age_group = 'Senior' and prot_results = 'Above Normal' and Gender= 'Male';

select Age, Total_Protein  from liver where age_group = 'Senior' and prot_results = 'Below Normal' and Gender= 'Male';

select Age, Total_Protein  from liver where age_group = 'Senior' and prot_results = 'Below Normal' and Gender= 'Female';
