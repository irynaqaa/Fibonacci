import java.util.ArrayList;
import java.util.List;

public class TransactionFilter {
    private List<Transaction> transactions;

    public TransactionFilter(List<Transaction> transactions) {
        this.transactions = transactions;
    }

    public List<Transaction> filterByType(String type) {
        List<Transaction> filteredTransactions = new ArrayList<>();
        for (Transaction transaction : this.transactions) {
            if (transaction.getType().equals(type)) {
                filteredTransactions.add(transaction);
            }
        }
        return filteredTransactions;
    }

    public List<Transaction> filterByDate(String date) {
        List<Transaction> filteredTransactions = new ArrayList<>();
        for (Transaction transaction : this.transactions) {
            if (transaction.getDate().equals(date)) {
                filteredTransactions.add(transaction);
            }
        }
        return filteredTransactions;
    }

    public List<Transaction> filterByAmount(double amount) {
        List<Transaction> filteredTransactions = new ArrayList<>();
        for (Transaction transaction : this.transactions) {
            if (transaction.getAmount() == amount) {
                filteredTransactions.add(transaction);
            }
        }
        return filteredTransactions;
    }
}