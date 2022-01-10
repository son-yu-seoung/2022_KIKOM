package com.example.app;

import android.content.Context;

import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.viewpager.widget.ViewPager;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.viewpager.widget.PagerAdapter;

import com.example.app.R;

public class Adapter extends PagerAdapter {

    private int[] images = {R.drawable.challenger,
            R.drawable.grandmaster,
            R.drawable.master};
    private LayoutInflater inflater;
    private Context context;

    public Adapter(Context context){
        this.context = context;
    }

    @Override
    public int getCount() {
        return images.length;
    }

    @Override
    public boolean isViewFromObject(View view, Object object) {
        return view == ((ConstraintLayout) object);
    }

    @Override
    public Object instantiateItem(ViewGroup container, int position) {
        inflater = (LayoutInflater)context.getSystemService
                (Context.LAYOUT_INFLATER_SERVICE);
        View v = inflater.inflate(R.layout.slider, container, false);
        ImageView imageView = (ImageView)v.findViewById(R.id.imageView);
        TextView textView = (TextView)v.findViewById(R.id.textView);

        imageView.setImageResource(images[position]);

        String text = (position + 1) + "번째 이미지";
        textView.setText(text);
        container.addView(v);
        return v;
    }

    @Override
    public void destroyItem(ViewGroup container, int position, Object object) {
        container.invalidate();
    }
}