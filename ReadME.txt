1)Install java
2)download spark folder here 'https://spark.apache.org/downloads.html'
3)
Setting up Spark
-------------------
   a. tar -xvzf spark-1.6.0.tgz # to extract the contents of the archive
   b. mv spark-1.6.0 /usr/local/spark # moves the folder from Downloads to local
   d. cd /usr/local/spark
   e. export PATH=$PATH:/usr/local/spark/bin  #Setting up the environment for Spark
   f. $ source ~/.bashrc
4) Verifying the Spark Installation
--------------------------------------
   a. $spark-shell
   
5)two ways of running python script using spark
        i) using spark-submit
              gawshalini@gawshalini:~/Documents/HSS/churn prediction$ /usr/local/spark/spark-2.4.3-bin-hadoop2.7/bin/spark-submit 4daysprotocolsummary.py
                 or
              /usr/local/spark/spark-2.4.3-bin-hadoop2.7/bin$ ./spark-submit /home/gawshalini/Documents/HSS/churn\ prediction/4daysprotocolsummary.py
         ii) using pycharm  
                follow this tutorial: (https://medium.com/hackernoon/pycharm-and-apache-spark-on-mac-os-x-990af6dc6f38#.jk5hl4kz0)
                             youtube: https://www.youtube.com/watch?v=t-cL3cL7qew
                To install dependencies add requirement.txt file and add dependencies inside that
                        for that follow this git link  (https://github.com/Gauravshah/pyspark-intellij-tutorial)
                        
               
               
               
      
                
