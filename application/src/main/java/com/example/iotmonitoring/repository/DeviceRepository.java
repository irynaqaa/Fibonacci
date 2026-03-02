package com.example.iotmonitoring.repository;

import com.example.iotmonitoring.model.Device;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repository interface for Device entity.
 */
@Repository
public interface DeviceRepository extends JpaRepository<Device, UUID> {
}
