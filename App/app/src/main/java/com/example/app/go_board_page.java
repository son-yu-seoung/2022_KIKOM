package com.example.app;

import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class go_board_page extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE); // -> 가로로 화면 전환
        setContentView(R.layout.board_page);

        Button go_board_twice_btn = (Button) findViewById(R.id.go_board_twice_btn);
        go_board_twice_btn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), go_board_twice.class);
                startActivity(intent);
            }
        });

        Button go_chatting_page_btn = (Button) findViewById(R.id.go_chatting_page_btn);
        go_chatting_page_btn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), go_chatting_page.class);
                startActivity(intent);

            }

        });
    }
}