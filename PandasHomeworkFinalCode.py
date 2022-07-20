#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


school_data_to_load = "C:/Users/krcon/OneDrive/Desktop/Class Master Folder/Pandas/pandas-challenge/Resources/schools_complete.csv.url.csv"
student_data_to_load = "C:/Users/krcon/OneDrive/Desktop/Class Master Folder/Pandas/pandas-challenge/Resources/students_complete.csv"


# In[3]:


school_data = pd.read_csv(school_data_to_load, encoding="utf-8")
school_data.head()
student_data =pd.read_csv(student_data_to_load, encoding="utf-8")
student_data.head()


# In[4]:


complete_data= pd.merge(student_data, school_data, how="left", on=["school_name"])


# In[5]:


complete_data.head()


# In[6]:


complete_data.describe()


# In[7]:


complete_data["school_name"].value_counts()


# In[8]:


# of schools total
total_schools=school_data["School ID"].count()
total_schools


# In[9]:


#total number of students
student_count= school_data["size"].sum()
student_count


# In[10]:


#total budget
total_budget=school_data["budget"].sum()
total_budget


# In[11]:


#average math score
avg_math_score=complete_data["math_score"].mean()
avg_math_score


# In[12]:


#average reading score
avg_reading_score=complete_data["reading_score"].mean()
avg_reading_score


# In[13]:


complete_data.head()


# In[14]:


# % passing math
math_passing_rate = (len(complete_data[complete_data["math_score"] >= 70])/student_count)*100
math_passing_rate


# In[15]:


# % passing reading
read_passing_rate = (len(complete_data[complete_data["reading_score"] >= 70])/student_count)*100
read_passing_rate


# In[16]:


df_total_passing_both= complete_data[(complete_data.math_score >=70) & (complete_data.reading_score >= 70)]
df_total_passing_both


# In[17]:


overall_passing_rate= len(df_total_passing_both)/(student_count) 
overall_passing_rate


# In[18]:


district_summary= pd.DataFrame(
    {"Total Schools":[total_schools], "Total Students":[student_count], "Total Budget":[total_budget], 
    "Average Math Score":[avg_math_score], "Average Reading Score":[avg_reading_score], "% Passing Math":[math_passing_rate], "% Passing Reading":[read_passing_rate], "Total Passing Both":[overall_passing_rate]})
                                                 

district_summary
    


# In[19]:


format_district_summary_df = district_summary.style.format({"Total Budget":"${:,.2f}"})


# In[20]:


format_district_summary_df


# In[21]:


per_school_types = school_data.set_index(["school_name"])["type"]
per_school_types


# In[22]:


school_types_df = pd.DataFrame(per_school_types)
school_types_df


# In[23]:


per_school_types_a = school_data.set_index(["school_name"])["type"]
per_school_types_a


# In[24]:


school_count = school_data.set_index(["school_name"])["size"]
school_count


# In[25]:


per_school_budget = school_data.set_index(["school_name"])["budget"]
per_school_budget


# In[26]:


per_student_budget = per_school_budget / school_count
per_student_budget


# In[27]:


per_school_math = student_data.set_index(["school_name"])["math_score"]
per_school_math


# In[28]:


student_data.columns


# In[29]:


per_school_math_a = student_data.groupby(["school_name"]).mean()["math_score"]
per_school_math_a


# In[30]:


per_school_passing_math = complete_data[(complete_data["math_score"] >= 70)]

per_school_passing_reading = complete_data[(complete_data["reading_score"] >= 70)]
print(per_school_passing_math)


# In[31]:


per_school_reading_a = student_data.groupby(["school_name"]).mean()["reading_score"]
per_school_reading_a


# In[32]:


per_school_passing_math = student_data[(student_data["math_score"] >= 70)]

per_school_passing_reading = student_data[(student_data["reading_score"] >= 70)]
print(per_school_passing_math)


# In[33]:


per_school_passing_math_a = per_school_passing_math.groupby(["school_name"]).count()["student_name"]

per_school_passing_reading_a = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]
print(per_school_passing_math_a)


# In[34]:


per_school_passing_math_percent = per_school_passing_math_a / school_count * 100

per_school_passing_reading_percent = per_school_passing_reading_a / school_count * 100

print(per_school_passing_math_percent)


# In[35]:


passing_math_reading = complete_data[(complete_data["math_score"] >= 70) & (complete_data["reading_score"] >= 70)]
passing_math_reading.head()


# In[36]:


per_complete_data=complete_data


# In[37]:


tot_passing_math_reading = passing_math_reading.groupby(["school_name"]).count()["student_name"]
print(tot_passing_math_reading)


# In[40]:


percent_overall_passing_percentage = tot_passing_math_reading / school_count * 100
print(percent_overall_passing_percentage)


# In[41]:


per_school_summary_df = pd.DataFrame({"School Type": per_school_types_a,"Total Students": school_count,"Total School Budget": per_school_budget,"Per Student Budget": per_student_budget,"Average Math Score": per_school_math_a,"Average Reading Score": per_school_reading_a,"% Passing Math": per_school_passing_math_percent,"% Passing Reading": per_school_passing_reading_percent,"% Overall Passing": percent_overall_passing_percentage})
per_school_summary_df.head()


# In[42]:


# Top five schools.
top_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=False)

top_schools.head()


# In[43]:


per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)
per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)

per_school_summary_df.head()


# In[44]:


top_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=False)

top_schools.head()


# In[45]:


bottom_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=True)

bottom_schools.head()


# In[46]:


ninth_graders = complete_data[(complete_data["grade"] == "9th")]
tenth_graders = complete_data[(complete_data["grade"] == "10th")]
eleventh_graders = complete_data[(complete_data["grade"] == "11th")]
twelth_graders = complete_data[(complete_data["grade"] == "12th")]
print(ninth_graders)


# In[47]:


ninth_graders_math_scores = ninth_graders.groupby(["school_name"]).mean()["math_score"]
print(ninth_graders_math_scores)


# In[48]:


tenth_graders_math_scores = tenth_graders.groupby(["school_name"]).mean()["math_score"]
eleventh_graders_math_scores = eleventh_graders.groupby(["school_name"]).mean()["math_score"]
twelfth_graders_math_scores = twelth_graders.groupby(["school_name"]).mean()["math_score"]
print(eleventh_graders_math_scores)


# In[50]:


ninth_graders_reading_scores = ninth_graders.groupby(["school_name"]).mean()["reading_score"]
tenth_graders_reading_scores = tenth_graders.groupby(["school_name"]).mean()["reading_score"]
eleventh_graders_reading_scores = eleventh_graders.groupby(["school_name"]).mean()["reading_score"]
twelfth_graders_reading_scores = twelth_graders.groupby(["school_name"]).mean()["reading_score"]
print(twelfth_graders_reading_scores)


# In[51]:


math_scores_by_grade = pd.DataFrame({"9th": ninth_graders_math_scores,"10th": tenth_graders_math_scores,"11th": eleventh_graders_math_scores,"12th": twelfth_graders_math_scores})

math_scores_by_grade.head()


# In[52]:


reading_scores_by_grade = pd.DataFrame({"9th": ninth_graders_reading_scores,"10th": tenth_graders_reading_scores,"11th": eleventh_graders_reading_scores,"12th": twelfth_graders_reading_scores})

reading_scores_by_grade.head()


# In[53]:


per_student_budget.describe()


# In[54]:


spending_bins =[0, 585, 630, 645, 675]
pd.cut(per_student_budget, spending_bins)


# In[55]:


per_student_budget.groupby(pd.cut(per_student_budget, spending_bins)).count()


# In[56]:


bin_names = ["<$584", "$585-629", "$630-644", "$645-675"]


# In[57]:


per_school_summary_df["Spending Ranges (Per Student)"] = pd.cut(per_student_budget, spending_bins, labels=bin_names)
per_school_summary_df


# In[60]:


spending_math_scores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Math Score"]

spending_reading_scores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Reading Score"]

spending_passing_math = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Math"]

spending_passing_reading = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Reading"]

overall_passing_spending = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Overall Passing"]
print(overall_passing_spending)


# In[62]:


spending_summary_df = pd.DataFrame({"Average Math Score" : spending_math_scores,"Average Reading Score": spending_reading_scores,"% Passing Math": spending_passing_math,"% Passing Reading": spending_passing_reading,"% Overall Passing": overall_passing_spending})

spending_summary_df


# In[63]:


school_size_bins = [0, 1000, 2000, 5000]
school_group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[64]:


per_school_summary_df["School Size"] = pd.cut(per_school_summary_df["Total Students"], school_size_bins, labels=school_group_names)

per_school_summary_df


# In[65]:


size_math_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Math Score"]
size_reading_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Reading Score"]
size_passing_math = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Math"]
size_passing_reading = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Reading"]
size_overall_passing = per_school_summary_df.groupby(["School Size"]).mean()["% Overall Passing"]


# In[ ]:


size_summary_df = pd.DataFrame({"Average Math Score" : size_math_scores,"Average Reading Score": size_reading_scores,"% Passing Math": size_passing_math,"% Passing Reading": size_passing_reading,"% Overall Passing": size_overall_passing})

size_summary_df


# In[67]:


type_math_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Math Score"]
type_reading_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Reading Score"]
type_passing_math = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Math"]
type_passing_reading = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Reading"]
type_overall_passing = per_school_summary_df.groupby(["School Type"]).mean()["% Overall Passing"]


# In[68]:


type_summary_df = pd.DataFrame({"Average Math Score" : type_math_scores, "Average Reading Score": type_reading_scores,"% Passing Math": type_passing_math,"% Passing Reading": type_passing_reading,"% Overall Passing": type_overall_passing})

type_summary_df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




