# -----------------------------------------------------------
# Assignment: Bug Tracking System using Class and Dictionary
# -----------------------------------------------------------

class BugTracker:
    def __init__(self):
        # Dictionary to store bugs
        # Format: { bug_id: {"description": ..., "severity": ..., "status": ...} }
        self.bugs = {}

    def add_bug(self, bug_id, description, severity):
        """Add a new bug with status 'Open'"""
        if bug_id in self.bugs:
            print(f"❌ Bug ID {bug_id} already exists! Choose a unique ID.")
        else:
            self.bugs[bug_id] = {
                "description": description,
                "severity": severity,
                "status": "Open"
            }
            print(f"✅ Bug {bug_id} added successfully.")
            

    def update_status(self, bug_id, new_status):
        """Update status of an existing bug"""
        if bug_id in self.bugs:
            self.bugs[bug_id]["status"] = new_status
            print(f"🔄 Bug {bug_id} status updated to '{new_status}'.")
        else:
            print(f"❌ Bug ID {bug_id} not found!")

    def list_all_bugs(self):
        """Print all bugs with details in readable format"""
        if not self.bugs:
            print("📭 No bugs recorded.")
        else:
            print("\n🪲 All Bug Records:")
            print("-" * 60)
            for bug_id, details in self.bugs.items():
                print(f"Bug ID: {bug_id}")
                print(f"  Description: {details['description']}")
                print(f"  Severity: {details['severity']}")
                print(f"  Status: {details['status']}")
                print("-" * 60)


# ----------------- Main Program -----------------
if __name__ == "__main__":
    # Create a BugTracker object
    tracker = BugTracker()

    # Add at least three bugs
    tracker.add_bug(101, "Login button not responding", "High")
    tracker.add_bug(102, "Incorrect total on checkout page", "Medium")
    tracker.add_bug(103, "Profile picture not updating", "Low")

    # Update statuses
    tracker.update_status(101, "In Progress")
    tracker.update_status(102, "Closed")

    # Display all bugs
    tracker.list_all_bugs()
