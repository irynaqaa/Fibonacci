package com.application;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;

import com.application.Transaction;

@RestController
@RequestMapping("/api/reports")
public class ReportController {

    private final ReportService reportService;

    @Autowired
    public ReportController(ReportService reportService) {
        this.reportService = reportService;
    }

    @GetMapping("/transactions/{month}")
    public ResponseEntity<List<Transaction>> getTransactionsForMonth(@PathVariable String month) {
        return ResponseEntity.ok(reportService.getTransactionsForMonth(month));
    }

    @GetMapping("/total-income/{month}")
    public ResponseEntity<Double> getTotalIncomeForMonth(@PathVariable String month) {
        return ResponseEntity.ok(reportService.getTotalIncomeForMonth(month));
    }

    @GetMapping("/total-expenses/{month}")
    public ResponseEntity<Double> getTotalExpensesForMonth(@PathVariable String month) {
        return ResponseEntity.ok(reportService.getTotalExpensesForMonth(month));
    }

    @GetMapping("/balance/{month}")
    public ResponseEntity<Double> getBalanceForMonth(@PathVariable String month) {
        return ResponseEntity.ok(reportService.getBalanceForMonth(month));
    }
}
