package com.example.iotmonitoring.service;

import org.springframework.stereotype.Service;

/**
 * Service for sending alert notifications.
 */
@Service
public class AlertNotificationService {
    /**
     * Sends an alert notification.
     * @param alertMessage the alert message to send.
     */
    public void sendAlertNotification(String alertMessage) {
        // Implementation for sending notifications (e.g., email, SMS, etc.)
    }
}