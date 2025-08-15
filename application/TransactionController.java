import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class TransactionController {
    private TransactionDAO dao;

    public TransactionController() {
        this.dao = new TransactionDAO();
    }

    public void saveTransaction(Transaction transaction) {
        dao.saveTransaction(transaction);
    }

    public List<Transaction> getTransactions() {
        return dao.getTransactions();
    }
}