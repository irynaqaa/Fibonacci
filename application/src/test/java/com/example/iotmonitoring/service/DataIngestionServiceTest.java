package com.example.iotmonitoring.service;

import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import java.util.Arrays;
import java.util.List;

/**
 * Unit tests for the DataIngestionService class.
 * This class tests the data ingestion functionality of the IoT Monitoring Microservice.
 */
class DataIngestionServiceTest {

    @InjectMocks
    private DataIngestionService dataIngestionService;

    @Mock
    private SensorDataService sensorDataService;

    /**
     * Initializes mocks before each test.
     */
    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    /**
     * Test for successful data ingestion.
     */
    @Test
    void testIngestData_Success() {
        SensorData data1 = new SensorData(); // Assume SensorData has a default constructor
        SensorData data2 = new SensorData();
        List<SensorData> sensorDataList = Arrays.asList(data1, data2);

        dataIngestionService.ingestData(sensorDataList);

        verify(sensorDataService, times(1)).save(data1);
        verify(sensorDataService, times(1)).save(data2);
    }

    /**
     * Test for retrieving cached sensor data.
     */
    @Test
    void testGetCachedSensorData() {
        String deviceId = "device123";
        List<SensorData> expectedData = Arrays.asList(new SensorData());
        when(sensorDataService.findByDeviceId(deviceId)).thenReturn(expectedData);

        List<SensorData> actualData = dataIngestionService.getCachedSensorData(deviceId);

        assertEquals(expectedData, actualData);
        verify(sensorDataService, times(1)).findByDeviceId(deviceId);
    }
}