# Python Log Analyzer
# This script analyzes a sample log file and identifies suspicious security events.

def analyze_log(file_path):
    suspicious_keywords = ["failed", "unauthorized", "denied", "invalid"]
    suspicious_events = []

    try:
        with open(file_path, "r") as file:
            for line in file:
                for keyword in suspicious_keywords:
                    if keyword in line.lower():
                        suspicious_events.append(line.strip())
                        break

        print("Security Log Analysis Report")
        print("----------------------------")
        print(f"Total suspicious events found: {len(suspicious_events)}")

        if suspicious_events:
            print("\nSuspicious Log Entries:")
            for event in suspicious_events:
                print(event)
        else:
            print("No suspicious activity found.")

    except FileNotFoundError:
        print("Log file not found. Please check the file path.")


if __name__ == "__main__":
    log_file = "sample_logs.txt"
    analyze_log(log_file)
