package com.example.iotmonitoring.repository;

import com.example.iotmonitoring.model.DeviceMetadata;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * DeviceMetadataRepository provides CRUD operations for DeviceMetadata.
 */
@Repository
public interface DeviceMetadataRepository extends JpaRepository<DeviceMetadata, Long> {
    DeviceMetadata findByDeviceId(String deviceId);
}