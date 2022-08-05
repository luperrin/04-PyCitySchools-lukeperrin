# Add the Pandas dependency.
import pandas as pd

# File to Load (Remember to change the path if needed.)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read the School Data and Student Data and store into a Pandas DataFrame
school_data_df = pd.read_csv(school_data_to_load)
student_data_df = pd.read_csv(student_data_to_load)

# Cleaning Student Names and Replacing Substrings in a Python String
# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ", "Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]

# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word, "")

# Check names.
print(student_data_df.head(10))


## Deliverable 1: Replace the reading and math scores.

### Replace the 9th grade reading and math scores at Thomas High School with NaN.
# Install numpy using conda install numpy or pip install numpy.
# Step 1. Import numpy as np.
import numpy as np
THS_9thgraders = student_data_df[(student_data_df["grade"] == "9th") & (student_data_df["reading_score"] >= 70)]

# # Step 2. Use the loc method on the student_data_df to select all the reading scores from the 9th grade at Thomas High School and replace them with NaN.
student_data_df.loc[student_data_df['grade'] == "9th", student_data_df['reading_score']]= None
print(student_data_df['reading_score'])
#
# #  Step 3. Refactor the code in Step 2 to replace the math scores with NaN.
# student_data_df.loc[:, 'math_score'] = None
# print(student_data_df['math_score'])
# #  Step 4. Check the student data for NaN's.
print(student_data_df.isnull())
student_data_df.isnull().sum()


## Deliverable 2 : Repeat the school district analysis
### District Summary
# Combine the data into a single dataset
school_data_complete_df = pd.merge(student_data_df, school_data_df, how="left", on=["school_name", "school_name"])
school_data_complete_df.head()
# Calculate the Totals (Schools and Students)
school_count = len(school_data_complete_df["school_name"].unique())
student_count = school_data_complete_df["Student ID"].count()

# Calculate the Total Budget
total_budget = school_data_df["budget"].sum()
# Calculate the Average Scores using the "clean_student_data".
average_reading_score = school_data_complete_df["reading_score"].mean()
average_math_score = school_data_complete_df["math_score"].mean()
# Step 1. Get the number of students that are in ninth grade at Thomas High School.
# These students have no grades.
#
#
# # Get the total student count
# student_count = school_data_complete_df["Student ID"].count()
#
# # Step 2. Subtract the number of students that are in ninth grade at
# # Thomas High School from the total student count to get the new total student count.
#
# # Calculate the passing rates using the "clean_student_data".
# passing_math_count = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)].count()["student_name"]
# passing_reading_count = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)].count()[
#     "student_name"]
# # Step 3. Calculate the passing percentages with the new total student count.
#
# # Calculate the students who passed both reading and math.
# passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)
#                                                & (school_data_complete_df["reading_score"] >= 70)]
#
# # Calculate the number of students that passed both reading and math.
# overall_passing_math_reading_count = passing_math_reading["student_name"].count()
#
# # Step 4.Calculate the overall passing percentage with new total student count.
#
# # Create a DataFrame
# district_summary_df = pd.DataFrame(
#     [{"Total Schools": school_count,
#       "Total Students": student_count,
#       "Total Budget": total_budget,
#       "Average Math Score": average_math_score,
#       "Average Reading Score": average_reading_score,
#       "% Passing Math": passing_math_percentage,
#       "% Passing Reading": passing_reading_percentage,
#       "% Overall Passing": overall_passing_percentage}])
#
# # Format the "Total Students" to have the comma for a thousands separator.
# district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)
# # Format the "Total Budget" to have the comma for a thousands separator, a decimal separator and a "$".
# district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)
# # Format the columns.
# district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)
# district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)
# district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.1f}".format)
# district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.1f}".format)
# district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.1f}".format)
#
# # Display the data frame
# district_summary_df
# ##  School Summary
# # Determine the School Type
# per_school_types = school_data_df.set_index(["school_name"])["type"]
#
# # Calculate the total student count.
# per_school_counts = school_data_complete_df["school_name"].value_counts()
#
# # Calculate the total school budget and per capita spending
# per_school_budget = school_data_complete_df.groupby(["school_name"]).mean()["budget"]
# # Calculate the per capita spending.
# per_school_capita = per_school_budget / per_school_counts
#
# # Calculate the average test scores.
# per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]
# per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]
#
# # Calculate the passing scores by creating a filtered DataFrame.
# per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]
# per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]
#
# # Calculate the number of students passing math and passing reading by school.
# per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]
# per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]
#
# # Calculate the percentage of passing math and reading scores per school.
# per_school_passing_math = per_school_passing_math / per_school_counts * 100
# per_school_passing_reading = per_school_passing_reading / per_school_counts * 100
#
# # Calculate the students who passed both reading and math.
# per_passing_math_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)
#                                                    & (school_data_complete_df["math_score"] >= 70)]
#
# # Calculate the number of students passing math and passing reading by school.
# per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]
#
# # Calculate the percentage of passing math and reading scores per school.
# per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100
# # Create the DataFrame
# per_school_summary_df = pd.DataFrame({
#     "School Type": per_school_types,
#     "Total Students": per_school_counts,
#     "Total School Budget": per_school_budget,
#     "Per Student Budget": per_school_capita,
#     "Average Math Score": per_school_math,
#     "Average Reading Score": per_school_reading,
#     "% Passing Math": per_school_passing_math,
#     "% Passing Reading": per_school_passing_reading,
#     "% Overall Passing": per_overall_passing_percentage})
#
# # per_school_summary_df.head()
# # Format the Total School Budget and the Per Student Budget
# per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)
# per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)
#
# # Display the data frame
# per_school_summary_df
# # Step 5.  Get the number of 10th-12th graders from Thomas High School (THS).
#
# # Step 6. Get all the students passing math from THS
#
# # Step 7. Get all the students passing reading from THS
#
# # Step 8. Get all the students passing math and reading from THS
#
# # Step 9. Calculate the percentage of 10th-12th grade students passing math from Thomas High School.
#
# # Step 10. Calculate the percentage of 10th-12th grade students passing reading from Thomas High School.
#
# # Step 11. Calculate the overall passing percentage of 10th-12th grade from Thomas High School.
#
#
# # Step 12. Replace the passing math percent for Thomas High School in the per_school_summary_df.
#
# # Step 13. Replace the passing reading percentage for Thomas High School in the per_school_summary_df.
#
# # Step 14. Replace the overall passing percentage for Thomas High School in the per_school_summary_df.
#
# # per_school_summary_df
# ## High and Low Performing Schools
# # Sort and show top five schools.
#
# # Sort and show top five schools.
#
# ## Math and Reading Scores by Grade
# # Create a DataFrame of scores by grade level using conditionals.
#
#
# # Group each grade level DataFrame by the school name for the average math score.
#
#
# # Group each grade level DataFrame by the school name for the average reading score.
#
# # Combine each grade level Series for average math scores into a single DataFrame.
#
# # Combine each grade level Series for average reading scores into a single DataFrame.
#
# # Format each grade column.
#
# # Remove the index.
#
#
# # Display the data frame
#
# ## Remove the index.
#
#
# # Display the data frame
#
# ## Scores by School Spending
# # Establish the spending bins and group names.
#
#
# # Categorize spending based on the bins.
#
# # Calculate averages for the desired columns.
#
# # Create the DataFrame
#
# # Format the DataFrame
#
# ## Scores by School Size
# # Establish the bins.
#
# # Categorize spending based on the bins.
#
# # Calculate averages for the desired columns.
#
# # Assemble into DataFrame.
#
# # Format the DataFrame
#
# ## Scores by School Type
# # Calculate averages for the desired columns.
#
# # Assemble into DataFrame.
#
# # # Format the DataFrame
#
#
# # In[208]:
#
#
# # Files to load
# school_data_to_load = "Resources/schools_complete.csv"
# student_data_to_load = "Resources/students_complete.csv"
#
#
# # In[209]:
#
#
# school_data_df = pd.read_csv(school_data_to_load)
# school_data_df
#
#
# # In[210]:
#
#
# # Read the student data file and store it in a Pandas DataFrame.
# student_data_df = pd.read_csv(student_data_to_load)
# student_data_df.head()
#
#
# # In[211]:
#
#
# # Determine if there are any missing values in the school data.
# school_data_df.count()
#
#
# # In[212]:
#
#
# # Determine if there are any missing values in the student data.
# student_data_df.count()
#
#
# # In[213]:
#
#
# # Determine if there are any missing values in the school data.
# school_data_df.isnull()
#
#
# # In[214]:
#
#
# # Determine if there are any missing values in the student data.
# student_data_df.isnull()
#
#
# # In[215]:
#
#
# # Determine if there are any missing values in the student data.
# student_data_df.isnull().sum()
#
#
# # In[216]:
#
#
# # Determine if there are not any missing values in the school data.
# school_data_df.notnull()
#
#
# # In[217]:
#
#
# # Determine if there are not any missing values in the student data.
# student_data_df.notnull().sum()
#
#
# # In[218]:
#
#
# # Put the student names in a list.
# student_names = student_data_df["student_name"].tolist()
# student_names
#
#
# # In[219]:
#
#
# # Split the student name and determine the length of the split name.
# for name in student_names:
#     print(name.split(), len(name.split()))
#
# # Create a new list and use it for the for loop to iterate through the list.
# students_to_fix = []
#
# # Use an if statement to check the length of the name.
# # If the name is greater than or equal to "3", add the name to the list.
#
# for name in student_names:
#     if len(name.split()) >= 3:
#         students_to_fix.append(name)
#
# # Get the length of the students whose names are greater than or equal to "3".
# len(students_to_fix)
#
#
# # In[220]:
#
#
# # Add the prefixes less than or equal to 4 to a new list.
# prefixes = []
# for name in students_to_fix:
#     if len(name.split()[0]) <= 4:
#         prefixes.append(name.split()[0])
#
# print(prefixes)
#
#
# # In[221]:
#
#
# # Add the suffixes less than or equal to 3 to a new list.
# suffixes = []
# for name in students_to_fix:
#     if len(name.split()[-1]) <= 3:
#         suffixes.append(name.split()[-1])
#
# print(suffixes)
#
#
# # In[222]:
#
#
# # Get the unique items in the "prefixes" list.
# set(prefixes)
# # Get the unique items in the "suffixes" list.
# set(suffixes)
#
#
# #
#
# # In[223]:
#
#
# # Strip "Mrs." from the student names
# for name in students_to_fix:
#     print(name.strip("Mrs."))
#
#
# # In[224]:
#
#
# # Replace "Dr." with an empty string.
# name = "Dr. Linda Santiago"
# name.replace("Dr.", "")
#
#
# # In[225]:
#
#
# # Add each prefix and suffix to remove to a list.
# prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]
# # Iterate through the "prefixes_suffixes" list and replace them with an empty space, "" when it appears in the student's name.
# for word in prefixes_suffixes:
#     student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")
#
#
# # In[226]:
#
#
# # Put the cleaned students' names in another list.
# student_names = student_data_df["student_name"].tolist()
# student_names
#
#
# # In[227]:
#
#
# # Create a new list and use it for the for loop to iterate through the list.
# students_fixed = []
#
# # Use an if statement to check the length of the name.
#
# # If the name is greater than or equal to 3, add the name to the list.
#
# for name in student_names:
#     if len(name.split()) >= 3:
#         students_fixed.append(name)
#
# # Get the length of the students' names that are greater than or equal to 3.
# len(students_fixed)
#
#
# # In[228]:
#
#
# # Add each prefix and suffix to remove to a list.
# prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]
# # Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
# for word in prefixes_suffixes:
#     student_data_df["student_name"].str.replace(word,"")
#
#
# # In[229]:
#
#
# # Combine the data into a single dataset.
# school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
# school_data_complete_df.head()
#
#
# # In[230]:
#
#
# # Get the total number of students.
# student_count = school_data_complete_df.count()
# student_count
#
#
# # In[231]:
#
#
# school_data_complete_df["Student ID"].count()
#
#
# # In[232]:
#
#
# # Calculate the total number of schools.
# school_count = school_data_df["school_name"].count()
# school_count
#
#
# # In[233]:
#
#
# # Calculate the total number of schools
# school_count_2 = school_data_complete_df["school_name"].unique()
# school_count_2
#
#
# # In[234]:
#
#
# # Calculate the total budget.
# total_budget = school_data_df["budget"].sum()
# total_budget
#
#
# # In[235]:
#
#
# # Calculate the average reading score.
# average_reading_score = school_data_complete_df["reading_score"].mean()
# average_reading_score
#
#
# # In[236]:
#
#
# # Calculate the average math score.
# average_math_score = school_data_complete_df["math_score"].mean()
# average_math_score
#
#
# # In[237]:
#
#
# passing_math = school_data_complete_df["math_score"] >= 70
# passing_reading = school_data_complete_df["reading_score"] >= 70
# passing_math
# passing_reading
#
#
# # In[238]:
#
#
# passing_math = school_data_complete_df["math_score"] >= 70
# passing_reading = school_data_complete_df["reading_score"] >= 70
#
# # Get all the students who are passing math in a new DataFrame.
# passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
# passing_math.head()
#
# # Calculate the number of students passing math.
# passing_math_count = passing_math["student_name"].count()
#
# # Calculate the number of students passing reading.
# passing_reading_count = passing_reading["student_name"].count()
#
#
# # In[ ]:
#
#
# # Calculate the percent that passed math.
# passing_math_percentage = passing_math_count / float(student_count) * 100
#
# # Calculate the percent that passed reading.
# passing_reading_percentage = passing_reading_count / float(student_count) * 100
#
#
# # In[ ]:
#
#
# # Calculate the students who passed both math and reading.
# passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]
#
# passing_math_reading.head()
#
#
# # In[ ]:
#
#
# # Calculate the number of students who passed both math and reading.
# overall_passing_math_reading_count = passing_math_reading["student_name"].count()
# overall_passing_math_reading_count
#
#
# # In[ ]:
#
#
# # Calculate the overall passing percentage.
# overall_passing_percentage = overall_passing_math_reading_count / student_count * 100
# overall_passing_percentage
#
#
# # In[ ]:
#
#
# # Adding a list of values with keys to create a new DataFrame.
# district_summary_df = pd.DataFrame(
#           [{"Total Schools": school_count,
#           "Total Students": student_count,
#           "Total Budget": total_budget,
#           "Average Math Score": average_math_score,
#           "Average Reading Score": average_reading_score,
#           "% Passing Math": passing_math_percentage,
#          "% Passing Reading": passing_reading_percentage,
#         "% Overall Passing": overall_passing_percentage}])
# district_summary_df
#
#
# # In[ ]:
#
#
# # Define a function that calculates the percentage of students that passed both
# # math and reading and returns the passing percentage when the function is called.
#
# def passing_math_percent(pass_math_count, student_count):
#     return pass_math_count / float(student_count) * 100
#
#
# # In[ ]:
#
#
# # # Call the function.
# # passing_math_percent(passing_math_count, total_student_count)
#
#
# # In[ ]:
#
#
# # Reorder the columns in the order you want them to appear.
# new_column_order = ["column2", "column4", "column1"]
#
# # Assign a new or the same DataFrame the new column order.
# df = df[new_column_order]
#
#
# # In[ ]:
#
#
# # Reorder the columns in the order you want them to appear.
# new_column_order = ["Total Schools", "Total Students", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]
#
# # Assign district summary df the new column order.
# district_summary_df = district_summary_df[new_column_order]
# district_summary_df
#
#
# # In[ ]:
#
#
# # Determine the school type.
# per_school_types = school_data_df.set_index(["school_name"])["type"]
# per_school_types
#
#
# # In[ ]:
#
#
# # Add the per_school_types into a DataFrame for testing.
# df = pd.DataFrame(per_school_types)
# df
#
#
# # In[ ]:
#
#
# # Calculate the total student count.
# per_school_counts = school_data_df["size"]
# per_school_counts
#
# # Calculate the total student count.
# per_school_counts = school_data_complete_df["school_name"].value_counts()
# per_school_counts
#
#
# # In[ ]:
#
#
# # Calculate the total school budget.
# per_school_budget = school_data_df.set_index(["school_name"])["budget"]
# per_school_budget
#
#
# # In[ ]:
#
#
# # Calculate the per capita spending.
# per_school_capita = per_school_budget / per_school_counts
# per_school_capita
#
#
# # In[ ]:
#
#
# # Calculate the math scores.
# student_school_math = student_data_df.set_index(["school_name"])["math_score"]
#
#
# # In[ ]:
#
#
# # Calculate the average math scores.
# per_school_averages = school_data_complete_df.groupby(["school_name"]).mean()
# per_school_averages
#
#
# # In[ ]:
#
#
# # Calculate the average test scores.
# per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]
#
# per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]
#
#
# # In[ ]:
#
#
# # Calculate the passing scores by creating a filtered DataFrame.
# per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]
#
# per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]
#
#
# # In[ ]:
#
#
# # Calculate the number of students passing math and passing reading by school.
# per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]
#
# per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]
#
#
# # In[ ]:
#
#
# # Calculate the percentage of passing math and reading scores per school.
# per_school_passing_math = per_school_passing_math / per_school_counts * 100
#
# per_school_passing_reading = per_school_passing_reading / per_school_counts * 100
#
#
# # In[ ]:
#
#
# # Calculate the students who passed both math and reading.
# per_passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]
#
# per_passing_math_reading.head()
#
#
# # In[ ]:
#
#
# # Calculate the number of students who passed both math and reading.
# per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]
#
#
# # In[ ]:
#
#
# # Calculate the overall passing percentage.
# per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100
#
#
# # In[ ]:
#
#
# # Adding a list of values with keys to create a new DataFrame.
#
# per_school_summary_df = pd.DataFrame({
#              "School Type": per_school_types,
#              "Total Students": per_school_counts,
#              "Total School Budget": per_school_budget,
#              "Per Student Budget": per_school_capita,
#              "Average Math Score": per_school_math,
#            "Average Reading Score": per_school_reading,
#            "% Passing Math": per_school_passing_math,
#            "% Passing Reading": per_school_passing_reading,
#            "% Overall Passing": per_overall_passing_percentage})
# per_school_summary_df.head()
#
#
# # In[ ]:
#
#
# # Format the Total School Budget and the Per Student Budget columns.
# per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)
#
# per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)
#
#
# # Display the data frame
# per_school_summary_df.head()
#
#
# # In[ ]:
#
#
# # Reorder the columns in the order you want them to appear.
# new_column_order = ["School Type", "Total Students", "Total School Budget", "Per Student Budget", "Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]
#
# # Assign district summary df the new column order.
# per_school_summary_df = per_school_summary_df[new_column_order]
#
# per_school_summary_df.head()
#
#
# # In[ ]:
#
#
# # Sort and show top five schools.
# top_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=False)
#
# top_schools.head()
#
#
# # In[ ]:
#
#
# # Sort and show top five schools.
# bottom_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=True)
#
# bottom_schools.head()
#
#
# # In[ ]:
#
#
# # Create a grade level DataFrames.
# ninth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "9th")]
#
# tenth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "10th")]
#
# eleventh_graders = school_data_complete_df[(school_data_complete_df["grade"] == "11th")]
#
# twelfth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "12th")]
#
#
# # In[ ]:
#
#
# # Group each grade level DataFrame by the school name for the average math score.
# ninth_grade_math_scores = ninth_graders.groupby(["school_name"]).mean()["math_score"]
#
# tenth_grade_math_scores = tenth_graders.groupby(["school_name"]).mean()["math_score"]
#
# eleventh_grade_math_scores = eleventh_graders.groupby(["school_name"]).mean()["math_score"]
#
# twelfth_grade_math_scores = twelfth_graders.groupby(["school_name"]).mean()["math_score"]
#
#
# # In[ ]:
#
#
# # Group each grade level DataFrame by the school name for the average reading score.
# ninth_grade_reading_scores = ninth_graders.groupby(["school_name"]).mean()["reading_score"]
#
# tenth_grade_reading_scores = tenth_graders.groupby(["school_name"]).mean()["reading_score"]
#
# eleventh_grade_reading_scores = eleventh_graders.groupby(["school_name"]).mean()["reading_score"]
#
# twelfth_grade_reading_scores = twelfth_graders.groupby(["school_name"]).mean()["reading_score"]
#
#
# # In[ ]:
#
#
# # Combine each grade level Series for average math scores by school into a single DataFrame.
# math_scores_by_grade = pd.DataFrame({
#                "9th": ninth_grade_math_scores,
#                "10th": tenth_grade_math_scores,
#                "11th": eleventh_grade_math_scores,
#                "12th": twelfth_grade_math_scores})
#
# math_scores_by_grade.head()
#
#
# # In[ ]:
#
#
# # Combine each grade level Series for average reading scores by school into a single DataFrame.
# reading_scores_by_grade = pd.DataFrame({
#               "9th": ninth_grade_reading_scores,
#               "10th": tenth_grade_reading_scores,
#               "11th": eleventh_grade_reading_scores,
#               "12th": twelfth_grade_reading_scores})
#
# reading_scores_by_grade.head()
#
#
# # In[ ]:
#
#
# # Format each grade column.
# math_scores_by_grade["9th"] = math_scores_by_grade["9th"].map("{:.1f}".format)
#
# math_scores_by_grade["10th"] = math_scores_by_grade["10th"].map("{:.1f}".format)
#
# math_scores_by_grade["11th"] = math_scores_by_grade["11th"].map("{:.1f}".format)
#
# math_scores_by_grade["12th"] = math_scores_by_grade["12th"].map("{:.1f}".format)
#
# # Make sure the columns are in the correct order.
# math_scores_by_grade = math_scores_by_grade[
#                ["9th", "10th", "11th", "12th"]]
#
# # Remove the index name.
# math_scores_by_grade.index.name = None
# # Display the DataFrame.
# math_scores_by_grade.head()
#
#
# # In[ ]:
#
#
# # Format each grade column.
# reading_scores_by_grade["9th"] = reading_scores_by_grade["9th"].map("{:,.1f}".format)
#
# reading_scores_by_grade["10th"] = reading_scores_by_grade["10th"].map("{:,.1f}".format)
#
# reading_scores_by_grade["11th"] = reading_scores_by_grade["11th"].map("{:,.1f}".format)
#
# reading_scores_by_grade["12th"] = reading_scores_by_grade["12th"].map("{:,.1f}".format)
#
# # Make sure the columns are in the correct order.
# reading_scores_by_grade = reading_scores_by_grade[
#                ["9th", "10th", "11th", "12th"]]
#
# # Remove the index name.
# reading_scores_by_grade.index.name = None
# # Display the data frame.
# reading_scores_by_grade.head()

