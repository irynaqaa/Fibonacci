package com.example.iotmonitoring.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Positive;
import java.util.Objects;

/**
 * Represents a threshold rule for alert generation based on sensor data.
 */
public class ThresholdRule {
    @NotNull
    private String sensorId;

    @Positive
    private double thresholdValue;

    @NotNull
    private String comparisonOperator;

    @NotNull
    private String alertMessage;

    public ThresholdRule(String sensorId, double thresholdValue, String comparisonOperator, String alertMessage) {
        this.sensorId = sensorId;
        this.thresholdValue = thresholdValue;
        this.comparisonOperator = comparisonOperator;
        this.alertMessage = alertMessage;
    }

    // Getters and Setters
    @JsonProperty
    public String getSensorId() {
        return sensorId;
    }

    public void setSensorId(String sensorId) {
        this.sensorId = sensorId;
    }

    @JsonProperty
    public double getThresholdValue() {
        return thresholdValue;
    }

    public void setThresholdValue(double thresholdValue) {
        this.thresholdValue = thresholdValue;
    }

    @JsonProperty
    public String getComparisonOperator() {
        return comparisonOperator;
    }

    public void setComparisonOperator(String comparisonOperator) {
        this.comparisonOperator = comparisonOperator;
    }

    @JsonProperty
    public String getAlertMessage() {
        return alertMessage;
    }

    public void setAlertMessage(String alertMessage) {
        this.alertMessage = alertMessage;
    }

    /**
     * Validates the threshold rule parameters.
     * @return true if valid, false otherwise.
     */
    public boolean isValid() {
        return sensorId != null && !sensorId.isEmpty() && thresholdValue > 0 &&
               (comparisonOperator.equals(">") || comparisonOperator.equals("<") || comparisonOperator.equals("=="));
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof ThresholdRule)) return false;
        ThresholdRule that = (ThresholdRule) o;
        return Double.compare(that.thresholdValue, thresholdValue) == 0 &&
               Objects.equals(sensorId, that.sensorId) &&
               Objects.equals(comparisonOperator, that.comparisonOperator) &&
               Objects.equals(alertMessage, that.alertMessage);
    }

    @Override
    public int hashCode() {
        return Objects.hash(sensorId, thresholdValue, comparisonOperator, alertMessage);
    }
}