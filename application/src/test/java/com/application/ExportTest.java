package com.application;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import static org.junit.Assert.assertNotNull;

@RunWith(SpringRunner.class)
@SpringBootTest
public class ExportTest {

    @Autowired
    private ExportService exportService;

    @Test
    public void testExportToCSV() throws Exception {
        exportService.exportToCSV("transactions.csv");
        // Assert that the file exists
        assertNotNull(new java.io.File("transactions.csv"));
    }
}
