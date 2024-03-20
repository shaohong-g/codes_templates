package com.springboot;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.RepositoryDefinition;


public interface CustomerRepository extends JpaRepository<Customer, Integer> {

}
