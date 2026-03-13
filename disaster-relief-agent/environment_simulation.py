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

        food_used = random.randint(10, 20)

        # prevent negative food values
        if self.food >= food_used:
            self.food -= food_used
        else:
            self.food = 0

        if self.food <= 20:
            print("[Environment] Food shortage detected")
            self.coordinator.current_event = "resource_shortage"


    async def simulate_medical_emergency(self):

        emergency_cases = random.randint(1, 3)

        # prevent negative medical kits
        kits_used = min(self.medical_kits, emergency_cases)

        self.medical_kits -= kits_used

        print(f"[Environment] {emergency_cases} medical emergencies reported")


        if self.medical_kits <= 5:
            print("[Environment] Medical supplies running low")

        self.coordinator.current_event = "medical_emergency"


    async def run_environment(self):

        while True:

            event = random.choice([
                self.simulate_victim_arrival,
                self.simulate_resource_shortage,
                self.simulate_medical_emergency
            ])

            await event()

            # ensure no negative values exist
            self.food = max(0, self.food)
            self.shelter = max(0, self.shelter)
            self.medical_kits = max(0, self.medical_kits)

            self.display_dashboard()

            await asyncio.sleep(12)