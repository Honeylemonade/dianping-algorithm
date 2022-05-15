"""
召回模型训练
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.recommendation import ALS
from conf import rate_path, als_model_path


def train_model():
    spark = SparkSession.builder.appName('DianpingRecommendations').getOrCreate()
    ratings = spark.read.csv(rate_path, header=True)

    # 数据清洗
    ratings = clean_data(ratings)
    als = init_als_model()

    # 训练模型
    model = als.fit(ratings)

    # 保存模型
    model.write().overwrite().save(als_model_path)


def clean_data(ratings):
    ratings = ratings. \
        withColumn("user_id", col("user_id").cast("integer")). \
        withColumn("shop_id", col("shop_id").cast("integer")). \
        withColumn("rate", col("rate").cast("float")). \
        drop("timestamp")
    print("数据清洗后:")
    ratings.show()
    return ratings


def init_als_model():
    return ALS(userCol="user_id",
               itemCol="shop_id",
               ratingCol="rate",
               maxIter=5,
               regParam=0.01,
               rank=150,
               nonnegative=True,
               implicitPrefs=False,
               coldStartStrategy="drop")


train_model()
