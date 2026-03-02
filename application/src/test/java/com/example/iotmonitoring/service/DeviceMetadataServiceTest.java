package com.example.iotmonitoring.service;

import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import java.util.Optional;

/**
 * Unit tests for the DeviceMetadataService class.
 * This class tests the device metadata storage and retrieval functionality.
 */
class DeviceMetadataServiceTest {

    @InjectMocks
    private DeviceMetadataService deviceMetadataService;

    @Mock
    private DeviceMetadataRepository deviceMetadataRepository;

    /**
     * Initializes mocks before each test.
     */
    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    /**
     * Test for adding new device metadata.
     */
    @Test
    void testAddDeviceMetadata() {
        DeviceMetadata metadata = new DeviceMetadata(); // Assume DeviceMetadata has a default constructor
        when(deviceMetadataRepository.save(metadata)).thenReturn(metadata);

        DeviceMetadata savedMetadata = deviceMetadataService.addDeviceMetadata(metadata);

        assertEquals(metadata, savedMetadata);
        verify(deviceMetadataRepository, times(1)).save(metadata);
    }

    /**
     * Test for updating existing device metadata.
     */
    @Test
    void testUpdateDeviceMetadata() {
        DeviceMetadata metadata = new DeviceMetadata(); // Assume DeviceMetadata has a default constructor
        metadata.setId(1L);
        when(deviceMetadataRepository.findById(1L)).thenReturn(Optional.of(metadata));
        when(deviceMetadataRepository.save(metadata)).thenReturn(metadata);

        DeviceMetadata updatedMetadata = deviceMetadataService.updateDeviceMetadata(1L, metadata);

        assertEquals(metadata, updatedMetadata);
        verify(deviceMetadataRepository, times(1)).save(metadata);
    }

    /**
     * Test for retrieving device metadata by ID.
     */
    @Test
    void testGetDeviceMetadataById() {
        DeviceMetadata metadata = new DeviceMetadata(); // Assume DeviceMetadata has a default constructor
        metadata.setId(1L);
        when(deviceMetadataRepository.findById(1L)).thenReturn(Optional.of(metadata));

        DeviceMetadata foundMetadata = deviceMetadataService.getDeviceMetadataById(1L);

        assertEquals(metadata, foundMetadata);
        verify(deviceMetadataRepository, times(1)).findById(1L);
    }
}
