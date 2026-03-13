import spade
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message


class MedicalBehaviour(CyclicBehaviour):

    async def run(self):

        msg = await self.receive(timeout=10)

        if msg:
            print(f"\n[Medical Agent] Request received: {msg.body}")

            if msg.body == "treat_patient":

                # simulate treatment
                treated_patients = 2
                kits_used = 2

                print("[Medical Agent] Providing medical treatment")
                print(f"[Medical Agent] Patients treated: {treated_patients}")
                print(f"[Medical Agent] Medical kits used: {kits_used}")

                reply = Message(to="coordinator_dc403@xmpp.jp")
                reply.body = f"medical_status:treated={treated_patients}"

                await self.send(reply)

                print("[Medical Agent] Treatment report sent")

            elif msg.body == "medical_supply_low":

                print("[Medical Agent] Medical supplies running low")

                reply = Message(to="coordinator_dc403@xmpp.jp")
                reply.body = "medical_status:supply_low"

                await self.send(reply)


class MedicalAgent(Agent):

    async def setup(self):

        print("Medical Agent started")

        behaviour = MedicalBehaviour()
        self.add_behaviour(behaviour)