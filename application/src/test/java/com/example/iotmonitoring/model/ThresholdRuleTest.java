package com.example.iotmonitoring.model;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Unit tests for the ThresholdRule class.
 */
class ThresholdRuleTest {

    /**
     * Test valid threshold rule.
     */
    @Test
    void testValidThresholdRule() {
        ThresholdRule rule = new ThresholdRule("sensor1", 100.0, ">", "High temperature");
        assertTrue(rule.isValid());
    }

    /**
     * Test invalid threshold rule with empty sensor ID.
     */
    @Test
    void testInvalidThresholdRuleEmptySensorId() {
        ThresholdRule rule = new ThresholdRule("", 100.0, ">", "High temperature");
        assertFalse(rule.isValid());
    }

    /**
     * Test invalid threshold rule with negative threshold value.
     */
    @Test
    void testInvalidThresholdRuleNegativeThreshold() {
        ThresholdRule rule = new ThresholdRule("sensor1", -10.0, ">", "High temperature");
        assertFalse(rule.isValid());
    }

    /**
     * Test invalid threshold rule with invalid comparison operator.
     */
    @Test
    void testInvalidThresholdRuleInvalidOperator() {
        ThresholdRule rule = new ThresholdRule("sensor1", 100.0, "!=", "High temperature");
        assertFalse(rule.isValid());
    }
}
