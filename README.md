# BitcoinRoulette

Bitcoin Roulette is a software that attempts to find Bitcoin private keys and addresses with balances by spinning. Test your luck!

Probability of Finding A Wallet with Balance is around 1/1,000,000,000,000,000,000,000,000,000,000,000,000,000,000 which mean what you are really lucky if your find one

---

## Requirements

1. **Connectivity Check**

   Ensure you have a stable internet connection by running the following command in your terminal (CMD for Windows, Terminal for macOS or Linux):

   ```sh
   ping blockchain.info
   ```

   The expected result should resemble:

   ```plaintext
   Pinging blockchain.info [xxx.xxx.xxx.xxx] with 32 bytes of data:
   Reply from xxx.xxx.xxx.xxx: bytes=32 time=184ms TTL=52
   Reply from xxx.xxx.xxx.xxx: bytes=32 time=192ms TTL=52
   Reply from xxx.xxx.xxx.xxx: bytes=32 time=181ms TTL=52
   Reply from xxx.xxx.xxx.xxx: bytes=32 time=183ms TTL=52

   Ping statistics for xxx.xxx.xxx.xxx:
       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
   Approximate round trip times in milli-seconds:
       Minimum = 181ms, Maximum = 192ms, Average = 185ms
   ```

   The packet loss rate should not exceed 25%. If it does, please verify your internet connection or consider using a VPN or proxy server if your country (e.g., CN, DPRK) has restrictions.

2. **Dependencies**

   Install the required libraries using pip:

   ```sh
   pip install bitcoin tkinter ecdsa
   ```

---

## Running the Program

You have two options to obtain the software:

1. [Download the entire program](https://github.com/HugoXOX3/BitcoinRoulette/archive/refs/heads/main.zip)

2. Download the specific version for your operating system:
   - [Windows Version](https://github.com/HugoXOX3/BitcoinRoulette/blob/main/Bitcoin_Roulette.exe)
   - [macOS and Linux Version](https://github.com/HugoXOX3/BitcoinRoulette/blob/main/main.py)

### Instructions for Running

- **macOS and Linux:**

  ```sh
  python3 main.py
  ```

- **Windows:**

  Double-click on `Bitcoin_Roulette.exe` to run the program.

---

## Cashing Out the Reward

The private keys and addresses with balances will be stored in `FoundAddress.txt`. Copy and paste the private key into a **trusted Bitcoin wallet** and transfer the balance to a trading market.

Please consider making a donation if you successfully find a balance.

**BTC Address:** `bc1qk5tpd68l4gfj6uzkq7u0l998dzvzyjpzhgpvnm`

---

Thank you for your attention!

---
