FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN pip install flask grpcio-tools
RUN python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/event.proto
RUN python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/user.proto
EXPOSE 50051
CMD ["python", "app.py"]
