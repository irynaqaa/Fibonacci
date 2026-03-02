package com.example.iotmonitoring.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.scheduling.annotation.Async;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.cache.annotation.EnableCaching;

import java.util.List;

/**
 * Service for handling data ingestion from IoT devices.
 * This service implements asynchronous processing and caching mechanisms to optimize performance.
 */
@Service
@EnableCaching
public class DataIngestionService {

    @Autowired
    private SensorDataService sensorDataService;

    /**
     * Asynchronously ingests data from IoT devices.
     * @param sensorDataList List of sensor data to be ingested.
     */
    @Async
    public void ingestData(List<SensorData> sensorDataList) {
        for (SensorData data : sensorDataList) {
            sensorDataService.save(data);
        }
    }

    /**
     * Retrieves cached sensor data for fast access.
     * @param deviceId The ID of the device whose data is to be retrieved.
     * @return List of sensor data for the specified device.
     */
    @Cacheable(value = "sensorDataCache", key = "#deviceId")
    public List<SensorData> getCachedSensorData(String deviceId) {
        return sensorDataService.findByDeviceId(deviceId);
    }
}