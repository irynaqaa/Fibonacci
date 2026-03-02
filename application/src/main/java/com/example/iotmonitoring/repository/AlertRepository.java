package com.example.iotmonitoring.repository;

import com.example.iotmonitoring.model.ThresholdRule;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repository interface for managing threshold rules in the database.
 */
@Repository
public interface AlertRepository extends JpaRepository<ThresholdRule, Long> {
}