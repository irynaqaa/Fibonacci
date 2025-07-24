package com.application;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ReportService {

    private final TransactionService transactionService;

    @Autowired
    public ReportService(TransactionService transactionService) {
        this.transactionService = transactionService;
    }

    public List<Transaction> getTransactionsForMonth(String month) {
        return transactionService.getAllTransactions().stream()
                .filter(transaction -> transaction.getDate().startsWith(month))
                .collect(Collectors.toList());
    }

    public Double getTotalIncomeForMonth(String month) {
        return getTransactionsForMonth(month).stream()
                .filter(transaction -> transaction.getType().equals("income"))
                .mapToDouble(Transaction::getAmount)
                .sum();
    }

    public Double getTotalExpensesForMonth(String month) {
        return getTransactionsForMonth(month).stream()
                .filter(transaction -> transaction.getType().equals("expense"))
                .mapToDouble(Transaction::getAmount)
                .sum();
    }

    public Double getBalanceForMonth(String month) {
        return getTotalIncomeForMonth(month) - getTotalExpensesForMonth(month);
    }
}
