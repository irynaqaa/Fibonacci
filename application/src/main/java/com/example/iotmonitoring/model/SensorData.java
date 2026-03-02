package com.example.iotmonitoring.model;

import javax.persistence.*;
import java.util.UUID;
import java.time.LocalDateTime;

/**
 * Entity representing sensor data associated with a device.
 */
@Entity
@Table(name = "sensor_data")
public class SensorData {
    @Id
    @GeneratedValue
    private UUID id;

    @Column(name = "device_id")
    private UUID deviceId;
    private LocalDateTime timestamp;
    private String data;
    private LocalDateTime createdAt;

    // Getters and Setters
    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public UUID getDeviceId() {
        return deviceId;
    }

    public void setDeviceId(UUID deviceId) {
        this.deviceId = deviceId;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDateTime timestamp) {
        this.timestamp = timestamp;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }
}
