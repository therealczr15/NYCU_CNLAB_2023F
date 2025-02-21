//  Package folder path, used for classification
package com.example.app109511207_lab1_3;

// Import the required libraries
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

// MainActivity inherits AppCompatActivity
public class MainActivity extends AppCompatActivity {

    // Declare the object variables that will be used
    TextView showtext;
    Button setbutton;
    Button resetbutton;
    EditText name;

    // Override the onCreate() function of the parent class AppCompatActivity
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        // Access members of the parent class
        super.onCreate(savedInstanceState);

        // Transform the layout through the setContentView() function
        setContentView(R.layout.activity_main);

        // Obtain the object through the id set in xml file
        showtext = (TextView)findViewById(R.id.showtext);
        setbutton = (Button)findViewById(R.id.setbutton);
        resetbutton = (Button)findViewById(R.id.resetbutton);
        name = (EditText)findViewById(R.id.name);

        // Listen for whether the setbutton triggers an event
        setbutton.setOnClickListener(new View.OnClickListener() {

            // Override the onClick() function of the parent class AppCompatActivity
            @Override
            public  void  onClick(View v) {

                // Update showtext and set it to "Welcome to Android, " + the text inside EditText
                showtext.setText("Welcome to Android, "+ name.getText().toString());
            }
        });

        // Listen for whether the resetbutton triggers an event
        resetbutton.setOnClickListener(new View.OnClickListener() {

            // Override the onClick() function of the parent class AppCompatActivity
            @Override
            public  void  onClick(View v) {

                // Update showtext and set it to "Hello World!"
                showtext.setText("Hello World!");
            }
        });
    }
}