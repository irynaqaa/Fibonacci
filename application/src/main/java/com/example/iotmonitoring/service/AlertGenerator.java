package com.example.iotmonitoring.service;

import com.example.iotmonitoring.model.ThresholdRule;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;
import java.util.Optional;

/**
 * Service for generating alerts based on threshold rules.
 */
@Service
public class AlertGenerator {
    private static final Logger logger = LoggerFactory.getLogger(AlertGenerator.class);

    private final List<ThresholdRule> thresholdRules;

    public AlertGenerator(List<ThresholdRule> thresholdRules) {
        this.thresholdRules = thresholdRules;
    }

    /**
     * Generates an alert if any threshold rule is violated.
     * @param sensorData the sensor data to check against the rules.
     * @return an alert message if a rule is violated, otherwise null.
     */
    public Optional<String> generateAlert(Map<String, Object> sensorData) {
        for (ThresholdRule rule : thresholdRules) {
            if (isThresholdViolated(rule, sensorData)) {
                String alertMessage = rule.getAlertMessage();
                logger.warn("Alert generated: {}", alertMessage);
                return Optional.of(alertMessage);
            }
        }
        return Optional.empty();
    }

    /**
     * Checks if the threshold rule is violated based on the sensor data.
     * @param rule the threshold rule to check.
     * @param sensorData the sensor data to check against the rule.
     * @return true if the threshold is violated, false otherwise.
     */
    private boolean isThresholdViolated(ThresholdRule rule, Map<String, Object> sensorData) {
        String sensorId = rule.getSensorId();
        if (sensorData.containsKey(sensorId)) {
            double sensorValue = (double) sensorData.get(sensorId);
            switch (rule.getComparisonOperator()) {
                case ">":
                    return sensorValue > rule.getThresholdValue();
                case "<":
                    return sensorValue < rule.getThresholdValue();
                case "==":
                    return sensorValue == rule.getThresholdValue();
                default:
                    return false;
            }
        }
        return false;
    }
}