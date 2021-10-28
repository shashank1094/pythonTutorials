import os

import grpc

from recommendations_pb2 import RecommendationRequest, BookCategory
from recommendations_pb2_grpc import RecommendationsStub

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost:50051")
channel = grpc.insecure_channel(f"{recommendations_host}")
client = RecommendationsStub(channel)
request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=2)
result = client.Recommend(request)
print("Result from the server : ", result.recommendations)
