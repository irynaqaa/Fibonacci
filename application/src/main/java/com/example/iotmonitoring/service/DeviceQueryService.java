package com.example.iotmonitoring.service;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import com.example.iotmonitoring.repository.DeviceRepository;
import com.example.iotmonitoring.model.Device;
import java.util.List;
import java.util.Optional;

/**
 * DeviceQueryService handles querying operations for devices.
 */
@Service
public class DeviceQueryService {

    private final DeviceRepository deviceRepository;

    @Autowired
    public DeviceQueryService(DeviceRepository deviceRepository) {
        this.deviceRepository = deviceRepository;
    }

    /**
     * Retrieve a device by its ID.
     */
    public Optional<Device> getDeviceById(UUID deviceId) {
        return deviceRepository.findById(deviceId);
    }

    /**
     * Retrieve all devices.
     */
    public List<Device> getAllDevices() {
        return deviceRepository.findAll();
    }
}