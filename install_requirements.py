import subprocess

def install_packages():
    packages = ['rembg', 'Pillow', 'numpy']
    for package in packages:
        subprocess.check_call([ 'pip', 'install', package ])
    print("✅ All packages installed successfully.")

if __name__ == "__main__":
    install_packages()
