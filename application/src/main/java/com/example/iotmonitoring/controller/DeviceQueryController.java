package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.service.DeviceQueryService;
import com.example.iotmonitoring.model.Device;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

/**
 * DeviceQueryController handles API requests for querying devices.
 */
@RestController
@RequestMapping("/api/devices/query")
public class DeviceQueryController {

    private final DeviceQueryService deviceQueryService;

    @Autowired
    public DeviceQueryController(DeviceQueryService deviceQueryService) {
        this.deviceQueryService = deviceQueryService;
    }

    /**
     * Get device by ID.
     */
    @GetMapping("/{deviceId}")
    public ResponseEntity<Device> getDeviceById(@PathVariable UUID deviceId) {
        return deviceQueryService.getDeviceById(deviceId)
            .map(ResponseEntity::ok)
            .orElseGet(() -> ResponseEntity.notFound().build());
    }

    /**
     * Get all devices.
     */
    @GetMapping
    public ResponseEntity<List<Device>> getAllDevices() {
        List<Device> devices = deviceQueryService.getAllDevices();
        return ResponseEntity.ok(devices);
    }
}