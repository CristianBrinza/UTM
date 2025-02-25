import unittest
import grpc
import event_pb2
import event_pb2_grpc

class TestEventService(unittest.TestCase):
    def setUp(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = event_pb2_grpc.EventServiceStub(channel)

    def test_CreateEvent(self):
        response = self.stub.CreateEvent(event_pb2.CreateEventRequest(
            title="Test Event", description="Test Description", date="2021-01-01"))
        self.assertIsNotNone(response.id)

    def test_ListEvents(self):
        response = self.stub.ListEvents(event_pb2.ListEventsRequest())
        self.assertIsInstance(response.events, list)

if __name__ == '__main__':
    unittest.main()
