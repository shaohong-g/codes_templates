package org.example;

import org.example.model.Blastoise;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan(basePackages = "org.example.model")
public class AppConfig {

//    @Bean
//    public Blastoise getBlastoise(){
//        return new Blastoise();
//    }

}
