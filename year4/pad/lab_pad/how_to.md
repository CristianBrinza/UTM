## Set Up the Environment
### First time Docker lunch
```
docker-compose up --build
```
### Restart the Docker
```
docker-compose down
docker-compose up --build
```
### Open terminal in VS code
```
toggle terminal
```
### Check port
```
lsof -i :5000
```
```
kill -9 <PID>
```

Communicatetion between 2 Services/APIs (Python and Node.js):
```
curl -X POST http://localhost:5000/events/create -H "Content-Type: application/json" -d '{"title": "Meeting", "description": "Team sync", "date": "2024-10-26"}'

```
## Check+Confirm if all services are running

```
docker ps
```

## Status Endpoint (Simple Endpoint for All Services)

Each service (Event Service, User Service, Gateway, and Service Discovery) has a /status endpoint to check if they are running.

Testing:
For Event Service, run:
```
curl http://localhost:50051/status
```
For User Service, run:
```
curl http://localhost:50052/status
```
For Gateway, run:
```
curl http://localhost:5000/status
```
For Service Discovery, run:
```
curl http://localhost:8000/status
```



---


---

### Service Discovery
```
curl -X GET "http://localhost:8000/register?name=event_service&address=localhost:50051"
```
```
curl -X GET "http://localhost:8000/register?name=user_service&address=localhost:50052"
```
```
curl -X GET "http://localhost:8000/get?name=event_service"
```
```
curl -X GET "http://localhost:8000/get?name=user_service"
```

### Event Service
```
curl -X POST http://localhost:50051/events/create -H "Content-Type: application/json" -d '{"title": "Team Sync", "description": "Weekly Team Sync", "date": "2024-10-30"}'
```
```
curl -X GET http://localhost:50051/events/list
```
```
curl -X GET http://localhost:50051/status
```

###
User Service
```
curl -X POST http://localhost:50052/sendNotification -H "Content-Type: application/json" -d '{"user_id": "1", "message": "Event Created"}'
```
```
curl -X GET http://localhost:50052/status
```




---
Service Discovery
```
curl -X GET "http://localhost:8000/register?name=event_service&address=localhost:50051"
curl -X GET "http://localhost:8000/register?name=user_service&address=localhost:50052"
curl -X GET "http://localhost:8000/get?name=event_service"
curl -X GET "http://localhost:8000/get?name=user_service"
```
Event Service
```
curl -X POST http://localhost:50051/events/create -H "Content-Type: application/json" -d '{"title": "Team Sync", "description": "Weekly Team Sync", "date": "2024-10-30"}'
curl -X GET http://localhost:50051/events/list
curl -X GET http://localhost:50051/status
```
User Service
```
curl -X POST http://localhost:50052/sendNotification -H "Content-Type: application/json" -d '{"user_id": "1", "message": "Event Created"}'
curl -X GET http://localhost:50052/status
```



---
### websockets:
```
# Create an event
curl -X POST http://localhost:50051/events/create -H "Content-Type: application/json" -d '{"title": "Team Sync", "description": "Weekly Team Sync", "date": "2024-10-30"}'

# Send a notification
curl -X POST http://localhost:50052/sendNotification -H "Content-Type: application/json" -d '{"user_id": "1", "message": "Event Created"}'
```

<br/><br/><br/><br/><br/><br/>
cbreack:
```
curl -X POST http://localhost:5000/events/create -H "Content-Type: application/json" -d '{"title": "Test Event", "description": "This is a test event", "date": "2024-10-30"}'
```


```
curl -X POST http://localhost:5000/events/create -H "Content-Type: application/json" -d '{"title": "Test Event", "description": "This is a test event", "date": "2024-10-30"}'
echo ""

curl -X POST http://localhost:5000/events/create -H "Content-Type: application/json" -d '{"title": "Test Event", "description": "This is a test event", "date": "2024-10-30"}'
echo ""

curl -X POST http://localhost:5000/events/create -H "Content-Type: application/json" -d '{"title": "Test Event", "description": "This is a test event", "date": "2024-10-30"}'
```
