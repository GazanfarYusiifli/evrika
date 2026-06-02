import os
import subprocess

def compress_large_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                filepath = os.path.join(root, file)
                # Check file size
                if os.path.getsize(filepath) > 1024 * 1024:  # > 1MB
                    print(f"Compressing: {filepath}")
                    try:
                        # Use macOS sips to resize and compress
                        # Max width/height 1920px, format jpeg, quality low/normal
                        subprocess.run([
                            'sips',
                            '-Z', '1920',
                            '-s', 'format', 'jpeg',
                            '-s', 'formatOptions', 'low',
                            filepath,
                            '--out', filepath
                        ], check=True, stdout=subprocess.DEVNULL)
                        print(f"Successfully compressed {file}")
                    except Exception as e:
                        print(f"Failed to compress {file}: {e}")

if __name__ == "__main__":
    directories = [
        "/Users/gazanfaryusifli/Downloads/Evrika/assets/eduhome",
        "/Users/gazanfaryusifli/Downloads/Evrika/assets/montesorriKids",
        "/Users/gazanfaryusifli/Downloads/Evrika/assets",
        "/Users/gazanfaryusifli/Downloads/Evrika/public/assets",
    ]
    for d in directories:
        if os.path.exists(d):
            compress_large_images(d)
