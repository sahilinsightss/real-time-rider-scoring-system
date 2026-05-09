# real-time-rider-scoring-system
AI-assisted rider behavior scoring and safety analytics system using Python and SQL.


## Overview
This project was developed during the Eureka 3.0 Hackathon under Team QuantEdge.

The system is designed to monitor rider behavior in real time using sensor-based inputs such as GPS, IMU, and proximity sensors. A Python-based scoring engine analyzes ride events and generates a rider safety score to classify riders into safe, moderate risk, or unsafe categories.

---

## Problem Statement
Traditional monitoring systems mainly focus on speed tracking and fail to capture overall riding behavior. This project aims to provide a multi-parameter rider behavior scoring system for improved road safety and analytics.

---

## Technologies Used
- Python
- SQL
- Data Analytics
- Sensor-Based Event Detection
- Power BI (planned for dashboard visualization)

---

## Key Features
- Real-time rider behavior analysis
- Rider safety score generation
- Overspeeding detection
- Harsh braking and acceleration analysis
- Proximity-based safety alerts
- SQL ride history logging
- Route risk identification

---

## Scoring Formula

The rider starts with an initial score of 100. Penalty points are deducted for unsafe riding events.

```
S = 100 − (5B + 4A + 6O + 3T + 2P)
```

Where:
- B = harsh braking events
- A = sudden acceleration events
- O = overspeed events
- T = unsafe turns
- P = proximity alerts

---

## System Workflow
1. Sensor Data Collection  
2. Real-Time Data Processing  
3. SQL Data Logging  
4. Python-Based Risk Analysis  
5. Visualization & Alerts  

---

## Sample Output
- Rider Score = 73
- Risk Level = Moderate Risk
- Left LED Alert = Red
- Right LED Alert = Green

---

## Business Applications
- Insurance risk assessment
- Fleet safety monitoring
- Rider training analytics
- Smart mobility systems
- Data-driven rider safety solutions

---

## Project Highlights
- Built a Python-based rider scoring prototype
- Structured ride history logging using SQL
- Designed a scalable analytics workflow
- Developed a real-time risk classification approach

---

## Future Improvements
- Live Power BI dashboard integration
- IoT sensor deployment
- Machine learning-based risk prediction
- Mobile application support
