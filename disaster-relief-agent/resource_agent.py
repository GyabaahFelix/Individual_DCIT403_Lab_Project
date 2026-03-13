import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message


class ResourceBehaviour(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=10)

        if msg:
            print(f"\n[Resource Agent] Request received: {msg.body}")

            if msg.body == "allocate_resources":

                # simulate allocation of resources
                allocated_food = 10
                allocated_shelter = 5

                print("[Resource Agent] Allocating resources...")
                print(f"[Resource Agent] Food distributed: {allocated_food}")
                print(f"[Resource Agent] Shelter spaces assigned: {allocated_shelter}")

                reply = Message(to="coordinator_dc403@xmpp.jp")
                reply.body = f"resource_status:food={allocated_food},shelter={allocated_shelter}"

                await self.send(reply)

                print("[Resource Agent] Resource allocation report sent")

            elif msg.body == "resource_shortage":

                print("[Resource Agent] Resource shortage detected")
                print("[Resource Agent] Requesting additional supplies")

                reply = Message(to="coordinator_dc403@xmpp.jp")
                reply.body = "resource_status:shortage_detected"

                await self.send(reply)


class ResourceAgent(Agent):

    async def setup(self):

        print("Resource Agent started")

        behaviour = ResourceBehaviour()
        self.add_behaviour(behaviour)