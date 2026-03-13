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

The system contains three main agents.

## 1. Relief Coordinator Agent

Responsible for monitoring disaster events and coordinating system responses.

Responsibilities:

* Monitor disaster environment
* Process victim arrival events
* Request resource allocation
* Request medical assistance

---

## 2. Resource Management Agent

Responsible for managing relief supplies.

Responsibilities:

* Allocate food resources
* Manage shelter spaces
* Respond to resource allocation requests

---

## 3. Medical Assistance Agent

Responsible for assisting injured victims.

Responsibilities:

* Respond to medical emergencies
* Provide treatment
* Report medical status

---

# System Environment

The environment simulates a disaster relief center where the following events may occur:

* Victim arrivals
* Resource shortages
* Medical emergencies
* Relief supply deliveries

The environment continuously generates events that trigger agent responses.

---

# System Dashboard

The system includes a **real-time dashboard** that displays the current disaster status.

The dashboard shows:

* Number of victims waiting
* Available food supplies
* Shelter capacity
* Medical kits available

The dashboard updates dynamically as events occur and resources are consumed or replenished.

---

# Technologies Used

This project uses the following technologies:

* Python
* SPADE (Smart Python Agent Development Environment)
* XMPP Messaging Protocol
* AsyncIO
* Colorama (for dashboard visualization)

---

# Project Structure

```
disaster-relief-agent
│
├── coordinator_agent.py
├── resource_agent.py
├── medical_agent.py
├── environment_simulation.py
├── main.py
├── README.md
└── .gitignore
```

---

# Installation

Clone the repository:

```
git clone https://github.com/GyabaahFelix/Individual_DCIT403_Lab_Project.git
```

Navigate to the project directory:

```
cd Individual_DCIT403_Lab_Project/disaster-relief-agent
```

Create a virtual environment:

```
python -m venv venv
```

Activate the virtual environment.

Linux / Mac:

```
source venv/bin/activate
```

Install dependencies:

```
pip install spade
pip install colorama
```

---

# XMPP Server Setup

This system uses a public XMPP server.

Create the following accounts at:

https://xmpp.jp/signup

```
coordinator_dc403@xmpp.jp
resource_dc403@xmpp.jp
medical_dc403@xmpp.jp
```

Use the **same password for all agents**.

---

# Running the System

Run the system using:

```
python main.py
```

The system will start all agents and begin the disaster environment simulation.

Example output:

```
REAL-TIME DISASTER RELIEF SYSTEM

Victims waiting : 15
Food supplies : 80
Shelter spaces : 45
Medical kits : 20
```

---

# Agent Behaviour

The system follows the **Perceive – Decide – Act** model.

### Perceive

Agents receive events from the disaster environment.

### Decide

The Coordinator Agent determines appropriate actions.

### Act

Resource and Medical Agents perform the required operations.

---

# Prometheus Methodology

The system design follows the **Prometheus Agent-Oriented Methodology**.

### Phase 1 – System Specification

* Problem description
* Goal specification
* Functionalities
* Scenarios
* Environment description

### Phase 2 – Architectural Design

* Agent types
* Functionality grouping
* Acquaintance diagram
* Agent descriptors

### Phase 3 – Interaction Design

* Interaction diagrams
* Message sequences

### Phase 4 – Detailed Design

* Capabilities
* Plans
* Data structures
* Percepts and actions

### Phase 5 – Implementation

* Multi-agent system built using SPADE

---

# Example Simulation Events

```
[Environment] 10 new victims arrived
[Coordinator] Processing victim arrival
[Resource Agent] Allocating food and shelter
```

```
[Environment] Medical emergency detected
[Coordinator] Requesting medical assistance
[Medical Agent] Treating injured victims
```

---

# Challenges Encountered

Some challenges faced during development include:

* Configuring XMPP communication for agents
* Designing agent coordination logic
* Preventing negative resource values during simulation
* Handling asynchronous event-driven simulation

---

# Future Improvements

Possible improvements to the system include:

* Integration with real-time disaster data
* Graphical dashboard interface
* Predictive resource allocation using machine learning
* Additional logistics and transportation agents

---

# Author

Felix Gyabaah
University of Ghana
DCIT 403 – Intelligent Agent Systems
