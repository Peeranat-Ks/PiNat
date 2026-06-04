# IT483 Defense Preparation Guide

Project: AI-Powered Indoor Surveillance Robot
Student: Peeranat K.

## 1) Mandatory Logistics Checklist

- [ ] Official and complete uniform
- [ ] Presentation duration rehearsed to 30 minutes
- [ ] Q&A preparation for 10 minutes
- [ ] Upload report in PDF and DOCX/ODT to FIT Senior Projects Teams
- [ ] Upload presentation in PDF and PPTX/ODP to FIT Senior Projects Teams

## 2) Required Presentation Structure (Committee Order)

Use this exact flow so all rubric items are covered.

1. Self and project introduction
2. Company profile, organizational chart, mission/goal related to the proposed solution
3. Description of the problem
4. Brief description of the proposed solution and its importance for the client
5. Objectives of the project
6. Related works and advantages of your proposal compared to them
7. Benefits of the proposed solution for the company
8. Summary of feasibility studies
9. Development environment
10. Risks
11. Planning
12. Summary of user requirements
13. Summary of infrastructure analysis
14. Physical design and database design

## 3) Recommended Slide Plan (15 Slides, 30 Minutes)

- Slide 1 (1 min): Title, student intro, project one-sentence pitch
- Slide 2 (2 min): Company profile + organizational chart + mission alignment
- Slide 3 (2 min): Problem statement and current gap after 10:00 PM
- Slide 4 (2 min): Proposed solution and stakeholder importance
- Slide 5 (3 min): General and specific objectives (measurable targets)
- Slide 6 (2 min): Related works
- Slide 7 (2 min): Comparative advantages table
- Slide 8 (2 min): Expected business benefits
- Slide 9 (2 min): Feasibility summary (technical, operational, legal, schedule, financial)
- Slide 10 (2 min): Development environment (hardware, software, methods)
- Slide 11 (2 min): Risks and mitigation
- Slide 12 (2 min): Planning and Gantt milestone status
- Slide 13 (2 min): User requirements summary
- Slide 14 (2 min): Infrastructure analysis (available vs required)
- Slide 15 (2 min): Physical design + database design + closing

Total: 30 minutes

## 4) Content You Should Emphasize for This Project

### Feasibility summary
- Technical: Raspberry Pi 4 + open-source AI libraries are practical for MVP scope
- Operational: Supports security staff with alerts, does not replace guards
- Legal/Ethical: No facial recognition, no biometric identity storage
- Schedule: Milestones tied to SDP calendar
- Financial: Student budget with low-cost hardware and open-source software

### Development environment
- Hardware: Raspberry Pi 4, camera module, HC-SR04, motor controller, 4WD chassis
- Software: Python, OpenCV, TensorFlow Lite/scikit-learn (as used), SMTP email service
- Process model: Iterative prototyping and incremental testing
- Repository: Institutional GitHub for version control

### Risks and mitigation
- WiFi outage -> local log and delayed-send strategy
- Low-light detection drop -> improve lighting and retrain with low-light samples
- Compute limitations on Pi -> model optimization (input size, quantization)
- Battery limits -> patrol schedule and charging plan
- Single-developer risk -> strict milestone tracking and advisor feedback loop

### User requirements summary
- Security Personnel: Receive alert email with image/time, view logs
- System Administrator: Configure patrol hours, email settings, thresholds, maintenance

### Infrastructure analysis summary
- Available: campus WiFi, indoor hall patrol area, charging points
- Required: robot hardware stack, model runtime, logging storage, SMTP connectivity
- Gap: robust remote dashboard and full CCTV integration are future work

### Physical and database design (simple, defendable)
- Physical design: camera and ultrasonic sensors on front; Pi control center; motor driver to 4WD base
- Data design (logical tables/files):
  - users (role, contact)
  - patrol_logs (time, zone, status)
  - detections (time, confidence, image_path)
  - alerts (time_sent, recipient, delivery_status)
  - zones (zone_id, label, reference_features)

## 5) Fast Defense Compliance Check

Before submission, confirm all are present in slides and report:

- [ ] Feasibility study summary slide
- [ ] Development environment slide
- [ ] Risk slide with mitigation
- [ ] User requirements summary slide
- [ ] Infrastructure analysis summary slide
- [ ] Physical design and database design slide
- [ ] Time practice completed at least 2 full runs
- [ ] Final files uploaded in all required formats

## 6) Likely Q&A Prompts

1. Why is this project needed if guards already patrol?
2. Why choose Raspberry Pi instead of higher-power hardware?
3. How will you evaluate detection accuracy and alert latency?
4. What are the biggest technical risks and fallback plans?
5. Why did you exclude facial recognition?
6. How does your design protect privacy and ethics?
7. What data structure supports auditability and future scaling?
8. What would be your first improvement in IT484?
