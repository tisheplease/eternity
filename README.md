ETERNITY: Anonymity and Privacy Tool

ETERNITY is a powerful privacy tool designed to enhance online anonymity and security. It supports various methods for masking your identity and protecting your online presence, including proxy connections, MAC address changes, DNS server modifications, WireGuard VPN setup, Tor setup, User-Agent spoofing, and more.
Features

    Proxy Connection:

        Connect to the internet through a proxy server to hide your real IP address.

        Supports proxy authentication (username/password) if needed.

    MAC Address Change:

        Change your MAC address on Linux-based systems to prevent tracking by network administrators.

    DNS Server Change:

        Modify your DNS servers for better security and privacy, preventing DNS leaks.

    Tor Setup:

        Install and configure the Tor network to route your traffic through multiple layers of encryption, ensuring anonymity.

    WireGuard VPN Setup:

        Install and configure WireGuard, a high-performance VPN solution, for a secure internet connection.

    User-Agent Spoofing:

        Change your User-Agent string to mask your browser/device, making it harder to track your online activity.

    Anonymity Mode (VPN + Proxy + Tor):

        Combine VPN, proxy, and Tor for maximum online anonymity.

    Proxychain Creation:

        Install and configure Proxychains to chain multiple proxies together for enhanced anonymity.

    Dependency Installation:

        Automatically install required dependencies like WireGuard, Tor, and Proxychains depending on your system's Linux distribution.

Installation
Requirements:

    Linux-based operating system (Ubuntu, Debian, Fedora, Arch, etc.)

    Python 3.x

    sudo privileges for installing and configuring network settings

Installation Steps:

    Clone the repository:

git clone https://github.com/tisheplease/eternity.git
cd eternity

Install dependencies:

python3 -m pip install -r requirements.txt

Run the script:

    sudo python3 eternity.py

    Note: You may be prompted to enter your password for commands requiring root privileges (e.g., changing MAC address, installing software).

Usage

Once the script is running, you'll be presented with a menu of options. Choose an option by entering the corresponding number:

    Connect to Proxy: Set up a proxy server to route your traffic through a different IP.

    Change MAC Address: Modify your MAC address to prevent tracking.

    Setup WireGuard VPN: Install and configure a WireGuard VPN.

    Create Proxychain: Set up Proxychains to route your traffic through multiple proxies.

    Change DNS: Change your DNS server settings.

    Setup Tor: Install and configure Tor for routing traffic through its anonymizing network.

    Change User-Agent: Spoof your User-Agent string to mask your browser.

    Enable Full Anonymity: Combine VPN, Proxy, and Tor for maximum privacy.

    Exit: Exit the application.

Supported Systems

    Linux: Ubuntu, Debian, Fedora, Arch

        Automatically installs the necessary dependencies (WireGuard, Tor, Proxychains) for these systems.

Contributing

Feel free to fork the repository and contribute improvements! To contribute:

    Fork the repository

    Create a new branch (git checkout -b feature-branch)

    Make your changes

    Commit your changes (git commit -am 'Add new feature')

    Push to your branch (git push origin feature-branch)

    Create a pull request

License

This project is licensed under the MIT License - see the LICENSE file for details.
Disclaimer

This software is intended for educational purposes only. Use it responsibly and ensure that you comply with all applicable laws and regulations in your jurisdiction. Misuse of the software for illegal activities is not endorsed or supported.
