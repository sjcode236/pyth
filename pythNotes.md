
 
## check the  wiki   
http://linux.macrofinances.com/index.php/2016/02/12/python-django/  
   
http://scikit-learn.org/stable/tutorial/basic/tutorial.html   
Scikit-learn requires:    
Python (>= 2.7 or >= 3.3),    
NumPy (>= 1.8.2),   
SciPy (>= 0.13.3).   
If you already have a working installation of numpy and scipy, the easiest way to install scikit-learn is using pip   
pip isntall NumPy     
pip install SciPy     
pip install --upgrade pip   
pip install TensorFlow   


   
    
pip install -U scikit-learn         
  pip install -U sklearn       
  pip uninstall scikit-learn               
      
    

SPARK install  notes          
wget http://mirror.fibergrid.in/apache/spark/spark-1.6.1/spark-1.6.1-bin-hadoop2.4.tgz  (or download from apache spark web)        
Decompress the Spark file into /softw directory    
tar –xvf spark-1.6.1-bin-hadoop2.4.tgz –C /softw       
Make a softlink to the actual spark directory (This will be helpful for any version upgrade in future)      
ln -s spark-1.5.2-bin-hadoop2.4 spark        
SPARK_HOME=/softw/spark          
export PATH=$SPARK_HOME/bin:$PATH           
Source the changed .bashrc file by the command        
source  ~/.bashrc            
We have successfully configured spark in standalone mode. To check let’s launch the Spark Shell by the following command:    
          
**spark-shell**      
Now in the launched spark-shell, let’s check the Spark’s Scala shell version by the following command           
sc.version            
ls $SPARK_HOME/bin            
pyspark             



