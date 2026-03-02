package com.example.iotmonitoring.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.ResponseEntity;

/**
 * HealthCheckController handles health check requests for the system.
 */
@RestController
public class HealthCheckController {

    /**
     * Check the health status of the system.
     */
    @GetMapping("/health")
    public ResponseEntity<String> healthCheck() {
        return ResponseEntity.ok("System is healthy");
    }
}