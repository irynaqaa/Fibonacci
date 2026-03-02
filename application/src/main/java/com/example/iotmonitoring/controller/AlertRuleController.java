package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.model.AlertRule;
import com.example.iotmonitoring.service.AlertRuleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.UUID;

/**
 * REST controller for managing alert rules.
 */
@RestController
@RequestMapping("/api/alert-rules")
public class AlertRuleController {
    private final AlertRuleService alertRuleService;

    @Autowired
    public AlertRuleController(AlertRuleService alertRuleService) {
        this.alertRuleService = alertRuleService;
    }

    @PostMapping
    public ResponseEntity<AlertRule> createAlertRule(@RequestBody AlertRule alertRule) {
        AlertRule createdRule = alertRuleService.createAlertRule(alertRule);
        return ResponseEntity.ok(createdRule);
    }

    @GetMapping("/{id}")
    public ResponseEntity<AlertRule> getAlertRule(@PathVariable UUID id) {
        return alertRuleService.getAlertRule(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping
    public ResponseEntity<List<AlertRule>> getAllAlertRules() {
        List<AlertRule> alertRules = alertRuleService.getAllAlertRules();
        return ResponseEntity.ok(alertRules);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteAlertRule(@PathVariable UUID id) {
        alertRuleService.deleteAlertRule(id);
        return ResponseEntity.noContent().build();
    }
}
