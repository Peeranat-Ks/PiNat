# IT483 Senior Project Defense Document

**Project:** AI-Powered Indoor Surveillance Robot  
**Student:** Peeranat K.  
**Institution:** Asia-Pacific International University  
**Faculty:** Faculty of Information Technology  
**Academic Year:** 2025–2026, Semester 2  
**Date:** May 7, 2026

---

## Executive Summary

This defense document presents a comprehensive overview of the AI-Powered Indoor Surveillance Robot project, designed to enhance security monitoring in the university's main hall during restricted hours (after 10:00 PM). The system combines Raspberry Pi 4 hardware with AI-driven capabilities in a layered subsumption architecture to provide autonomous patrol, real-time human detection, and automated alert generation. This document covers feasibility analysis, development environment, risks, planning, user requirements, and system design elements required for IT483 senior project defense.

---

## 1. Self and Project Introduction

**Student Name:** Peeranat K.  
**Program:** Bachelor of Science, Faculty of Information Technology  
**Specialization:** Robotics and Artificial Intelligence  
**Project Title:** AI-Powered Indoor Surveillance Robot  

**One-Sentence Pitch:** An autonomous, cost-effective AI surveillance robot that patrols a university main hall after 10:00 PM, detects unauthorized human presence, and immediately alerts security personnel via Telegram with photographic evidence.

**Project Relevance:** This project directly applies computer vision, robotics control systems, and machine learning—core competencies of the Information Technology faculty—to solve a real-world campus security challenge.

---

## 2. Company Profile and Organizational Context

### 2.1 Organization: Asia-Pacific International University (AIU)

| Field | Details |
|---|---|
| **Official Name** | Asia-Pacific International University |
| **Address** | 195 Moo 3, Muak Lek, Saraburi 18180, Thailand |
| **Line of Business** | Higher Education Institution |
| **Telephone** | (+66) 036 720 777 |
| **Email** | info@apiu.edu |
| **Founded** | 1998 |

### 2.2 Primary Stakeholders

1. **Campus Security Department**
   - **Contact:** Security Director, sweerakoon@apiu.edu
   - **Role:** Primary end-user; responsible for nighttime monitoring and incident response
   - **Need:** Enhanced security coverage and faster detection of unauthorized access

2. **Faculty of Information Technology**
   - **Contact:** Dean, deanit@apiu.edu
   - **Role:** Academic supervisor and institutional support
   - **Need:** Student capstone project supporting faculty research goals

### 2.3 Organizational Chart (Project-Relevant Units)

```
Asia-Pacific International University
│
├─ Office of the President
│
├─ VP for Academic Administration
│  └─ Faculty of Information Technology ← [Academic Supervision]
│
└─ VP for Financial Administration & Development
   └─ General Manager
      └─ Campus Security Department ← [Primary Stakeholder / End-User]
```

### 2.4 Mission Alignment

**AIU's Six Core Missions:**

1. Produce graduates with virtuous character and practical skills
2. **Active research and innovation in each academic faculty** ← Aligned
3. Academic service and humanitarian programs
4. Preservation of arts and culture
5. **Administrative system meeting international quality standards** ← Aligned
6. Financial stability and environmental friendliness

**Alignment:** This project directly supports **Mission 2** by demonstrating applied research in AI and robotics for campus infrastructure, and **Mission 5** by enhancing operational efficiency through automation and technology integration.

---

## 3. Problem Description and Security Gap

### 3.1 Current Situation

The university's main hall is a high-traffic multi-purpose space serving students, staff, and visitors during operational hours. Access restrictions are implemented after 10:00 PM to maintain security and building integrity.

**Current Monitoring Approach:**
- Manual security patrol by personnel (typically 1-2 guards per shift)
- Periodic walkthroughs at irregular intervals
- Reactive incident response after unauthorized access is discovered
- No continuous automated monitoring system

### 3.2 Identified Problems

| Problem | Impact |
|---|---|
| **Inconsistent Coverage** | Manual patrols cannot simultaneously cover all areas; security gaps exist during shift changes or personnel absences. |
| **Limited Visibility** | Single guard covers multiple blind spots and cannot be in two locations simultaneously. |
| **Detection Latency** | Unauthorized presence may go undetected for extended periods until next patrol. |
| **Human Fatigue** | Night-shift security staff experience fatigue, reducing alertness and response effectiveness. |
| **Reactive Response** | Incidents are discovered after occurrence rather than detected in real-time. |
| **Limited Evidence** | No systematic capture of incident documentation or security event records. |

### 3.3 Security Requirements

- Continuous monitoring of the main hall during restricted hours (after 10:00 PM)
- Real-time detection of unauthorized human presence after 10:00 PM
- Immediate notification to security personnel via Telegram
- Documented evidence collection (timestamped images)
- Non-intrusive monitoring (no facial identification or biometric profiling)

---

## 4. Proposed Solution and Stakeholder Importance

### 4.1 Solution Overview

The AI-Powered Indoor Surveillance Robot provides **continuous autonomous patrol** combined with **real-time AI-driven human detection** and **automated alerting**. The robot operates using a **layered subsumption architecture** that separates:

- **Lower layers:** Reactive local control (obstacle avoidance, basic navigation)
- **Higher layers:** AI-driven intelligence (human detection, zone recognition, boundary enforcement)

This architecture ensures the robot can function reliably even if AI processing is delayed, while leveraging advanced machine learning when available.

### 4.2 How It Addresses the Problem

| Problem | Solution |
|---|---|
| Inconsistent coverage | Autonomous patrol after 10:00 PM with predefined routes |
| Limited visibility | Continuous video monitoring with field-of-view advantages in central patrol path |
| Detection latency | Real-time frame processing with < 200 ms latency |
| Human fatigue | Eliminates fatigue factor through automation |
| Reactive response | Proactive detection triggers immediate Telegram alert (≤ 30 seconds) |
| Limited evidence | Automatic image capture and timestamp logging of all events |

### 4.3 Importance for Stakeholders

**For Campus Security Department:**
- Faster incident response through automated Telegram alerts with photographic evidence
- Reduced workload during low-activity periods with targeted response capability
- Enhanced detection coverage during off-peak hours
- Systematic incident documentation for investigation and reporting

**For University Administration:**
- Demonstrates technology innovation and commitment to modern security practices
- Cost-effective augmentation of security operations without increasing personnel headcount
- Potential model for expanding automation to other campus areas
- Research and development capability within the institution

**For Faculty of Information Technology:**
- Practical application of AI, robotics, and computer vision technologies
- Real-world system development experience for student learning outcomes
- Potential for future research and student projects

---

## 5. Project Objectives

### 5.1 General Objective

**To design, develop, and deploy an AI-powered autonomous indoor surveillance robot using Raspberry Pi 4 and AI technologies that can patrol a university main hall, detect human presence, and provide security alerts during restricted hours (after 10:00 PM).**

### 5.2 Specific Objectives (Measurable and Defendable)

| # | Objective | Success Criterion |
|---|---|---|
| 1 | Build the robot platform | 4WD mobile platform functional with Raspberry Pi 4 controller and ultrasonic obstacle avoidance |
| 2 | Implement real-time human detection | ≥ 85% detection accuracy at distances up to 3 m in normal indoor lighting |
| 3 | Develop zone recognition model | ≥ 80% classification accuracy identifying location within main hall |
| 4 | Implement virtual boundary detection | Successfully recognizes and avoids exiting designated patrol zone |
| 5 | Develop automated Telegram alert system | Sends alert with image and timestamp within ≤ 30 seconds of human detection after 10:00 PM |
| 6 | Implement layered subsumption architecture | Separation of reactive control (lower layers) from AI decision-making (higher layers) verified through behavioral testing |
| 7 | Integrate AI decision support | High-level decision layer integrated (OpenRouter API when available, rule-based fallback otherwise) and validated on contextual test scenarios |
| 8 | Evaluate system performance | Document detection accuracy, patrol coverage, response time, and operational reliability |

### 5.3 Measurable Targets

- **Human detection accuracy:** ≥ 85% (benchmark: industry standard for embedded AI)
- **Zone recognition accuracy:** ≥ 80% (classification threshold)
- **Full patrol cycle time:** ≤ 15 minutes for main hall coverage
- **Telegram alert latency:** ≤ 30 seconds from detection to delivery
- **Obstacle detection range:** 2 cm to 400 cm (HC-SR04 specification)
- **Frame processing latency:** ≤ 200 ms per frame for 5+ FPS real-time processing
- **Continuous operation duration:** ≥ 2 hours on single battery charge
- **Patrol speed:** ~0.3 m/s (safe indoor navigation velocity)

### 5.4 Measurement Methodology (For Defense and Acceptance Test)

To ensure all objectives are measurable and defendable, the following methods will be used.

#### 5.4.1 Human Detection Accuracy (Target: >= 85% at up to 3 m)

- **Test setup:** Mark distances at 1 m, 2 m, and 3 m in normal indoor lighting.
- **Dataset:** For each distance, collect positive samples (person present) and negative samples (no person) across multiple angles and poses.
- **Confusion matrix terms:**
   - `TP`: Person present and detected
   - `FN`: Person present but not detected
   - `FP`: No person but detected
   - `TN`: No person and not detected
- **Primary formula:**

$$
Accuracy = \frac{TP + TN}{TP + TN + FP + FN} \times 100\%
$$

- **Support metrics (recommended):**

$$
Precision = \frac{TP}{TP + FP} \times 100\%, \quad
Recall = \frac{TP}{TP + FN} \times 100\%
$$

- **Note on camera zoom lens:** Distances beyond 3 m (for example 5-9 m) are reported as extended performance results and do not replace the official 3 m objective threshold.

#### 5.4.2 Zone Recognition Accuracy (Target: >= 80%)

- **Test setup:** Divide the main hall into labeled zones (for example Zone A, B, C, D, E).
- **Dataset:** Collect labeled images or feature samples for each zone under realistic patrol conditions.
- **Evaluation:** Compare predicted zone against ground-truth zone labels.
- **Formula:**

$$
Zone\ Accuracy = \frac{Correct\ Predictions}{Total\ Predictions} \times 100\%
$$

- **Evidence:** Include a confusion matrix to show per-zone strengths and weaknesses.

#### 5.4.3 Telegram Alert Latency (Target: <= 30 s)

- Record `t_detected` at first valid human detection event.
- Record `t_sent` when Telegram API confirms message/photo delivery request.
- Formula:

$$
Alert\ Latency = t_{sent} - t_{detected}
$$

- Report minimum, average, and maximum latency across trials.

#### 5.4.4 Frame Processing Latency and FPS (Target: <= 200 ms/frame and >= 5 FPS)

- Record `t_start` before per-frame AI inference and `t_end` after inference output is available.
- Per-frame latency:

$$
Latency_{frame} = t_{end} - t_{start}
$$

- Frame rate:

$$
FPS = \frac{1}{Average\ Latency_{frame}}
$$

- Report average and 95th percentile latency to show real-time stability.

#### 5.4.5 Continuous Operation Duration (Target: >= 2 h)

- If battery is available: measure uninterrupted runtime from full charge to minimum safe voltage cutoff.
- If battery is not yet available: report as pending hardware validation and include adapter-powered endurance logs as interim evidence.

---

## 6. Related Works and Comparative Analysis

### 6.1 Existing Solutions Review

#### 6.1.1 Knightscope K5 Autonomous Security Robot

**Description:** Commercial autonomous security robot deployed in malls, parking lots, and corporate environments.

**Strengths:**
- Advanced autonomous navigation with GPS
- Multi-sensor integration (cameras, thermal, LiDAR)
- Real-time anomaly detection and alerting
- Established track record

**Weaknesses:**
- Designed for outdoor/semi-outdoor environments
- Commercial cost ($60,000+) prohibitive for academic use
- Requires dedicated infrastructure
- Proprietary system with limited customization

**Relevance:** Demonstrates commercial viability but not applicable to student-budget projects.

#### 6.1.2 Cobalt Robotics Indoor Security Robot

**Description:** Commercially available indoor security robot with human-in-the-loop monitoring for office buildings.

**Strengths:**
- Indoor-specific design
- Cloud-based monitoring dashboard
- Two-way communication capability
- Established enterprise customer base

**Weaknesses:**
- High commercial cost ($30,000+ annually with service fees)
- Dependency on cloud services and ongoing support contracts
- Designed for corporate rather than educational settings
- Limited customization for specific institutional needs

**Relevance:** Illustrates market demand but highlights cost barrier for institutional implementation.

#### 6.1.3 Academic AI-Based Human Detection Systems

**Description:** Open-source projects utilizing YOLO, SSD, or Faster R-CNN for real-time human detection on embedded systems.

**Strengths:**
- Free and open-source
- Proven effectiveness on Raspberry Pi
- Extensive documentation and community support
- Applicable to mobile robotics

**Weaknesses:**
- Primarily stationary camera setups
- Limited autonomous navigation capabilities
- Lack of integrated zone recognition or boundary enforcement
- Minimal alert integration

**Relevance:** Demonstrates technical feasibility but shows gap in mobile integration.

#### 6.1.4 Raspberry Pi-Based Surveillance Systems

**Description:** Various hobbyist and academic projects combining Pi camera with motion detection and Telegram alerts.

**Strengths:**
- Low-cost implementation
- Accessible to students
- Good documentation available
- Suitable for prototype development

**Weaknesses:**
- Stationary deployment only
- No autonomous navigation
- Limited AI integration
- Typically single-location monitoring

**Relevance:** Shows foundation of available components but highlights innovation opportunity in mobile integration.

#### 6.1.5 Subsumption Architecture in Robotics

**Description:** Brooks' reactive architecture organizing behavior into layers where higher layers suppress lower-layer outputs.

**Strengths:**
- Proven robustness in dynamic environments
- Allows reactive fallback if AI processing delayed
- Suitable for embedded systems
- Clear separation of concerns

**Weaknesses:**
- Requires careful layer design
- Testing complexity increases with layers
- May seem less efficient than unified planning

**Relevance:** Provides architectural foundation ensuring system reliability even with AI processing limitations on Raspberry Pi.

### 6.2 Comparative Advantages

| Feature | K5 | Cobalt | AI Projects | Pi Surveillance | **Proposed** |
|---|---|---|---|---|---|
| **Cost-effective** | ✗ | ✗ | ✓ | ✓ | **✓** |
| **Indoor-focused** | ✗ | ✓ | ✓ | ✓ | **✓** |
| **Mobile patrol** | ✓ | ✓ | ✗ | ✗ | **✓** |
| **Human detection** | ✓ | ✓ | ✓ | ✓ | **✓** |
| **Zone recognition** | ✗ | ✗ | ✗ | ✗ | **✓** |
| **Virtual boundary** | ✗ | ✗ | ✗ | ✗ | **✓** |
| **Automated alerts** | ✓ | ✓ | ✗ | ✓ | **✓** |
| **AI decision support** | Proprietary | Proprietary | Limited | ✗ | **✓** |
| **Subsumption architecture** | ✗ | ✗ | ✗ | ✗ | **✓** |
| **Educational/customizable** | ✗ | ✗ | ✓ | ✓ | **✓** |
| **Student-budget implementation** | ✗ | ✗ | ✓ | ✓ | **✓** |

### 6.3 Innovation Gap Addressed

**Gap Identified:** No existing cost-effective solution combines mobile autonomous patrol, AI-based zone recognition, virtual boundary enforcement, automated alerting, and subsumption architecture specifically designed for institutional indoor security.

**Proposed Contribution:** A student-implementable, university-focused security automation system that demonstrates practical integration of AI, robotics, and embedded systems within realistic budgetary and skill constraints.

---

## 7. Expected Business Benefits

### 7.1 Security Enhancements

**Continuous Coverage:** The autonomous patrol eliminates gaps in nighttime monitoring by providing patrol coverage after 10:00 PM through designated patrol routes, complementing security personnel.

**Proactive Detection:** AI-powered human detection identifies unauthorized presence in real-time rather than waiting for periodic manual discovery, enabling faster response.

**Objective Evidence Collection:** Timestamped images automatically captured during detection incidents provide documented evidence for investigation and incident reconstruction.

### 7.2 Operational Benefits

**Improved Incident Response:** Automated Telegram alerts reduce response latency from minutes (next scheduled patrol) to seconds (immediate notification), enabling security personnel to respond while incident is occurring.

**Consistent Monitoring:** Robot maintains consistent patrol patterns and detection performance without fatigue, weather, or distraction factors affecting human guards.

**Reduced Personnel Burden:** Automation of routine nighttime monitoring allows security staff to focus on incident response and investigation rather than exhaustive patrols.

**Scalability Path:** Successful implementation provides model for extending similar systems to other campus areas (parking, dormitories, other buildings).

### 7.3 Strategic Benefits

**Technology Innovation Demonstration:** Showcases university's commitment to technology-driven solutions and practical AI application, enhancing institutional reputation.

**Research and Development Platform:** System provides foundation for future student projects, faculty research, and technology partnerships.

**Cost Efficiency:** Low-cost automated solution with current out-of-pocket spending not over $150 demonstrates significant operational savings compared to commercial alternatives ($30,000-$60,000+).

**Digital Transformation:** Contributes to university's broader technology modernization initiative and positions IT department as innovation leader.

### 7.4 Stakeholder Value

| Stakeholder | Benefit |
|---|---|
| **Campus Security** | Faster alerts, better coverage, evidence documentation, reduced workload during low-activity periods |
| **University Administration** | Cost-effective security enhancement, technology leadership positioning, potential revenue from similar deployments |
| **Faculty of IT** | Capstone project demonstrating student competency, research platform potential, industry-relevant training |
| **Student (Developer)** | Comprehensive project portfolio piece, skills in robotics/AI/systems integration, potential publication opportunity |

---

## 8. Feasibility Study Summary

### 8.1 Technical Feasibility

**Assessment:** ✓ **FEASIBLE**

**Supporting Factors:**
- Raspberry Pi 4 has proven capability for embedded AI with TensorFlow Lite and OpenCV
- Pre-trained human detection models (MobileNet SSD, YOLO) are optimized for Pi deployment
- HC-SR04 ultrasonic sensor is well-documented with proven obstacle detection accuracy
- 4WD motor systems are commonly used in Raspberry Pi robotics projects
- Telegram Bot API integration is straightforward and well-supported

**Mitigating Risks:**
- Limited computational resources → Use lightweight models (MobileNet, TensorFlow Lite with quantization)
- Model inference latency → Target 5-15 FPS processing rate adequate for stationary subjects
- Camera resolution/lighting → Use Pi Camera V2 (8MP) with configurable resolution and gain

**Conclusion:** Standard components and proven open-source libraries support technical implementation within Raspberry Pi 4 constraints.

### 8.2 Operational Feasibility

**Assessment:** ✓ **FEASIBLE**

**Supporting Factors:**
- System designed to augment (not replace) existing security personnel
- Robot operates within controlled indoor environment with predictable lighting
- Patrol routes are predefined and testable
- Alert delivery via Telegram is reliable on campus WiFi network

**Mitigating Factors:**
- WiFi dependency → Implement local logging with delayed alert retry
- Battery life → Design for 2+ hours operation; use external power during testing
- Maintenance → Regular checks and simple modular design for easy repairs

**Conclusion:** System fits within existing operational framework and can be supported by current facilities with minimal infrastructure addition.

### 8.3 Legal and Ethical Feasibility

**Assessment:** ✓ **FEASIBLE WITH SAFEGUARDS**

**Legal Considerations:**
- Thailand's Personal Data Protection Act (PDPA) — System complies by:
  - Not performing facial recognition or personal identification
  - Storing only detection event images (not person database)
  - Retaining only necessary images for security review (14-30 day retention policy)

**Ethical Considerations:**
- Privacy concerns addressed through:
  - Detection-only approach (human presence, not identification)
  - only person who have that chatbot on telegram will be able to get notification
  - Transparent documentation of monitoring areas and hours
  - No biometric data collection or profiling

**Institutional Compliance:**
- Requires approval from university administration and security department
- Coordinates with existing security protocols and incident response procedures
- Should be documented in campus security policies

**Conclusion:** Ethically defensible approach to security enhancement with appropriate safeguards for privacy and legal compliance.

### 8.4 Schedule Feasibility

**Assessment:** ✓ **FEASIBLE**

**Official Timeline:**
- IT483 Deliverables Due: **December 1, 2026** (Week 15)
- Proposal Defense: **Currently ongoing** (May 2026)
- Remaining IT483 Development Time: **7 Months** (as of May 7, 2026)

**Project Phases:**
1. **Weeks 1-4:** Hardware assembly and motor control testing
2. **Weeks 5-8:** Camera integration and data collection
3. **Weeks 9-12:** Model training and initial system integration
4. **Weeks 13-14:** System testing and refinement
5. **Week 15:** Report finalization and IT483 submission
6. **IT484 (if continued):** Full deployment and extended testing

**Feasibility Assessment:**
- MVP (Minimum Viable Product) with basic human detection and alerting: **Achievable by week 15**
- Full feature set with zone recognition and advanced features: **Requires IT484 continuation**
- Defense timeline: **Currently on track**

**Conclusion:** Feasible with clear phasing between IT483 MVP and IT484 extended development.

### 8.5 Financial Feasibility

**Assessment:** ✓ **FEASIBLE**

**Budget Analysis:**

| Item | Cost | Status |
|---|---|---|
| Raspberry Pi 4 (1GB RAM) | ฿2,000 | ✓ Sourced |
| Pi Camera Module V2 | ฿1,000 | ✓ Available |
| HC-SR04 Ultrasonic Sensor (×4) | ฿200 | ✓ Available |
| 4WD Mobile Chassis + Motors | ฿800 | ✓ Available |
   | Motor Driver (L298N) | ฿150 | ✓ In stock |
   | Bench Power Supply / 12V Battery Pack (future) | ฿240 | ✓ Available |
   | SD Card (32GB Class 10) | ฿70 | ✓ In stock |
   | **TOTAL HARDWARE** | **~฿4,460** | ✓ Within budget |
   | **CURRENT SPENDING** | **Not over $150** | ✓ Student prototype budget |
   | **Variance** | Out-of-pocket spending stays low because many components are already available in the lab |

**Cost Management Strategy:**
- Utilize existing lab equipment and components from university IT infrastructure
- Leverage open-source software (zero licensing cost)
- Use pre-trained models (no training data purchase required)
- Campus WiFi (existing infrastructure)

**Conclusion:** Financially feasible through combination of student budget and institutional resource access. Software entirely open-source (TensorFlow Lite, OpenCV, Python, scikit-learn).

### 8.6 Resource and Skill Feasibility

**Assessment:** ✓ **FEASIBLE WITH MENTORING**

**Available Resources:**
- Faculty of IT lab access with electronics equipment
- Advisor support and guidance (assigned faculty mentor)
- Institutional repository (GitHub)
- Campus WiFi network
- Main hall access for testing and data collection
- github copilot

**Student Skills (Peeranat K.):**
- Python programming experience (foundational to advanced)
- Basic electronics and sensor integration
- Robotics project experience 

**Skill Development Required:**
- Subsumption architecture implementation
- Embedded systems debugging on Raspberry Pi
- Full software systems integration

**Support Available:**
- Faculty advisor for architecture and design guidance
- Online communities (Raspberry Pi forums, GitHub discussions)
- Extensive tutorial documentation for all required libraries
- IT483/484 instructor feedback and milestones

**Conclusion:** Student possesses foundational skills; identified gaps can be closed through mentoring and independent research supported by extensive community resources.

---

## 9. Development Environment

### 9.1 Hardware Architecture

#### 9.1.1 Primary Components

| Component | Specification | Function |
|---|---|---|
| **Raspberry Pi 4** | 1GB RAM, BCM2711 Cortex-A72 processor @ 1.5 GHz | Main controller and AI processing unit |
| **Pi Camera Module V2** | 8MP, 3280×2464 resolution, 77° field of view | Real-time video capture for detection |
| **HC-SR04 Ultrasonic Sensor** | Range: 2 cm to 400 cm, ±3 mm accuracy | Obstacle detection (×4 sensors for 360° coverage) |
| **4WD Mobile Chassis** | Aluminum frame, four 100 RPM DC motors, ~20 cm wheelbase | Autonomous navigation platform |
| **L298N Motor Driver** | 2A per channel, 5-35V input | Motor control and PWM speed regulation |
| **Bench Power Supply** | 12V regulated output for motors; 5V step-down for Raspberry Pi during testing | Current test power source |
| **SD Card** | 32GB Class 10, microSD format | OS and software storage |

### 9.2 Software Environment

#### 9.2.1 Operating System and Runtime

| Layer | Technology | Purpose |
|---|---|---|
| **OS** | Raspberry Pi OS (Bookworm, Debian-based Linux) | Lightweight, optimized for Pi 4 |
| **Python Runtime** | Python 3.11+ | Primary development language |
| **Virtual Environment** | venv | Dependency isolation and reproducibility |

#### 9.2.2 Core Libraries and Frameworks

| Library | Version | Purpose |
|---|---|---|
| **TensorFlow Lite** | 2.11+, quantized models | Lightweight AI inference on Pi |
| **OpenCV** | 4.8+ | Real-time image processing and frame capture |
| **scikit-learn** | 1.2+ | Machine learning model training (zone recognition) |
| **Pillow (PIL)** | 10.0+ | Image manipulation and JPEG encoding |
| **RPi.GPIO** | 0.7.0+ | GPIO control for motors and sensors |
| **Telegram Bot API** | Telegram platform API | Telegram alert delivery |
| **PyYAML** | 6.0+ | Configuration file management |
| **requests** | 2.31+ | WiFi connectivity testing and HTTP operations |

#### 9.2.3 Development Tools

| Tool | Purpose |
|---|---|
| **Git / GitHub** | Version control and institutional repository |
| **VS Code / PyCharm** | Code editing and debugging |
| **pytest** | Unit testing framework |
| **logging (Python stdlib)** | System activity and error logging |
| **GPIO PIN mapping utilities** | Sensor/motor pin configuration |

#### 9.2.4 Pre-trained Models

| Model | Source | Purpose | File Size |
|---|---|---|---|
| **MobileNet SSD v2** | TensorFlow Hub | Human detection (quantized for Pi) | ~3-4 MB |
| **Custom Zone Recognition** | Trained locally via scikit-learn + OpenCV | Location classification inside hall | ~1-2 MB |
| **OpenRouter API** | OpenRouter | High-level decision support via cloud model access | N/A (cloud API) |

### 9.3 Development Process and Methodology

#### 9.3.1 Development Approach

**Iterative Prototyping:** 
- Short development cycles (1-2 week sprints)
- Incremental feature addition and testing
- Regular integration testing

**Incremental Integration:**
1. **Phase 1:** Motor control and navigation
2. **Phase 2:** Camera integration and frame capture
3. **Phase 3:** Human detection model integration
4. **Phase 4:** Zone recognition and virtual boundary
5. **Phase 5:** Alert system integration
6. **Phase 6:** Subsumption architecture layers

**Agile Testing:**
- Unit tests for individual components (sensor reading, motor control, model inference)
- Integration tests for layer interactions
- System tests in simulated and actual environments

#### 9.3.2 Repository Structure

```
20252026s2-Peeranat-Ks/
├── README.md
├── rpi.py
├── SDP.code-workspace
├── doc/
│   ├── SDP_Proposal_Draft.md
│   ├── IT483_Defense_Preparation.md
│   ├── IT483_Defense_Document.md
│   └── ...other documentation
├── src/
│   ├── __init__.py
│   ├── config.yaml
│   ├── main.py
│   ├── control/
│   │   ├── motor_control.py
│   │   └── navigation.py
│   ├── sensors/
│   │   ├── camera.py
│   │   └── ultrasonic.py
│   ├── ai/
│   │   ├── human_detection.py
│   │   ├── zone_recognition.py
│   │   └── boundary_detection.py
│   ├── alerts/
│   │   └── telegram_alert.py
│   ├── architecture/
│   │   ├── subsumption_layers.py
│   │   └── layer_controller.py
│   └── utils/
│       ├── logging_config.py
│       └── helpers.py
├── tests/
│   ├── test_motor_control.py
│   ├── test_detection.py
│   └── test_integration.py
├── models/
│   ├── mobilenet_ssd_v2.tflite
│   ├── zone_recognition_model.pkl
│   └── openrouter_config.json (if included)
├── logs/
│   └── .gitkeep
└── data/
    ├── training_data/
    │   ├── zone_1_images/
    │   ├── zone_2_images/
    │   └── zone_3_images/
    └── alerts/
        └── captured_images/
```

#### 9.3.3 Deployment Environment

**Target Deployment:**
- Raspberry Pi 4 running Raspberry Pi OS (Bookworm)
- Operated in IT building 1st floor after 10:00 PM
- WiFi connected to university network (AIU-WiFi)

**Testing Environment:**
- Lab mock-up of main hall (smaller scale)
- Controlled lighting and obstacle setup
- Safe perimeter for movement testing

---

## 10. Risks and Mitigation Strategies

### 10.1 Technical Risks

#### Risk 1: AI Model Inference Performance

**Risk Description:** TensorFlow Lite model inference on Raspberry Pi 4 may exceed target latency (200 ms/frame), resulting in detection lag and missed events.

**Likelihood:** Medium  
**Impact:** High

**Mitigation Strategies:**
1. **Model Optimization:**
   - Use quantized (INT8) versions of MobileNet SSD for faster inference
   - Reduce input image resolution (320×240 instead of 640×480) for faster processing
   - Test inference latency early in development cycle

2. **Performance Tuning:**
   - Enable Raspberry Pi GPU acceleration (OpenGL ES)
   - Use multi-threading: capture frame in one thread, process in another
   - Implement frame skipping if necessary (detect every 2nd frame)

3. **Contingency:**
   - Fallback to lower-resolution detection if latency exceeds threshold
   - If critical performance gap, use OpenRouter API decision support only and disable the AI layer locally

**Success Criteria:** Achieve ≥ 5 FPS (200 ms/frame) at 320×240 resolution with 85%+ detection accuracy.

---

#### Risk 2: Poor Detection Accuracy in Variable Lighting

**Risk Description:** Human detection accuracy may degrade below 85% threshold in low-light conditions or with varying indoor lighting in the main hall.

**Likelihood:** Medium  
**Impact:** Medium

**Mitigation Strategies:**
1. **Training Approach:**
   - Collect training data in actual main hall at different times and lighting conditions
   - Include low-light scenarios in training set
   - Augment training data with brightness/contrast variations

2. **Runtime Adjustment:**
   - Implement camera gain and exposure control for adaptive lighting
   - Deploy histogram equalization preprocessing if needed
   - Consider IR illumination as future enhancement

3. **Threshold Tuning:**
   - Set detection confidence threshold conservatively (0.6-0.7)
   - Accept false positives over false negatives for security application
   - Implement context filtering (human-sized objects in human-height zones)

**Success Criteria:** Achieve ≥ 85% detection accuracy across various lighting conditions documented in test log.

---

#### Risk 3: WiFi Connectivity Loss

**Risk Description:** Campus WiFi interruption may prevent Telegram alert delivery, creating undetected security events.

**Likelihood:** Medium  
**Impact:** High

**Mitigation Strategies:**
1. **Local Logging:**
   - Store all detection events to local SD card with timestamp
   - Include captured image file references
   - Enable post-incident review and delayed alert retry

2. **Alert Retry Mechanism:**
   - Queue failed alerts in local database
   - Implement exponential backoff retry (1 min, 5 min, 15 min intervals)
   - Attempt re-send when WiFi reconnects

3. **Connectivity Monitoring:**
   - Ping test to campus gateway every 30 seconds
   - Log WiFi disconnection events
   - Alert system administrator of prolonged outages

4. **Alternative Notification (Future):**
   - USB logging for manual review on administrator device
   - Optional SMS gateway integration (if available)

**Success Criteria:** All detection events logged locally; 100% of alerts sent within 30 seconds when WiFi available; zero missed events.

---

#### Risk 4: Future 12V Battery Runtime During Patrol

**Risk Description:** After moving from bench-supply testing to 12V battery operation, the battery may provide insufficient runtime, requiring mid-shift charging and reducing patrol coverage.

**Likelihood:** Medium  
**Impact:** Medium

**Mitigation Strategies:**
1. **Power Management:**
   - Implement sleep mode for idle periods (reduce polling frequency)
   - Disable unnecessary services (Bluetooth, HDMI)
   - Profile power consumption early (expected ~2 W for Pi + 1 W for motors = ~3 W average)

2. **Charging Schedule:**
   - Design patrol rotation after battery deployment: 2 hours active, 1 hour charging if needed
   - Select an appropriate 12V battery pack for final deployment
   - Coordinate with Building Management for charging station setup

3. **Capacity Monitoring:**
   - Implement battery voltage monitoring via ADC after battery integration
   - Define low-voltage cutoff for the 12V battery pack
   - Log battery performance data for optimization

**Success Criteria:** ≥ 2 hours continuous operation per charge after battery deployment; system safely handles low-voltage conditions when needed.

---

### 10.2 Operational Risks

#### Risk 5: Robot Collision and Physical Damage

**Risk Description:** Robot may collide with obstacles, furniture, or people despite ultrasonic sensors, resulting in equipment damage or safety hazard.

**Likelihood:** Medium  
**Impact:** Medium

**Mitigation Strategies:**
1. **Sensor Coverage:**
   - Deploy 4× HC-SR04 sensors (front, back, left, right) for 360° coverage
   - Implement emergency stop if any sensor detects obstacle within 20 cm
   - Test sensor accuracy in actual hall before deployment

2. **Speed Control:**
   - Limit patrol speed to 0.3 m/s (safe indoor velocity)
   - Reduce speed when obstacles detected (graduallyslow down rather than hard stop)
   - Implement manual speed override for testing

3. **Physical Protection:**
   - Design bumper frame to absorb minor impacts
   - Install foam padding on corners and protrusions
   - Test navigation in mock-up environment first

4. **Testing Protocol:**
   - Conduct obstacle avoidance tests in controlled environment
   - Verify sensor accuracy at different distances and angles
   - Gradually increase test complexity before full hall deployment

**Success Criteria:** Zero collisions during 10+ hour testing period; all obstacles detected within specified range.

---

#### Risk 6: False Positive Detections Creating Alert Fatigue

**Risk Description:** High false positive rate (detecting non-human objects as humans) may cause security staff alert fatigue and reduce system credibility.

**Likelihood:** High  
**Impact:** Medium

**Mitigation Strategies:**
1. **Confidence Threshold Tuning:**
   - Set detection confidence threshold to 0.7+ (conservative)
   - Implement multi-frame verification (human must appear in 2+ consecutive frames)
   - Require minimum bounding box size (filter small false positives)

2. **Contextual Filtering:**
   - Zone-based detection rules (humans expected in entry/exit zones, less likely in center)
   - Time-based filtering (stricter after 11 PM when halls should be empty)
   - Size/proportion filtering (reject objects not matching human proportions)

3. **User Feedback Loop:**
   - Include "False Alarm" button in Telegram alert for security staff
   - Collect feedback on alert accuracy
   - Adjust thresholds based on field data

4. **Documentation:**
   - Log all alerts with confidence scores
   - Enable review of captured images for false positive analysis
   - Continuous model improvement based on actual deployment data

**Success Criteria:** < 10% false positive rate after tuning; positive user feedback from security staff.

---

### 10.3 Environmental and External Risks

#### Risk 7: Changes to Hall Configuration

**Risk Description:** Furniture rearrangement or hall modifications may invalidate zone recognition model or navigation routes.

**Likelihood:** Low  
**Impact:** Medium

**Mitigation Strategies:**
1. **Flexible Route Configuration:**
   - Define patrol routes in configuration file (not hardcoded)
   - Enable manual route adjustment without code changes
   - Test alternative routes before deployment

2. **Zone Recognition Robustness:**
   - Use feature-based recognition (structural elements, lighting patterns) rather than furniture
   - Collect training data from multiple angles and times
   - Implement periodic retraining schedule

3. **Maintenance Procedures:**
   - Document process for updating routes when hall layout changes
   - Schedule monthly navigation verification tests
   - Train administrator on route update procedures

**Success Criteria:** Successful adaptation to minor layout changes without model retraining; documented procedures for major changes.

---

#### Risk 8: Regulatory or Institutional Policy Changes

**Risk Description:** University administration may modify security policies or restrict autonomous robot operation during development timeline.

**Likelihood:** Low  
**Impact:** High

**Mitigation Strategies:**
1. **Early Stakeholder Alignment:**
   - Obtain written approval from Campus Security and administration before deployment
   - Document agreed operational parameters and monitoring zones
   - Establish communication channel for policy changes

2. **Documentation and Compliance:**
   - Maintain clear documentation of system capabilities and limitations
   - Ensure compliance with data privacy regulations (PDPA)
   - Implement access controls for alert data and logs

3. **Contingency Planning:**
   - Design system modularly so components can be disabled if needed
   - Prepare alternative deployment scenarios (daytime testing only, restricted zones, etc.)
   - Maintain flexibility in project timeline

**Success Criteria:** Written institutional approval obtained; no project delays due to policy barriers.

---

### 10.4 Risk Summary Matrix

| Risk | Category | Likelihood | Impact | Mitigation Priority |
|---|---|---|---|---|
| Inference performance | Technical | Medium | High | **HIGH** |
| Detection accuracy | Technical | Medium | Medium | **HIGH** |
| WiFi connectivity | Technical | Medium | High | **HIGH** |
| Battery life | Technical | Medium | Medium | **MEDIUM** |
| Collision damage | Operational | Medium | Medium | **MEDIUM** |
| False positives | Operational | High | Medium | **MEDIUM** |
| Hall configuration changes | Environmental | Low | Medium | **MEDIUM** |
| Policy changes | External | Low | High | **MEDIUM** |

---

## 11. Planning and Timeline

### 11.1 Project Phases and Milestones

#### Phase 1: Hardware Assembly and Motor Control (Weeks 1-4)
**Deliverables:**
- ✓ Raspberry Pi 4 OS installation and configuration
- ✓ 4WD chassis assembly and motor testing
- ✓ Motor controller integration and PWM control
- ✓ Ultrasonic sensor calibration and integration
- **Milestone:** Robot can move in straight line and turn on command

#### Phase 2: Camera Integration and Data Collection (Weeks 5-8)
**Deliverables:**
- ✓ Pi Camera Module installation and video stream capture
- ✓ Frame capture at 10+ FPS at 320×240 resolution
- ✓ Real-time video display on development machine
- ✓ Training data collection in main hall (human and non-human images)
- ✓ Zone labeling and image annotation for training set
- **Milestone:** System captures video; training dataset ready (500+ images per zone)

#### Phase 3: AI Model Integration (Weeks 9-12)
**Deliverables:**
- ✓ TensorFlow Lite human detection model integrated and tested
- ✓ Zone recognition model training on collected data
- ✓ Boundary detection model (exit door recognition) training
- ✓ Real-time inference testing on Raspberry Pi 4
- ✓ Performance benchmarking (FPS, accuracy, latency)
- **Milestone:** Human detection working at ≥ 5 FPS with ≥ 85% accuracy

#### Phase 4: Alert System Development (Weeks 10-13)
**Deliverables:**
- ✓ Telegram alert implementation
- ✓ Captured image attachment functionality
- ✓ Timestamp and metadata logging
- ✓ Alert throttling to prevent spam
- ✓ Local logging fallback for WiFi outages
- **Milestone:** Alert system sends Telegram message with image within 30 seconds of detection

#### Phase 5: Subsumption Architecture Implementation (Weeks 11-14)
**Deliverables:**
- ✓ Layer 0: Obstacle avoidance reactive control
- ✓ Layer 1: Autonomous navigation with patrol patterns
- ✓ Layer 2: Virtual boundary enforcement
- ✓ Layer 3: Human detection and alert
- ✓ Layer 4: Zone recognition
- ✓ Layer 5: AI decision support (OpenRouter-based if time permits)
- ✓ Layer interaction and suppression logic
- **Milestone:** Multi-layer system functional with behavioral verification

#### Phase 6: Integration Testing and Documentation (Weeks 13-15)
**Deliverables:**
- ✓ System integration testing in controlled environment
- ✓ Performance evaluation against quantitative targets
- ✓ Code documentation and inline comments
- ✓ Deployment guide and operational manual
- ✓ IT483 final report preparation
- **Milestone:** Complete IT483 deliverables; report and code submitted

### 11.2 IT483 Timeline (Official)

| Week | Milestone | Status |
|---|---|---|
| **Week 1-5** | Proposal development and feedback | ✓ **Completed** (Proposal submitted) |
| **Week 6-14** | Development and integration | **In Progress** (Current week: post-proposal defense) |
| **Week 15** | Final report and presentation submission | **Upcoming** (May 1, 2026 deadline) |

**Current Status:** Post-proposal defense phase; IT483 development window: 3-4 weeks remaining

### 11.3 IT484 Timeline (Tentative, if registered)

| Week | Phase |
|---|---|
| **Weeks 1-4** | Extended testing and optimization |
| **Weeks 5-8** | Full hall deployment and field testing |
| **Weeks 9-12** | Performance monitoring and refinement |
| **Weeks 13-15** | Final evaluation and IT484 submission |

### 11.4 Gantt Chart (ASCII Representation)

```
Project: AI-Powered Indoor Surveillance Robot
Timeline: Weeks 1-15 (IT483) + Weeks 16-33 (IT484, optional)

Phase 1: Hardware Assembly (Weeks 1-4)
████████

Phase 2: Camera Integration (Weeks 5-8)
        ████████

Phase 3: AI Integration (Weeks 9-12)
                ████████

Phase 4: Alert System (Weeks 10-13)
                ██████████

Phase 5: Subsumption Architecture (Weeks 11-14)
                  ████████

Phase 6: Testing & Documentation (Weeks 13-15)
                      ██████

IT483 Submission: Week 15 | **DEADLINE**

IT484 Extended Development (Optional)
                          ████████████████

Milestones:
- Week 4: Motors functional ★
- Week 8: Camera & training data ready ★
- Week 12: AI models integrated ★
- Week 13: Alert system tested ★
- Week 15: IT483 submission ★ **CRITICAL**
```

---

## 12. User Requirements Summary

### 12.1 User Roles and Responsibilities

#### Role 1: Security Personnel

**Profile:**
- Campus security guards and supervisors
- Operate in 2-3 person teams during night shifts
- Experience with Telegram alerts and alert management
- Non-technical background

**Responsibilities:**
- Monitor Telegram alerts from surveillance robot
- Review captured images and incident details
- Respond to detected unauthorized presence
- Manually override robot if needed for safety
- Log incident reports based on robot notifications

**Access Requirements:**
- Receive Telegram alerts with attached images and timestamps
- View stored alert logs and images (read-only)
- No access to system configuration or AI models

#### Role 2: System Administrator

**Profile:**
- Dedicated IT staff member (typically from university IT department)
- Technical background with systems administration experience
- Responsible for system maintenance and configuration

**Responsibilities:**
- Configure restricted operating hours (currently: after 10:00 PM)
- Set Telegram alert recipients and bot parameters
- Monitor robot battery and charging status
- Perform routine maintenance (software updates, log rotation)
- Troubleshoot system issues and failures
- Coordinate with Campus Security on operational changes

**Access Requirements:**
- Full system configuration access
- Ability to modify patrol routes and detection thresholds
- Access to all logs, system status, and diagnostic information
- WiFi and SSH access to Raspberry Pi for remote administration

#### Role 3: Faculty Advisor / Project Supervisor

**Profile:**
- Faculty member from Faculty of Information Technology
- Research and academic mentoring role
- Interim supervisor during development

**Responsibilities:**
- Provide technical guidance and architectural feedback
- Approve major design decisions
- Facilitate institutional approvals and stakeholder coordination
- Evaluate project progress against objectives

**Access Requirements:**
- Read-only access to source code and documentation
- Ability to review system logs and performance data
- Direct communication with student developer

### 12.2 Functional User Requirements

#### Security Personnel Requirements

| Requirement | Description | Priority |
|---|---|---|
| **FR-1: Alert Notification** | Receive Telegram notification within 30 seconds of human detection after 10:00 PM | **HIGH** |
| **FR-2: Alert Content** | Telegram message includes captured image, timestamp, detection confidence, and location zone | **HIGH** |
| **FR-3: Alert Archive** | View historical alerts and corresponding images for incident review | **HIGH** |
| **FR-4: Manual Override** | Ability to manually stop/restart robot via web interface or text command | **MEDIUM** |
| **FR-5: System Status** | Check robot operational status (battery, WiFi, last patrol time) | **MEDIUM** |
| **FR-6: Incident Logging** | Annotate alerts with incident classification (authorized/unauthorized, action taken) | **LOW** |

#### System Administrator Requirements

| Requirement | Description | Priority |
|---|---|---|
| **FR-7: Configuration Management** | Modify restricted hours, detection sensitivity, patrol routes | **HIGH** |
| **FR-8: Telegram Setup** | Configure bot token, alert chat ID list, message format | **HIGH** |
| **FR-9: Model Thresholds** | Adjust detection confidence threshold and false positive filtering | **MEDIUM** |
| **FR-10: Maintenance Mode** | Enable diagnostic mode for hardware testing without AI detection | **MEDIUM** |
| **FR-11: Log Access** | View and export system logs for troubleshooting | **HIGH** |
| **FR-12: Performance Monitoring** | Monitor CPU usage, memory, inference latency on Pi 4 | **MEDIUM** |

### 12.3 Non-Functional User Requirements

| Requirement | Description | Target |
|---|---|---|
| **Performance** | Human detection inference latency | ≤ 200 ms (≥ 5 FPS) |
| **Accuracy** | Human detection true positive rate | ≥ 85% within 3 m |
| **Availability** | System operational during restricted hours | ≥ 98% uptime |
| **Reliability** | Mean time between failures (MTBF) | ≥ 20 hours continuous |
| **Response Time** | Telegram alert delivery latency | ≤ 30 seconds |
| **Usability** | Security personnel training time | ≤ 30 minutes |
| **Maintainability** | Code documentation and comments | ≥ 80% function documentation |
| **Security** | Access control and authentication | Restricted to authorized staff |

---

## 13. Infrastructure Analysis

### 13.1 Current Infrastructure (Available)

#### 13.1.1 Facilities

| Resource | Available | Details |
|---|---|---|
| **Main Hall Space** | ✓ Yes | Monitored surveillance area (~60m × 20m) |
| **WiFi Network** | ✓ Yes | Campus WiFi (AIU-WiFi) with good coverage |
| **Electrical Power** | ✓ Yes | Multiple outlets in main hall; additional outlets in maintenance areas |
| **Charging Station Infrastructure** | ◐ Partial | Outlets available; dedicated charging station not yet established |
| **Laboratory Space** | ✓ Yes | Faculty of IT lab for development, testing, and integration |
| **Server Infrastructure** | ✓ Yes | Campus network access available for Telegram alert delivery |

#### 13.1.2 IT Infrastructure

| Resource | Available | Details |
|---|---|---|
| **GitHub Repository** | ✓ Yes | Institutional repository (Faculty-of-IT organization) |
| **WiFi Access** | ✓ Yes | Static IP address allocation available for Pi if needed |
| **Telegram Service** | ✓ Yes | Telegram bot API access with authentication token |
| **IT Support** | ✓ Yes | Faculty of IT technical support available for hardware/network issues |

#### 13.1.3 Development Resources

| Resource | Available | Details |
|---|---|---|
| **Hardware Components** | ✓ Partial | Some components in lab inventory; others sourced |
| **Software Tools** | ✓ Yes | Open-source (free) TensorFlow Lite, OpenCV, Python, scikit-learn |
| **Documentation** | ✓ Yes | Extensive online resources for Raspberry Pi, AI frameworks, robotics |
| **Community Support** | ✓ Yes | Large community forums for Raspberry Pi and TensorFlow projects |

### 13.2 Required Infrastructure

#### 13.2.1 New Resources Needed

| Resource | Requirement | Implementation Timeline |
|---|---|---|
| **Dedicated Charging Station** | Dedicated outlet with charging dock for robot docking/charging | Weeks 1-2 (coordinate with Building Management) |
| **Configuration Management System** | Central location for storing patrol routes, alert thresholds, user credentials | Weeks 5-6 (implement as YAML config file in repository) |
| **Monitoring Dashboard (Optional)** | Web-based system status dashboard for administrators | IT484 phase (post-IT483) |
| **Backup Power Supply** | UPS or secondary battery for critical periods | Not required for IT483 scope |

#### 13.2.2 Infrastructure Setup Plan

**Week 1 - 2:** 
- [ ] Coordinate with Building Management for charging station placement
- [ ] Test WiFi signal strength and coverage in main hall
- [ ] Establish Telegram bot access and test delivery

**Week 5 - 6:**
- [ ] Deploy charging station equipment
- [ ] Configure WiFi network security for robot device
- [ ] Initialize GitHub repository with project structure

**Week 10 - 11:**
- [ ] Configure Telegram alert chat ID list
- [ ] Set up log file storage on campus server (if available)
- [ ] Test Telegram delivery with actual alert generation

### 13.3 Infrastructure Gap Analysis

#### 13.3.1 Gaps and Mitigation

| Gap | Impact | Mitigation |
|---|---|---|
| **No dedicated charging dock initially** | Robot requires manual charging during development | Manual charging acceptable for IT483; automate for IT484 |
| **Limited remote monitoring dashboard** | Admins must manually check robot status | Provide simple status-check script; full dashboard in IT484 |
| **Local data storage constraints on Pi** | Limited SD card space for logs and images | Implement automatic log rotation; transfer old images to server |
| **Network bandwidth during peak usage** | Telegram alerts with images may face delays on congested WiFi | Queue-based delivery; retry transmission during off-peak hours |

#### 13.3.2 Out-of-Scope Infrastructure

The following infrastructure components are **out-of-scope** for IT483 and proposed for IT484 or future enhancements:

- 24/7 centralized monitoring dashboard
- Full integration with existing campus CCTV system
- Cloud-based image storage and analysis
- Multi-robot coordination system
- Advanced anomaly detection (behavior pattern recognition)

---

## 14. Physical Design

### 14.1 Robot Platform Architecture

#### 14.1.1 Physical Dimensions and Layout

```
┌────────────────────────────────┐
│   [Pi Camera V2 Module]         │ ← Front (Field of View)
├────────────────────────────────┤
│                                │
│  [Raspberry Pi 4 Module]        │ ← Main Controller (center)
│  [Motor Driver (L298N)]         │ ← Control Board
│                                │
├────────────────────────────────┤
│   [Power Input Module]           │ ← External bench supply during testing; 12V battery later
└────────────────────────────────┘
  ↓           ↓           ↓           ↓
[Motor1]  [Motor2]   [Motor3]   [Motor4]
 Front     Front      Back        Back
  Left     Right      Left       Right
  
[HC-SR04 Sensors] × 4
  Front, Back, Left, Right (360° coverage)
```

#### 14.1.2 Mechanical Specifications

| Parameter | Specification |
|---|---|
| **Overall Dimensions** | ~25 cm (length) × 18 cm (width) × 12 cm (height) |
| **Wheelbase** | 20 cm |
| **Wheel Diameter** | 6 cm (typical for 4WD chassis) |
| **Total Mass** | ~2.5 kg (estimate: Pi 0.2kg + Motors 0.3kg + Chassis 0.8kg + Battery 0.6kg + Sensors 0.2kg + Housing 0.4kg) |
| **Payload Capacity** | ~1 kg (operational margin for components) |
| **Ground Clearance** | 3-4 cm |

#### 14.1.3 Component Placement Rationale

**Raspberry Pi 4 (center, elevated):**
- Central position for weight distribution
- Mounted on standoffs to avoid direct contact with chassis
- Adequate ventilation for cooling

**Pi Camera Module (front, top):**
- Front-facing for forward obstacle and human detection
- Elevated to maximize field of view
- 77° FOV covers ~2 m width at 2 m distance

**Motor Driver (adjacent to Pi):**
- Close proximity to GPIO pins (short signal lines)
- Elevated for component access and heat dissipation

**Power Input Module (underside during final deployment):**
   - Future 12V battery pack will be mounted low for stability
   - During testing, robot will be powered by an external bench supply instead of an onboard battery

**HC-SR04 Sensors:**
- Four-point placement: front, back, left, right
- Mounted at ~15 cm height (human and object detection level)
- Spacing optimized for 360° coverage with minimal blind spots

---

### 14.2 Sensor and Actuator Configuration

#### 14.2.1 Motor Configuration

**Motor Type:** DC 3-6V, 100 RPM motors with gearbox (standard 4WD kit)

**Configuration:** 4-wheel independent drive (Mecanum or standard wheels)

**Speed Control:** PWM via L298N motor driver
- Duty cycle 0-100% controls speed 0-0.3 m/s
- Individual motor PWM enables differential steering (turning)

#### 14.2.2 Sensor Configuration Details

**HC-SR04 Ultrasonic Sensors:**
- **Trig pins:** GPIO pins 17, 27, 22, 23 (front, back, left, right)
- **Echo pins:** GPIO pins 4, 5, 6, 12 (corresponding)
- **Polling frequency:** 10 Hz (100 ms interval)
- **Detection range:** 2 cm - 400 cm effective indoor range

**Pi Camera Module V2:**
- **Interface:** CSI ribbon cable (Camera Serial Interface)
- **Resolution:** 3280 × 2464 max; operated at 320 × 240 for processing speed
- **Frame rate:** 10 FPS at operational resolution
- **Exposure:** Auto-adjusting based on ambient light

#### 14.2.3 Power Distribution

```
Bench Power Supply (testing) / 12V Battery (future deployment)
    ↓
   ├─→ [L298N Motor Driver] ← (12V supply for motors)
    │        ↓
    │    ┌──[Motor1]──┬──[Motor2]┐
    │    └──[Motor3]──┬──[Motor4]┘
    │
   ├─→ [Raspberry Pi 4] (via 5V step-down / USB power)
    │        ├─ [Pi Camera]
    │        ├─ [HC-SR04 Sensors] (3.3V GPIO-powered)
    │        └─ [GPIO pins] (power and signal distribution)
    │
   └─→ Margin for future 12V battery integration
```

**Power Budget (Estimate):**
- Raspberry Pi 4: ~600 mA @ 5V = 3 W
- Motors (active): ~400 mA @ 5V = 2 W (typical)
- Sensors (HC-SR04): ~50 mA @ 5V = 0.25 W
- **Total Average:** ~5.25 W
- **Peak (all motors full power):** ~8 W
- **Testing power:** external bench supply, so runtime is not measured in the current prototype stage
- **Future deployment:** 12V battery runtime will be measured after final battery integration

---

### 14.3 Mechanical Systems

#### 14.3.1 Drive System

**Propulsion:** Four independent DC motors with 1:20 gearbox
- **Torque output:** ~1.2 kg·cm per motor (sufficient for 2.5 kg robot mass)
- **Linear speed:** ~0.3 m/s forward/backward
- **Turning radius:** ~0.4 m (tight quarters maneuvering capability)

**Chassis:** Aluminum 4WD chassis (standard robotics kit)
- **Material:** Aluminum alloy (lightweight, corrosion-resistant)
- **Mounting points:** Multiple screw holes for component attachment
- **Wheels:** Rubber tires (traction and floor protection)

#### 14.3.2 Caster or Stabilization

**Optional:** Small caster wheel for stability (may be included in 4WD kit)
- Improves balance on uneven surfaces
- Reduces drag on turns

---

### 14.4 Housing and Protection

#### 14.4.1 Component Housing

**Material:** 3D-printed PLA or laser-cut acrylic enclosure

**Design Features:**
- Protective bumper frame around perimeter (absorbs minor impacts)
- Camera housing with clear front panel (protects lens, maintains FOV)
- Ventilation openings for Pi thermal cooling
- Cable management clips to organize sensor and motor wiring
- Accessibility panels for component replacement

#### 14.4.2 Impact Protection

- Soft foam padding on corners and edges
- Bumper height ~1 cm to absorb furniture leg impacts
- Minimal overhang to reduce caught-corner risk

---

## 15. Database Design

### 15.1 Data Model Overview

The system manages five primary data entities:

1. **Users** - System operators and alert recipients
2. **Patrol Routes** - Predefined navigation paths through main hall
3. **Detection Events** - Human detection occurrences with metadata
4. **Alerts** - Telegram notifications sent to security personnel
5. **Zones** - Labeled regions within main hall for location classification

### 15.2 Detailed Schema

#### 15.2.1 users Table

```
users:
  - user_id: integer (primary key, auto-increment)
  - username: string (unique, max 50 chars)
   - telegram_chat_id: string (Telegram chat identifier)
  - role: string (enum: 'security_personnel', 'system_admin', 'faculty_advisor')
  - password_hash: string (bcrypt hash, not plain text)
  - created_at: timestamp
  - updated_at: timestamp
  - is_active: boolean
```

**Purpose:** Authentication and access control  
**Primary Users:** System administrators, authorized security personnel  

#### 15.2.2 patrol_routes Table

```
patrol_routes:
  - route_id: integer (primary key)
  - route_name: string (e.g., "Main Hall Circuit A")
  - waypoints: json array
    [
      {"x": 0.5, "y": 0.2, "wait_time": 5},
      {"x": 1.2, "y": 0.8, "wait_time": 3},
      {"x": 2.0, "y": 0.4, "wait_time": 2},
      ...
    ]
  - total_distance: float (meters)
  - estimated_cycle_time: integer (seconds)
  - is_active: boolean
  - created_at: timestamp
  - updated_at: timestamp
```

**Purpose:** Store predefined navigation routes  
**Configuration:** Modifiable by system administrator  
**Constraint:** Must normalize coordinates to main hall dimensions  

#### 15.2.3 detections Table

```
detections:
  - detection_id: integer (primary key)
  - timestamp: datetime (detection occurrence time)
  - zone_id: integer (foreign key to zones table)
  - confidence: float (0.0 - 1.0, AI model confidence score)
  - image_path: string (relative path: "alerts/YYYY_MM_DD_HH_MM_SS.jpg")
  - image_size: integer (bytes)
  - frame_number: integer (sequence within session)
  - is_alert_sent: boolean
  - is_false_positive: boolean (populated after human review)
  - notes: string (optional annotation by security personnel)
  - created_at: timestamp
```

**Purpose:** Record all human detection events for analysis and audit trail  
**Indexing:** timestamp, zone_id for efficient querying  
**Retention:** 30-day automatic archival, then compressed storage  

#### 15.2.4 alerts Table

```
alerts:
   - alert_id: integer (primary key)
   - detection_id: integer (foreign key to detections)
   - recipient_chat_id: string
  - subject: string (e.g., "Security Alert: Unauthorized presence detected")
  - body: string (html formatted)
  - image_attachment_path: string
  - sent_at: datetime
  - delivery_status: string (enum: 'sent', 'failed', 'queued')
  - retry_count: integer (0 - 5)
  - next_retry_time: datetime (nullable)
  - created_at: timestamp
  - updated_at: timestamp
```

**Purpose:** Track Telegram alert delivery and enable retry mechanism  
**Audit Trail:** Complete history of notifications sent  
**Failure Handling:** Support for WiFi outage retry logic  

#### 15.2.5 zones Table

```
zones:
  - zone_id: integer (primary key)
  - zone_name: string (e.g., "Entrance Area", "Central Hall", "Corridor A")
  - zone_label: string (short identifier: "ENTRANCE", "CENTRAL", "CORRIDOR_A")
  - description: string
  - boundary_coordinates: json
    {
      "min_x": 0.0, "max_x": 5.0,
      "min_y": 0.0, "max_y": 3.0
    }
  - reference_image_path: string (sample image from zone)
  - model_accuracy: float (0.0 - 1.0, validation accuracy for zone)
  - created_at: timestamp
  - updated_at: timestamp
```

**Purpose:** Define and manage labeled regions for zone classification  
**Training:** Used for zone recognition model training and validation  
**Reference Images:** Support model retraining when layout changes  

### 15.3 Data Storage Implementation

#### 15.3.1 Primary Storage (Raspberry Pi SD Card)

**SQLite Database:**
- Lightweight, embedded SQL engine
- No server required
- Suitable for single-user embedded system
- File: `data/robot.db` (~50 MB capacity, shrinkable)

**File System Storage:**
- Alert images: `data/alerts/YYYY_MM_DD_HH_MM_SS.jpg`
- Logs: `logs/robot.log`, `logs/detections.log`
- Configuration: `config/config.yaml`

#### 15.3.2 Backup and Archive Strategy

**Daily Backups:**
- SQLite database backup at midnight
- Old images (>14 days) compressed to ZIP archives
- Stored in secondary location (USB drive or network share)

**Log Rotation:**
- `robot.log` rotates when >10 MB
- Retains last 5 rotated logs (~50 MB total)
- Older logs archived to network share

#### 15.3.3 Data Privacy and Retention

**Captured Images:**
- Retained for 14 days for incident review
- After 14 days, deleted unless flagged as evidence
- Evidence-flagged images retained per security protocol

**Alert Records:**
- Permanent retention in database (audit trail)
- Queryable by date range for incident review
- Access restricted to authorized personnel

**User Credentials:**
- Never stored in plain text
- Password hashes using bcrypt
- API tokens (if used) encrypted at rest

### 15.4 SQL Queries (Sample Operations)

#### Query 1: Recent Detection Events

```sql
SELECT d.detection_id, d.timestamp, z.zone_name, d.confidence, d.image_path
FROM detections d
JOIN zones z ON d.zone_id = z.zone_id
WHERE d.timestamp >= datetime('now', '-24 hours')
ORDER BY d.timestamp DESC
LIMIT 50;
```

**Use:** Security staff reviewing alerts from past 24 hours

#### Query 2: Alert Delivery Status

```sql
SELECT a.alert_id, a.recipient_chat_id, a.delivery_status, a.sent_at
FROM alerts a
WHERE a.delivery_status = 'failed' OR (a.delivery_status = 'queued' AND a.next_retry_time < datetime('now'))
ORDER BY a.created_at ASC;
```

**Use:** Administrator checking failed alerts for retry/troubleshooting

#### Query 3: Zone Detection Statistics

```sql
SELECT z.zone_name, COUNT(d.detection_id) as detections, AVG(d.confidence) as avg_confidence
FROM zones z
LEFT JOIN detections d ON z.zone_id = d.zone_id AND d.timestamp >= datetime('now', '-7 days')
GROUP BY z.zone_id, z.zone_name
ORDER BY detections DESC;
```

**Use:** Performance analysis - which zones have highest activity/detection

---

## 16. System Summary and Closing

### 16.1 Project Feasibility Conclusion

The AI-Powered Indoor Surveillance Robot project is **technically, operationally, and financially feasible** for implementation as an IT483 capstone project with the following key findings:

**Technical Feasibility:** ✓ CONFIRMED
- Raspberry Pi 4 capable of real-time inference with TensorFlow Lite optimizations
- Proven AI models available for human detection and zone classification
- Embedded Linux ecosystem provides mature robotics libraries
- Estimated performance (5-10 FPS human detection under bench-supply testing) meets requirements; 12V battery runtime will be validated after final deployment

**Operational Feasibility:** ✓ CONFIRMED
- System designed to augment (not replace) existing security operations
- Integration points with campus WiFi and Telegram infrastructure well-understood
- Maintenance and monitoring procedures straightforward for IT staff
- Deployment in controlled indoor environment minimizes operational complexity

**Financial Feasibility:** ✓ CONFIRMED
- Hardware cost (~฿4,460) substantially below commercial alternatives (฿1,000,000+)
- Student prototype spending over $150 supplemented by institutional lab resources
- All software open-source (zero licensing cost)
- ROI potential through scalability to additional campus areas

**Legal and Ethical Feasibility:** ✓ CONFIRMED WITH SAFEGUARDS
- System respects privacy through detection-only approach (no facial recognition)
- Compliant with Thailand PDPA through appropriate data handling
- Requires institutional approval and stakeholder alignment
- Transparent operation with documented monitoring zones and hours

**Schedule Feasibility:** ✓ CONFIRMED
- MVP deliverable achievable by IT483 deadline (May 1, 2026)
- Phased approach with core features in IT483, advanced features in IT484
- Clear milestone structure with risk mitigation strategies
- 3-4 weeks remaining for IT483 completion

---

### 16.2 Key Strengths of Proposed Solution

1. **Cost-Effectiveness:** At not over $150 in current prototype spending + $0 software, substantially more affordable than commercial alternatives
2. **Customization:** Fully open-source and modular design enables ongoing adaptation and improvement
3. **Innovation Integration:** Combines subsumption architecture with AI for robust layered control
4. **Institutional Alignment:** Supports university missions in research, innovation, and operational excellence
5. **Scalability:** Successful implementation provides model for expansion to other campus security areas
6. **Educational Value:** Comprehensive capstone project demonstrating systems integration, AI, and robotics

---

### 16.3 Next Steps and Action Items

#### Immediate (This Week)
- [ ] Finalize proposal feedback and submit any required revisions
- [ ] Obtain written approval from Campus Security Department and administration
- [ ] Confirm advisor assignment and schedule regular check-in meetings

#### Short-term (Weeks 1-2)
- [ ] Initiate hardware assembly and motor control development
- [ ] Coordinate with Building Management for charging station setup
- [ ] Establish GitHub repository and code structure
- [ ] Conduct initial WiFi and Telegram service testing

#### Mid-term (Weeks 5-10)
- [ ] Collect training data in main hall
- [ ] Integrate and test AI models
- [ ] Develop alert system and Telegram integration
- [ ] Implement subsumption architecture layers

#### Long-term (Weeks 11-15)
- [ ] Conduct integrated system testing
- [ ] Document design decisions and deployment procedures
- [ ] Prepare IT483 final report and presentation
- [ ] Plan IT484 extended development (if registered)

---

### 16.4 Defense Presentation Note

This defense document supports the comprehensive presentation of the AI-Powered Indoor Surveillance Robot project to the IT483 committee. The document addresses all required evaluation criteria:

✓ **Self and Project Introduction** (Section 1)  
✓ **Company Profile and Organizational Alignment** (Section 2)  
✓ **Problem Description and Security Gap** (Section 3)  
✓ **Proposed Solution and Stakeholder Importance** (Section 4)  
✓ **Objectives (General and Specific)** (Section 5)  
✓ **Related Works and Comparative Advantages** (Section 6)  
✓ **Expected Business Benefits** (Section 7)  
✓ **Feasibility Study Summary** (Section 8)  
✓ **Development Environment** (Section 9)  
✓ **Risks and Mitigation** (Section 10)  
✓ **Planning and Timeline** (Section 11)  
✓ **User Requirements Summary** (Section 12)  
✓ **Infrastructure Analysis** (Section 13)  
✓ **Physical and Database Design** (Sections 14-15)  

---

## Appendix A: Glossary

| Term | Definition |
|---|---|
| **AI** | Artificial Intelligence; computer systems designed to perform tasks that typically require human intelligence |
| **Subsumption Architecture** | Reactive robot control framework with layers where higher layers can suppress lower-layer behaviors |
| **TensorFlow Lite** | Lightweight machine learning inference framework optimized for mobile and embedded devices |
| **Raspberry Pi 4** | Low-cost single-board computer with quad-core ARM processor, WiFi, and GPIO for sensor/actuator control |
| **HC-SR04** | Ultrasonic distance sensor for obstacle detection |
| **PWM** | Pulse Width Modulation; signal control technique for varying motor speed via duty cycle |
| **Telegram Bot API** | Telegram platform interface used for sending alert messages and images |
| **PDPA** | Thailand Personal Data Protection Act; privacy regulation |
| **GPIO** | General Purpose Input/Output; digital pins on microcontroller for sensor/actuator communication |
| **FPS** | Frames Per Second; video/image processing speed metric |
| **MobileNet SSD** | Lightweight pre-trained AI model for real-time object detection |
| **Zone Recognition** | AI classification model for identifying robot location within predetermined regions |

---

## Appendix B: Reference Documents

- SDP_Proposal_Draft.md (full proposal document with detailed specifications)
- IT483_Defense_Preparation.md (defense requirements and structure guidelines)
- GitHub Repository: https://github.com/Faculty-of-IT/20252026s2-Peeranat-Ks

---

**Document prepared by:** Peeranat K.  
**Date:** May 7, 2026  
**Status:** Ready for IT483 Defense Presentation  
**Version:** 1.0

---
