//  Package folder path, used for classification
package com.example.app109511207_lab2;

// Import the required libraries
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

// MainActivity inherits AppCompatActivity
public class MainActivity extends AppCompatActivity {

    // Declare the object variables that will be used
    Button button;
    EditText ID;
    EditText name;

    // Override the onCreate() function of the parent class AppCompatActivity
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        // Access members of the parent class
        super.onCreate(savedInstanceState);

        // Transform the layout through the setContentView() function
        setContentView(R.layout.activity_main);

        // Obtain the object through the id set in xml file
        button = (Button)findViewById(R.id.button);
        ID = (EditText)findViewById(R.id.ID);
        name = (EditText)findViewById(R.id.name);

        // Listen for whether the button triggers an event
        button.setOnClickListener(new View.OnClickListener() {

            // Override the onClick() function of the parent class AppCompatActivity
            @Override
            public  void  onClick(View v) {

                // Create a new intent
                Intent intent = new Intent();

                // MainActivity intends to open MainActivity2 through an intent
                intent.setClass(MainActivity.this, MainActivity2.class);

                // Create a new bundle
                Bundle bundle = new Bundle();

                // Put the data to be sent into the bundle with the key 'name'
                bundle.putString("name", name.getText().toString());

                // Put the data to be sent into the bundle with the key 'ID'
                bundle.putString("ID", ID.getText().toString());

                // Place the data bundle to be sent onto the transportation vehicle intent
                intent.putExtras(bundle);

                // Switch activity
                startActivity(intent);
            }
        });
    }
}