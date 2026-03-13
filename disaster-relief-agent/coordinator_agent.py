import asyncio
import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message


class CoordinatorBehaviour(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=10)

        if msg:
            print(f"\n[Coordinator] Received: {msg.body}")

            if "victim_arrival" in msg.body:
                print("[Coordinator] Processing victim arrival")

                request = Message(to="resource_dc403@xmpp.jp")
                request.body = "allocate_resources"

                await self.send(request)

            elif "resource_shortage" in msg.body:
                print("[Coordinator] Requesting additional supplies")

            elif "medical_emergency" in msg.body:
                print("[Coordinator] Requesting medical assistance")

                request = Message(to="medical_dc403@xmpp.jp")
                request.body = "treat_patient"

                await self.send(request)


class CoordinatorAgent(Agent):

    async def setup(self):
        print("Coordinator Agent started")

        behaviour = CoordinatorBehaviour()
        self.add_behaviour(behaviour)