# IoT Monitoring Microservice

## Project Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd IoTMonitoringMicroservice
   ```

2. **Build the project**
   ```bash
   mvn clean install
   ```

3. **Run the application**
   ```bash
   mvn spring-boot:run
   ```

## Environment Variables
- `DATABASE_URL`: URL for the database connection.

## Configuring Alert Rules
- Define alert rules in the database for device monitoring.

## Data Ingestion Methods
- Supports HTTP and MQTT for data ingestion.

## Performance Optimization
- Implemented asynchronous data processing to improve data ingestion throughput.
- Batch processing is used for incoming data to reduce overhead and achieve sub-second latency for data retrieval.
- Caching mechanisms (e.g., Redis) are utilized to store frequently accessed data, reducing database load.

## Horizontal Scaling Strategy
- The microservice is designed to be stateless, facilitating easy scaling across multiple instances.
- Container orchestration tools like Kubernetes are recommended for managing scaling and load balancing.
- A service discovery mechanism is implemented to allow instances to communicate effectively, ensuring health monitoring APIs can check device statuses.