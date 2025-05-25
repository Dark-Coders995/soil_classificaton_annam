#!/bin/bash

# -------------------------------------------------------------------------------
# Download Kaggle Competition Dataset (Hardcoded Competition)
# 
# Usage:
#   ./download.sh
# 
# Dataset will be saved to: data/dataset/
# -------------------------------------------------------------------------------

# Exit on error and undefined variables
set -eu

# Hardcoded competition name (replace with your competition name)
COMPETITION="soil-classification-part-2"

# Path configuration
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"  # Script location
TARGET_DIR="${SCRIPT_DIR}/dataset"                              # Output directory
KAGGLE_DIR="${HOME}/.kaggle"                                    # Kaggle config directory

# First-time setup check
setup_kaggle() {
  # Create .kaggle directory if it doesn't exist
  mkdir -p "${KAGGLE_DIR}"
  
  # Check for kaggle.json in common locations
  if [ ! -f "${KAGGLE_DIR}/kaggle.json" ]; then
    echo "Kaggle API token not found. Checking Downloads folder..."
    
    if [ -f "${HOME}/Downloads/kaggle.json" ]; then
      echo "Found kaggle.json in Downloads. Configuring..."
      mv "${HOME}/Downloads/kaggle.json" "${KAGGLE_DIR}/"
      chmod 600 "${KAGGLE_DIR}/kaggle.json"
    else
      echo "ERROR: kaggle.json not found. Please:"
      echo "1. Go to https://www.kaggle.com/settings/account"
      echo "2. Click 'Create New API Token' to download kaggle.json"
      echo "3. Save it to your Downloads folder and run this script again"
      exit 1
    fi
  fi

  # Verify Kaggle CLI installation
  if ! command -v kaggle &> /dev/null; then
    echo "Installing Kaggle CLI..."
    pip install --user kaggle
    export PATH="${HOME}/.local/bin:${PATH}"
  fi
}

# Main download function
download_dataset() {
  echo "Downloading ${COMPETITION} dataset..."
  mkdir -p "${TARGET_DIR}"
  
  kaggle competitions download -c "${COMPETITION}" -p "${TARGET_DIR}"
  unzip -q "${TARGET_DIR}/${COMPETITION}.zip" -d "${TARGET_DIR}"
  rm "${TARGET_DIR}/${COMPETITION}.zip"
}

# Run the full workflow
setup_kaggle
download_dataset

echo "✅ Dataset downloaded to: ${TARGET_DIR}"