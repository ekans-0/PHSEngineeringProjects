# Falconia Rover Project

## 🌍 About Falconia
**Falconia** is a **transdisciplinary project** that combines concepts from **Earth-Space Systems, Computer Science, and Engineering**. Students work in small groups to **design, build, and test** a rover capable of exploring the newly discovered planet **Falconia**. 

### 🔍 Concepts Covered:
- **Computer-Aided Drawing (CAD)**
- **Journaling & Documentation**
- **Decision-Making in Engineering**
- **Oral Presentation & Report Writing**
- **Embedded Systems & Sensor Integration**

## 🎯 Mission Objective
The **Falconia Rover** will explore the volcanic terrain of Falconia, collecting data on:
- **Temperature & Humidity**
- **Gyroscope & Motion (Rotation, Acceleration)**
- **Gas Emissions & Atmospheric Composition**

This data will help researchers understand volcanic processes, internal heating, and how geological activity affects Falconia’s atmosphere and potential habitability.

## 🔧 Engineering Design
### **Key Features**
1. **Multi-Terrain Rover** powered by **Raspberry Pi**
2. **1:5 Gear Ratio** for efficient movement
3. **Four 8-diameter wheels** for stability
4. **Rectangular chassis:** 15cm x 6.4cm x 1.6cm
5. **Two LEGO motors** for movement
6. **Servo-controlled camera** for capturing images
7. **Ultrasonic Sensor** for obstacle detection
8. **Gyroscope & Accelerometer** for navigation
9. **Humiture & Gas Sensors** for environmental analysis
10. **Hall Sensor** for magnetic field detection & motor speed monitoring

### ⚙️ **Component Placement**
- **Camera:** Mounted on top with a rotating servo
- **Ultrasonic Sensor:** Front-mounted for obstacle detection
- **Gyroscope:** Centered for balance and motion sensing
- **Humiture & Gas Sensors:** Front-facing, angled downward for volcano analysis
- **Hall Sensor:** Near the motor, measuring speed & magnetic field variations

## 📏 Rules and Constraints
- Must traverse Falconia’s volcanic terrain
- Must successfully climb the volcano
- Must maintain structural integrity throughout the mission
- Must collect data from **at least two points** on Falconia
- **2-week design timeframe**
- **Limited supply of LEGO parts** (only 2 LEGO motors available)

## 📂 Repository Structure
```
Falconia/
├── camera.py         # Camera control for image capture
├── controlpanel.py   # Main control interface for the rover
├── electro.py        # Hall sensor integration for magnetic field detection
├── gas.py            # Gas sensor data collection
├── gyroaccel.py      # Gyroscope & accelerometer control
├── humiture.py       # Humidity and temperature sensor
├── motor.py          # Motor control and movement logic
├── sensor.py         # General sensor integration
├── README.md         # Project documentation
├── Data/             # Project data, collected into CSV files, stored seperately
└── __pycache__/      # Cached Python files
```

## 🛠️ How to Run the Code
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/ekans-0/PHSEngineeringProjects.git
   cd Falconia
   ```
2. **Set Up the Python Environment:**
   ```sh
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt  # If a requirements file is available
   ```
4. **Run the Rover Code:**
   ```sh
   python3 controlpanel.py
   ```

## 🚀 Future Enhancements
- Improve **obstacle detection accuracy**
- Optimize **power efficiency** for extended missions
- Expand sensor suite for additional environmental monitoring
- Completely autonomize the rover for **complete** control **hands-off**, with __adaptive sensor detection__


