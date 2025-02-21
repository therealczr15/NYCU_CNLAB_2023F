//  Package folder path, used for classification
package com.example.app109511207_lab2;

// Import the required libraries
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

// MainActivity inherits AppCompatActivity
public class MainActivity3 extends AppCompatActivity {

    // Declare the object variables that will be used
    Button back;
    TextView id, Name, bestrecord;

    // Override the onCreate() function of the parent class AppCompatActivity
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        // Access members of the parent class
        super.onCreate(savedInstanceState);

        // Transform the layout through the setContentView() function
        setContentView(R.layout.activity_main3);

        // Obtain the object through the id set in xml file
        back = (Button)findViewById(R.id.back);
        id = (TextView)findViewById(R.id.id);
        Name = (TextView)findViewById(R.id.Name);
        bestrecord = (TextView)findViewById(R.id.bestrecord);

        // Declare a bundle and get the data sent from the previous activity
        Bundle bundle = this.getIntent().getExtras();

        // Place the data in the bundle with the key 'ID' into the variable 'ID'
        String ID = (String)bundle.getString("ID");

        // Place the data in the bundle with the key 'name' into the variable 'name'
        String name = (String)bundle.getString("name");

        // Place the data in the bundle with the key 'history' into the variable 'history'
        int history = bundle.getInt("history");

        // Update the text
        id.setText("學號: \t\t" + ID);
        Name.setText("姓名: \t\t" + name);
        bestrecord.setText("最佳紀錄: \t" + history);

        // Listen for whether the back triggers an event
        back.setOnClickListener(new View.OnClickListener() {

            // Override the onClick() function of the parent class AppCompatActivity
            @Override
            public  void  onClick(View v) {

                // Create a new intent
                Intent intent = new Intent();

                // MainActivity3 intends to open MainActivity through an intent
                intent.setClass(MainActivity3.this, MainActivity.class);

                // Create a new bundle
                Bundle bundle = new Bundle();

                // Place the data bundle to be sent onto the transportation vehicle intent
                intent.putExtras(bundle);

                // Switch activity
                startActivity(intent);
            }
        });
    }
}