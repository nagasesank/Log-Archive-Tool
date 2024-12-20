import os
import tarfile
import argparse
import datetime

def create_archive(log_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_filename = f"logs_archive_{timestamp}.tar.gz"
    archive_path = os.path.join(output_directory, archive_filename)
    
    with tarfile.open(archive_path, "w:gz") as tar:
        for root, _, files in os.walk(log_directory):
            for file in files:
                file_path = os.path.join(root, file)
                tar.add(file_path, arcname=os.path.relpath(file_path, log_directory))
    
    return archive_path

def log_archive_details(archive_path, log_file):
    log_entry = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Archived: {archive_path}\n"
    with open(log_file, "a") as log:
        log.write(log_entry)

def main():
    parser = argparse.ArgumentParser(description="Archive log files from a specified directory.")
    parser.add_argument("log_directory", type=str, help="Path to the directory containing log files to be archived.")
    parser.add_argument("--output-dir", type=str, default="/var/log/archives", help="Directory where the archive will be stored (default: /var/log/archives).")
    parser.add_argument("--log-file", type=str, default="/var/log/archive_tool.log", help="Path to the log file where archive details will be recorded (default: /var/log/archive_tool.log).")
    
    args = parser.parse_args()
    
    try:
        if not os.path.isdir(args.log_directory):
            raise FileNotFoundError(f"The specified log directory does not exist: {args.log_directory}")
        
        archive_path = create_archive(args.log_directory, args.output_dir)
        log_archive_details(archive_path, args.log_file)
        print(f"Successfully archived logs to {archive_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
