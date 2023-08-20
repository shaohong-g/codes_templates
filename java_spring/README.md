# java_spring

This repo shows the fundamental structure of how Spring works.

## Theories
1. Dependency injection
   - Initializing the class directly make it difficult to change the object at runtime. For eg, we have to rerun/test again if Charizard was to change or result in error.
      ```java
      Charizard pokemon = new Charizard();
      pokemon.pokedex();
      ```
   - Make it loosely coupled by injecting the said object only at runtime:
      ```java
        // Option 1: Use ClassPathXmlApplicationContext to get Beans (Charizard implements Pokemon)
        ApplicationContext context = new ClassPathXmlApplicationContext("spring.xml");

        Pokemon pokemon = (Pokemon)context.getBean("selectedPokemon");
        pokemon.pokedex();
      ```
2. Annotations used:
    - Component
      - Used so that class can be detected as Beans
    - Autowired
      - Auto configure attributes to relevant Beans
    - Qualifier 
      - In case of non-unique beans, qualifier allows us to indicate which beans to autowired.
    - Configuration
      - Used for AnnotationConfigApplicationContext
    - ComponentScan
      - Scan for classes with Component annotations (used as Beans)
    - Bean
      - Configure methods as Beans


## Resources
1. Model Entities
    - Pokemon
      - [Charizard](https://pokemondb.net/pokedex/charizard)
      - [Venusaur](https://pokemondb.net/pokedex/venusaur)
      - [Blastoise](https://pokemondb.net/pokedex/blastoise)

## Acknowledgements
- [Youtube: Spring Framework Tutorial | Full Course](https://www.youtube.com/watch?v=If1Lw4pLLEo&ab_channel=Telusko)