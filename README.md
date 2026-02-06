# 📡 Network Collision Simulation (CSMA/CD Model)

A Python-based simulation that models **network device communication** over a shared channel using a simplified **CSMA/CD-like (Carrier Sense Multiple Access with Collision Detection)** mechanism.

---

## 📌 Project Overview

This simulation represents multiple devices attempting to transmit data over a shared communication channel.  
Each device:
- Senses the channel before transmitting
- Attempts transmission based on probability
- Detects collisions
- Applies random backoff strategy
- Retries transmission after waiting

The model demonstrates how collisions occur and how backoff mechanisms reduce repeated collisions.

---

## 🧠 Simulation Logic

1. Devices sense the channel (idle/busy)
2. Idle devices attempt transmission probabilistically
3. Channel checks for multiple transmitters
4. Collisions are detected if more than one device transmits
5. Devices enter backoff state after collision
6. Random backoff timer is applied
7. Devices retry after backoff
8. Successful transmissions are counted

---

## ⚙️ Parameters

```python
num_devices = 5
simulation_time = 20        # seconds
collision_probability = 0.3
time_slot = 1               # seconds
Parameter	Description
num_devices	Number of network devices
simulation_time	Total simulation duration
collision_probability	Probability of transmission attempt
time_slot	Time granularity
🛠️ Technologies Used
Python

Standard Library:

random

📂 Project Structure
network-simulation/
│
├── simulation.py
🧪 States Definition
State	Meaning
0	Idle
1	Transmitting
-1	Backoff (waiting)
📊 Metrics Tracked
✅ Successful transmissions

❌ Collisions

⏳ Backoff retries

📡 Channel state

🖧 Device states

🚀 How to Run
python simulation.py
📈 Output
The program prints:

Time step logs

Device actions

Collision events

Backoff states

Transmission success

Final summary report

Example:

Simulation Summary:
Total Successful Transmissions: X
Total Collisions: Y
🎯 Educational Purpose
This simulation is useful for understanding:

Network contention

Shared medium communication

Collision detection

Backoff algorithms

MAC layer behavior

Distributed systems communication

🔮 Future Enhancements
Visualization using matplotlib

Real-time simulation graphs

Variable backoff algorithms

Adaptive probability control

Token-based channel simulation

Packet queue simulation

Throughput analysis

Delay metrics

👩‍💻 Author
Shereen Alaa
Machine Learning Engineer

GitHub: https://github.com/shreenalaa

LinkedIn: https://www.linkedin.com/in/shreen-alaa/

✨ Educational simulation for understanding network communication and collision management.



