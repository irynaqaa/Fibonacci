package com.example.iotmonitoring.service;

import com.example.iotmonitoring.model.ThresholdRule;
import com.example.iotmonitoring.repository.AlertRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Service for managing alert rules.
 */
@Service
public class AlertService {
    private final AlertRepository alertRepository;

    @Autowired
    public AlertService(AlertRepository alertRepository) {
        this.alertRepository = alertRepository;
    }

    /**
     * Retrieves all threshold rules from the database.
     * @return a list of threshold rules.
     */
    public List<ThresholdRule> getAllThresholdRules() {
        return alertRepository.findAll();
    }

    /**
     * Saves a new threshold rule to the database.
     * @param rule the threshold rule to save.
     * @return the saved threshold rule.
     */
    public ThresholdRule saveThresholdRule(ThresholdRule rule) {
        return alertRepository.save(rule);
    }
}