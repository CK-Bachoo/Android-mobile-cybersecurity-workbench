#!/bin/bash
DOMAIN="http://127.0.0.1:8080"
TESTS_PASSED=0
TESTS_FAILED=0

echo "=== G0DM0D3 Purple Team Quick Test ==="

echo -n "Test 1 (Dashboard Availability): "
if curl -s -o /dev/null -w "%{http_code}" $DOMAIN | grep -q "200"; then
  echo "PASS"; ((TESTS_PASSED++))
else
  echo "FAIL (Is dashboard.py running?)"; ((TESTS_FAILED++))
fi

echo -n "Test 2 (Telemetry API): "
RESPONSE=$(curl -s "$DOMAIN/api/telemetry")
if echo "$RESPONSE" | jq . > /dev/null 2>&1; then
  COUNT=$(echo "$RESPONSE" | jq 'length')
  echo "PASS ($COUNT events)"; ((TESTS_PASSED++))
else
  echo "FAIL"; ((TESTS_FAILED++))
fi

echo -n "Test 3 (Watchdog Log Exists): "
LOG="$HOME/Project-Dreadnought/vault/logs/threat_radar.json"
if [ -f "$LOG" ] && [ -s "$LOG" ]; then
  LINES=$(wc -l < "$LOG")
  echo "PASS ($LINES log entries)"; ((TESTS_PASSED++))
else
  echo "FAIL (No log file found)"; ((TESTS_FAILED++))
fi

echo "--------------------------------------"
echo "Results: $TESTS_PASSED Passed, $TESTS_FAILED Failed"
