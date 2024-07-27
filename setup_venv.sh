#!/usr/bin/env bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo_info() {
    echo -e "${GREEN}info${NC}: $1"
}

echo_error() {
    echo -e "${RED}error${NC}: $1"
}

# Check if python3 is installed
if ! command -v python3 &>/dev/null; then
    echo_error "python3 is not installed"
    exit 1
fi

echo_info "creating virtual environment"
python3 -m venv venv

# Activate the virtual environment
echo_info "activating venv"
source venv/bin/activate

# Upgrade pip
echo_info "upgrading pip"
pip install --upgrade pip

# Install dependencies
echo_info "installing pygame-ce"
pip install pygame-ce

# Deactivate the virtual environment
deactivate

echo_info "setup complete"
