package com.example.iotmonitoring.config;

import com.example.iotmonitoring.model.ThresholdRule;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.ArrayList;
import java.util.List;

/**
 * Configuration class for alerting functionality.
 */
@Configuration
public class AlertConfig {
    @Bean
    public List<ThresholdRule> thresholdRules() {
        List<ThresholdRule> rules = new ArrayList<>();
        // Add threshold rules here, e.g.,
        // rules.add(new ThresholdRule("sensor1", 100.0, ">", "Temperature exceeded 100°C"));
        return rules;
    }
}