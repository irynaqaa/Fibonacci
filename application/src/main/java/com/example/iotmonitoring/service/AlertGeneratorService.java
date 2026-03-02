package com.example.iotmonitoring.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Map;

/**
 * Service for generating alerts based on sensor data.
 */
@Service
public class AlertGeneratorService {
    private final AlertGenerator alertGenerator;

    @Autowired
    public AlertGeneratorService(AlertGenerator alertGenerator) {
        this.alertGenerator = alertGenerator;
    }

    /**
     * Processes incoming sensor data and generates alerts if necessary.
     * @param sensorData the incoming sensor data.
     * @return an alert message if a rule is violated, otherwise null.
     */
    public String processSensorData(Map<String, Object> sensorData) {
        return alertGenerator.generateAlert(sensorData).orElse(null);
    }
}