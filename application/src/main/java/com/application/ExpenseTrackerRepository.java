import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.stereotype.Repository;

import javax.sql.DataSource;

@Repository
public class ExpenseTrackerRepository {
    private JdbcTemplate jdbcTemplate;

    public ExpenseTrackerRepository(DataSource dataSource) {
        this.jdbcTemplate = new JdbcTemplate(dataSource);
    }

    // Implement database operations
    public void saveExpense(Expense expense) {
        String query = "INSERT INTO expenses (amount, category, date, description) VALUES (?, ?, ?, ?)";
        jdbcTemplate.update(query, expense.getAmount(), expense.getCategory(), expense.getDate(), expense.getDescription());
    }

    public List<Expense> getAllExpenses() {
        String query = "SELECT * FROM expenses";
        return jdbcTemplate.query(query, new ExpenseRowMapper());
    }
}

class ExpenseRowMapper implements RowMapper<Expense> {
    @Override
    public Expense mapRow(ResultSet resultSet, int rowNum) throws SQLException {
        Expense expense = new Expense();
        expense.setId(resultSet.getLong("id"));
        expense.setAmount(resultSet.getBigDecimal("amount"));
        expense.setCategory(resultSet.getString("category"));
        expense.setDate(resultSet.getDate("date"));
        expense.setDescription(resultSet.getString("description"));
        return expense;
    }
}
