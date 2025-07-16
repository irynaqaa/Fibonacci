import java.util.ArrayList;
import java.util.List;

public class TransactionService {
    private List<Transaction> transactions = new ArrayList<>();

    public void addTransaction(Transaction transaction) {
        transactions.add(transaction);
    }

    public List<Transaction> getTransactions() {
        return transactions;
    }

    public void deleteTransaction(Transaction transaction) {
        transactions.remove(transaction);
    }

    public void editTransaction(Transaction oldTransaction, Transaction newTransaction) {
        transactions.remove(oldTransaction);
        transactions.add(newTransaction);
    }
}