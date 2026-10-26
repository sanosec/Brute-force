# LAIN SCANNER

<h3 align="center"> Rapido e indiscreto Scanner de portas escrito em Python. By: Sanosec.
<p align="center">
<img src="https://github.com/sanosec/Port-scanner/blob/gitignoreimage.png"> 
<p align="center">
  <img src="https://img.shields.io/badge/Author-Sanosec-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-darkgreen?style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python-darkcyan?style=flat-square">
</p>

***
<h3><p align="center">Disclaimer</p></h3>

<i>Any actions and or activities related to <b>Lain Scanner Port Scanner</b> is solely your responsibility. The misuse of this script can result in <b>criminal charges</b> brought against the persons in question. <b>The contributors will not be held responsible</b> in the event any criminal charges be brought against any individuals misusing this toolkit to break the law.

***

## Requirements
- python 3.10 or higher
- Install the dependency:

```bash
pip install -r requirements.txt
```

> **Note:** `pythonping` requires raw socket privileges to send ICMP packets. On Linux and macOS, run the script with `sudo`. On Windows, run your terminal as Administrator.

***

## Installation

Clone or download the repository and enter the directory:

```bash
git clone https://github.com/sanosec/Port-scanner
cd Port-scanner
```

***

## Usage

```
sudo python portscan.py -t <target> [options]
```

### Arguments

| Argument | Short | Required | Default | Description |
|---|---|---|---|---|
| `--target` | `-t` | Yes | — | Target IP address or hostname |
| `--timeout` | — | No | Auto (ping-based) | Per-port timeout in milliseconds |
| `--threads` | — | No | 30 | Number of concurrent worker threads |
| `--output` | `-o` | No | None | File path to save open ports |
| `--top-10k` | — | No | False | Scan top 10,000 ports instead of top 1,000 |

***
