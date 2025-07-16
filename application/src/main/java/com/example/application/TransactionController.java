import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping("/transactions")
public class TransactionController {
    @Autowired
    private TransactionService transactionService;

    @GetMapping
    public String getTransactions(Model model) {
        model.addAttribute("transactions", transactionService.getTransactions());
        return "transactions";
    }

    @PostMapping
    public String addTransaction(@RequestParam double amount, @RequestParam String category, @RequestParam String date, @RequestParam String description) {
        Transaction transaction = new Transaction(amount, category, date, description);
        transactionService.addTransaction(transaction);
        return "redirect:/transactions";
    }

    @PostMapping("/delete")
    public String deleteTransaction(@RequestParam int index) {
        transactionService.deleteTransaction(transactionService.getTransactions().get(index));
        return "redirect:/transactions";
    }

    @PostMapping("/edit")
    public String editTransaction(@RequestParam int index, @RequestParam double amount, @RequestParam String category, @RequestParam String date, @RequestParam String description) {
        Transaction oldTransaction = transactionService.getTransactions().get(index);
        Transaction newTransaction = new Transaction(amount, category, date, description);
        transactionService.editTransaction(oldTransaction, newTransaction);
        return "redirect:/transactions";
    }
}