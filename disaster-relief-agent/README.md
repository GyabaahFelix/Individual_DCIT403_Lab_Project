# Disaster Relief Coordination Agent System

## DCIT 403 – Intelligent Agent Systems  
**Semester Project**

This project implements an **Intelligent Disaster Relief Coordination System** using the **Prometheus Methodology** and the **SPADE Multi-Agent Framework** in Python.

The system simulates how intelligent agents can coordinate disaster response activities such as managing resources, assisting victims, and responding to emergencies.

---

# Project Overview

Natural disasters often create complex and dynamic environments where resources must be distributed efficiently. This project demonstrates how **autonomous agents** can cooperate to manage disaster relief operations.

The system consists of multiple agents that interact with each other and with the environment to coordinate relief efforts.

---

# Agents in the System

The system contains three main agents:

### 1. Relief Coordinator Agent
Responsible for monitoring disaster events and coordinating system responses.

Responsibilities:
- Monitor disaster environment
- Process victim arrival events
- Request resources
- Request medical assistance

---

### 2. Resource Management Agent
Responsible for managing relief supplies.

Responsibilities:
- Allocate food resources
- Manage shelter spaces
- Respond to resource requests

---

### 3. Medical Assistance Agent
Responsible for assisting injured victims.

Responsibilities:
- Respond to medical emergencies
- Provide treatment
- Report medical status

---

# System Environment

The environment simulates a disaster relief center where the following events may occur:

- Victim arrivals
- Resource shortages
- Medical emergencies
- Relief supply deliveries

The environment continuously generates events that trigger agent responses.

---

# System Dashboard

The system includes a **real-time dashboard** that displays the current disaster status:

- Victims waiting
- Food supplies
- Shelter capacity
- Medical kits available

The dashboard updates dynamically as events occur and resources are consumed or replenished.

---

# Technologies Used

- **Python**
- **SPADE (Smart Python Agent Development Environment)**
- **XMPP Messaging Protocol**
- **AsyncIO**
- **Colorama (for dashboard visualization)**

---

# Project Structure
