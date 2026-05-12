# Python Log Analyzer

## Overview
This project is a Python-based security log analysis tool designed to review system logs and identify suspicious activity such as failed login attempts and unauthorized access attempts.

## Objectives
- Read and analyze log files using Python
- Detect failed login attempts
- Identify unauthorized access attempts
- Count suspicious events
- Generate a simple security summary report

## Tools & Technologies
- Python
- Log Analysis
- Security Monitoring
- File Handling
- Cybersecurity Automation

## Features
- Reads log files from a text file
- Detects failed login attempts
- Detects unauthorized access attempts
- Counts suspicious events
- Displays suspicious log entries
- Provides a simple summary report

## Project Files
- `log_analyzer.py` - Main Python script used to analyze logs
- `sample_logs.txt` - Sample log file used for testing
- `requirements.txt` - Project dependency file

## How to Run

```bash
python log_analyzer.py

## Sample Output

```text
Security Log Analysis Report
----------------------------
Total suspicious events found: 4

Suspicious Log Entries:
2026-05-01 10:17:45 Failed login attempt for user root
2026-05-01 10:19:02 Unauthorized access attempt from 192.168.1.25
2026-05-01 10:28:30 Access denied for user guest
2026-05-01 10:31:11 Invalid password attempt for user test


