package com.application;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import static org.junit.Assert.assertNotNull;

@RunWith(SpringRunner.class)
@SpringBootTest
public class ReportTest {

    @Autowired
    private ReportService reportService;

    @Test
    public void testGetTransactionsForMonth() {
        List<Transaction> transactions = reportService.getTransactionsForMonth("2023-09");
        assertNotNull(transactions);
    }
}
