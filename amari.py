import requests
import json
import time
import logging
import subprocess
from typing import Dict, Any, List, Optional


class AmarisoftUESimulator:
    """Class to interact with Amarisoft UE Simulator via its REST API"""

    def __init__(self, host: str = "localhost", port: int = 9000, log_level: str = "INFO"):
        """Initialize the UE Simulator interface

        Args:
            host: Hostname or IP of the Amarisoft UE simulator
            port: Port number of the REST API
            log_level: Logging level
        """
        self.base_url = f"http://{host}:{port}"
        self.session = requests.Session()

        # Setup logging
        logging.basicConfig(
            level=getattr(logging, log_level),
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger("AmarisoftUESim")

    def send_command(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Send a command to the UE simulator

        Args:
            endpoint: API endpoint
            data: Command data as a dictionary

        Returns:
            Response data as a dictionary
        """
        url = f"{self.base_url}/{endpoint}"
        self.logger.debug(f"Sending request to {url} with data: {data}")

        try:
            response = self.session.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {e}")
            raise

    def start_ue(self, imsi: str, config: Optional[Dict[str, Any]] = None) -> bool:
        """Start a UE with the given IMSI

        Args:
            imsi: IMSI of the UE to start
            config: Additional configuration parameters

        Returns:
            True if started successfully
        """
        data = {
            "command": "start_ue",
            "imsi": imsi
        }

        if config:
            data.update(config)

        response = self.send_command("api/ue", data)
        success = response.get("status") == "ok"

        if success:
            self.logger.info(f"UE with IMSI {imsi} started successfully")
        else:
            self.logger.error(f"Failed to start UE: {response.get('error', 'Unknown error')}")

        return success

    def stop_ue(self, imsi: str) -> bool:
        """Stop a UE with the given IMSI

        Args:
            imsi: IMSI of the UE to stop

        Returns:
            True if stopped successfully
        """
        data = {
            "command": "stop_ue",
            "imsi": imsi
        }

        response = self.send_command("api/ue", data)
        success = response.get("status") == "ok"

        if success:
            self.logger.info(f"UE with IMSI {imsi} stopped successfully")
        else:
            self.logger.error(f"Failed to stop UE: {response.get('error', 'Unknown error')}")

        return success

    def get_ue_status(self, imsi: str) -> Dict[str, Any]:
        """Get status of a UE with the given IMSI

        Args:
            imsi: IMSI of the UE

        Returns:
            Status information as a dictionary
        """
        data = {
            "command": "get_ue_status",
            "imsi": imsi
        }

        response = self.send_command("api/ue", data)
        if response.get("status") == "ok":
            return response.get("ue_status", {})
        else:
            self.logger.error(f"Failed to get UE status: {response.get('error', 'Unknown error')}")
            return {}

    def execute_data_transfer_test(self, imsi: str, target_ip: str, duration: int = 30) -> Dict[str, Any]:
        """Execute a data transfer test

        Args:
            imsi: IMSI of the UE to test
            target_ip: Target IP for the data transfer
            duration: Test duration in seconds

        Returns:
            Test results as a dictionary
        """
        data = {
            "command": "execute_test",
            "imsi": imsi,
            "test_type": "data_transfer",
            "parameters": {
                "target_ip": target_ip,
                "duration": duration,
                "dl_bitrate": 10000000,  # 10 Mbps
                "ul_bitrate": 5000000  # 5 Mbps
            }
        }

        response = self.send_command("api/test", data)
        if response.get("status") == "ok":
            self.logger.info(f"Data transfer test started for UE {imsi}")
            # Wait for test to complete
            time.sleep(duration + 5)  # Add 5 seconds buffer

            # Get test results
            results = self.get_test_results(imsi, response.get("test_id"))
            return results
        else:
            self.logger.error(f"Failed to start data transfer test: {response.get('error')}")
            return {}

    def get_test_results(self, imsi: str, test_id: str) -> Dict[str, Any]:
        """Get the results of a test

        Args:
            imsi: IMSI of the UE
            test_id: ID of the test

        Returns:
            Test results as a dictionary
        """
        data = {
            "command": "get_test_results",
            "imsi": imsi,
            "test_id": test_id
        }

        response = self.send_command("api/test", data)
        if response.get("status") == "ok":
            return response.get("results", {})
        else:
            self.logger.error(f"Failed to get test results: {response.get('error')}")
            return {}