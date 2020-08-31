package com.example.laptopfinder;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class Main2Activity extends AppCompatActivity {

    private TextView textViewResult;
    private TextView textViewResult2;
    private TextView textViewResult3;
    private String URL1;
    private String URL2;
    private String URL3;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        textViewResult = findViewById(R.id.text_view_result);
        textViewResult2 = findViewById(R.id.text_view_result2);
        textViewResult3 = findViewById(R.id.text_view_result3);

        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://192.168.0.151:8000/api/laptops_by_price/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        LaptopFinderApi laptopFinderApi = retrofit.create(LaptopFinderApi.class);

        Call<List<Laptops>> call = laptopFinderApi.getLaptops(getIntent().getStringExtra("speechResult"));

        call.enqueue((new Callback<List<Laptops>>() {
            @Override
            public void onResponse(Call<List<Laptops>> call, Response<List<Laptops>> response) {
                if(!response.isSuccessful()) {
                    textViewResult.setText("Code: " + response.code());
                    return;
                }
                List<Laptops> laptops_by_price  = response.body();

                    String content = "";
                    content += "Laptop Model: " + laptops_by_price.get(0).getLaptopModel()+ "\n";
                    content += "Price: " + laptops_by_price.get(0).getPrice() + "\n";



                    textViewResult.setText(content);
                    URL1 = laptops_by_price.get(0).getUrl();
                new DownloadImageTask((ImageView) findViewById(R.id.laptop1))
                        .execute(laptops_by_price.get(0).getLaptopImage());


                    String content2 = "";
                    content2 += "Laptop Model: " + laptops_by_price.get(1).getLaptopModel()+ "\n";
                    content2 += "Price: " + laptops_by_price.get(1).getPrice() + "\n";

                    textViewResult2.setText(content2);
                URL2 = laptops_by_price.get(1).getUrl();
                new DownloadImageTask((ImageView) findViewById(R.id.laptop2))
                        .execute(laptops_by_price.get(1).getLaptopImage());

                    String content3 = "";
                    content3 += "Laptop Model: " + laptops_by_price.get(2).getLaptopModel()+ "\n";
                    content3 += "Price: " + laptops_by_price.get(2).getPrice() + "\n";


                    textViewResult3.setText(content3);
                URL3 = laptops_by_price.get(2).getUrl();
                new DownloadImageTask((ImageView) findViewById(R.id.laptop3))
                        .execute(laptops_by_price.get(2).getLaptopImage());
                }



            @Override
            public void onFailure(Call<List<Laptops>> call, Throwable t) {
                textViewResult.setText((t.getMessage()));
            }
        }));


    }
    void GoToURL(String url){
        Uri uri = Uri.parse(url);
        Intent intent= new Intent(Intent.ACTION_VIEW,uri);
        startActivity(intent);
    }

    public void openURL1(View view) {
        GoToURL(URL1);
    }

    public void openURL2(View view) {
        GoToURL(URL2);
    }

    public void openURL3(View view) {
        GoToURL(URL3);
    }
}
