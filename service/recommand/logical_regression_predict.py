import random

from joblib import load
import numpy as np
from conf import lr_model_path
from db.db_connect import select_recommend


class ShopProb:
    def __init__(self, id, prob):
        self.id = id
        self.prob = prob


def model_predict(user_id):
    # 根据 user_id 从数据库中取出召回的店铺 id 列表
    shop_id_list = __get_recall_shop_id_list(user_id)

    # 构建特征，该步骤应该从数据库中获取用户和商品特征进行拼装
    # Key：shop Id, value features
    user_shop_feature_list = []
    for i in range(len(shop_id_list)):
        user_shop_feature_list.append(__build_feature_array())

    # 加载模型，进行预测
    lr_model = load(lr_model_path)
    predict_result_list = lr_model.predict_proba(np.array(user_shop_feature_list))

    shop_prob_list = []
    for i in range(len(shop_id_list)):
        shop_prob_list.append(ShopProb(shop_id_list[i], predict_result_list[i][1]))

    # 排序
    shop_prob_list.sort(key=lambda x: x.prob, reverse=True)

    # 得到结果
    result_id = []
    for i in shop_prob_list:
        result_id.append(int(i.id))

    return result_id


def __get_recall_shop_id_list(user_id):
    data = select_recommend(user_id)
    return data[1].split(",")


def __build_feature_array():
    features = []

    for i in range(64):
        features.append(random.uniform(-8.0, 8.0))
    return np.array(features)
