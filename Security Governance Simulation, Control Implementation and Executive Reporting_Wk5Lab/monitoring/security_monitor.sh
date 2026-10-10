#!/bin/bash

# Security Monitoring Script

# Monitor for suspicious HTTP requests
grep -i "Content-Type.*multipart/form-data" /var/log/nginx/access.log > /tmp/suspicious_requests.log

# Monitor for database access
mysql -u root -ppassword -e "SHOW PROCESSLIST" > /tmp/database_access.log

# Check for file changes
find /var/www -type f -mtime -1 > /tmp/recent_file_changes.log

# Send alerts for suspicious activity
if [ -s /tmp/suspicious_requests.log ]; then
    echo "ALERT: Suspicious HTTP requests detected" >> /tmp/security_alerts.log
fi

if grep -q "customer_data" /tmp/database_access.log; then
    echo "ALERT: Access to customer_data database detected" >> /tmp/security_alerts.log
fi

if [ -s /tmp/recent_file_changes.log ]; then
    echo "ALERT: Recent file changes detected" >> /tmp/security_alerts.log
fi
