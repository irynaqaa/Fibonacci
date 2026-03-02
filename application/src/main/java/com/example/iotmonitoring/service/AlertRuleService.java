package com.example.iotmonitoring.service;

import com.example.iotmonitoring.model.AlertRule;
import com.example.iotmonitoring.repository.AlertRuleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

/**
 * Service class for managing alert rules in the IoT Monitoring System.
 */
@Service
public class AlertRuleService {
    private final AlertRuleRepository alertRuleRepository;

    @Autowired
    public AlertRuleService(AlertRuleRepository alertRuleRepository) {
        this.alertRuleRepository = alertRuleRepository;
    }

    public AlertRule createAlertRule(AlertRule alertRule) {
        return alertRuleRepository.save(alertRule);
    }

    public Optional<AlertRule> getAlertRule(UUID id) {
        return alertRuleRepository.findById(id);
    }

    public List<AlertRule> getAllAlertRules() {
        return alertRuleRepository.findAll();
    }

    public void deleteAlertRule(UUID id) {
        alertRuleRepository.deleteById(id);
    }
}
