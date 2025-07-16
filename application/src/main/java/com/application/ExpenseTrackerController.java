import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ExpenseTrackerController {
    private final ExpenseTrackerService service;

    @Autowired
    public ExpenseTrackerController(ExpenseTrackerService service) {
        this.service = service;
    }

    @GetMapping("/expenses")
    public String getExpenses() {
        return "Expenses";
    }

    @PostMapping("/expenses")
    public String addExpense(@RequestBody String expense) {
        return "Expense added";
    }
}