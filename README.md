# PyStressLab

PyStressLab is a powerful and flexible Python-based toolkit designed to stress test servers by simulating different types of system loads. It includes CPU-intensive tasks, memory exhaustion, disk I/O overload, network stress, and database query pressure. Each script supports command-line arguments, allowing users to dynamically adjust the load.

## Features
- CPU, Memory, Disk I/O, Network, and Database stress tests
- Multithreading and multiprocessing for maximum resource utilization
- Customizable parameters via command-line arguments
- Lightweight and easy to use
- Suitable for performance testing, benchmarking, and system resilience evaluation

## Installation
PyStressLab requires Python 3.6 or later. Clone the repository and install necessary dependencies:

```bash
git clone https://github.com/yourusername/PyStressLab.git
cd PyStressLab
pip install -r requirements.txt
```

## Usage
Run different stress tests by choosing the appropriate script:

### 1. Simple Sleep (Minimal Load)
```bash
python simple_sleep.py --seconds 100
```

### 2. Simple CPU Load (Infinite Loop)
```bash
python simple_cpu.py --seconds 10000
```

### 3. Moderate CPU Load (Factorial Calculation)
```bash
python moderate_cpu.py --num 50000
```

### 4. Heavy CPU Load (Multithreaded Prime Calculation)
```bash
python heavy_cpu.py --size 500000
```

### 5. Memory Load (Large List Allocation)
```bash
python memory_load.py --size 5000
```

### 6. High Disk I/O Load (File Write Loop)
```bash
python high_disk_io.py --filename "output.txt" --lines 500000
```

### 7. High Network Load (HTTP Requests)
```bash
python http_request.py --url "https://www.example.com" --delay 2 --count 300
```

## Contributing
Contributions are welcome! Fork the repository, make improvements, and submit a pull request.

## License
This project is licensed under the GNU License. See `LICENSE` for details.

## Disclaimer
Use PyStressLab responsibly. Running stress tests on production systems can cause instability or downtime. Always test in a controlled environment first.

---

🚀 Push your system to its limits with **PyStressLab**!

