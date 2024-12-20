# Log-Archive-Tool

This Python script creates a command-line tool to archive log files. It takes the log directory as an argument, compresses the files into a tar.gz archive, and logs the archive's date, time, and location in a log file.

1. CLI Usage:
   ```bash
    python log_archiver.py <log-directory> --output-dir <output-directory> --log-file <log-file-path>
2. Options:
  log_directory: Required. The path of the log directory to archive.
  --output-dir: Optional. Default is /var/log/archives. Where the tar.gz file will be stored.
  --log-file: Optional. Default is /var/log/archive_tool.log. Where archive details will be logged.
3. Log Details:
  The date, time, and archive location are recorded in the specified log file.
  You can modify the output-dir and log-file paths as needed for your system.

https://roadmap.sh/projects/log-archive-tool
