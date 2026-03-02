package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.model.ThresholdRule;
import com.example.iotmonitoring.service.AlertService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Controller for managing alert rules.
 */
@RestController
@RequestMapping("/api/alerts")
public class AlertController {
    private final AlertService alertService;

    @Autowired
    public AlertController(AlertService alertService) {
        this.alertService = alertService;
    }

    /**
     * Retrieves all threshold rules.
     * @return a list of threshold rules.
     */
    @GetMapping
    public ResponseEntity<List<ThresholdRule>> getAllThresholdRules() {
        List<ThresholdRule> rules = alertService.getAllThresholdRules();
        return ResponseEntity.ok(rules);
    }

    /**
     * Creates a new threshold rule.
     * @param rule the threshold rule to create.
     * @return the created threshold rule.
     */
    @PostMapping
    public ResponseEntity<ThresholdRule> createThresholdRule(@RequestBody ThresholdRule rule) {
        ThresholdRule savedRule = alertService.saveThresholdRule(rule);
        return ResponseEntity.ok(savedRule);
    }
}