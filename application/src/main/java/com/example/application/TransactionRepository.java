import com.example.application.Transaction;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface TransactionRepository extends CrudRepository<Transaction, String> {
    Optional<Transaction> findById(String id);
    List<Transaction> findAll();
    Transaction save(Transaction transaction);
    void deleteById(String id);
}