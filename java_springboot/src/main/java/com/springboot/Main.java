package com.springboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@SpringBootApplication
@RestController
@RequestMapping("api/v1/customers")
public class Main {
    public static void main(String[] args) {
        SpringApplication.run(Main.class, args);
    }

    @GetMapping("/test1")
    public String test() {
        return "Hello World!";
    }
    @GetMapping("/test2")
    public testResponse testResponse() {
        return new testResponse(
                "Hello World!",
                List.of("Java", "Golang", "Python"),
                new Person("Alex", 28, 30_000.5)

        ); // Response: {"test1":"Hello","test2":"World!"}
    }

    record Person(String name, int age, double savings){} // equivalent to a class with final, constructor, getter, tostring, etc
    record testResponse(String test1, List<String> progLang, Person person){}


    private final CustomerRepository customerRepository;
    public Main(CustomerRepository customerRepository){
        this.customerRepository = customerRepository;
    }
    @GetMapping
    public List<Customer> getCustomers(){
        return customerRepository.findAll();
    }

    @PostMapping
    public void addCustomer(@RequestBody Customer customerRequest){
        customerRepository.save(customerRequest);
    }

    @DeleteMapping("{customerId}")
    public void deleteCustomer(@PathVariable("customerId") Integer id){
        customerRepository.deleteById(id);
    }


}
