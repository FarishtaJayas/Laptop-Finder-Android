package com.example.laptopfinder;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

public interface LaptopFinderApi {
        @GET("{speechResult}")
        Call<List<Laptops>> getLaptops(@Path("speechResult") String speechResult);
}
