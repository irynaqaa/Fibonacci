package com.example.iotmonitoring.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

/**
 * Service for logging alerts.
 */
@Service
public class AlertLoggingService {
    private static final Logger logger = LoggerFactory.getLogger(AlertLoggingService.class);

    /**
     * Logs the alert message.
     * @param alertMessage the alert message to log.
     */
    public void logAlert(String alertMessage) {
        logger.warn("Alert: {}", alertMessage);
    }
}