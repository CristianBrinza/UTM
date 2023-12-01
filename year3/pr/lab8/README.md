
## Implementation of RAFT Algorithm

The RAFT algorithm is employed for determining the Leader among the services. The process is as follows:

1. **Initialization**: All services attempt to connect using UDP and bind to the connection;

2. **Leader Election**: Only one service succeeds in this step, becoming the Leader. The others automatically become Followers;

3. **Role Acknowledgment**: Followers send an 'Accept' message to the Leader, acknowledging its role;

4. **Exchange of Credentials**:

   - The Leader sends its HTTP credentials (IP, port, token for writes) to the Followers;

   - Followers, upon receiving this information, send back their HTTP credentials to the Leader;

5. **Credential Storage**: The Leader stores the Followers' credentials for future communication.

6. **HTTP Server Activation**: The HTTP server starts up, enabling communication between the Leader and Followers.



- **Followers**: Post-election, they handle only read requests from external sources;

- **Leader**: Manages all types of requests. For write operations, it forwards these requests to the Followers using the stored credentials.
