#!/usr/bin/env bash
#
# Generate PDF

# Header
echo "Creating a PDF... if this fails check out the documentation at: https://toolchain.gitbook.com/ebook.html"

# NPM Install
npm install -g gitbook-cli svgexport

# Load the error code
ERROR_CODE=$?

# Check the shell for errors
if [ $ERROR_CODE -ne 0 ]; then
  echo "ERROR! Failed to run npm install"
  exit 1
fi

# Copy the files
cp readme/_sidebar.md readme/SUMMARY.md

# Load the error code
ERROR_CODE=$?

# Check the shell for errors
if [ $ERROR_CODE -ne 0 ]; then
  echo "ERROR! Failed to run cp"
  exit 1
fi

# Run the gitbook
gitbook pdf readme/ readme/book.pdf

# Load the error code
ERROR_CODE=$?

# Check the shell for errors
if [ $ERROR_CODE -ne 0 ]; then
  echo "ERROR! Failed to run gitbook"
  exit 1
fi

# Remove dead file
rm readme/SUMMARY.md

# Load the error code
ERROR_CODE=$?

# Check the shell for errors
if [ $ERROR_CODE -ne 0 ]; then
  echo "ERROR! Failed to run rm"
  exit 1
fi

# Footer
echo "Your PDF is at readme/book.pdf. Commit it to your repo if you'd like to."
