import com.example.blockchain.MonthlySummary;
import com.example.blockchain.MonthlySummaryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MonthlySummaryServiceImpl implements com.example.blockchain.MonthlySummaryService {
    @Autowired
    private MonthlySummaryRepository monthlySummaryRepository;
    @Override
    public void addMonthlySummary(MonthlySummary monthlySummary) {
        monthlySummaryRepository.save(monthlySummary);
    }
    @Override
    public List<MonthlySummary> getAllMonthlySummaries() {
        return monthlySummaryRepository.findAll();
    }
    @Override
    public void editMonthlySummary(MonthlySummary monthlySummary) {
        monthlySummaryRepository.save(monthlySummary);
    }
    @Override
    public void deleteMonthlySummary(Long id) {
        monthlySummaryRepository.deleteById(id);
    }
}