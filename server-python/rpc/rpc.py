import redis
import grpc
from concurrent import futures

from predictions_pb2 import (
    PredictionResponse,
    Prediction
)

from predictions_pb2_grpc import (
    PredictionsServicer,
    add_PredictionsServicer_to_server
)

r = redis.Redis(
    host='localhost',
    port=6379)


class PredictionService(PredictionsServicer):

    def GetPredictions(self, request, context):
        
        key = f"predictions:{request.id_client}"
        predictions = r.hgetall(key)

        predictions = [Prediction(class_name=k.decode("utf-8"),
                                  value=float(v))
                       for k, v
                       in predictions.items()]

        return PredictionResponse(predictions=predictions)

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PredictionsServicer_to_server(
        PredictionService(),
        server
    )

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
