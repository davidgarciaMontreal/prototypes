package com.industries.garcam.alphaapp;


import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.support.v4.app.NotificationCompat;

public class AlertReceiver extends BroadcastReceiver {

    private final String NOTIFICATION_CHANNEL_ID = "my_notification_channel";
    @Override
    public void onReceive(Context context, Intent intent) {
        
        // TODO: check for intent.action
        createNotification(context, "Times Up", "5 Seconds Has Passed", "Alert");
    }

    private void createNotification(Context context, String msg, String msgText, String msgAlert) {

        PendingIntent mPendingIntent = PendingIntent.getActivity(context, 0,
                new Intent(context, MainActivity.class), 0);

        Quartet mData = new Quartet(msg, msgText,msgAlert, R.drawable.notification_mail_icon);

        NotificationCompat.Builder mBuilder = Utils.getGnrcBuilder(context, mData, NOTIFICATION_CHANNEL_ID);

        mBuilder.setContentIntent(mPendingIntent);
        mBuilder.setDefaults(NotificationCompat.DEFAULT_LIGHTS);
        mBuilder.setAutoCancel(true);

        NotificationManager mNotificationManager = Utils.getNotifManager(context, NOTIFICATION_CHANNEL_ID);
        // Display now
        mNotificationManager.notify(1, mBuilder.build());
    }
}
