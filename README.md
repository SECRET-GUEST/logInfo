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

ndler for Python applications. It provides comprehensive error logging features, including logging to files and console output. The module comes in 3 versions: one without email notification support and another one with email notification support for critical errors, and a last one displaying errors pop ups.

# 🔑 Key Features

- 📄 Log messages to files with customizable log file names.
- 🖥️ Display log messages in the console.
- 📧 (Optional) Send email notifications for critical errors (available in the version with email support).
- 💡 Easily configurable and importable in your Python projects.
- 📈 Filter log messages based on severity levels.
- 💬 Pop ups handled by QMessageBox.



# 🛠️ Usage

   1. Import the `logInfo.py` file in your Python project:

```python
   from logInfo import configLogs
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
 
   4 . Use the msgLog logger to display message in your application : 
  
   - In main page :

```python
 from msgLog import configLogs
 from Application import YourApplication
 
 logger = configLogs("MyApplication", "my_application.log", use_qt_dialogs=True)
 autoclicker = YourApplication(logger)
  ```
 
 
 
   - in sub pages : 
    
 ```python
 class YourApplication:
     def __init__(self, logger):  # Don't forget to add the logger here
         self.logger = logger
 
 
 def launch_script(self):
     try:
          
         # ... your code ...
 
     except Exception as e:
         self.logger.error(f"Error: {e}")
  ```
  
   5 . Use the log info with custom message box script :
   
As before, you have to import the system in your main page, then you can use it into your subclass by this way : 


```python
 class YourAPPLICATION(QWidget):
     def __init__(self, logger): #Don't forget to add logger at arguments
         super().__init__()
 
         # Error handler
         self.logger = logger
 
         # ...


   def some_method(self):

       # Use the logger to show a custom message box from msgbox handler

       self.logger.show_message_box(self, "I HAVE A BULLET FOR YOU", self.sacrifice_all)

        # Or for display error messages
         try:
             # Some code that might raise an exception
             pass

         except Exception as e:
             # Log the exception
             self.logger.exception("An error occured : %s", str(e))
 
             # Use the logger to show a custom error message box
             self.logger.show_error_box(self, f"Une erreur s'est produite : {str(e)}")
   
```

A better example would be to watch the code in on of my application using it, you can find one here  :

https://github.com/SECRET-GUEST/autoclicker
  
  
## :scroll: License

This repository is released under the [MIT License](LICENSE). Please see the `LICENSE` file for more information.


## :question: Support & Questions

If you have any questions or need support, please feel free to open an issue or join my twitter.


