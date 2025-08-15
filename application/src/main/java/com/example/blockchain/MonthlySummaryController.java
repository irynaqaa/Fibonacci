import com.example.blockchain.MonthlySummary;
import com.example.blockchain.MonthlySummaryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/monthly-summaries")
public class MonthlySummaryController {
    @Autowired
    private MonthlySummaryService monthlySummaryService;
    @GetMapping
    public ResponseEntity<List<MonthlySummary>> getAllMonthlySummaries() {
        return new ResponseEntity<>(monthlySummaryService.getAllMonthlySummaries(), HttpStatus.OK);
    }
    @GetMapping("/{id}")
    public ResponseEntity<MonthlySummary> getMonthlySummaryById(@PathVariable Long id) {
        return new ResponseEntity<>(monthlySummaryService.getAllMonthlySummaries().stream().filter(monthlySummary -> monthlySummary.getId().equals(id)).findFirst().orElse(null), HttpStatus.OK);
    }
    @PostMapping
    public ResponseEntity<MonthlySummary> addMonthlySummary(@RequestBody MonthlySummary monthlySummary) {
        monthlySummaryService.addMonthlySummary(monthlySummary);
        return new ResponseEntity<>(monthlySummary, HttpStatus.CREATED);
    }
    @PutMapping("/{id}")
    public ResponseEntity<MonthlySummary> updateMonthlySummary(@PathVariable Long id, @RequestBody MonthlySummary monthlySummary) {
        monthlySummaryService.editMonthlySummary(monthlySummary);
        return new ResponseEntity<>(monthlySummary, HttpStatus.OK);
    }
    @DeleteMapping("/{id}")
    public ResponseEntity<HttpStatus> deleteMonthlySummary(@PathVariable Long id) {
        monthlySummaryService.deleteMonthlySummary(id);
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }
}