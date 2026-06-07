#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

echo "🔧 WAKEWORD CONFIGURATION"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

read -p "Enter wake word (alphanumeric + underscore only): " WAKEWORD

if [ -z "$WAKEWORD" ]; then
    WAKEWORD="bunker"
fi

# SECURE: Input validation — only allow safe characters
if ! [[ "$WAKEWORD" =~ ^[A-Za-z0-9_]+$ ]]; then
    echo "❌ INVALID WAKE WORD!"
    echo "   Use only: letters (A-Z, a-z), numbers (0-9), underscores (_)"
    exit 1
fi

# Now safe to use — input is sanitized
sed -i '/bunker_wake/d' ~/.bashrc || true
echo "" >> ~/.bashrc
echo "alias ${WAKEWORD}='cd ~/Android-mobile-cybersecurity-workbench && bash scripts/bunker_wake.sh'" >> ~/.bashrc
source ~/.bashrc

echo "✅ ALIAS SET SUCCESSFULLY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Wake word: ${WAKEWORD}"
echo ""
echo "🚀 TYPE THIS TO WAKE BUNKER:"
echo "   ${WAKEWORD}"
