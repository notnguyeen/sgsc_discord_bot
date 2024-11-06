# commands/hello_command.py
import requests
from ping3 import ping


class HelloCommand:
    def get_internet_data(self):
        """Checks internet connectivity and retrieves detailed connection data."""
        data = {}

        # Check Internet Connectivity
        try:
            response = requests.get("https://www.google.com", timeout=5)
            data["status"] = (
                "Connected" if response.status_code == 200 else "Disconnected"
            )
        except requests.RequestException:
            data["status"] = "Disconnected"
            return data  # Return immediately if not connected

        # Get Public IP Address
        try:
            ip_response = requests.get("https://api.ipify.org?format=json", timeout=5)
            data["ip"] = ip_response.json().get("ip")
        except requests.RequestException:
            data["ip"] = "Unavailable"

        # Measure Latency
        try:
            latency = ping("google.com")
            data["latency_ms"] = round(latency * 1000, 2) if latency else "Unavailable"
        except Exception:
            data["latency_ms"] = "Unavailable"

        return data

    async def execute(self, update, context):
        # Get internet connection data
        data = self.get_internet_data()

        # Prepare the response text with user name and connection details
        response_text = (
            f"Hello, {update.message.from_user.first_name}!\n\n"
            f"**Internet Connection Status**\n"
            f"Status: {data['status']}\n"
            f"Public IP: {data.get('ip', 'Unavailable')}\n"
            f"Latency: {data.get('latency_ms', 'Unavailable')} ms"
        )

        # Send the message to the user
        await update.message.reply_text(response_text)
