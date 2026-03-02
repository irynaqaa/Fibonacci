package com.example.iotmonitoring.service;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.transaction.annotation.Transactional;

import com.example.iotmonitoring.model.Device;
import com.example.iotmonitoring.model.SensorData;
import com.example.iotmonitoring.model.AlertRule;
import com.example.iotmonitoring.repository.DeviceRepository;
import com.example.iotmonitoring.repository.SensorDataRepository;
import com.example.iotmonitoring.repository.AlertRuleRepository;

import java.util.Optional;

/**
 * Unit tests for the database functionality of the IoT Monitoring Microservice.
 */
@ExtendWith(SpringExtension.class)
@DataJpaTest
@Transactional
class DatabaseServiceTest {

    @Autowired
    private DeviceRepository deviceRepository;

    @Autowired
    private SensorDataRepository sensorDataRepository;

    @Autowired
    private AlertRuleRepository alertRuleRepository;

    /**
     * Test for creating and retrieving a device.
     */
    @Test
    void testCreateAndRetrieveDevice() {
        Device device = new Device();
        device.setName("Device 1");
        device.setType("Sensor");
        device.setLocation("Location 1");

        deviceRepository.save(device);

        Optional<Device> retrievedDevice = deviceRepository.findById(device.getId());
        assertTrue(retrievedDevice.isPresent());
        assertEquals(device.getName(), retrievedDevice.get().getName());
    }

    /**
     * Test for creating and retrieving sensor data.
     */
    @Test
    void testCreateAndRetrieveSensorData() {
        Device device = new Device();
        device.setName("Device 1");
        device.setType("Sensor");
        device.setLocation("Location 1");
        deviceRepository.save(device);

        SensorData sensorData = new SensorData();
        sensorData.setDeviceId(device.getId());
        sensorData.setTimestamp(System.currentTimeMillis());
        sensorData.setData("{"value": 25}");

        sensorDataRepository.save(sensorData);

        Optional<SensorData> retrievedData = sensorDataRepository.findById(sensorData.getId());
        assertTrue(retrievedData.isPresent());
        assertEquals(sensorData.getData(), retrievedData.get().getData());
    }

    /**
     * Test for creating and retrieving an alert rule.
     */
    @Test
    void testCreateAndRetrieveAlertRule() {
        Device device = new Device();
        device.setName("Device 1");
        device.setType("Sensor");
        device.setLocation("Location 1");
        deviceRepository.save(device);

        AlertRule alertRule = new AlertRule();
        alertRule.setDeviceId(device.getId());
        alertRule.setThreshold(100.0);
        alertRule.setCondition(">");
        alertRule.setNotificationMethod("Email");

        alertRuleRepository.save(alertRule);

        Optional<AlertRule> retrievedRule = alertRuleRepository.findById(alertRule.getId());
        assertTrue(retrievedRule.isPresent());
        assertEquals(alertRule.getThreshold(), retrievedRule.get().getThreshold());
    }
}
