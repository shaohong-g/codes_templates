package org.example.model;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component
public class Blastoise implements Pokemon{

    @Autowired
    @Qualifier("selectedPokemon")
    private Pokemon strongAgainst;

    private int totalStats;

    private String ability;

    private String characteristic = "A brutal POKéMON with pressurized water jets on its shell. They are used for high speed tackles.";

    public void pokedex(){
        System.out.println("I am a Blastoise... I am stronger than " + strongAgainst);
    }

    public Blastoise() {
    }

    public Blastoise(int totalStats, String ability) {
        this.totalStats = totalStats;
        this.ability = ability;
    }

    @Override
    public String toString() {
        return "Blastoise{" +
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
