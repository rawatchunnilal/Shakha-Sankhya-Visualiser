### README: Sankhya Visualizer

#### Overview

The Sankhya Visualizer is a tool designed to analyze and visualize daily attendance (Sankhya) data from your Shakha's WhatsApp group chat. It reads a WhatsApp chat export file, processes the messages, and generates a line graph to help you track attendance trends over time.

#### Features

- **Message Parsing**: Extracts and processes messages from the WhatsApp chat file.
- **Date and Time Handling**: Converts message timestamps to a standard format.
- **Attendance Analysis**: Identifies and aggregates attendance data.
- **Visualization**: Displays attendance trends using a line graph.

#### Requirements

- Jupyter Lab

#### Usage

1. **Export WhatsApp Chat Data**:
   - Open WhatsApp on your mobile device.
   - Navigate to the group chat whose attendance data you want to analyze.
   - Export the chat history as a text file. Choose the option to export without media for easier processing.

2. **Format of WhatsApp Chat Export**:
   - The exported chat file should be in a text format (`WhatsApp Chat with [Group Name].txt`).
   - Each attendance entry should follow a standard format, typically structured as:
     ```
     गणेश नगर स्याम शाखा 
     आज की संख्या 
     - शिशु: 6
     - बाल: 10
     - तरुण: 6
     कुल: 22
     अभ्यागत श्री विवेक जी सावरकर, बौद्धिक प्रमुख, नगर
     ```
     Replace numbers (`6`, `10`, `22`, etc.) with actual attendance figures.

3. **Open Jupyter Lab**:
   - Launch Jupyter Lab on your system.

4. **Run the Notebook**:
   - Open the provided Jupyter Notebook (`Sankhya_Visualizer.ipynb`).
   - Execute the cells in the notebook to parse the chat file and generate the attendance graph.

5. **View the Graph**:
   - The notebook will display a line graph showing daily attendance trends.

#### Notes

- Ensure the WhatsApp chat file (`WhatsApp Chat with [Group Name].txt`) is accessible to the Jupyter Notebook for processing.
- Customize the parsing and visualization logic in the notebook as per specific requirements or variations in the chat data format.

This README provides a structured guide to utilizing the Sankhya Visualizer tool in Jupyter Lab for analyzing and visualizing attendance data from WhatsApp group chats.
