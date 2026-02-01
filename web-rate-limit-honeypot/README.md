# Rate Limiting + Honeypot Decoy Paths

## Goal
Implement defensive controls in a simple python HTTP server:
- Temporary IP bans after request bursts
- Decoy/honeypot endpoints that log access attempts

## Environment
- Target: Raspberry Pi (python HTTP server)
- Attacker: Kali Linux (curl loops)

## What I Built
- Rate limiting (429)
- Temporary bans (403)
- Decoy paths like '/.decoy/' that get logged

## What I Learned
Defensive controls can be added even to lightweight services, and logging "weird" paths is a strong early signal of malicius activity.
