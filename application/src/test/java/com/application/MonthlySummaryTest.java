package com.application;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import static org.junit.Assert.assertNotNull;

@RunWith(SpringRunner.class)
@SpringBootTest
public class MonthlySummaryTest {

    @Autowired
    private ReportService reportService;

    @Test
    public void testGetMonthlySummary() {
        MonthlySummary monthlySummary = reportService.getMonthlySummary("2023-09");
        assertNotNull(monthlySummary);
    }
}
