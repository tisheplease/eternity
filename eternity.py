import requests
import pyfiglet
import os
import subprocess
import paramiko
from termcolor import colored
from fake_useragent import UserAgent


def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art = pyfiglet.figlet_format("ETERNITY", font="doom")
    print(colored("=============================================================\n", "cyan"))
    print(colored(ascii_art, "cyan"))
    print(colored("        anonimity soft by @tisheplease", "cyan"))
    print(colored("=============================================================", "cyan"))
    print(colored("1. Подключение к прокси\t\t 5. Смена DNS-серверов", "cyan"))
    print(colored("2. Смена MAC-адреса (Linux)\t\t 6. Настройка Tor", "cyan"))
    print(colored("3. Установка и настройка WireGuard VPN\t 7. Подмена User-Agent", "cyan"))
    print(colored("4. Создание проксичейна\t\t 8. Включение анонимности (VPN + Proxy + Tor)", "cyan"))
    print(colored("=============================================================", "cyan"))
    print(colored("9. Выход", "cyan"))


def connect_proxy():
    ip = input("Введите IP прокси: ")
    port = input("Введите порт прокси: ")
    user = input("Введите имя пользователя (оставьте пустым, если не требуется): ")
    passwd = input("Введите пароль (оставьте пустым, если не требуется): ")

    if user and passwd:
        proxy_url = f"http://{user}:{passwd}@{ip}:{port}"
    else:
        proxy_url = f"http://{ip}:{port}"

    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }

    try:
        response = requests.get("http://checkip.amazonaws.com/", proxies=proxies, timeout=10)
        print(colored(f"Успешное подключение через прокси! Ваш IP: {response.text.strip()}", "green"))
    except requests.exceptions.RequestException as e:
        print(colored(f"Ошибка подключения к прокси: {e}", "red"))


def change_mac():
    interface = input("Введите имя сетевого интерфейса (например, eth0 или wlan0): ")
    new_mac = input("Введите новый MAC-адрес: ")

    try:
        subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
        subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac], check=True)
        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
        print(colored(f"MAC-адрес успешно изменен на {new_mac}", "green"))
    except subprocess.CalledProcessError as e:
        print(colored(f"Ошибка при изменении MAC-адреса: {e}", "red"))


def change_dns():
    dns1 = input("Введите первичный DNS-сервер: ")
    dns2 = input("Введите вторичный DNS-сервер: ")

    try:
        with open("/etc/resolv.conf", "w") as file:
            file.write(f"nameserver {dns1}\n")
            file.write(f"nameserver {dns2}\n")
        print(colored(f"DNS-серверы успешно изменены на {dns1} и {dns2}", "green"))
    except PermissionError:
        print(colored("Не хватает прав для изменения DNS-серверов. Используйте sudo.", "red"))
    except Exception as e:
        print(colored(f"Ошибка при изменении DNS-серверов: {e}", "red"))


def setup_tor():
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "tor"], check=True)
        subprocess.run(["sudo", "systemctl", "start", "tor"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "tor"], check=True)
        print(colored("Tor успешно установлен и запущен!", "green"))
    except subprocess.CalledProcessError as e:
        print(colored(f"Ошибка при установке Tor: {e}", "red"))


def setup_wireguard():
    server_ip = input("Введите IP-адрес сервера: ")
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server_ip, username=username, password=password)

        commands = [
            "sudo apt update",
            "sudo apt install -y wireguard",
            "sudo wg genkey | tee privatekey | wg pubkey > publickey",
            "sudo systemctl enable wg-quick@wg0",
            "sudo systemctl start wg-quick@wg0"
        ]

        for cmd in commands:
            stdin, stdout, stderr = client.exec_command(cmd)
            print(colored(stdout.read().decode(), "green"))
            print(colored(stderr.read().decode(), "red"))

        print(colored("WireGuard успешно установлен и запущен на сервере!", "green"))
        client.close()
    except Exception as e:
        print(colored(f"Ошибка при установке WireGuard: {e}", "red"))


def change_user_agent():
    ua = UserAgent()
    print(colored(f"Ваш новый User-Agent: {ua.random}", "green"))


def enable_anonymity():
    try:
        subprocess.run(["sudo", "systemctl", "start", "tor"], check=True)
        print(colored("Tor успешно подключен!", "green"))

        subprocess.run(["sudo", "wg-quick", "up", "wg0"], check=True)
        print(colored("VPN успешно подключен!", "green"))

        os.environ["http_proxy"] = "http://127.0.0.1:8080"
        os.environ["https_proxy"] = "http://127.0.0.1:8080"
        print(colored("Прокси успешно настроен!", "green"))

        print(colored("Все уровни анонимности включены!", "green"))
    except subprocess.CalledProcessError as e:
        print(colored(f"Ошибка при включении анонимности: {e}", "red"))


def create_proxychain():
    try:
        subprocess.run(["sudo", "apt", "install", "-y", "proxychains"], check=True)
        print(colored("Proxychains успешно установлен!", "green"))
    except subprocess.CalledProcessError as e:
        print(colored(f"Ошибка при установке Proxychains: {e}", "red"))


def install_dependencies():
    dist = os.uname().sysname.lower()

    try:
        if dist == "linux":
            # Для Debian, Ubuntu
            subprocess.run(["sudo", "apt", "install", "-y", "wireguard", "tor", "proxychains"], check=True)
        elif dist == "fedora":
            subprocess.run(["sudo", "dnf", "install", "-y", "wireguard-tools", "tor", "proxychains"], check=True)
        elif dist == "arch":
            subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "wireguard-tools", "tor", "proxychains"], check=True)
        else:
            print(colored(f"Операционная система {dist} не поддерживается", "red"))
        print(colored("Все зависимости успешно установлены!", "green"))
    except subprocess.CalledProcessError as e:
        print(colored(f"Ошибка при установке зависимостей: {e}", "red"))


def main():
    while True:
        show_menu()
        choice = input("Выберите опцию: ")

        if choice == "1":
            connect_proxy()
        elif choice == "2":
            change_mac()
        elif choice == "3":
            setup_wireguard()
        elif choice == "4":
            create_proxychain()
        elif choice == "5":
            change_dns()
        elif choice == "6":
            setup_tor()
        elif choice == "7":
            change_user_agent()
        elif choice == "8":
            enable_anonymity()
        elif choice == "9":
            print(colored("Выход из программы...", "yellow"))
            break
        else:
            print(colored("Неверный выбор, попробуйте снова.", "red"))

        input("Нажмите Enter, чтобы вернуться в меню...")


if __name__ == "__main__":
    install_dependencies()
    main()
