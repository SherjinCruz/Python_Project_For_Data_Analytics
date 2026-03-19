# Overview

Welcome to my analysis of the data job market, focusing on data analyst roles. This project was created out of a desire to navigate and understand the job market more effectively. It delves into the top-paying and in-demand skills to help find optimal job opportunities for data analysts.

The data sourced from [Luke Barousse's Python Course](https://lukebarousse.com/python) which provides a foundation for my analysis, containing detailed information on job titles, salaries, locations, and essential skills. Through a series of Python scripts, I explore key questions such as the most demanded skills, salary trends, and the intersection of demand and salary in data analytics.

# The Questions

Below are the questions I want to answer in my project:

1. What are the skills most in demand for the top 3 most popular data roles?
2. How are in-demand skills trending for Data Analysts?
3. How well do jobs and skills pay for Data Analysts?
4. What are the optimal skills for data analysts to learn? (High Demand AND High Paying)

# Tools I Used

For my deep dive into the data analyst job market, I harnessed the power of several key tools:

- **Python:** The backbone of my analysis, allowing me to analyze the data and find critical insights.I also used the following Python libraries:
    - **Pandas Library:** This was used to analyze the data.
    - **Matplotlib Library:** I visualized the data.
    - **Seaborn Library:** Helped me create more advanced visuals.
- **Jupyter Notebooks:** The tool I used to run my Python scripts which let me easily include my notes and analysis.
- **Visual Studio Code:** My go-to for executing my Python scripts.
- **Git & GitHub:** Essential for version control and sharing my Python code and analysis, ensuring collaboration and project tracking.

# Data Preparation and Cleanup

This section outlines the steps taken to prepare the data for analysis, ensuring accuracy and usability.

## Import & Clean Up Data

I start by importing necessary libraries and loading the dataset, followed by initial data cleaning tasks to ensure data quality.

```python
# Importing Libraries
import ast
import pandas as pd
import seaborn as sns
from datasets import load_dataset
import matplotlib.pyplot as plt  

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)
```

## Filter US Jobs

To focus my analysis on the U.S. job market, I apply filters to the dataset, narrowing down to roles based in the United States.

```python
df_US = df[df['job_country'] == 'United States']

```
# The Analysis

Each Jupyter notebook for this project aimed at investigating specific aspects of the data job market. Here’s how I approached each question:

## 1. What are the most demanded skills for the top 3 most popular data roles?

To find the most demanded skills for the top 3 most popular data roles. I filtered out those positions by which ones were the most popular, and got the top 5 skills for these top 3 roles. This query highlights the most popular job titles and their top skills, showing which skills I should pay attention to depending on the role I'm targeting.

View my notebook with detailed steps here [Skill Demand](/3_project/2_skill_demand.ipynb)

```python
fig,ax = plt.subplots(len(job_titles),1)
for i,titles in enumerate(job_titles):
    df_plot_percent = df_skills_perc[df_skills_perc['job_title_short'] == titles].head(5)
    sns.barplot(data=df_plot_percent,x='percent',y='job_skills', ax=ax[i],legend=False, hue='count',palette='dark:r_r')
    ax[i].set_xlabel('Percent of Job Count')
    ax[i].set_ylabel('')
    ax[i].set_title(titles)
    ax[i].set_xlim(0,15)
    ax[i].xaxis.set_major_formatter(plt.FuncFormatter (lambda x,pos: f'{x}%'))

    for n,v in enumerate(df_plot_percent['percent']):
        ax[i].text(v,n,f'{v:.0f}%',va='center')
    if i != (len(job_titles)-1):
        ax[i].set_xticks([])

fig.suptitle('Likelihood of Skills Required in Job Postings')
fig.tight_layout(h_pad=.5) #fix the overlap

```
### Results

![Likelihood of Skills Requested in the US Job Postings](/3_project/Images/Liklihood%20of%20Skills%20Required%20in%20Job%20Postings.png)

*Bar graph visualizing the salary for the top 3 data roles and their top 5 skills associated with each.*

### Insights:

- SQL is the most requested skill for Data Analysts and Data Scientists, with it in over half the job postings for both roles. For Data Engineers, Python is the most sought-after skill, appearing in 68% of job postings.
- Data Engineers require more specialized technical skills (AWS, Azure, Spark) compared to Data Analysts and Data Scientists who are expected to be proficient in more general data management and analysis tools (Excel, Tableau).
- Python is a versatile skill, highly demanded across all three roles, but most prominently for Data Scientists (72%) and Data Engineers (65%).

## 2. How are in-demand skills trending for Data Analysts?

To find how skills are trending in 2023 for Data Analysts, I filtered data analyst positions and grouped the skills by the month of the job postings. This got me the top 5 skills of data analysts by month, showing how popular skills were throughout 2023.

View my notebook with detailed steps here: [Skills Trend](/3_project/3_skills_trend.ipynb).

### Visualize Data

```python

sns.lineplot(data=df_DA_US_percent_top_5,legend=False, dashes=False,palette='tab10')
sns.set_theme(style='ticks')
sns.despine()
plt.xlabel('2023')
plt.ylabel('Likelihood of Job Postings')
plt.title('Trending Top Skills of Data Analyst in US')
ax=plt.gca()
#ax.yaxis.set_major_formatter(plt.FuncFormatter (lambda x,pos: f'{x:.0f}%'))
from matplotlib.ticker import PercentFormatter
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))

for i in range(5):
    plt.text(11,df_DA_US_percent_top_5.iloc[-1,i],df_DA_US_percent_top_5.columns[i])

```

### Results

![Trending Top Skills for Data Analysts in the US](/3_project/Images/Trending%20Top%20Skills%20For%20Data%20Analyst%20in%20US.png)  
*Bar graph visualizing the trending top skills for data analysts in the US in 2023.*

### Insights:
- SQL remains the most consistently demanded skill throughout the year, although it shows a gradual decrease in demand.
- Excel experienced a significant increase in demand starting around September, surpassing both Python and Tableau by the end of the year.
- Both Python and Tableau show relatively stable demand throughout the year with some fluctuations but remain essential skills for data analysts. Power BI, while less demanded compared to the others, shows a slight upward trend towards the year's end.

## 3. How well do jobs and skills pay for Data Analysts?

To identify the highest-paying roles and skills, I only got jobs in the United States and looked at their median salary. But first I looked at the salary distributions of common data jobs like Data Scientist, Data Engineer, and Data Analyst, to get an idea of which jobs are paid the most. 

View my notebook with detailed steps here: [Salary Analysis](/3_project/4_salary_analysis.ipynb).

#### Visualize Data 

```python

sns.boxplot(data=df_US_top_6,x='salary_year_avg',y='job_title_short',order=median)
sns.set_theme(style='ticks')
#df_US_top_6.plot(kind='box',column='salary_year_avg',by='job_title_short',vert=False)
plt.ylabel('')
plt.xlabel('Yearly Salary ($USD)')
plt.xlim(0,600000)
plt.title("Salary Distribution of Data Jobs in US")
ax=plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x,pos: f'${int(x/1000)}k'))
plt.show()

```

#### Results

![Salary Distributions of Data Jobs in the US](/3_project/Images/Salary%20Distribution%20of%20Data%20Jobs%20in%20US.png)  
*Box plot visualizing the salary distributions for the top 6 data job titles.*

#### Insights

- There's a significant variation in salary ranges across different job titles. Senior Data Scientist positions tend to have the highest salary potential, with up to $600K, indicating the high value placed on advanced data skills and experience in the industry.

- Senior Data Engineer and Senior Data Scientist roles show a considerable number of outliers on the higher end of the salary spectrum, suggesting that exceptional skills or circumstances can lead to high pay in these roles. In contrast, Data Analyst roles demonstrate more consistency in salary, with fewer outliers.

- The median salaries increase with the seniority and specialization of the roles. Senior roles (Senior Data Scientist, Senior Data Engineer) not only have higher median salaries but also larger differences in typical salaries, reflecting greater variance in compensation as responsibilities increase.

### Highest Paid & Most Demanded Skills for Data Analysts

Next, I narrowed my analysis and focused only on data analyst roles. I looked at the highest-paid skills and the most in-demand skills. I used two bar charts to showcase these.

#### Visualize Data

```python

fig,ax=plt.subplots(2,1)
sns.set_theme(style='ticks')
sns.barplot(data=df_DA_top_pay,x='median',y=df_DA_top_pay.index,hue='median',palette='dark:g_r',ax=ax[0],legend=False)
ax[0].set_title('Top 10 Highest Paid Skills for Data Analyst')
ax[0].set_xlabel('Yearly Salary ($USD)')
ax[0].set_ylabel('')
ax[0].xaxis.set_major_formatter(plt.FuncFormatter (lambda x,pos: f'${int(x/1000)}K'))

sns.barplot(data=df_DA_skills,x='count',y=df_DA_top_pay.index,hue='count',palette='dark:r_r',ax=ax[1])
ax[1].set_title('Top 10 Most In Demand Skills for Data Analyst')
ax[1].set_xlabel('Count')
ax[1].set_ylabel('')
ax[1].legend().remove()
sns.despine()
plt.tight_layout()

```
#### Results
Here's the breakdown of the highest-paid & most in-demand skills for data analysts in the US:

![The Highest Paid & Most In-Demand Skills for Data Analysts in the US](/3_project/Images/Highest%20Paid%20and%20Most%20In%20Demand%20Skills%20for%20Data%20Analytics%20in%20US.png)
*Two separate bar graphs visualizing the highest paid skills and most in-demand skills for data analysts in the US.*

#### Insights:

- The top graph shows specialized technical skills like `dplyr`, `Bitbucket`, and `Gitlab` are associated with higher salaries, some reaching up to $200K, suggesting that advanced technical proficiency can increase earning potential.

- The bottom graph highlights that foundational skills like `Excel`, `PowerPoint`, and `SQL` are the most in-demand, even though they may not offer the highest salaries. This demonstrates the importance of these core skills for employability in data analysis roles.

- There's a clear distinction between the skills that are highest paid and those that are most in-demand. Data analysts aiming to maximize their career potential should consider developing a diverse skill set that includes both high-paying specialized skills and widely demanded foundational skills.

## 4. What are the most optimal skills to learn for Data Analysts?

To identify the most optimal skills to learn ( the ones that are the highest paid and highest in demand) I calculated the percent of skill demand and the median salary of these skills. To easily identify which are the most optimal skills to learn. 

View my notebook with detailed steps here: [Optimal Skills](/3_project/5_optimal_skills.ipynb).

#### Visualize Data

```python

sns.scatterplot(data=df_DA_skills_demand,x='percent',y='median_salary',hue='job_skills',palette='deep',legend=False)

for i,txt in enumerate(df_DA_skills_demand.index):
    plt.text(df_DA_skills_demand['percent'].iloc[i]+.1,df_DA_skills_demand['median_salary'].iloc[i],txt)
plt.title('Most Optimal Skills For Data Analyst Jobs')
plt.xlabel('Percent of Data Analyst Jobs')
plt.ylabel('Median Salary ($USD)')
ax=plt.gca()

from matplotlib.ticker import PercentFormatter
ax.xaxis.set_major_formatter(PercentFormatter(decimals=0))
#ax.xaxis.set_major_formatter(plt.FuncFormatter (lambda x,pos: f'{x}%'))
ax.yaxis.set_major_formatter(plt.FuncFormatter (lambda x,pos: f'${int(x/1000)}k'))

sns.despine()
plt.show()
```
#### Results

![Most Optimal Skills for Data Analysts in the US](/3_project/Images/Most%20Optimal%20Skills%20for%20Data%20Analyst%20in%20US.png)    
*A scatter plot visualizing the most optimal skills (high paying & high demand) for data analysts in the US.*

#### Insights:

- The skill `Oracle` appears to have the highest median salary of nearly $97K, despite being less common in job postings. This suggests a high value placed on specialized database skills within the data analyst profession.

- More commonly required skills like `Excel` and `SQL` have a large presence in job listings but lower median salaries compared to specialized skills like `Python` and `Tableau`, which not only have higher salaries but are also moderately prevalent in job listings.

- Skills such as `Python`, `Tableau`, and `SQL Server` are towards the higher end of the salary spectrum while also being fairly common in job listings, indicating that proficiency in these tools can lead to good opportunities in data analytics.

### Visualizing Different Techonologies

Let's visualize the different technologies as well in the graph. We'll add color labels based on the technology (e.g., {Programming: Python})

#### Visualize Data

```python

sns.scatterplot(data=df_plot,x='percent',y='median_salary',hue='technology',palette='deep')

for i,txt in enumerate(df_plot['job_skills']):
    plt.text(df_plot['percent'].iloc[i]+.1,df_plot['median_salary'].iloc[i],txt)
plt.title('Most Optimal Skills For Data Analyst Jobs')
plt.xlabel('Percent of Data Analyst Jobs')
plt.ylabel('Median Salary ($USD)')
ax=plt.gca()

from matplotlib.ticker import PercentFormatter
ax.xaxis.set_major_formatter(PercentFormatter(decimals=0))
#ax.xaxis.set_major_formatter(plt.FuncFormatter (lambda x,pos: f'{x}%'))
ax.yaxis.set_major_formatter(plt.FuncFormatter (lambda x,pos: f'${int(x/1000)}k'))

sns.despine()
plt.show()

```
#### Results

![Most Optimal Skills for Data Analysts in the US with Coloring by Technology](/3_project/Images/Most%20Optimal%20Skills%20for%20Data%20Analyst%20in%20US%20by%20Technology.png)  
*A scatter plot visualizing the most optimal skills (high paying & high demand) for data analysts in the US with color labels for technology.*

#### Insights:

- The scatter plot shows that most of the `programming` skills (colored blue) tend to cluster at higher salary levels compared to other categories, indicating that programming expertise might offer greater salary benefits within the data analytics field.

- The database skills (colored orange), such as Oracle and SQL Server, are associated with some of the highest salaries among data analyst tools. This indicates a significant demand and valuation for data management and manipulation expertise in the industry.

- Analyst tools (colored green), including Tableau and Power BI, are prevalent in job postings and offer competitive salaries, showing that visualization and data analysis software are crucial for current data roles. This category not only has good salaries but is also versatile across different types of data tasks.

# What I Learned

Throughout this project, I deepened my understanding of the data analyst job market and enhanced my technical skills in Python, especially in data manipulation and visualization. Here are a few specific things I learned:

- **Advanced Python Usage**: Utilizing libraries such as Pandas for data manipulation, Seaborn and Matplotlib for data visualization, and other libraries helped me perform complex data analysis tasks more efficiently.
- **Data Cleaning Importance**: I learned that thorough data cleaning and preparation are crucial before any analysis can be conducted, ensuring the accuracy of insights derived from the data.
- **Strategic Skill Analysis**: The project emphasized the importance of aligning one's skills with market demand. Understanding the relationship between skill demand, salary, and job availability allows for more strategic career planning in the tech industry.


# Insights

This project provided several general insights into the data job market for analysts:

- **Skill Demand and Salary Correlation**: There is a clear correlation between the demand for specific skills and the salaries these skills command. Advanced and specialized skills like Python and Oracle often lead to higher salaries.
- **Market Trends**: There are changing trends in skill demand, highlighting the dynamic nature of the data job market. Keeping up with these trends is essential for career growth in data analytics.
- **Economic Value of Skills**: Understanding which skills are both in-demand and well-compensated can guide data analysts in prioritizing learning to maximize their economic returns.


# Challenges I Faced

This project was not without its challenges, but it provided good learning opportunities:

- **Data Inconsistencies**: Handling missing or inconsistent data entries requires careful consideration and thorough data-cleaning techniques to ensure the integrity of the analysis.
- **Complex Data Visualization**: Designing effective visual representations of complex datasets was challenging but critical for conveying insights clearly and compellingly.
- **Balancing Breadth and Depth**: Deciding how deeply to dive into each analysis while maintaining a broad overview of the data landscape required constant balancing to ensure comprehensive coverage without getting lost in details.


# Conclusion

This exploration into the data analyst job market has been incredibly informative, highlighting the critical skills and trends that shape this evolving field. The insights I got enhance my understanding and provide actionable guidance for anyone looking to advance their career in data analytics. As the market continues to change, ongoing analysis will be essential to stay ahead in data analytics. This project is a good foundation for future explorations and underscores the importance of continuous learning and adaptation in the data field.