package com.application;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import static org.junit.Assert.assertNotNull;

@RunWith(SpringRunner.class)
@SpringBootTest
public class PerformanceTest {

    @Autowired
    private TransactionService transactionService;

    @Test
    public void testPerformance() {
        for (int i = 0; i < 1000; i++) {
            Transaction transaction = new Transaction();
            transaction.setAmount(100.0);
            transaction.setCategory("Food");
            transaction.setDate("2023-09-01");
            transaction.setDescription("Lunch");
            transaction.setType("expense");
            transactionService.createTransaction(transaction);
        }
    }
}
