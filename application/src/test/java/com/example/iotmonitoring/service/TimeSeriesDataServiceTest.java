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
 * Unit tests for the TimeSeriesDataService class.
 * This class tests the time-series data storage and retrieval functionality.
 */
class TimeSeriesDataServiceTest {

    @InjectMocks
    private TimeSeriesDataService timeSeriesDataService;

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
     * Test for storing time-series data points.
     */
    @Test
    void testStoreTimeSeriesData() {
        TimeSeriesData data = new TimeSeriesData(); // Assume TimeSeriesData has a default constructor
        when(timeSeriesDataRepository.save(data)).thenReturn(data);

        TimeSeriesData savedData = timeSeriesDataService.storeTimeSeriesData(data);

        assertEquals(data, savedData);
        verify(timeSeriesDataRepository, times(1)).save(data);
    }

    /**
     * Test for retrieving time-series data for a specific time range.
     */
    @Test
    void testGetTimeSeriesDataByTimeRange() {
        List<TimeSeriesData> expectedData = Arrays.asList(new TimeSeriesData());
        when(timeSeriesDataRepository.findByTimestampBetween(any(), any())).thenReturn(expectedData);

        List<TimeSeriesData> actualData = timeSeriesDataService.getTimeSeriesDataByTimeRange("2023-01-01T00:00:00Z", "2023-01-02T00:00:00Z");

        assertEquals(expectedData, actualData);
        verify(timeSeriesDataRepository, times(1)).findByTimestampBetween(any(), any());
    }

    /**
     * Test for handling empty datasets.
     */
    @Test
    void testGetTimeSeriesData_EmptyDataset() {
        when(timeSeriesDataRepository.findByTimestampBetween(any(), any())).thenReturn(Arrays.asList());

        List<TimeSeriesData> actualData = timeSeriesDataService.getTimeSeriesDataByTimeRange("2023-01-01T00:00:00Z", "2023-01-02T00:00:00Z");

        assertTrue(actualData.isEmpty());
        verify(timeSeriesDataRepository, times(1)).findByTimestampBetween(any(), any());
    }
}
