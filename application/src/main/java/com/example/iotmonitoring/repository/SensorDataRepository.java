package com.example.iotmonitoring.repository;

import com.example.iotmonitoring.model.SensorData;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repository interface for SensorData entity.
 */
@Repository
public interface SensorDataRepository extends JpaRepository<SensorData, UUID> {
}
