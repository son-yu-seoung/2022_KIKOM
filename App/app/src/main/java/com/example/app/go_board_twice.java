package com.example.app;

import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class go_board_twice extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.board_twice);

    /*
    // Spinner 구현 Start
    textView = findViewById(R.id.BoardtextView);
    Spinner spinner = findViewById(R.id.Boardspinner);
    ArrayAdapter<String> adapter = new ArrayAdapter<String>(
            this, android.R.layout.simple_spinner_item, items);
        adapter.setDropDownViewResource(
    android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);
        spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
        @Override
        public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
            textView.setText(items[position]);
        }

        @Override
        public void onNothingSelected(AdapterView<?> parent) {
            textView.setText("");
        }
    });
    // Spinner End
*/

        Button tw_go_board_page_btn = (Button) findViewById(R.id.tw_go_board_page_btn);
        tw_go_board_page_btn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), go_board_page.class);
                startActivity(intent);
            }

        });

        Button go_board_writing_page_btn = (Button) findViewById(R.id.go_board_writing_page_btn);
        go_board_writing_page_btn.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), go_board_writing_page.class);
                startActivity(intent);
            }

        });


    }
}
