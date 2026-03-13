import asyncio
import random


class DisasterEnvironment:

    def __init__(self, coordinator_agent):

        self.coordinator = coordinator_agent

        # initial environment state
        self.victims = 0
        self.food = 100
        self.shelter = 50
        self.medical_kits = 30


    def display_dashboard(self):

        print("\n==============================")
        print("   DISASTER RELIEF DASHBOARD")
        print("==============================")
        print(f"Victims waiting : {self.victims}")
        print(f"Food supplies   : {self.food}")
        print(f"Shelter spaces  : {self.shelter}")
        print(f"Medical kits    : {self.medical_kits}")
        print("==============================\n")


    async def simulate_victim_arrival(self):

        new_victims = random.randint(5, 15)

        self.victims += new_victims

        print(f"[Environment] {new_victims} new victims arrived")

        self.coordinator.current_event = f"victim_arrival:{new_victims}"


    async def simulate_resource_shortage(self):

        self.food -= random.randint(10, 20)

        if self.food < 20:
            print("[Environment] Food shortage detected")

            self.coordinator.current_event = "resource_shortage"


    async def simulate_medical_emergency(self):

        emergency_cases = random.randint(1, 3)

        print(f"[Environment] {emergency_cases} medical emergencies reported")

        self.coordinator.current_event = "medical_emergency"


    async def run_environment(self):

        while True:

            event = random.choice([
                self.simulate_victim_arrival,
                self.simulate_resource_shortage,
                self.simulate_medical_emergency
            ])

            await event()

            # display dashboard after event
            self.display_dashboard()

            await asyncio.sleep(12)