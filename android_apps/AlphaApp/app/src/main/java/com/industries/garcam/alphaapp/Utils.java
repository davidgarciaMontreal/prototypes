package com.industries.garcam.alphaapp;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.TaskStackBuilder;
import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.os.Build;
import android.support.annotation.NonNull;
import android.support.v4.app.NotificationCompat;


public class Utils {

    @NonNull
    public static NotificationCompat.Builder getBuilder(Context mCtx, Class mClazz, Quartet mData,
                                                        String notifID) {

        NotificationCompat.Builder notificBuilder = getGnrcBuilder(mCtx, mData, notifID);

        PendingIntent mPendingIntent = getPendingIntentWithTaskStackBuilder(mCtx, mClazz);

        notificBuilder.setContentIntent(mPendingIntent);

        return notificBuilder;
    }

    public static NotificationCompat.Builder getGnrcBuilder(Context mCtx, Quartet mData,
                                                            String notifID) {

        return new NotificationCompat.Builder(mCtx,notifID)
                .setSmallIcon(mData.getSmallIcon())
                .setContentTitle(mData.getContentTitle())
                .setTicker(mData.getTicker())
                .setContentText(mData.getContextText());
    }

    private static PendingIntent getPendingIntentWithTaskStackBuilder(Context aContext, Class aClazz) {
        Class mClazz = aClazz;
        Context mCtx = aContext;
        int requestCode = 0;
        int mPendingFlag = PendingIntent.FLAG_UPDATE_CURRENT;
        Intent mIntent = new Intent(mCtx, mClazz);

        TaskStackBuilder mTaskStackBuilder = TaskStackBuilder.create(mCtx);
        mTaskStackBuilder.addParentStack(mClazz);
        mTaskStackBuilder.addNextIntent(mIntent);

        return mTaskStackBuilder.getPendingIntent(requestCode, mPendingFlag);
    }

    public static PendingIntent getPendingIntentWithBroadcast(Context mContext, Class mClazz) {

        Intent anIntent = new Intent(mContext, mClazz);
        int mFlag = PendingIntent.FLAG_UPDATE_CURRENT;

        return PendingIntent.getBroadcast(mContext, 1, anIntent, mFlag);
    }

     public static NotificationManager getNotifManager(Context mContext,
                                                       String NOTIFICATION_CHANNEL_ID){

        NotificationManager mNotificationManager = (NotificationManager)
                mContext.getSystemService(mContext.NOTIFICATION_SERVICE);

         if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
             NotificationChannel notificationChannel = new NotificationChannel(NOTIFICATION_CHANNEL_ID, "My Notifications", NotificationManager.IMPORTANCE_DEFAULT);

             // Configure the notification channel.
             notificationChannel.setDescription("Channel description");
             notificationChannel.enableLights(true);
             notificationChannel.setLightColor(Color.RED);
             notificationChannel.setVibrationPattern(new long[]{0, 1000, 500, 1000});
             notificationChannel.enableVibration(true);
             mNotificationManager.createNotificationChannel(notificationChannel);
         }
        return mNotificationManager;
     }
}
