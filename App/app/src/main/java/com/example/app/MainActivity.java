package com.example.app;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.content.res.Configuration;
import android.content.res.Resources;
import android.graphics.drawable.Drawable;
import android.media.Image;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ProgressBar;
import android.widget.Spinner;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    // PrograssBar Start
    int pStatus = 0;
    private Handler handler = new Handler();
    TextView tv;
    // PrograssBar End

    // Spinner Start
    TextView textView;
    String[] items = {"게시판 1", "게시판 2", "게시판 3", "게시판 4", "게시판 5" };
    // Spinner End

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE); // -> 가로로 화면 전환
        setContentView(R.layout.activity_main);


        // ProgressBar Code Start
        Resources res = getResources();
        Drawable drawable = res.getDrawable(R.drawable.circular);
        final ProgressBar mProgress = (ProgressBar) findViewById(R.id.circularProgressbar);
        mProgress.setProgress(0);   // Main Progress
        mProgress.setSecondaryProgress(100); // Secondary Progress
        mProgress.setMax(100); // Maximum Progress
        mProgress.setProgressDrawable(drawable);

        tv = (TextView) findViewById(R.id.tv);
        new Thread(new Runnable() {
            @Override
            public void run() {
                // TODO Auto-generated method stub
                while (pStatus < 100) {
                    pStatus += 1;
                    handler.post(new Runnable() {
                        @Override
                        public void run() {
                            // TODO Auto-generated method stub
                            mProgress.setProgress(pStatus);
                            tv.setText(pStatus + "%");
                        }
                    });
                    try {
                        // Sleep for 200 milliseconds.
                        // Just to display the progress slowly
                        Thread.sleep(8); //thread will take approx 1.5 seconds to finish
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }).start();
        // PrograssBar End

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