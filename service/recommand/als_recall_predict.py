"""
召回模型预测
"""

from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALSModel
from conf import als_model_path
from pyspark.sql import Row
from db.db_connect import replace_recommend, select_users


def model_predict():
    spark = SparkSession.builder.getOrCreate()
    als_model = ALSModel.load(als_model_path)
    user_row_list = []
    data = select_users()

    for user in data:
        user_row_list.append(Row(user_id=user[0]))

    # 给用户做预测
    df = spark.createDataFrame(user_row_list)
    predict_df = als_model.recommendForUserSubset(df, 300)
    predict_df = predict_df.toPandas()
    store_to_db(predict_df)


def store_to_db(predict_df):
    for index, row in predict_df.iterrows():
        print(row)
        user_id = row["user_id"]
        recommend_shop_id_list = []
        for item in row["recommendations"]:
            recommend_shop_id_list.append(item["shop_id"])
        recommend_shop_id_list = str(recommend_shop_id_list)
        recommend_shop_id_list = recommend_shop_id_list.replace('[', '')
        recommend_shop_id_list = recommend_shop_id_list.replace(']', '')
        replace_recommend(user_id, recommend_shop_id_list)


model_predict()
