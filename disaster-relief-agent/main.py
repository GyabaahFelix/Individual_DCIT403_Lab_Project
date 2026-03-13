import asyncio

from coordinator_agent import CoordinatorAgent
from resource_agent import ResourceAgent
from medical_agent import MedicalAgent
from environment_simulation import DisasterEnvironment


async def main():

    # Create Coordinator Agent
    coordinator = CoordinatorAgent(
        "coordinator_dc403@xmpp.jp",
        "password123",
        verify_security=False
    )

    # Create Resource Agent
    resource = ResourceAgent(
        "resource_dc403@xmpp.jp",
        "password123",
        verify_security=False
    )

    # Create Medical Agent
    medical = MedicalAgent(
        "medical_dc403@xmpp.jp",
        "password123",
        verify_security=False
    )

    # Start agents
    await coordinator.start(auto_register=True)
    print("Coordinator Agent started")

    await resource.start(auto_register=True)
    print("Resource Agent started")

    await medical.start(auto_register=True)
    print("Medical Agent started")

    print("\nAll agents started successfully\n")

    # Create disaster environment simulation
    environment = DisasterEnvironment(coordinator)

    # Run environment simulation in background
    asyncio.create_task(environment.run_environment())

    # Keep system running
    try:
        while True:
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping agents...")

        await coordinator.stop()
        await resource.stop()
        await medical.stop()

        print("Agents stopped successfully")


if __name__ == "__main__":
    asyncio.run(main())