package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.model.DeviceMetadata;
import com.example.iotmonitoring.service.DeviceMetadataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

/**
 * DeviceMetadataController handles API requests for device metadata.
 */
@RestController
@RequestMapping("/api/devices")
public class DeviceMetadataController {

    private final DeviceMetadataService deviceMetadataService;

    @Autowired
    public DeviceMetadataController(DeviceMetadataService deviceMetadataService) {
        this.deviceMetadataService = deviceMetadataService;
    }

    /**
     * Register a new device.
     */
    @PostMapping
    public ResponseEntity<DeviceMetadata> registerDevice(@RequestBody DeviceMetadata deviceMetadata) {
        DeviceMetadata savedDevice = deviceMetadataService.registerDevice(deviceMetadata);
        return new ResponseEntity<>(savedDevice, HttpStatus.CREATED);
    }

    /**
     * Update existing device.
     */
    @PutMapping("/{deviceId}")
    public ResponseEntity<DeviceMetadata> updateDevice(@PathVariable String deviceId, @RequestBody DeviceMetadata deviceMetadata) {
        deviceMetadata.setDeviceId(deviceId);
        DeviceMetadata updatedDevice = deviceMetadataService.updateDevice(deviceMetadata);
        return new ResponseEntity<>(updatedDevice, HttpStatus.OK);
    }

    /**
     * Delete device by ID.
     */
    @DeleteMapping("/{deviceId}")
    public ResponseEntity<Void> deleteDevice(@PathVariable String deviceId) {
        deviceMetadataService.deleteDevice(deviceId);
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

    /**
     * Get device by ID.
     */
    @GetMapping("/{deviceId}")
    public ResponseEntity<DeviceMetadata> getDevice(@PathVariable String deviceId) {
        Optional<DeviceMetadata> deviceMetadata = deviceMetadataService.findDeviceById(deviceId);
        return deviceMetadata.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }
}