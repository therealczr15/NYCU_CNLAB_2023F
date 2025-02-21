//  Package folder path, used for classification
package com.example.app109511207;

// Import the required libraries
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.TypedValue;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

// MainActivity inherits AppCompatActivity
public class MainActivity extends AppCompatActivity {

    // Declare the object variables that will be used
    TextView showtext;
    Button   demobutton;
    Button   backbutton;

    // Override the onCreate() function of the parent class AppCompatActivity
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        // Access members of the parent class
        super.onCreate(savedInstanceState);

        // Transform the layout through the setContentView() function
        setContentView(R.layout.activity_main);

        // Obtain the object through the id set in xml file
        showtext   = (TextView)findViewById(R.id.showtext);
        demobutton = (Button)findViewById(R.id.demobutton);
        backbutton = (Button)findViewById(R.id.backbutton);

        // Listen for whether the demobutton triggers an event
        demobutton.setOnClickListener(new View.OnClickListener() {

            // Override the onClick() function of the parent class AppCompatActivity
            @Override
            public  void  onClick(View v) {

                // Update showtext and set it to "Pass!"
                showtext.setText("Pass!");

                // Get text size
                int size = (int)showtext.getTextSize();

                // Text size + 5
                size += 5;

                // Update showtext size
                showtext.setTextSize(TypedValue.COMPLEX_UNIT_PX, size);
            }
        });

        // Listen for whether the backbutton triggers an event
        backbutton.setOnClickListener(new View.OnClickListener() {

            // Override the onClick() function of the parent class AppCompatActivity
            @Override
            public  void  onClick(View v) {

                // Update showtext and set it to "Android Lab1 demo"
                showtext.setText("Android Lab1 demo");

                // Get text size
                int size = (int)showtext.getTextSize();

                // Text size - 5
                size -= 5;

                // Update showtext size
                showtext.setTextSize(TypedValue.COMPLEX_UNIT_PX, size);
            }
        });
    }
}