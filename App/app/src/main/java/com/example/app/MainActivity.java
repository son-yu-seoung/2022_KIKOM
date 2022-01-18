package com.example.app;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;

import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.content.res.Resources;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ProgressBar;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {



    // Spinner Start
    TextView textView;
    String[] items = {"게시판 1", "게시판 2", "게시판 3", "게시판 4", "게시판 5" };
    // Spinner End

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE); // -> 가로로 화면 전환
        setContentView(R.layout.activity_main);

        // Button 전환

        ImageButton go_chatting_page_btn = (ImageButton) findViewById(R.id.go_chatting_page_btn);
        go_chatting_page_btn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), com.example.app.go_chatting_page.class);
                startActivity(intent);
            }
        });

        Button go_lutin_recommend_btn = (Button) findViewById(R.id.go_lutin_recommend_btn);
        go_lutin_recommend_btn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), go_lutin_recommend.class);
                startActivity(intent);
            }
        });

        ImageButton go_exercise_page_btn = (ImageButton) findViewById(R.id.go_exercise_page_btn);
        go_exercise_page_btn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), go_exercise_page.class);
                startActivity(intent);
            }
        });

        // Button 전환

/*
        Button go_board_twice_btn = (ImageButton) findViewById(R.id.go_board_twice_btn);
        go_board_twice_btn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), go_board_twice);
                startActivity(intent);
            }
        });

        */
    }
    
}

