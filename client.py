import grpc
from proto import dianping_pb2_grpc, dianping_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = dianping_pb2_grpc.DianPingStub(channel)

req = dianping_pb2.RecommendRequest(user_id=1)


res: dianping_pb2.RecommendReply = stub.Recommend(req)

print(res.shop_ids)
