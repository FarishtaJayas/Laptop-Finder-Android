package com.example.laptopfinder;

import com.google.gson.annotations.SerializedName;

public class Laptops {
    @SerializedName("lapModel")
    private String laptopModel;
    private double price;
    private String url;
    @SerializedName("image_url")
    private String laptopImage;

    public String getUrl() {
        return url;
    }

    public Laptops() {
    }

    public String getLaptopModel() {
        return laptopModel;
    }

    public double getPrice() {
        return price;
    }

    public String getLaptopImage() {
        return laptopImage;
    }
}
