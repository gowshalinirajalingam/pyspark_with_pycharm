#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pyspark.sql import SQLContext
import pyspark


# In[7]:


from pyspark import SparkContext 
from pyspark.conf import SparkConf
from  pyspark.sql import SparkSession


# In[8]:


spark = SparkSession.builder     .master("local")     .appName("Word Count")     .config("spark.some.config.option", "some-value")     .getOrCreate()


# In[11]:


df = spark.read.option("header", "true").csv("C:\\Users\\GowshaliniR\\Desktop\\data.csv")


# In[13]:


df.show()


# In[15]:


df.createOrReplaceTempView("table1")
df2 = spark.sql("SELECT * from table1")
df2.collect()
df2.show()


# In[ ]:




