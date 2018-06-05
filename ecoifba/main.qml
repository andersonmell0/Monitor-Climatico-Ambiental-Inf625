import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import QtWebView 1.0

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("IFBA GSORT")

    WebView {
              id: webView
              anchors.fill: parent
              url: "http://192.168.0.7/monitor-ambiental-climatico/"
          }
}
