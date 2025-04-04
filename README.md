# Smartphone-Suggestion-System-Python-MySQL
The Smartphone Database Management System is a Python-MySQL-based project designed to manage and analyse smartphone data efficiently. It provides a centralized database containing essential details like brand, model, price, specifications, and ratings. 
The system includes two interfaces: an administrator section for performing CRUD (create, read, update, and delete) operations and a viewer section for filtering and sorting smartphones based on user-defined preferences such as budget, processor brand, or smartphone brand. 
This project demonstrates practical applications of database management, modular programming, and user interface design. It is a functional tool for users to make informed decisions and for administrators to maintain accurate and updated records.


## Input Requirements:
1.	 Administrator Inputs:
•	Smartphone details such as brand, model, price, specifications (processor, RAM, storage, etc.), and ratings.
•	Options for modifying or deleting existing records.
•	Viewer requests for additional data or features.

2.	 Viewer Inputs:
•	Preferences such as budget range, brand, processor type, or specific features (e.g., 5G support).
•	Requests for information on unavailable models or data.

## Output Requirements:
1.	 For Administrators:
•	Confirmation messages for successful additions, updates, or deletions of records.
•	Viewer request logs for analysis and action.
•	The complete list of stored smartphone data for review.

2.	 For Viewers:
•	A filtered and sorted list of smartphones based on selected preferences.
•	Suggestions matching their input criteria (e.g., affordable smartphones with 5G).
•	Notifications for successfully submitted data requests.


## HARDWARE/SOFTWARE REQUIREMENTS
1.	 Hardware Requirements:
•	Processor: Intel Core i3 or higher.
•	RAM: Minimum 4 GB (8 GB recommended).
•	Storage: At least 10 GB free space.
•	Display: Standard monitor with 1366x768 resolution or higher.
•	Peripherals: Keyboard and mouse for input.
2.	 Software Requirements:
•	Operating System: Windows 10/11, Linux, or macOS.
•	Programming Language: Python (v3.9).
•	Database: MySQL Community Server (v8).
•	Text Editor/IDE: Visual Studio Code.
•	Python Libraries:
	mysql.connector for database connectivity.
	pickle for request handling.
	os for file operations.


## DATABASE DICTIONARY

### Field Name, Data Type, Description
brand_name,	VARCHAR(30),	Stores the brand name of the smartphone
model,	VARCHAR(50),	Stores the name of the model of the smartphone.
price,	INT,	Stores the price of the smartphone in INR.
rating,	INT,	Stores the rating of the smartphone (out of 100)
has_5g, VARCHAR(5),	Indicates if the smartphone supports 5G (TRUE/FALSE).
has_nfc,	VARCHAR(5),		Indicates if the smartphone supports NFC (TRUE/FALSE).
processor_name,	VARCHAR(30),	Stores the name of the processor used in the smartphone.
processor_brand,	VARCHAR(30),	Stores the brand of the processor used in the smartphone. 
num_cores,	INT,	Stores the number of cores in the smartphone processor.
battery_capacity,	INT,	Stores the battery capacity of the smartphone (in mAh).
ram_capacity,	INT,	Stores the RAM capacity of the smartphone (in GB).
internal_memory, INT,	Stores the internal storage capacity (in GB).
refresh_rate,	INT,	Stores the display refresh rate (in Hz).
primary_camera_rear, INT,	Stores the resolution of the primary rear camera (in MP).
primary_camera_front,	INT,	Stores the resolution of the primary front camera (in MP).


