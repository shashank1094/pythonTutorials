# References

* [GRPC in python](https://realpython.com/python-microservices-grpc/#why-microservices)

```
python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/recommendations.proto
         
> ls 
recommendations_pb2.py          recommendations_pb2_grpc.py

from recommendations_pb2 import BookCategory, RecommendationRequest
>>> BookCategory.SCIENCE_FICTION
```
