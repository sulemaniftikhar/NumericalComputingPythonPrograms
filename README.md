# Numerical Computing Assignment

This repository contains solutions to **Assignment #1** for the **Numerical Computing** course (Spring 2024). The assignment focuses on implementing computational methods such as root-finding, solving ordinary differential equations (ODEs), and data interpolation.

---

## 📑 Contents

### Part 1: Differential Equations and Numerical Methods
1. **Newton-Raphson Method**  
   - Implementation of the Newton-Raphson method to solve algebraic and transcendental equations.
   - Demonstration with an example to find all roots of a selected equation.

2. **Solving an ODE**  
   - Finding the **exact solution**.
   - Solving numerically using:
     - **Euler's method**.
     - **Runge-Kutta (RK) method of order 4**.
   - Extracting, interpolating, and visualizing the data solutions.

3. **System of First-Order ODEs**  
   - Code implementation of the RK method (order 4) to solve a system of first-order ODEs.

4. **Second-Order ODE**  
   - Solution of a second-order ODE using the RK method (order 4).

### Part 2: Interpolation and System of Equations
1. **Data Interpolation**  
   - Perform cubic spline interpolation on the data provided in `bps.dat`.
   - Plot the interpolated results for visualization.

2. **Explicit Solution for a System of Equations**  
   - Derive analytical expressions for \(x\), \(y\), and \(z\) from a given system of equations.

3. **Population Estimation**  
   - Use **Newton's Backward Interpolation Formula** to estimate population growth for given census data.

---

## 📂 Files in the Repository
- **`solutions.py`**: Python script containing implementations of all required numerical methods and visualization.
- **`bps.dat`**: Input dataset for interpolation tasks.
- **Sample Questions**: Embedded as comments at the end of `solutions.py`.

---

## 🚀 How to Run

1. **Install Dependencies**

   Ensure you have the required Python libraries installed:
   
   

## 🏃‍♂️‍➡️ Run the Code

   Execute the script to see results:

   ```bash
   python solutions.py

