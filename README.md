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

### CPU Load Test
```bash
python cpu_stress.py --iterations 1000000
```

### Memory Load Test
```bash
python memory_stress.py --size 5000000
```

### Disk I/O Load Test
```bash
python disk_stress.py --filename "output.txt" --lines 500000
```

### Network Load Test
```bash
python network_stress.py --url "https://www.example.com"
```

### Database Load Test
```bash
python db_stress.py --dbname test --user username --password secret --table test_table
```

## Contributing
Contributions are welcome! Fork the repository, make improvements, and submit a pull request.

## License
This project is licensed under the GNU License. See `LICENSE` for details.

## Disclaimer
Use PyStressLab responsibly. Running stress tests on production systems can cause instability or downtime. Always test in a controlled environment first.

---

🚀 Push your system to its limits with **PyStressLab**!

