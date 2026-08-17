import time
import datetime
import requests

class AutomatedAPITester:
    def __init__(self, target_url):
        # Clean extra spaces or brackets if any
        self.target_url = target_url.strip()
        self.report_data = []

    def run_performance_and_status_check(self):
        """Tests the server status and response time automatically."""
        start_time = time.time()
        try:
            response = requests.get(self.target_url, timeout=5)
            end_time = time.time()
            
            response_time = round((end_time - start_time) * 1000, 2)
            status_code = response.status_code
            
            is_passed = status_code == 200 and response_time < 2000
            
            result = {
                "status_code": status_code,
                "response_time_ms": response_time,
                "passed": is_passed
            }
            self.report_data.append(result)
            return result
            
        except Exception as e:
            result = {"error": str(e), "passed": False}
            self.report_data.append(result)
            return result

    def generate_final_report(self):
        """Generates a professional text report for management."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report_text = f"""
==================================================
        CLOUD & API HEALTH AUDITOR
==================================================
Date/Time: {timestamp}
Target Service: {self.target_url}
--------------------------------------------------
RESULTS SUMMARY:
"""
        for index, res in enumerate(self.report_data, 1):
            if "error" in res:
                report_text += f"Test #{index}: FAILED | Error: {res['error']}\n"
            else:
                status = "PASSED" if res['passed'] else "FAILED"
                report_text += f"Test #{index}: {status} | Status Code: {res['status_code']} | Response Time: {res['response_time_ms']} ms\n"
                
        report_text += "==================================================\n"
        
        with open("Test_Execution_Report.txt", "w", encoding="utf-8") as file:
            file.write(report_text)
            
        return report_text

# --- Interactive Tool Execution ---
if __name__ == "__main__":
    print("=== ​CLOUD & API AUTOMATED TESTING TOOL ===")
    user_url = input("Enter the URL to test: ")
    
    tester = AutomatedAPITester(user_url)
    tester.run_performance_and_status_check()
    
    print(tester.generate_final_report())
