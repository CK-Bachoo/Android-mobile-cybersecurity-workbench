#!/data/data/com.termux/files/usr/bin/bash
echo "⚓ BUNKER WAKE WORD SETUP"
echo "Choose your personal wake word."
echo "Examples: bunker, sentinel, nighthawk, fortress, shadow"
read -p "Enter your wake word: " WAKEWORD
if [ -z "$WAKEWORD" ]; then
    WAKEWORD="bunker"
fi
sed -i '/bunker_wake/d' ~/.bashrc
echo "" >> ~/.bashrc
echo "alias ${WAKEWORD}='cd ~/Android-mobile-cybersecurity-workbench && bash scripts/bunker_wake.sh'" >> ~/.bashrc
source ~/.bashrc
echo "✅ Wake word SET: ${WAKEWORD}"
echo "Type ${WAKEWORD} in any new Termux session to wake everything."
