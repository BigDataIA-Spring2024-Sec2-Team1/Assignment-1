from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.generic.database import SQL
from diagrams.onprem.queue import Kafka
from diagrams.aws.compute import Lambda

with Diagram("ETL Data Pipeline", show=False):

    with Cluster("ETL Process"):
        gymequip = Custom("Equipment", "./Resources/GYM-EQUIP.jpg")
        micro_controller = Custom("Micro Controller", "./Resources/ardino.jpg")
        kafka = Kafka("Kafka")
        transform = Lambda("Transform")
        load = SQL("Load")

        gymequip >> micro_controller >> kafka >> transform >> load
