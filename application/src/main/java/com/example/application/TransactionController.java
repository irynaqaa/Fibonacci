import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class TransactionController {
    @Autowired
    private TransactionService transactionService;

    @PostMapping("/transactions")
    public ResponseEntity<String> addTransaction(@RequestBody Transaction transaction) {
        transactionService.addTransaction(transaction);
        return new ResponseEntity<>("Transaction added successfully", HttpStatus.CREATED);
    }

    @GetMapping("/transactions")
    public ResponseEntity<List<Transaction>> viewAllTransactions() {
        List<Transaction> transactions = transactionService.viewAllTransactions();
        return new ResponseEntity<>(transactions, HttpStatus.OK);
    }

    @PutMapping("/transactions/{transactionId}/category")
    public ResponseEntity<String> categorizeTransaction(@PathVariable String transactionId, @RequestBody String category) {
        // Find the transaction by id and categorize it
        Transaction transaction = new Transaction();
        transaction.setId(transactionId);
        transactionService.categorizeTransaction(transaction, category);
        return new ResponseEntity<>("Transaction categorized successfully", HttpStatus.OK);
    }

    @GetMapping("/monthly-summary")
    public ResponseEntity<MonthlySummary> generateMonthlySummary() {
        MonthlySummary monthlySummary = transactionService.generateMonthlySummary();
        return new ResponseEntity<>(monthlySummary, HttpStatus.OK);
    }
}