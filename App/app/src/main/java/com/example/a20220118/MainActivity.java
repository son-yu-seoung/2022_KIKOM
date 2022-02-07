package com.example.a20220118;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;

import android.content.pm.ActivityInfo;
import android.os.Bundle;
import android.os.Handler;
import android.os.SystemClock;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import android.view.LayoutInflater;

import androidx.appcompat.app.AppCompatActivity;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    Fragment login, register, main, welcome, chatting, board, exercise, gaesipan, ranking, recommend;
    private EditText setid, setpw, setname, edid, edpw;

    TextView textView;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE); // -> 가로로 화면 전환
        // setContentView(R.layout.activity_main);
        setContentView(R.layout.activity_main);
        // Page
        board = new Go_board_page();
        chatting = new Go_chatting_page();
        exercise = new Go_exercise_page();
        gaesipan = new Go_gaesipan_page();
        ranking = new Go_ranking_page();
        recommend = new Go_recommend_page();
        login = new Login();
        main = new Main();
        register = new Register();
        welcome = new Welcome();
        // Timer
        starttimer = (Button)findViewById(R.id.startbtn);
        pausetimer = (Button)findViewById(R.id.pausebtn);
        resettimer = (Button)findViewById(R.id.resetbtn);
        handler = new Handler() ;

        // 페이지 로딩
        getSupportFragmentManager().beginTransaction().add(R.id.mainboard, board).commit();
        getSupportFragmentManager().beginTransaction().add(R.id.mainboard, chatting).commit();
        getSupportFragmentManager().beginTransaction().add(R.id.mainboard, exercise).commit();
        getSupportFragmentManager().beginTransaction().add(R.id.mainboard, gaesipan).commit();
        getSupportFragmentManager().beginTransaction().add(R.id.mainboard, ranking).commit();
        getSupportFragmentManager().beginTransaction().add(R.id.mainboard, recommend).commit();
        getSupportFragmentManager().beginTransaction().add(R.id.mainboard, main).commit();
        getSupportFragmentManager().beginTransaction().add(R.id.mainboard, register).commit();
        getSupportFragmentManager().beginTransaction().add(R.id.mainboard, welcome).commit();

        getSupportFragmentManager().beginTransaction().hide(board).commit();
        getSupportFragmentManager().beginTransaction().hide(chatting).commit();
        getSupportFragmentManager().beginTransaction().hide(exercise).commit();
        getSupportFragmentManager().beginTransaction().hide(gaesipan).commit();
        getSupportFragmentManager().beginTransaction().hide(ranking).commit();
        getSupportFragmentManager().beginTransaction().hide(recommend).commit();
        getSupportFragmentManager().beginTransaction().hide(main).commit();
        getSupportFragmentManager().beginTransaction().hide(register).commit();
        getSupportFragmentManager().beginTransaction().hide(welcome).commit();

        getSupportFragmentManager().beginTransaction().add(R.id.loginform, login).commit();

        // Timer
        ListElementsArrayList = new ArrayList<String>(Arrays.asList(ListElements));
        adapter = new ArrayAdapter<String>(this,
                android.R.layout.simple_list_item_1,
                ListElementsArrayList
        );
    }

    public void resettimer(View view) { // Timer - 리셋
        TextView textView;
        textView = (TextView)findViewById(R.id.Timer);
        textView.setText("00:00:00");

        MillisecondTime = 0L ;
        StartTime = 0L ;
        TimeBuff = 0L ;
        UpdateTime = 0L ;
        Seconds = 0 ;
        Minutes = 0 ;
        MilliSeconds = 0 ;

        ListElementsArrayList.clear();
        adapter.notifyDataSetChanged();
    }

    public void starttimer(View view) { // Timer - 시작
        StartTime = SystemClock.uptimeMillis();
        handler.postDelayed(runnable, 0);
        // resettimer.setEnabled(false);
    }

    public void pausetimer(View view) { // Timer - 정지
        TimeBuff += MillisecondTime;
        handler.removeCallbacks(runnable);
    }

    public void gotoboard(View view){   // 게시판으로 이동
        getSupportFragmentManager().beginTransaction().hide(chatting).commit();
        getSupportFragmentManager().beginTransaction().hide(gaesipan).commit();
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE);
        getSupportFragmentManager().beginTransaction().show(board).commit();
    }

    public void gotochatting(View view){    // 채팅으로 이동
        getSupportFragmentManager().beginTransaction().hide(main).commit();
        getSupportFragmentManager().beginTransaction().hide(exercise).commit();
        getSupportFragmentManager().beginTransaction().hide(ranking).commit();
        getSupportFragmentManager().beginTransaction().hide(board).commit();
        getSupportFragmentManager().beginTransaction().show(chatting).commit();
    }

    public void gotoexercise(View view) {   // 운동으로 이동
        getSupportFragmentManager().beginTransaction().hide(main).commit();
        getSupportFragmentManager().beginTransaction().hide(chatting).commit();
        getSupportFragmentManager().beginTransaction().hide(board).commit();
        getSupportFragmentManager().beginTransaction().hide(ranking).commit();
        getSupportFragmentManager().beginTransaction().show(exercise).commit();
    }

    public void gotogaesipan(View view) {   // 게시판(확대 버전)으로 이동
        getSupportFragmentManager().beginTransaction().hide(board).commit();
        getSupportFragmentManager().beginTransaction().hide(gaesipan).commit();
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        getSupportFragmentManager().beginTransaction().show(gaesipan).commit();
    }

    public void gotoranking(View view) {    // 랭킹 페이지로 이동
        getSupportFragmentManager().beginTransaction().hide(main).commit();
        getSupportFragmentManager().beginTransaction().hide(exercise).commit();
        getSupportFragmentManager().beginTransaction().hide(chatting).commit();
        getSupportFragmentManager().beginTransaction().hide(board).commit();
        getSupportFragmentManager().beginTransaction().show(ranking).commit();
    }

    public void gotorecommend(View view) {  // 운동 추천 페이지로 이동
        getSupportFragmentManager().beginTransaction().hide(main).commit();
        getSupportFragmentManager().beginTransaction().show(recommend).commit();
    }

    public void gotomain(View view) {   // 메인 페이지로 이동
        setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE);
        getSupportFragmentManager().beginTransaction().hide(welcome).commit();
        getSupportFragmentManager().beginTransaction().hide(exercise).commit();
        getSupportFragmentManager().beginTransaction().hide(chatting).commit();
        getSupportFragmentManager().beginTransaction().hide(board).commit();
        getSupportFragmentManager().beginTransaction().hide(ranking).commit();
        getSupportFragmentManager().beginTransaction().hide(recommend).commit();
        getSupportFragmentManager().beginTransaction().show(main).commit();
    }

    public void loginbtn(View view){
        edid = (EditText) findViewById(R.id.validateid);
        edpw = (EditText) findViewById(R.id.validatepw);
        String userID = edid.getText().toString();
        String userPass = edpw.getText().toString();
        if (userID.equals("")||userPass.equals("")){
            Toast.makeText( getApplicationContext(), "로그인을 먼저 해주세요", Toast.LENGTH_SHORT ).show();
            return;
        }

        Response.Listener<String> responseListener = new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {


                try {
                    JSONObject jsonObject = new JSONObject( response );
                    boolean success = jsonObject.getBoolean( "success" );

                    if(success) {//로그인 성공시
                        String UName = jsonObject.getString( "userName" );

                        Toast.makeText( getApplicationContext(), UName+"님 오늘도 화이팅", Toast.LENGTH_SHORT ).show();
                        getSupportFragmentManager().beginTransaction().hide(login).commit();
                        getSupportFragmentManager().beginTransaction().show(welcome).commit();

                    } else {//로그인 실패시
                        Toast.makeText( getApplicationContext(), "아이디 또는 비밀번호를\n  다시 확인 해주세요", Toast.LENGTH_SHORT ).show();
                        return;
                    }

                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        };
        LoginRequest loginRequest = new LoginRequest( userID, userPass, responseListener );
        RequestQueue queue = Volley.newRequestQueue( MainActivity.this );
        queue.add( loginRequest );
    }


    public void registerbtn(View view){
        setid = findViewById(R.id.setid);
        setpw = findViewById(R.id.setpw);
        setname = findViewById(R.id.setname);

        String userId = setid.getText().toString();
        String userPw = setpw.getText().toString();
        String userName = setname.getText().toString();

        Response.Listener<String> responseListener = new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {

                try {
                    JSONObject jsonObject = new JSONObject( response );
                    boolean success = jsonObject.getBoolean( "success" );

                    //회원가입 성공시
                    if(success) {
                        getSupportFragmentManager().beginTransaction().hide(register).commit();
                        getSupportFragmentManager().beginTransaction().show(login).commit();

                        //회원가입 실패시
                    } else {
                        Toast.makeText( getApplicationContext(), "실패", Toast.LENGTH_SHORT ).show();
                        return;
                    }

                } catch (JSONException e) {
                    e.printStackTrace();
                }

            }
        };

        //서버로 Volley를 이용해서 요청
        RegisterRequest registerRequest = new RegisterRequest(userId, userPw, userName, responseListener);
        RequestQueue queue = Volley.newRequestQueue(MainActivity.this );
        queue.add(registerRequest);
    }

    public void newRegister(View view){
        getSupportFragmentManager().beginTransaction().hide(login).commit();
        getSupportFragmentManager().beginTransaction().show(register).commit();

    }

    Button starttimer, pausetimer, resettimer ;
    long MillisecondTime, StartTime, TimeBuff, UpdateTime = 0L ;
    Handler handler;
    int Seconds, Minutes, MilliSeconds ;
    String[] ListElements = new String[] {  };
    List<String> ListElementsArrayList ;
    ArrayAdapter<String> adapter ;


    public Runnable runnable = new Runnable() {     // Timer

        public void run() {
            TextView textView;
            textView = (TextView)findViewById(R.id.Timer);
            textView.setText("" + String.format("%02d", Minutes) + ":" + String.format("%02d", Seconds) + ":" + String.format("%02d", MilliSeconds));

            MillisecondTime = SystemClock.uptimeMillis() - StartTime;
            UpdateTime = TimeBuff + MillisecondTime;
            Seconds = (int) (UpdateTime / 1000);
            Minutes = Seconds / 60;
            Seconds = Seconds % 60;
            MilliSeconds = (int) (UpdateTime % 100);
            handler.postDelayed(this, 0);
        }

    };

    public void startchatting(View view){
        WebSettings mWebSettings;
        WebView webView = (WebView) findViewById(R.id.webview);
        webView.setWebViewClient(new WebViewClient());

        mWebSettings = webView.getSettings();
        mWebSettings.setJavaScriptEnabled(true); // 웹페이지 자바스클비트 허용 여부
        mWebSettings.setSupportMultipleWindows(false); // 새창 띄우기 허용 여부
        mWebSettings.setJavaScriptCanOpenWindowsAutomatically(false); // 자바스크립트 새창 띄우기(멀티뷰) 허용 여부
        mWebSettings.setLoadWithOverviewMode(true); // 메타태그 허용 여부
        mWebSettings.setUseWideViewPort(true); // 화면 사이즈 맞추기 허용 여부
        mWebSettings.setSupportZoom(false); // 화면 줌 허용 여부
        mWebSettings.setBuiltInZoomControls(false); // 화면 확대 축소 허용 여부
        mWebSettings.setLayoutAlgorithm(WebSettings.LayoutAlgorithm.SINGLE_COLUMN); // 컨텐츠 사이즈 맞추기
        mWebSettings.setCacheMode(WebSettings.LOAD_NO_CACHE); // 브라우저 캐시 허용 여부
        mWebSettings.setDomStorageEnabled(true); // 로컬저장소 허용 여부
        webView.loadUrl("http://localhost:5000");
    }

    // Timer



}

