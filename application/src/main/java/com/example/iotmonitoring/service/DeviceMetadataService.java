package com.example.iotmonitoring.service;

import com.example.iotmonitoring.model.DeviceMetadata;
import com.example.iotmonitoring.repository.DeviceMetadataRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

/**
 * DeviceMetadataService handles business logic for device metadata operations.
 */
@Service
public class DeviceMetadataService {

    private final DeviceMetadataRepository deviceMetadataRepository;

    @Autowired
    public DeviceMetadataService(DeviceMetadataRepository deviceMetadataRepository) {
        this.deviceMetadataRepository = deviceMetadataRepository;
    }

    /**
     * Register a new device metadata.
     */
    @Transactional
    public DeviceMetadata registerDevice(DeviceMetadata deviceMetadata) {
        return deviceMetadataRepository.save(deviceMetadata);
    }

    /**
     * Update existing device metadata.
     */
    @Transactional
    public DeviceMetadata updateDevice(DeviceMetadata deviceMetadata) {
        return deviceMetadataRepository.save(deviceMetadata);
    }

    /**
     * Delete device metadata by device ID.
     */
    @Transactional
    public void deleteDevice(String deviceId) {
        DeviceMetadata deviceMetadata = deviceMetadataRepository.findByDeviceId(deviceId);
        if (deviceMetadata != null) {
            deviceMetadataRepository.delete(deviceMetadata);
        }
    }

    /**
     * Find device metadata by device ID.
     */
    public Optional<DeviceMetadata> findDeviceById(String deviceId) {
        return Optional.ofNullable(deviceMetadataRepository.findByDeviceId(deviceId));
    }
}