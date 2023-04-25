Python 3.10
```
███████╗██████╗ ██████╗  ██████╗ ██████╗ ███████╗    ██╗  ██╗ █████╗ ███╗   ██╗██████╗ ██╗     ███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝    ██║  ██║██╔══██╗████╗  ██║██╔══██╗██║     ██╔════╝██╔══██╗
█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝███████╗    ███████║███████║██╔██╗ ██║██║  ██║██║     █████╗  ██████╔╝
██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗╚════██║    ██╔══██║██╔══██║██║╚██╗██║██║  ██║██║     ██╔══╝  ██╔══██╗
███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║███████║    ██║  ██║██║  ██║██║ ╚████║██████╔╝███████╗███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                               
```
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Logging](https://img.shields.io/badge/Logging-Enhanced-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

# 📝 Description

This module is an enhanced error handler for Python applications. It provides comprehensive error logging and handling features, including logging to files, console output, and sending critical error notifications via email.

# 🔑 Key Features

- 📄 Log messages to files with customizable log file names.
- 🖥️ Display log messages in the console.
- 📧 Send email notifications for critical errors.
- 💡 Easily configurable and importable in your Python projects.
- 📈 Filter log messages based on severity levels.

# 🛠️ Usage

1. Import the `logInfo.py` file in your Python project:

   ```python
   from error_handler import configure_logger
```

2. Create a logger instance using the configure_logger function:

   ```python
email_config = {
    "from_email": "your-email@example.com",
    "to_email": "recipient@example.com",
    "email_password": "your-email-password",
    "smtp_server": "smtp.example.com",
    "smtp_port": 465
}

logger = configure_logger("LoggerName", "log_file.log", email_config=email_config)

   ```
   3. Use the logger to record messages based on the error level:
      
 ```python
logger.debug("Debug level message")
logger.info("Info level message")
logger.warning("Warning level message")
logger.error("Error level message")
logger.critical("Critical level message")


   ```
   
# License

This program is licensed under the MIT license, which means you can use, modify, and distribute it freely, as long as you mention the original author and include a copy of the license. See the LICENSE.md file for more information.