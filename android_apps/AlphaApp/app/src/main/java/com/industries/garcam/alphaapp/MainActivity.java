package com.industries.garcam.alphaapp;

import android.app.AlarmManager;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.os.SystemClock;
import android.support.v4.app.NotificationCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private static String TAG;
    private TextView mTextView;
    private String mTransientState;
    private Button mShowButton, mStopButton, mAlertButton;
    private NotificationManager mNotificationManager;
    boolean isNotificActive = false;
    int NOTIFICATION_ID = 33;
    private int NUMBER_OF_MILLIS_IN_A_SEC = 1000;
    private final String NOTIFICATION_CHANNEL_ID = "my_notification_channel";
    /**
     * TODO: Perform basic application startup logic that should happen only
     * TODO: once for the entire life of the activity
     * @param savedInstanceState
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.TAG = getString(R.string.package_name_log);

        setContentView(R.layout.activity_main);
        mShowButton = (Button) findViewById(R.id.mShowButton);
        mStopButton = (Button) findViewById(R.id.mShowButton);
        mAlertButton = (Button) findViewById(R.id.mAlertButton);

        Log.i(TAG,"onCreate is done now");
    }

    /**
     *
     */
    @Override
    protected void onStart() {
        super.onStart();
        Log.i(TAG,"onStart is done now");
    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.i(TAG,"onStop is done now");
    }

    /**
     * Dispatch onPause() to fragments.
     * TODO: Perform heavy-load shutdown operations during onStop
     * TODO: use the onPause() method to release system resources, such as \
     * TODO: broadcast receivers, handles to sensors (like GPS), or any \
     * TODO: resources that may affect battery life while your activity is paused
     */
    @Override
    protected void onPause() {
        super.onPause();
        Log.i(TAG,"onPause is done now");
    }

    /**
     * TODO: You should implement onResume() to \
     * TODO:  initialize components that you release during onPause()
     * Dispatch onResume() to fragments.  Note that for better inter-operation
     * with older versions of the platform, at the point of this call the
     * fragments attached to the activity are <em>not</em> resumed.  This means
     * that in some cases the previous state may still be saved, not allowing
     * fragment transactions that modify the state.  To correctly interact
     * with fragments in their proper state, you should instead override
     * {@link #onResumeFragments()}.
     */
    @Override
    protected void onResume() {
        super.onResume();
        Log.i(TAG,"onResume is done now");
    }

    public void showNotificationWithTaskStackSupport(View view) {

        Context mCtx = this;
        Class mClazz = MoreInfoNotification.class;

        mNotificationManager = Utils.getNotifManager(mCtx, NOTIFICATION_CHANNEL_ID);

        Quartet mData = new Quartet("Message", "New Message"
         , "Alert New Message", R.drawable.notification_mail_icon);

        NotificationCompat.Builder notificBuilder = Utils.getBuilder(mCtx, mClazz, mData, NOTIFICATION_CHANNEL_ID);
        // Display now
        notificBuilder.setAutoCancel(true);
        mNotificationManager.notify(NOTIFICATION_ID, notificBuilder.build());

        isNotificActive = true;
    }

    public void setAlarm(View view) {
        Context mCtx = this;
        Class mClazz = AlertReceiver.class;
        Long alertTime = SystemClock.elapsedRealtime() + 5*NUMBER_OF_MILLIS_IN_A_SEC;

        PendingIntent mPendingIntent = Utils.getPendingIntentWithBroadcast(mCtx, mClazz);

        AlarmManager mAlarmManager = (AlarmManager) getSystemService(Context.ALARM_SERVICE);
        mAlarmManager.set(AlarmManager.RTC_WAKEUP, alertTime, mPendingIntent);

    }

    public void stopNotification(View view) {

        if (isNotificActive) {
            mNotificationManager.cancel(NOTIFICATION_ID);
        }
    }
}
