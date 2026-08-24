## Requirements Table

### Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| **FR-001** | Functional | The system shall match an outgoing courier request with the nearest active delivery rider within a **3 km radius**. | High | **Pass:** Rider receives a dispatch notification with the pickup location. **Fail:** Order is assigned to an offline rider. | Ensures courier requests are assigned quickly to a suitable nearby rider. |
| **FR-002** | Functional | The system shall optimize the delivery route when a rider has multiple pickup or delivery stops. | High | **Pass:** The system generates an optimized sequence of stops. **Fail:** Stops are assigned without route optimization. | Reduces unnecessary travel and improves delivery efficiency. |
| **FR-003** | Functional | The system shall provide the sender with the delivery rider's live GPS location and current delivery status during an active delivery. | High | **Pass:** Sender can view the rider's current location and delivery status. **Fail:** Tracking information is unavailable or significantly outdated. | Provides real-time visibility of the courier. |
| **FR-004** | Functional | The system shall verify the recipient using an OTP before marking the parcel as delivered. | High | **Pass:** Valid OTP allows delivery completion. **Fail:** Invalid OTP prevents the parcel from being marked as delivered. | Ensures that the parcel is delivered to the intended recipient. |
| **FR-005** | Functional | The system shall notify the sender when important delivery events occur, including rider assignment, parcel pickup, and delivery completion. | Medium | **Pass:** Sender receives the corresponding status notification. **Fail:** A delivery status changes without notifying the sender. | Keeps the sender informed throughout the delivery process. |

### Non-Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| **NFR-001** | Performance & Security | Delivery status and live GPS telemetry from riders shall be transmitted to the sender client with **under 2-second latency**. | High | **Pass:** Benchmarking tests confirm the target latency and security standards under simulated peak load. **Fail:** The target latency or security standards are not met. | Low-latency updates are essential for effective live delivery tracking. |
| **NFR-002** | Security | The system shall protect courier tracking, delivery status, and OTP-related information from unauthorized access during transmission and access. | High | **Pass:** Unauthorized users cannot access protected delivery or tracking information. **Fail:** Protected delivery information can be accessed without authorization. | Courier location and delivery information must remain secure. |


