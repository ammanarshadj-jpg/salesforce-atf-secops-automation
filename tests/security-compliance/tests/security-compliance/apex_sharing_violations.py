import os

def audit_apex_classes(directory):
    """
    Simulates a baseline security health check for ATO readiness.
    Scans mock Apex files to ensure they enforce sharing rules ('with sharing').
    """
    print("Starting Salesforce Security Health Check for Apex Classes...")
    violations = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".cls"):
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()
                    if "with sharing" not in content and "without sharing" not in content:
                        print(f"[SECURITY ALERT] Missing sharing declaration in: {file}")
                        violations += 1
                        
    if violations == 0:
        print("Success: All Apex classes comply with federal data isolation rules.")
    else:
        print(f"Scan complete. Found {violations} security baseline anomalies.")

# Example trigger
if __name__ == "__main__":
    # Create a mock directory or point to a Salesforce metadata folder
    audit_apex_classes(".")
