package org.example.model;

import org.springframework.stereotype.Component;

@Component("selectedPokemon")
public class Charizard implements Pokemon{

    private int totalStats;
    private String ability;

    private String characteristic = "Spits fire that is hot enough to melt boulders. Known to cause forest fires unintentionally.";

    public void pokedex(){
        System.out.println("I am a Charizard...");
    }

    @Override
    public String toString() {
        return "Charizard{" +
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
