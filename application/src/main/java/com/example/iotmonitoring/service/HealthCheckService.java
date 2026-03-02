package com.example.iotmonitoring.service;

import org.springframework.stereotype.Service;

/**
 * HealthCheckService provides methods to check the health of the system.
 */
@Service
public class HealthCheckService {

    /**
     * Check the health status of the system.
     */
    public String checkHealth() {
        return "System is healthy";
    }
}