import os
import shutil

def find_roblox_exe(versions_folder, exe_name):
    for root, dirs, files in os.walk(versions_folder):
        if exe_name in files:
            return os.path.join(root, exe_name)
    return None

def copy_settings_to_folder(settings_file, destination_folder):
    shutil.copy(settings_file, destination_folder)

def create_client_settings_file(file_path):
    with open(file_path, 'w') as f:
        f.write('{"DFIntTaskSchedulerTargetFps": 144}')

# Get the absolute path of the script directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script directory
os.chdir(script_directory)

# Use absolute path for ClientAppSettings.json
settings_file_path = os.path.join(script_directory, "ClientAppSettings.json")

print("Welcome to FPS Unlock v.1.0.0")

if os.path.isfile(settings_file_path):
    print("Found ClientAppSettings.json...")
    print("Finding correct folder...")
    pathone = "C:/Program Files (x86)/Roblox/Versions"
    versions = [d for d in os.listdir(pathone) if os.path.isdir(os.path.join(pathone, d)) and d.startswith("version")]

    if versions:
        print("Found the following versions:")
        for version in versions:
            print(version)
            roblox_exe = find_roblox_exe(os.path.join(pathone, version), "RobloxPlayerBeta.exe")
            if roblox_exe:
                print("robloxplayerbeta.exe found in:", roblox_exe)
                client_settings_folder = os.path.join(os.path.dirname(roblox_exe), "ClientSettings")
                print("Checking for ClientSettings folder in:", client_settings_folder)
                if os.path.exists(client_settings_folder):
                    print("ClientSettings folder found in:", client_settings_folder)
                    settings_file_in_folder = os.path.join(client_settings_folder, "ClientAppSettings.json")
                    if os.path.exists(settings_file_in_folder):
                        print("FPS is already unlocked.")
                    else:
                        print("Creating ClientAppSettings.json in the folder...")
                        create_client_settings_file(settings_file_in_folder)
                        print("FPS is now unlocked.")
                        input("Press [ENTER] to exit")
                else:
                    print("ClientSettings folder not found.")
                    print("Creating the ClientSettings folder...")
                    os.makedirs(client_settings_folder)
                    print("Creating ClientAppSettings.json in the folder...")
                    create_client_settings_file(os.path.join(client_settings_folder, "ClientAppSettings.json"))
                    print("FPS is now unlocked.")
                    input("Press [ENTER] to exit")
                break
        else:
            print("RobloxPlayerBeta.exe not found in any version folder.")
    else:
        print("No versions found.")
else:
    print("ClientAppSettings.json not found.")
    create_file = input("Do you want to create ClientAppSettings.json? (yes/no): ")
    if create_file.lower() == "yes":
        print("Creating ClientAppSettings.json...")
        create_client_settings_file(settings_file_path)
        print("FPS is now unlocked.")
        input("Press [ENTER] to exit")
    else:
        input("Press [ENTER] to exit")