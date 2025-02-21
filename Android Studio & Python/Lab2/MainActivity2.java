//  Package folder path, used for classification
package com.example.app109511207_lab2;

// Import the required libraries
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

// MainActivity inherits AppCompatActivity
public class MainActivity2 extends AppCompatActivity {

    // Declare the object variables that will be used
    Button enter, restart, finish;
    TextView hint, times, best;
    EditText guess;

    // Declare the variables that will be used in the game
    int randNum = 0, history = 999;
    int min = 1, max = 50, count = 0;

    // Override the onCreate() function of the parent class AppCompatActivity
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        // Access members of the parent class
        super.onCreate(savedInstanceState);

        // Transform the layout through the setContentView() function
        setContentView(R.layout.activity_main2);

        // Obtain the object through the id set in xml file
        enter = (Button)findViewById(R.id.enter);
        restart = (Button)findViewById(R.id.restart);
        finish = (Button)findViewById(R.id.finish);
        hint = (TextView)findViewById(R.id.hint);
        times = (TextView)findViewById(R.id.times);
        best = (TextView)findViewById(R.id.best);
        guess = (EditText)findViewById(R.id.guess);

        // Random an answer between 1~50
        randNum=(int)(Math.random() * 50 + 1);

        // Declare a bundle and get the data sent from the previous activity
        Bundle bundle = this.getIntent().getExtras();

        // Listen for whether the enter triggers an event
        enter.setOnClickListener(new View.OnClickListener() {

            // Override the onClick() function of the parent class AppCompatActivity
            @Override
            public  void  onClick(View v) {

                // Parse the string into an integer and store it in variable 'in'
                int in = Integer.parseInt(guess.getText().toString());

                // If the input value is within the range
                if(in <= max && in >= min){

                    // count + 1
                    count += 1;

                    // If the input value > the answer
                    if(in > randNum){

                        // Update max = in
                        max = in;

                        // Update the text
                        times.setText("猜測次數: " + count);
                        hint.setText("請輸入" + min + "~" + max + "的數字");
                    }

                    // If the input value < the answer
                    else if(in < randNum) {

                        // Update min = in
                        min = in;

                        // Update the text
                        times.setText("猜測次數: " + count);
                        hint.setText("請輸入" + min + "~" + max + "的數字");
                    }

                    // If the input value = the answer
                    else if(in == randNum){

                        // If count < history(best record), update history(best record) = count
                        if(count < history){
                            history = count;
                        }

                        // Update the text
                        times.setText("猜測次數: " + count);
                        hint.setText("答對");
                        best.setText("最佳紀錄: " + history);
                    }
                }

                // If the input value is out of the range
                else{

                    // Update the text
                    hint.setText("請輸入" + min + "~" + max + "的數字，請輸入正常值");
                }
            }
        });

        // Listen for whether the restart triggers an event
        restart.setOnClickListener(new View.OnClickListener() {

            // Override the onClick() function of the parent class AppCompatActivity
            @Override
            public  void  onClick(View v) {

                // Reset an answer between 1~50
                randNum=(int)(Math.random() * 50 + 1);

                // Reset the variables that will be used in the game
                min = 1;
                max = 50;
                count = 0;

                // Update the text
                times.setText("猜測次數: " + count);
                hint.setText("請輸入" + min + "~" + max + "的數字");
            }
        });

        // Listen for whether the finish triggers an event
        finish.setOnClickListener(new View.OnClickListener() {

            // Override the onClick() function of the parent class AppCompatActivity
            @Override
            public  void  onClick(View v) {

                // Create a new intent
                Intent intent = new Intent();

                // MainActivity2 intends to open MainActivity3 through an intent
                intent.setClass(MainActivity2.this, MainActivity3.class);

                // Put the data to be sent into the bundle with the key 'history'
                bundle.putInt("history", history);

                // Place the data bundle to be sent onto the transportation vehicle intent
                intent.putExtras(bundle);

                // Switch activity
                startActivity(intent);
            }
        });
    }
}