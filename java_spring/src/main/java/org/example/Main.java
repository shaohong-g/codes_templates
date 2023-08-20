package org.example;

import org.example.model.Blastoise;
import org.example.model.Pokemon;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;


public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");

        // Option 0: Initialize class directly
        /*
        Charizard pokemon = new Charizard();
        pokemon.pokedex();
         */

        // Option 1: Use ClassPathXmlApplicationContext to get Beans
        /*
        ApplicationContext context = new ClassPathXmlApplicationContext("spring.xml");

        Pokemon pokemon = (Pokemon)context.getBean("blastoise");
        pokemon.pokedex();
        System.out.println(pokemon);
         */

        // Option 2: Use AnnotationConfigApplicationContext (self-defined in Java)
        ApplicationContext factory = new AnnotationConfigApplicationContext(AppConfig.class);
        Blastoise blastoise = factory.getBean(Blastoise.class);
        blastoise.pokedex();




    }
}