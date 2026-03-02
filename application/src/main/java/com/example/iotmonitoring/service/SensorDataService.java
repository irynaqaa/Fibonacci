package com.example.iotmonitoring.service;

import com.example.iotmonitoring.model.SensorData;
import com.example.iotmonitoring.repository.SensorDataRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

/**
 * Service class for managing sensor data in the IoT Monitoring System.
 */
@Service
public class SensorDataService {
    private final SensorDataRepository sensorDataRepository;

    @Autowired
    public SensorDataService(SensorDataRepository sensorDataRepository) {
        this.sensorDataRepository = sensorDataRepository;
    }

    public SensorData createSensorData(SensorData sensorData) {
        return sensorDataRepository.save(sensorData);
    }

    public Optional<SensorData> getSensorData(UUID id) {
        return sensorDataRepository.findById(id);
    }

    public List<SensorData> getAllSensorData() {
        return sensorDataRepository.findAll();
    }

    public void deleteSensorData(UUID id) {
        sensorDataRepository.deleteById(id);
    }
}
