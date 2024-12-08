import random

# Parameters
num_devices = 5
simulation_time = 20  # seconds
collision_probability = 0.3
time_slot = 1  # seconds

# Initialize device states
device_states = [0] * num_devices  # 0 = idle, 1 = transmitting, -1 = waiting
channel_state = 0  # 0 = idle, 1 = busy
successful_transmissions = 0
collisions = 0
device_backoff_times = [0] * num_devices

# Simulation Loop
for t in range(simulation_time):
    print(f"\nTime: {t}")

    # Each device checks the channel state before transmitting
    for i in range(num_devices):
        if device_states[i] == 0:  # Device is idle
            if channel_state == 0:  # Channel is idle
                if random.random() < collision_probability:
                    device_states[i] = 1  # Attempt to transmit
                    print(f"Device {i+1} senses channel idle and attempts to transmit.")
            else:
                print(f"Device {i+1} senses channel busy and waits.")

    # Check for collisions
    transmitting_devices = [i for i in range(num_devices) if device_states[i] == 1]
    if len(transmitting_devices) > 1:
        # Collision detected
        collisions += 1
        print(f"Collision detected between devices: {[i+1 for i in transmitting_devices]}")
        for i in transmitting_devices:
            device_states[i] = -1  # Enter backoff state
            device_backoff_times[i] = random.randint(1, 3)  # Random backoff time
    elif len(transmitting_devices) == 1:
        # Successful transmission
        successful_transmissions += 1
        print(f"Device {transmitting_devices[0]+1} successfully transmitted.")
        device_states[transmitting_devices[0]] = 0  # Return to idle
        channel_state = 1
    else:
        channel_state = 0  # Idle channel

    # Handle backoff
    for i in range(num_devices):
        if device_states[i] == -1:  # In backoff state
            device_backoff_times[i] -= 1
            if device_backoff_times[i] <= 0:
                device_states[i] = 0  # Ready to retry
                print(f"Device {i+1} is ready to retry after backoff.")

# Summary of results
print("\nSimulation Summary:")
print(f"Total Successful Transmissions: {successful_transmissions}")
print(f"Total Collisions: {collisions}")
