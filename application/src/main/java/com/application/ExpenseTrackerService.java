import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ExpenseTrackerService {
    private final ExpenseTrackerRepository repository;

    @Autowired
    public ExpenseTrackerService(ExpenseTrackerRepository repository) {
        this.repository = repository;
    }

    // Implement business logic
    public List<Expense> getAllExpenses() {
        return repository.findAll();
    }
}