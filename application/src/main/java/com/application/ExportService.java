package com.application;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

@Service
public class ExportService {

    private final TransactionService transactionService;

    @Autowired
    public ExportService(TransactionService transactionService) {
        this.transactionService = transactionService;
    }

    public void exportToCSV(String filename) throws IOException {
        List<Transaction> transactions = transactionService.getAllTransactions();
        try (PrintWriter writer = new PrintWriter(new FileWriter(filename))) {
            writer.println("Date,Category,Amount,Type,Description");
            for (Transaction transaction : transactions) {
                writer.println(String.format("%s,%s,%.2f,%s,%s",
                        transaction.getDate(),
                        transaction.getCategory(),
                        transaction.getAmount(),
                        transaction.getType(),
                        transaction.getDescription()));
            }
        }
    }
}
