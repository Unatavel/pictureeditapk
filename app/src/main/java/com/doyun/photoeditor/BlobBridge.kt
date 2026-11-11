package com.doyun.photoeditor

import android.webkit.JavascriptInterface

class BlobBridge(private val activity: MainActivity) {

    @JavascriptInterface
    fun save(dataUrl: String, filename: String, mimeType: String) {
        activity.saveDataUrl(dataUrl, filename, mimeType)
    }
}
