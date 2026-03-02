package com.example.iotmonitoring.repository;

import com.example.iotmonitoring.model.AlertRule;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repository interface for AlertRule entity.
 */
@Repository
public interface AlertRuleRepository extends JpaRepository<AlertRule, UUID> {
}
