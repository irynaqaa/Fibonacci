package com.example.iotmonitoring.service;

import com.example.iotmonitoring.model.ThresholdRule;
import com.example.iotmonitoring.repository.AlertRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

/**
 * Unit tests for the AlertService class.
 */
class AlertServiceTest {

    @Mock
    private AlertRepository alertRepository;

    @InjectMocks
    private AlertService alertService;

    /**
     * Set up the test environment before each test.
     */
    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    /**
     * Test retrieving all threshold rules.
     */
    @Test
    void testGetAllThresholdRules() {
        // Arrange
        ThresholdRule rule1 = new ThresholdRule("sensor1", 100.0, ">", "High temperature");
        ThresholdRule rule2 = new ThresholdRule("sensor2", 50.0, "<", "Low temperature");
        when(alertRepository.findAll()).thenReturn(Arrays.asList(rule1, rule2));

        // Act
        List<ThresholdRule> rules = alertService.getAllThresholdRules();

        // Assert
        assertEquals(2, rules.size());
        assertEquals(rule1, rules.get(0));
        assertEquals(rule2, rules.get(1));
    }

    /**
     * Test saving a new threshold rule.
     */
    @Test
    void testSaveThresholdRule() {
        // Arrange
        ThresholdRule rule = new ThresholdRule("sensor1", 100.0, ">", "High temperature");
        when(alertRepository.save(rule)).thenReturn(rule);

        // Act
        ThresholdRule savedRule = alertService.saveThresholdRule(rule);

        // Assert
        assertNotNull(savedRule);
        assertEquals("sensor1", savedRule.getSensorId());
        assertEquals(100.0, savedRule.getThresholdValue());
    }
}