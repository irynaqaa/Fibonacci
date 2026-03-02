package com.example.iotmonitoring.service;

import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

/**
 * Unit tests for the IndexingService class.
 * This class tests the indexing functionality for device metadata and time-series data.
 */
class IndexingServiceTest {

    @InjectMocks
    private IndexingService indexingService;

    @Mock
    private DeviceMetadataRepository deviceMetadataRepository;

    @Mock
    private TimeSeriesDataRepository timeSeriesDataRepository;

    /**
     * Initializes mocks before each test.
     */
    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    /**
     * Test for indexing device metadata.
     */
    @Test
    void testIndexDeviceMetadata() {
        DeviceMetadata metadata = new DeviceMetadata(); // Assume DeviceMetadata has a default constructor
        when(deviceMetadataRepository.save(metadata)).thenReturn(metadata);

        DeviceMetadata indexedMetadata = indexingService.indexDeviceMetadata(metadata);

        assertEquals(metadata, indexedMetadata);
        verify(deviceMetadataRepository, times(1)).save(metadata);
    }

    /**
     * Test for indexing time-series data.
     */
    @Test
    void testIndexTimeSeriesData() {
        TimeSeriesData data = new TimeSeriesData(); // Assume TimeSeriesData has a default constructor
        when(timeSeriesDataRepository.save(data)).thenReturn(data);

        TimeSeriesData indexedData = indexingService.indexTimeSeriesData(data);

        assertEquals(data, indexedData);
        verify(timeSeriesDataRepository, times(1)).save(data);
    }
}
