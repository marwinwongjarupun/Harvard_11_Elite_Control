import serial
import time

# Configure serial connection
ser = serial.Serial(
    port='COM11',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS,
    timeout=1  # Optional: Set a timeout for reading
)

# Check if the serial port is open
if not ser.isOpen():
    ser.open()

# Initial command to run the pump (if necessary)
input_command = 'run'
ser.write((input_command + '\r\n').encode())
time.sleep(1)  # Wait for a moment for the command to be processed

# Read any response from the initial command
out = b''
while ser.inWaiting() > 0:
    out += ser.read(1)
if out:
    print(out.decode())

# Command to infuse a small volume (e.g., 0.1 ul/min)
move_command = 'irat 1 ml/min'  # Adjust '12' to your pump address if needed
ser.write((move_command + '\r\n').encode())
time.sleep(1)  # Wait for a moment for the command to be processed



# Read and print any response from the pump regarding the move command
out = b''  # Reset output for new read
while ser.inWaiting() > 0:
    out += ser.read(1)
if out:
    print(out.decode())  # Decode bytes to string for printing

# Close the serial connection
ser.close()
