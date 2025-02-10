import subprocess
import re

class WifiSecurityAnalysis:
    def __init__(self):
        self.networks = []

    def scan_networks(self):
        """Scan available Wi-Fi networks and fetch security information"""
        networks_info = subprocess.check_output(['netsh', 'wlan', 'show', 'network']).decode('utf-8')
        self.networks = self.parse_networks(networks_info)

    def parse_networks(self, networks_info):
        """Parse the output of Wi-Fi networks"""
        networks = []
        network_details = networks_info.split('\n\n')
        
        for network in network_details:
            network_info = {}
            for line in network.split('\n'):
                if "SSID" in line:
                    network_info['SSID'] = line.split(':')[1].strip()
                elif "Authentication" in line:
                    network_info['Authentication'] = line.split(':')[1].strip()
                elif "Encryption" in line:
                    network_info['Encryption'] = line.split(':')[1].strip()
            
            if network_info:
                networks.append(network_info)
        
        return networks

    def print_networks(self):
        """Display the networks"""
        for network in self.networks:
            print(f"SSID: {network['SSID']}")
            print(f"Authentication: {network['Authentication']}")
            print(f"Encryption: {network['Encryption']}")
            print('-' * 50)

    def analyze_security(self):
        """Analyze the security of each network"""
        for network in self.networks:
            if "WPA2" in network['Authentication']:
                print(f"{network['SSID']} uses WPA2 encryption, which is secure.")
            elif "WEP" in network['Authentication']:
                print(f"{network['SSID']} uses WEP encryption, which is insecure!")
            else:
                print(f"Security information for {network['SSID']} is unknown.")

if __name__ == '__main__':
    wifi_security = WifiSecurityAnalysis()
    wifi_security.scan_networks()
    wifi_security.print_networks()
    wifi_security.analyze_security()
