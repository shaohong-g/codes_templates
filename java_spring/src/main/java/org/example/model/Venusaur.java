package org.example.model;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;

@Component
@Primary // Primary Component to use
public class Venusaur implements Pokemon{
    private int totalStats;
    private String ability;

    private String characteristic = "The plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight.";

    public void pokedex(){
        System.out.println("I am a Venusaur...");
    }

    @Override
    public String toString() {
        return "Venusaur{" +
                "totalStats=" + totalStats +
                ", ability='" + ability + '\'' +
                ", characteristic='" + characteristic + '\'' +
                '}';
    }

    public int getTotalStats() {
        return totalStats;
    }

    public void setTotalStats(int totalStats) {
        this.totalStats = totalStats;
    }

    public String getAbility() {
        return ability;
    }

    public void setAbility(String ability) {
        this.ability = ability;
    }
}
