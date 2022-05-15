from concurrent import futures
import grpc
from proto import dianping_pb2, dianping_pb2_grpc
from service.recommand import logical_regression_predict


class DianPing(dianping_pb2_grpc.DianPingServicer):
    def Recommend(self, request, context):
        print("Grpc server get {Recommend} request.")
        user_id = request.user_id
        result_id = logical_regression_predict.model_predict(user_id)
        return dianping_pb2.RecommendReply(shop_ids=result_id)


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor())
    dianping_pb2_grpc.add_DianPingServicer_to_server(DianPing(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Grpc server start in port: 50051")
    server.wait_for_termination()
