package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.model.SensorData;
import com.example.iotmonitoring.service.SensorDataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.UUID;

/**
 * REST controller for managing sensor data.
 */
@RestController
@RequestMapping("/api/sensor-data")
public class SensorDataController {
    private final SensorDataService sensorDataService;

    @Autowired
    public SensorDataController(SensorDataService sensorDataService) {
        this.sensorDataService = sensorDataService;
    }

    @PostMapping
    public ResponseEntity<SensorData> createSensorData(@RequestBody SensorData sensorData) {
        SensorData createdData = sensorDataService.createSensorData(sensorData);
        return ResponseEntity.ok(createdData);
    }

    @GetMapping("/{id}")
    public ResponseEntity<SensorData> getSensorData(@PathVariable UUID id) {
        return sensorDataService.getSensorData(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping
    public ResponseEntity<List<SensorData>> getAllSensorData() {
        List<SensorData> sensorDataList = sensorDataService.getAllSensorData();
        return ResponseEntity.ok(sensorDataList);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteSensorData(@PathVariable UUID id) {
        sensorDataService.deleteSensorData(id);
        return ResponseEntity.noContent().build();
    }
}
