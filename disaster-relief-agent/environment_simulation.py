import asyncio
import random
import os
from colorama import Fore, Style


class DisasterEnvironment:

    def __init__(self, coordinator_agent):

        self.coordinator = coordinator_agent

        self.victims = 0
        self.food = 100
        self.shelter = 50
        self.medical_kits = 30


    def clear_screen(self):
        os.system("clear")


    def display_dashboard(self):

        self.clear_screen()

        print("====================================")
        print("   REAL-TIME DISASTER RELIEF SYSTEM")
        print("====================================")

        print(f"Victims waiting : {self.victims}")

        if self.food < 20:
            print(Fore.RED + f"Food supplies   : {self.food}" + Style.RESET_ALL)
        else:
            print(f"Food supplies   : {self.food}")

        if self.shelter < 10:
            print(Fore.YELLOW + f"Shelter spaces  : {self.shelter}" + Style.RESET_ALL)
        else:
            print(f"Shelter spaces  : {self.shelter}")

        if self.medical_kits < 5:
            print(Fore.RED + f"Medical kits    : {self.medical_kits}" + Style.RESET_ALL)
        else:
            print(f"Medical kits    : {self.medical_kits}")

        print("====================================\n")


    async def simulate_victim_arrival(self):

        new_victims = random.randint(5, 15)

        self.victims += new_victims

        print(f"[Environment] {new_victims} new victims arrived")

        self.coordinator.current_event = f"victim_arrival:{new_victims}"


    async def simulate_resource_shortage(self):

        food_used = random.randint(10, 20)

        self.food = max(0, self.food - food_used)

        if self.food <= 20:
            print("[Environment] Food shortage detected")
            self.coordinator.current_event = "resource_shortage"


    async def simulate_medical_emergency(self):

        emergency_cases = random.randint(1, 3)

        kits_used = min(self.medical_kits, emergency_cases)

        self.medical_kits -= kits_used

        print(f"[Environment] {emergency_cases} medical emergencies reported")

        self.coordinator.current_event = "medical_emergency"


    async def simulate_resupply(self):

        resupply_type = random.choice(["food", "medical", "shelter"])

        if resupply_type == "food":

            food_added = random.randint(30, 50)
            self.food += food_added

            print(f"[Relief Truck] Food resupply arrived (+{food_added})")

        elif resupply_type == "medical":

            kits_added = random.randint(10, 20)
            self.medical_kits += kits_added

            print(f"[Medical Shipment] Medical kits delivered (+{kits_added})")

        elif resupply_type == "shelter":

            shelter_added = random.randint(10, 20)
            self.shelter += shelter_added

            print(f"[Relief Team] Temporary shelters opened (+{shelter_added})")


    async def process_victims(self):

        # simulate victims receiving help

        if self.victims > 0 and self.food > 0 and self.shelter > 0:

            served = min(self.victims, random.randint(2, 5))

            self.victims -= served
            self.food = max(0, self.food - served)
            self.shelter = max(0, self.shelter - served)

            print(f"[System] {served} victims assisted")


    async def run_environment(self):

        while True:

            event = random.choice([
                self.simulate_victim_arrival,
                self.simulate_resource_shortage,
                self.simulate_medical_emergency,
                self.simulate_resupply
            ])

            await event()

            await self.process_victims()

            self.display_dashboard()

            await asyncio.sleep(8)