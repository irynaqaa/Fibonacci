import com.example.blockchain.Transaction;
import com.example.blockchain.TransactionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

@Service
public class ExportToCSV {

    @Autowired
    private TransactionRepository transactionRepository;

    public void exportToCSV() {
        List<Transaction> transactions = transactionRepository.findAll();
        try (FileWriter writer = new FileWriter("transactions.csv")) {
            writer.write("Id,Amount,Category,Date,Description,Type
");
            for (Transaction transaction : transactions) {
                writer.write(String.format("%d,%f,%s,%s,%s,%s
", transaction.getId(), transaction.getAmount(), transaction.getCategory(), transaction.getDate(), transaction.getDescription(), transaction.getType()));
            }
        } catch (IOException e) {
            System.err.println("Error writing to CSV file: " + e.getMessage());
        }
    }
