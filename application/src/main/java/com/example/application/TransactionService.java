import java.util.ArrayList;
import java.util.List;

public class TransactionService {
    private List<Transaction> transactions = new ArrayList<>();

    public void addTransaction(Transaction transaction) {
        transactions.add(transaction);
    }

    public List<Transaction> viewAllTransactions() {
        return transactions;
    }

    public void categorizeTransaction(Transaction transaction, String category) {
        transaction.setCategory(category);
    }

    public MonthlySummary generateMonthlySummary() {
        MonthlySummary monthlySummary = new MonthlySummary();
        double totalIncome = 0;
        double totalExpenses = 0;
        for (Transaction transaction : transactions) {
            if (transaction.getCategory().equals("income")) {
                totalIncome += transaction.getAmount();
            } else if (transaction.getCategory().equals("expense")) {
                totalExpenses += transaction.getAmount();
            }
        }
        monthlySummary.setTotalIncome(totalIncome);
        monthlySummary.setTotalExpenses(totalExpenses);
        monthlySummary.setNetBalance(totalIncome - totalExpenses);
        return monthlySummary;
    }
}