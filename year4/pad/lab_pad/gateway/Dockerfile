FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/event.proto
RUN python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/user.proto
EXPOSE 5000
CMD ["python", "app.py"]
