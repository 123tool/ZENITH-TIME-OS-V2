#!/bin/bash
# Warna
R='\033[0;31m' G='\033[0;32m' Y='\033[1;33m' B='\033[0;34m' NC='\033[0m'
echo -e "${B}╔══════════════════════════════╗${NC}"
echo -e "${B}║   TERMINAL TOOLS SUITE      ║${NC}"
echo -e "${B}║   FULLSCREEN EDITION        ║${NC}"
echo -e "${B}╚══════════════════════════════╝${NC}"
echo -e "${Y}[...] Detecting OS...${NC}"
sleep 0.5
if [[ "$OSTYPE" == "linux-android"* ]]; then
    echo -e "${G}[✓] Termux detected${NC}"
    pkg update -y && pkg install python -y
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo -e "${G}[✓] Linux detected${NC}"
    sudo apt update && sudo apt install python3 python3-pip -y
elif [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "cygwin"* ]]; then
    echo -e "${G}[✓] Windows (MSYS) detected${NC}"
    # Biarkan user menginstall Python sendiri
else
    echo -e "${R}[!] OS tidak dikenali, lanjutkan dengan asumsi Python tersedia${NC}"
fi
echo -e "${Y}[...] Installing dependencies...${NC}"
pip install -r requirements.txt
echo -e "${G}[✓] Instalasi selesai. Jalankan: bash start.sh${NC}"
