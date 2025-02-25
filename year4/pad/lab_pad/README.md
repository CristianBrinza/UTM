  # Real-Time Collaborative Event Planning Platform

  This platform enables multiple users to collaborate in real-time to plan and manage events efficiently. With features like shared calendars, task assignments, and live updates, it ensures seamless communication and coordination between all participants. The platform leverages WebSockets for instant collaboration and allows each service (such as user management, event scheduling, and task management) to operate independently, ensuring scalability and smooth user experiences even under heavy loads.



## Table of Contents

- [Overview](#overview)


  ## Overview
  ### Why Microservices?

  Microservices architecture is an ideal choice for real-time, collaborative applications where multiple users need to interact simultaneously while different aspects of the application can be independently scaled. In the case of a real-time collaborative event planning platform, the following advantages make microservices a suitable approach:

  1.	Componentization of Event Planning and User Management:
    -	Event creation, updates, task assignment, and user communication can be broken down into individual services. This leads to easier maintenance and development, as each service can be developed, updated, and scaled independently.
  2.	Scalability:
    -	Real-time collaboration requires managing a large number of simultaneous users. By using microservices, components like event handling, user authentication, and notifications can scale independently based on demand. This ensures better resource allocation and system responsiveness.
  3.	High Availability:
    -	In a distributed system, failures in one service do not necessarily bring down the entire application. If the EventService experiences issues, the UserService and NotificationService will continue to function, ensuring continuous service availability.
  4.	Real-Time Communication:
    -	The use of WebSockets or other real-time communication methods is essential for real-time updates in event planning. By isolating the real-time communication (e.g., via the EventService), the rest of the system (e.g., notifications or document storage) can operate asynchronously, leading to a responsive user experience.

### Service Boundaries

1. **Event and Task Management Service (Multiple Instances)**
   - Handles event creation, updates, task assignments, and real-time collaboration.
   - Manages WebSocket connections for instant updates.
   - Utilizes Redis Queue for task distribution and load balancing.

2. **User, Notification, and Calendar Service**
   - Manages user authentication, profiles, and permissions.
   - Handles notifications via email, push notifications, or in-app alerts.
   - Integrates with third-party calendar APIs for syncing events.

3. **API Gateway**
   - Acts as the entry point for all clients.
   - Routes requests to the appropriate services.
   - Manages WebSocket connections and ensures proper authentication and authorization.


  ```mermaid
flowchart TD
  subgraph Event_and_Task_Management_Service_Replicas
    E1["Event & Task Management Service"]
    E2["Event & Task Management Service"]
    E3["Event & Task Management Service"]
  end

  subgraph User_Notification_Calendar_Service
    U["User, Notification & Calendar Service"]
  end

  A["User"] -- REST, WebSocket --> E1 & E2 & E3
  A -- REST --> B["API Gateway"]
  
  %% Added new path from API Gateway to Event & Task Management Service
  B -- REST --> E1 & E2 & E3
  
  B -- gRPC --> U
  E1 & E2 & E3 -- publish/subscribe --> C[("Redis Queue")]
  E1 & E2 & E3 -- read/write --> D[("Event & Task DB")]
  U -- read/write --> F[("User DB")]
  B -- gRPC --> G["Service Discovery"]
  C -- message --> E1 & E2 & E3
  B:::gateway
  E1:::service
  E2:::service
  E3:::service
  U:::service
  C:::queue
  D:::database
  F:::database
  G:::service

  classDef service stroke:#333,stroke-width:2px
  classDef database stroke:#333,stroke-width:2px
  classDef gateway stroke:#333,stroke-width:4px
  classDef queue stroke:#333,stroke-width:2px

  ```

  ## Technology Stack and Communication Patterns

  1.	Event Service:
    -	Language: Node.js
    -	Framework: Express.js
    -	Communication: WebSocket for real-time updates.
    -	Description: The Event Service will manage event creation, task management, and updates. WebSocket will enable real-time collaboration between users, ensuring they receive immediate updates when changes occur within an event.
  2.	User Service:
    -	Language: Python
    -	Framework: Flask
    -	Communication: RESTful API for synchronous communication with the API Gateway.
    -	Description: The User Service will handle user authentication, registration, and profile management. Flask will serve a REST API that the API Gateway will call for all user-related requests, ensuring modular and isolated handling of user-specific functionalities.
  3.	Notification Service:
    -	Language: Node.js
    -	Framework: Express.js
    -	Communication: Uses a message queue (e.g., RabbitMQ) for asynchronous communication.
    -	Description: The Notification Service will handle the dispatch of notifications asynchronously using a message queue system like RabbitMQ. This ensures that even when the Event Service is under heavy load, notifications such as emails, SMS, or in-app notifications are still processed and delivered.
  4.	API Gateway:
    -	Language: Python
    -	Framework: Flask
    -	Communication: RESTful API and WebSocket handling, routing requests to respective services.
    -	Description: The API Gateway, built with Flask, will handle incoming client requests and route them to the appropriate microservice (EventService, UserService, NotificationService). It will also manage WebSocket connections for real-time event updates, ensuring all communication is properly authenticated and routed.


  - Node.js: Used for both the Event Service and Notification Service due to its non-blocking I/O and suitability for real-time, high-concurrency scenarios (WebSockets, message queues).
  -	Python: Used for the User Service and API Gateway to handle synchronous API requests and the routing of communication between services.
  -	Message Queue (RabbitMQ): Maintains asynchronous communication between services (particularly useful for handling notifications).

  ## Data Management

  1.	Event Service:
    -	Manages events and tasks in a MongoDB database.
    -	Data example: Event details, task lists, real-time updates in JSON format.
  2.	User Service:
    -	Manages user data and permissions in a PostgreSQL database.
    -	Data example: User profiles, permissions, and authentication details in JSON format.
  3.	Notification Service:
    -	Uses Redis for caching notification status and a MySQL database for long-term storage of notification logs.
    -	Data example: Notification logs, status tracking.


  Data is exchanged between microservices using REST APIs in JSON format. Each service manages its own database, ensuring modularity and scalability.

  -  Event Service: Manages event creation, updating, and task assignments.
  - User Service: Manages user authentication, registration, and user data.
  - Notification Service: Handles sending notifications for upcoming events or important changes.

  Each microservice is containerized using Docker, and services communicate with each other through the API Gateway.


  ## Services and Endpoints

  ### Event Service

  1.	POST /events/create
  Create a new event.
  - Input:
      
  ```
      {

  "event_name": "Project Kickoff",
  "date": "2024-10-10",
  "participants": ["user123", "user456"]
}

  ```

  - Output:

  ```
  {
    "event_id": "event789",
    "status": "created"
  }
  ```
  2.	POST /events/update
  Update an existing event.
  -	Input:

  ```
  {
    "event_id": "event789",
    "new_date": "2024-11-11"
  }
  ```

  -	Output:
  ```
  {
    "event_id": "event789",
    "status": "updated"
  }
  ```
  
  3.	GET /events/list
  Retrieve the list of events.
  -	Output:

  ```
  [
  {
    "event_id": "event123",
    "event_name": "Team Meeting",
    "date": "2024-09-15"
  },
  {
    "event_id": "event789",
    "event_name": "Project Kickoff",
    "date": "2024-11-11"
  }
]

```

### WebSocket Collaboration

- WebSocket Endpoint: /ws/events/event_id
- Users can subscribe to event changes in real-time.
- Client Message Example:
```
{
  "type": "subscribe",
  "payload": {
    "event_id": "event789"
  }
}
```


Server Update Example:
```
Copy code
{
  "type": "update",
  "payload": {
    "event_id": "event789",
    "new_data": {
      "status": "completed"
    },
    "timestamp": 1234567890
  }
}
```

### User, Notification & Calendar Service
POST /user/register

- Register a new user.
- Input:
```
{
  "username": "newuser",
  "password": "securepassword"
}
```

- Output:

```
{
  "user_id": "user789",
  "status": "registered"
}
POST /user/login

```

Log in an existing user.

- Input:
```
{
  "username": "newuser",
  "password": "securepassword"
}
```

- Output:

```
{
  "token": "jwt-token"
}

```

POST /notifications/send

Send a notification to users.
- Input:

```
{
  "user_id": "user123",
  "message": "Event Reminder: Project Kickoff tomorrow."
}
```
- Output:

```
{
  "status": "sent",
  "notification_id": "notif789"
}
```

### Calendar Integration (via API Gateway)

- The calendar sync service interacts with third-party calendar APIs through the API Gateway.
- It allows users to sync their events across multiple platforms.
- Service Discovery Integration
- The Event & Task Management Service and User, Notification & Calendar Service register and deregister with the Service Discovery system (e.g., Consul) for dynamic routing.
- Example Service Discovery information:

```
{
  "service": "Event & Task Management Service",
  "address": "10.0.0.1",
  "port": 8080,
  "status": "active"
}
```

### API Gateway Role
- The API Gateway is responsible for handling external requests to services like the User, Notification & Calendar Service.
- It interacts with the Service Discovery system to locate and communicate with active service instances.
- Example API Gateway Interaction:

When a request like GET /events/list comes in, the API Gateway queries the Service Discovery system to fetch the active address of the Event & Task Management Service before routing the request.

```
{
  "service": "Event & Task Management Service",
  "address": "10.0.0.1",
  "port": 8080,
  "status": "active"
}
```

### Summary of Key Endpoints

- Event & Task Management Service
  - POST /events/create
  - POST /events/update
  - GET /events/list
- WebSocket: /ws/events
  - User, Notification & Calendar Service
  - POST /user/register
  - POST /user/login
  - POST /notifications/send
- API Gateway
  - Handles user, notification, and calendar services via REST and gRPC.

### Service Discovery integration:

  - Each service (Event Service, User Service, Notification Service) needs to register and deregister with the Service Discovery tool.
  - 	Example API Gateway interaction:
  - 	When the API Gateway receives a request, such as a request for the event list from the Event Service (GET /events/list), it queries the Service Discovery system to get the current active address of the Event Service before routing the request.
  Example:
  ```
  {
    "service": "Event Service",
    "address": "10.0.0.1",
    "port": 8080,
    "status": "active"
  }
  ```
  The API Gateway uses this information to make a request to the appropriate instance of the Event Service.
  ### Notification Service

  1.	POST /notifications/send
  Send a notification to users.
  -	Input:

  ```
  {
    "user_id": "user123",
    "message": "Event Reminder: Project Kickoff tomorrow."
  }
  ```

  -	Output:
  ```
  {
    "status": "sent",
    "notification_id": "notif789"
  }
  ```


  ### WebSocket Collaboration

  For real-time updates, a WebSocket-based communication system allows users to subscribe to changes in the events they are collaborating on.

  -	WebSocket Endpoint: /ws/events
  -	Client Message Example:


  ```
  {
    "type": "subscribe",
    "payload": {
      "event_id": "event789"
    }
  }
  ```

  - 	Server Update Example:

  ```
  {
    "type": "update",
    "payload": {
      "event_id": "event789",
      "new_data": {
        "status": "completed"
      },
      "timestamp": 1234567890
    }
  }
  ```
  ## Deployment and Scaling

  The platform uses Docker to containerize each microservice, ensuring portability and consistent deployment across environments. The services are managed via Docker Compose, enabling both vertical and horizontal scaling.

  1.	Containerization: Each service is containerized using Docker to ensure consistency across different environments. Each service in the platform is containerized using Docker to ensure consistent deployment across different environments, enabling the application to run smoothly in diverse infrastructure settings.
  2.	Orchestration: Docker is used to orchestrate and manage the deployment, scaling, and monitoring of the services. The platform leverages Docker to orchestrate these containers, managing the deployment, scaling, and monitoring of services. Docker ensures that containers are dynamically allocated based on resource demand, improving resource utilization and availability.
  3.	Scaling: The EventService is expected to be the most heavily used, so it is set up with horizontal scaling using Docker. Each service can scale independently, with EventService replicas dynamically adjusting based on WebSocket connections.


  Each service has its own Dockerfile. For example, for the Event Service:

  ```Dokerfile
  # Event Service Dockerfile
  FROM node:14
  WORKDIR /app
  COPY . .
  RUN npm install
  CMD ["npm", "start"]
  ```

  Example Docker Compose

  ```
  version: '3.8'
  services:
    event-service:
      build: ./event-service
      ports:
        - "3001:3001"
    user-service:
      build: ./user-service
      ports:
        - "3002:3002"
    notification-service:
      build: ./notification-service
      ports:
        - "3003:3003"
    redis:
      image: "redis:alpine"
  ```
  ## Additional Features

  1.	Lobby Mechanism (WebSocket):
    -	The EventService provides a lobby mechanic where users can join an event planning session in real time, collaborating on tasks, updates, and changes through WebSockets.

- Implemented within the Event & Task Management Service. <br>
- Allows users to join a lobby for collaborative planning sessions.<br>
- Manages user presence and real-time updates within the lobby.<br>
2.	API Consumption:
    -	The Notification Service consumes a third-party API, such as Twilio, to send SMS notifications to users for critical updates (in addition to in-app notifications).
- Utilizes Consul for dynamic service discovery.<br>
- Ensures that services can locate each other without hardcoded endpoints.<br>
- Facilitates load balancing and fault tolerance.

3.	Service Discovery:
-	A service discovery mechanism is implemented using Consul to allow services to discover each other dynamically and facilitate load balancing.

4. Redis Queue
- Used for distributing tasks among multiple instances of the Event & Task Management Service.<br>
- Enhances scalability by balancing the workload.<br>
- Ensures that tasks are processed efficiently even under heavy load.<br>
    

    
  -  Scalability: By integrating Service Discovery, each microservice can now scale independently without requiring manual intervention in the API Gateway.

  - Fault Tolerance: If a service goes down, the Service Discovery will automatically update the status, and the API Gateway will stop routing requests to that instance.





  ## Architecture Diagram

  1.	User Service:
    -	Handles authentication, user management, and user roles.
  2.	Event Service:
    -	Manages event creation, scheduling, task updates, and real-time communication.
  3.	Notification Service:
    -	Sends notifications to users through various channels asynchronously.
  4.	API Gateway:
    - 	Acts as the front-facing entry point, handling client requests, routing, and WebSocket connections.



## Scaling Strategy:
- Event Service: This service experiences high demand due to real-time collaboration. Horizontal scaling is implemented to ensure that additional instances can be spun up as the number of WebSocket connections increases.
- 	User Service: This service handles user authentication and profiles. It will scale based on login and registration requests, ensuring quick responses during peak usage times (e.g., event start times).
- 	Notification Service: Scales based on queue length for asynchronous tasks, such as sending notifications. Worker nodes can be added or removed dynamically based on the message queue load.
- 	API Gateway: Doker ensures the API Gateway can scale horizontally to handle increasing client requests. As the entry point for all REST and WebSocket communications, it ensures balanced load distribution across services.



### Fault Tolerance: 
1.	Service Restarts:
Docker Compose allows you to automatically restart services in case of failures by using the restart policy. This ensures that if a service fails, Docker will restart it automatically.
2.	Health Checks:
Docker Compose supports health checks that continuously monitor the health of a service. If a service becomes unhealthy, it can be restarted or trigger some other action.
3.	Service Discovery:
Consul for service discovery in Docker Compose to ensure that only healthy service instances are used. This allows services to discover each other dynamically and avoid routing requests to failed or unhealthy services.

```
version: '3.8'

services:
  api-gateway:
    image: api-gateway:latest
    restart: always
    depends_on:
      - event-task-service
      - user-notification-service
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    ports:
      - "3000:3000"

  event-task-service:
    image: event-task-service:latest
    restart: always
    depends_on:
      - redis
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3001/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    ports:
      - "3001:3001"

  user-notification-service:
    image: user-notification-service:latest
    restart: always
    depends_on:
      - postgres
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3002/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    ports:
      - "3002:3002"

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    restart: always

  postgres:
    image: postgres:latest
    environment:
      POSTGRES_PASSWORD: yourpassword
    ports:
      - "5432:5432"
    restart: always

  consul:
    image: consul
    command: agent -dev -client=0.0.0.0
    ports:
      - "8500:8500"  # Consul UI
      - "8600:8600"  # DNS
    restart: always

networks:
  default:
    driver: bridge

```

### Service Discovery and Worker Distribution: 
1.	Service Discovery with Consul:
	-	Consul will be used for service discovery, allowing services to register themselves and discover each other dynamically. This ensures that only healthy services are used for communication, similar to how Doker handles service discovery.
2.	Worker Distribution:
	-	Docker Compose allows you to scale services by running multiple instances of a service (such as the Notification Service workers) using the docker-compose up --scale command.
	-	Workers can be distributed across multiple instances, and as the task queue grows, more worker instances can be manually scaled up to handle the increased load.

Example Docker Compose for Service Discovery and Worker Distribution:

```
version: '3.8'

services:
  api-gateway:
    image: api-gateway:latest
    restart: always
    depends_on:
      - event-task-service
      - notification-worker
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    environment:
      - CONSUL_HTTP_ADDR=consul:8500
    command: ["register-service", "api-gateway"]
    ports:
      - "3000:3000"

  event-task-service:
    image: event-task-service:latest
    restart: always
    depends_on:
      - redis
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3001/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    environment:
      - CONSUL_HTTP_ADDR=consul:8500
    command: ["register-service", "event-task-service"]
    ports:
      - "3001:3001"

  notification-worker:
    image: notification-worker:latest
    restart: always
    depends_on:
      - redis
    environment:
      - CONSUL_HTTP_ADDR=consul:8500
    command: ["register-service", "notification-worker"]
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3002/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    ports:
      - "3002:3002"

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    restart: always

  consul:
    image: consul
    command: agent -dev -client=0.0.0.0
    ports:
      - "8500:8500"  # Consul UI
      - "8600:8600"  # DNS
    restart: always

networks:
  default:
    driver: bridge
```

  ## Conclusion

  By leveraging microservices for the real-time collaborative event planning platform, the architecture remains scalable, modular, and fault-tolerant. It ensures smooth real-time updates, independent service scaling, and a high degree of reliability.




  ## Service Repositories

- [Event Service](https://github.com/username/event-service)
- [User Service](https://github.com/username/user-service)
- [Notification Service](https://github.com/username/notification-service)
- [API Gateway](https://github.com/username/api-gateway)
- [Task Management Service](https://github.com/username/task-management-service)
- [Service Discovery](https://github.com/username/service-discovery)

---

## Research Resources

- [Building Collaborative Applications with WebSockets](https://dev.to/someone/building-collaborative-applications-with-websockets)
- [Best Practices for Microservices in Real-Time Applications](https://real-time-microservices.dev.io/)
 - [Scaling Services with Docker Compose](https://docs.docker.com/compose/compose-file/compose-file-v3/#scale)
- [The Role of Service Discovery in Microservice Architectures](https://blog.service-discovery-in-microservices.com)
- [Using Redis for Caching in High-Traffic Applications](https://redis.io/topics/caching)
 - [Deploying Microservices Using Docker and Docker Compose](https://medium.com/@user/deploying-microservices-using-docker-and-Docker)
