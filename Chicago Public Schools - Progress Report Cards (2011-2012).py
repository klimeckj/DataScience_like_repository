#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')
import ibm_db_sa
import ibm_db
import sqlalchemy


# In[2]:


get_ipython().run_line_magic('sql', 'ibm_db_sa://cbz91652:m4b%40n5t1k069mhs0@dashdb-txn-sbox-yp-lon02-02.services.eu-gb.bluemix.net:50000/BLUDB')


# In[6]:


get_ipython().run_line_magic('sql', "select * from SYSCAT.TABLES where TABNAME = 'SCHOOLS'")


# In[7]:


get_ipython().run_line_magic('sql', "select TABSCHEMA, TABNAME, CREATE_TIME from SYSCAT.TABLES where TABSCHEMA='cbz91652'")


# In[10]:


get_ipython().run_line_magic('sql', "select count(*) from SYSCAT.COLUMNS where TABNAME = 'SCHOOLS'")


# In[14]:


get_ipython().run_line_magic('sql', "select COLNAME, TYPENAME, LENGTH from SYSCAT.COLUMNS where TABNAME = 'SCHOOLS'")


# In[15]:


get_ipython().run_line_magic('sql', "select distinct(NAME), COLTYPE, LENGTH from SYSIBM.SYSCOLUMNS where TBNAME = 'SCHOOLS'")


# In[17]:


get_ipython().run_line_magic('sql', 'SELECT * FROM SCHOOLS;')


# In[20]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM schools WHERE "Elementary, Middle, or High School" = \'ES\'')


# In[22]:


get_ipython().run_line_magic('sql', 'SELECT MAX(safety_score) FROM schools;')


# In[21]:


get_ipython().run_line_magic('sql', 'SELECT name_of_school FROM schools WHERE safety_score = (SELECT MAX(safety_score) FROM schools);')


# In[27]:


get_ipython().run_line_magic('sql', 'SELECT name_of_school FROM schools ORDER BY average_student_attendance DESC nulls last limit 10;')


# In[32]:


get_ipython().run_line_magic('sql', 'SELECT name_of_school, average_student_attendance FROM schools ORDER BY average_student_attendance  nulls last limit 5;')


# In[33]:


get_ipython().run_line_magic('sql', 'SELECT Name_of_School, Average_Student_Attendance  from SCHOOLS order by Average_Student_Attendance fetch first 5 rows only')


# In[39]:


get_ipython().run_line_magic('sql', "SELECT Name_of_School, REPLACE(Average_Student_Attendance, '%', '') AS Average_Student_attendance  from SCHOOLS order by Average_Student_Attendance fetch first 5 rows only")


# In[42]:


get_ipython().run_line_magic('sql', "SELECT Name_of_school, Average_Student_Attendance FROM schools WHERE DECIMAL(REPLACE(Average_Student_Attendance, '%', '0')) < 70 ORDER BY Average_Student_Attendance;")


# In[51]:


get_ipython().run_line_magic('sql', 'SELECT Community_Area_Name, SUM(College_Enrollment) FROM schools GROUP BY Community_Area_Name;')


# In[52]:


get_ipython().run_line_magic('sql', 'SELECT Community_Area_Name, SUM(College_Enrollment) FROM schools GROUP BY Community_Area_Name ORDER BY SUM(College_Enrollment) LIMIT 5;')


# In[65]:


get_ipython().run_line_magic('sql', 'SELECT c.hardship_index, s.College_Enrollment FROM chicago_socioeconomic_data c, schools s WHERE s.community_area_number = c.ca and college_enrollment = 4368')


# In[75]:


get_ipython().run_line_magic('sql', 'SELECT c.ca, c.hardship_index, s.College_Enrollment, s.community_area_name FROM chicago_socioeconomic_data c, schools s WHERE s.community_area_number = c.ca and college_enrollment = (SELECT MAX(s.College_Enrollment) FROM schools s)')


# In[ ]:




