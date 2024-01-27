from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.integration import Eventbridge
from diagrams.custom import Custom
from diagrams import Edge
from diagrams.aws.ml import Comprehend

with Diagram("Resume Processing", show=False):
   ats = Custom("ATS UI", "./Resources/ATS.png")
   api = APIGateway("API")
   api1 = APIGateway("API")
   eventbridge1 = Eventbridge("Eventbridge")
   _lambda1 = Lambda("Lambda")
   
   with Cluster("Data Storage"):
      _lambda = Lambda("Lambda")
      eventbridge = Eventbridge("Eventbridge")
      s3 = S3("S3")

   with Cluster("Comprehend"):
      comprenhend = Comprehend("Comprehend") 

   with Cluster("Database"):
      rds = RDS("RDS")

   with Cluster("Job Description processing"):
      lam = Lambda("Lambda")

   ats >> api >> Edge(label="Upload resume store in s3") >> _lambda >> s3 >> Edge(label="Event Trigger") >> eventbridge >> comprenhend >> rds

   ats >> api1 >>  Edge(label="Job Description processing") >> lam >> comprenhend

   rds >> eventbridge1 >> _lambda1 >> ats
   
   